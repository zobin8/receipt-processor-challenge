"""Stubs for the service tests."""

from datetime import date
from datetime import time

from receipt_processor.backend.receipts.models import Receipt


good_receipt = Receipt(
    retailer='retail',
    purchaseDate=date(2001, 2, 3),
    purchaseTime=time(1, 2, 3),
    items=[
        dict(shortDescription='desc1', price=1.25),
        dict(shortDescription='desc2', price=1.75),
    ],
    total=3.0,
)

bad_receipt = Receipt(
    retailer='retail',
    purchaseDate=date(2001, 2, 3),
    purchaseTime=time(1, 2, 3),
    items=[
        dict(shortDescription='desc1', price=1.25),
        dict(shortDescription='desc2', price=1.75),
    ],
    total=3.5,
)
