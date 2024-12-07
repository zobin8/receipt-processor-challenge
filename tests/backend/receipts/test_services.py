"""Unit tests for the receipt services."""

import pytest

from receipt_processor.backend.receipts.models import Receipt
from receipt_processor.backend.receipts.services import AddReceiptService
from receipt_processor.backend.receipts.services import GetPointsService
from receipt_processor.backend.receipts.services import GetReceiptService
from receipt_processor.backend.receipts.services import ScoreReceiptService

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


class TestGetReceiptService:
    """Test GetReceiptService"""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Run for every test case"""
        self.db = {stubs.id: stubs.good_receipt}
        self.service = GetReceiptService(self.db)

    def test_get_correct(self):
        """Test happy path"""

        receipt = self.service.start(stubs.id)
        assert receipt == stubs.good_receipt

    def test_get_wrong(self):
        """Test unhappy path with bad id"""

        assert self.service.start('other') is None


class TestScoreReceiptService:
    """Test ScoreReceiptService"""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Run for every test case"""
        self.service = ScoreReceiptService()

    @pytest.mark.parametrize("name,receipt,score", stubs.receipt_scores)
    def test_scores(self, name: str, receipt: Receipt, score: int):
        """Test score matches expectation"""
        actual_score = self.service.start(receipt)
        assert score == actual_score, f'Failed {name}: {score}!={actual_score}'


class TestGetPointsService:
    """Test GetPointsService"""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, mocker):
        """Run for every test case"""

        # Mocks
        self.get_receipt = mocker.MagicMock()
        self.score_receipt = mocker.MagicMock()
        self.receipt = mocker.MagicMock()

        self.receipt.points = None
        self.get_receipt.start.return_value = self.receipt

        self.service = GetPointsService(
            get_receipt=self.get_receipt,
            score_receipt=self.score_receipt,
        )

    def test_get_correct(self):
        """Test happy path"""

        points = self.service.start(stubs.id)

        self.get_receipt.start.assert_called_once_with(stubs.id)
        self.score_receipt.start.assert_called_once_with(self.receipt)

        assert points == self.score_receipt.start.return_value
        assert self.receipt.points == points

    def test_get_shortcut(self):
        """Test happy path when points already calculated"""

        self.receipt.points = 5
        points = self.service.start(stubs.id)

        self.get_receipt.start.assert_called_once_with(stubs.id)
        self.score_receipt.start.assert_not_called()

        assert points == 5

    def test_get_not_found(self):
        """Test unhappy path with bad id"""

        self.get_receipt.start.return_value = None

        assert self.service.start(stubs.id) is None
