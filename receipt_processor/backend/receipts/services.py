"""Services for receipts"""

from typing import Dict
from typing import Optional

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

        id = receipt.id
        self.receipt_db[id] = receipt

        return receipt.id