"""Stubs for the service tests."""

from datetime import date
from datetime import time

from receipt_processor.backend.receipts.models import Receipt


id = 'test_uid'

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


receipt_scores = [
    (
        'Empty receipt',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(1, 2, 3),
            items=[
            ],
            total=3.99,
        ),
        0
    ),
    (
        'Retailer name',
        Receipt(
            retailer='M&M Fact0ry',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(1, 2, 3),
            items=[
            ],
            total=3.99,
        ),
        9
    ),
    (
        'Round dollar',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(1, 2, 3),
            items=[
            ],
            total=4,
        ),
        75
    ),
    (
        'Round quarter dollar',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(1, 2, 3),
            items=[
            ],
            total=4.25,
        ),
        25
    ),
    (
        'Count pairs',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(1, 2, 3),
            items=[
                dict(shortDescription='1', price=1.25),
                dict(shortDescription='1', price=1.25),
                dict(shortDescription='1', price=1.25),
            ],
            total=3.99,
        ),
        5
    ),
    (
        'Item length',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(1, 2, 3),
            items=[
                dict(shortDescription='123', price=99.99),
            ],
            total=3.99,
        ),
        20
    ),
    (
        'Odd date',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 3),
            purchaseTime=time(1, 2, 3),
            items=[
            ],
            total=3.99,
        ),
        6
    ),
    (
        'Just before 2pm',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(13, 59, 59),
            items=[
            ],
            total=3.99,
        ),
        0
    ),
    (
        'Just after 2pm',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(14, 0, 1),
            items=[
            ],
            total=3.99,
        ),
        10
    ),
    (
        'Just before 4pm',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(15, 59, 59),
            items=[
            ],
            total=3.99,
        ),
        10
    ),
    (
        'Just after 4pm',
        Receipt(
            retailer='',
            purchaseDate=date(2001, 2, 4),
            purchaseTime=time(16, 0, 1),
            items=[
            ],
            total=3.99,
        ),
        0
    ),
]