"""Services for receipts"""

from datetime import time
from typing import Dict
from typing import Optional
import math
import re

from receipt_processor.backend._base import BaseService

from .models import Receipt


# Receipt database is a static in-memory dict for now.
# Replace with DB backend in future.
RECEIPT_DB: Dict[str, Receipt] = dict()


class AddReceiptService(BaseService):
    """Service to add a receipt to the DB"""

    def __init__(
        self,
        receipt_db: Dict[str, Receipt]  = RECEIPT_DB,
    ):
        """Create the service.
        
        Arguments:
            receipt_db: Dict[str, Receipt]
                The receipt database, currently a dict.
        """
        self.receipt_db = receipt_db

    def start(self, receipt: Receipt) -> Optional[str]:
        """Add receipt to database if valid.
        
        Arguments:
            receipt: Receipt
                The receipt to add

        Returns:
            Receipt ID if valid
            None if not
        """

        # Verify total is correct
        expected_total = sum([item.price for item in receipt.items])
        if abs(receipt.total - expected_total) > 1e-3:
            return None

        id = receipt.id
        self.receipt_db[id] = receipt

        return id


class GetReceiptService(BaseService):
    """Service to get a receipt from the DB"""

    def __init__(
        self,
        receipt_db: Dict[str, Receipt]  = RECEIPT_DB,
    ):
        """Create the service.

        Arguments:
            receipt_db: Dict[str, Receipt]
                The receipt database, currently a dict.
        """
        self.receipt_db = receipt_db

    def start(self, id: str) -> Optional[Receipt]:
        """Get a receipt from the database

        Arguments:
            id: str
                The receipt ID

        Returns:
            Receipt if found
            None if not
        """
        return self.receipt_db.get(id)


class ScoreReceiptService(BaseService):
    """Service to get a receipt's points."""

    def start(self, receipt: Receipt) -> int:
        """Calculate a receipt's points. If this business logic becomes more complicated,
        service should be split into individual scoring services.

        Arguments:
            receipt: Receipt
                The receipt to score

        Returns:
            The point total
        """
        points = 0

        # One point for every alphanumeric character in the retailer name.
        alphanum_only = re.sub('\W', '', receipt.retailer)
        points += len(alphanum_only)

        # 50 points if the total is a round dollar amount with no cents.
        if receipt.total == int(receipt.total):
            points += 50

        # 25 points if the total is a multiple of 0.25.
        if receipt.total * 4 == int(receipt.total * 4):
            points += 25

        # 5 points for every two items on the receipt.
        pairs = len(receipt.items) // 2
        points += 5 * pairs

        # If the trimmed length of the item description is a multiple of 3, multiply the price by
        # 0.2 and round up to the nearest integer. The result is the number of points earned.
        for item in receipt.items:
            if len(item.shortDescription.strip()) % 3 != 0:
                continue

            points += math.ceil(item.price * 0.2)

        # 6 points if the day in the purchase date is odd.
        if receipt.purchaseDate.day % 2 == 1:
            points += 6

        # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
        if receipt.purchaseTime > time(14) and receipt.purchaseTime < time(16):
            points += 10

        return points


class GetPointsService(BaseService):
    """Service to get a receipt's points."""

    def __init__(
        self,
        get_receipt: GetReceiptService = GetReceiptService(),
        score_receipt: ScoreReceiptService = ScoreReceiptService(),
    ):
        """Create the service
        
        Arguments:
            get_receipt: GetReceiptService
                service to get the receipt.
        """
        self.get_receipt = get_receipt
        self.score_receipt = score_receipt

    def start(self, id: str) -> Optional[int]:
        """Get a receipt's point total. Lazy evaluation.

        Arguments:
            id: str
                The receipt ID

        Returns:
            The point total, if receipt is found
            None if not
        """

        receipt = self.get_receipt.start(id)
        if receipt is None:
            return None
        
        if receipt.points is None:
            receipt.points = self.score_receipt.start(receipt)

        return receipt.points