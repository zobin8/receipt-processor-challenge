"""Unit tests for the receipt services."""

import pytest

from receipt_processor.backend.receipts.services import AddReceiptService

from . import stubs


class TestAddReceiptService:
    """Test AddReceiptService"""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Run for every test case"""
        self.db = dict()
        self.service = AddReceiptService(self.db)

    def test_add_correct(self):
        """Test happy path"""

        id = self.service.start(stubs.good_receipt)

        assert id in self.db
        assert len(self.db) == 1
        assert self.db[id] == stubs.good_receipt

    def test_add_wrong(self):
        """Test unhappy path with bad total"""

        id = self.service.start(stubs.bad_receipt)

        assert id is None
        assert len(self.db) == 0
