"""Datastructures for receipts."""

from dataclasses import dataclass
from datetime import date
from datetime import time
from typing import List
from typing import Optional
from uuid import uuid4


@dataclass
class Item:
    """A receipt item."""

    shortDescription: str
    price: float

    def __post_init__(self):
        """Initialize types for members"""
        self.price = float(self.price)


@dataclass
class Receipt:
    """A customer receipt."""

    retailer: str
    purchaseDate: date
    purchaseTime: time
    items: List[Item]
    total: float

    _id: Optional[str] = None
    points: Optional[int] = None

    def __post_init__(self):
        """Initialize types for members"""
        self.items = [Item(**item) for item in self.items]
        self.total = float(self.total)

    @property
    def id(self):
        """Get the object id. Create if not set."""
        if self._id is None:
            self._id = str(uuid4())
        return self._id