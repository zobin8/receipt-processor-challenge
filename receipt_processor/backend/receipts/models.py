"""Datastructures for receipts."""

from dataclasses import dataclass
from datetime import date
from datetime import time
from typing import List


@dataclass
class Item:
    """A receipt item."""

    shortDescription: str
    price: str


@dataclass
class Receipt:
    """A customer receipt."""

    retailer: str
    purchaseDate: date
    purchaseTime: time
    items: List[Item]
    total: float

