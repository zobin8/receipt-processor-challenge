"""Tests for the /receipts endpoints"""

import pytest
from flask.testing import FlaskClient

from receipt_processor.restapi import flask_app

from . import stubs


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


class TestIntegration:
    """Test endpoint integration"""

    @pytest.mark.parametrize('json,score', stubs.integration_tests)
    def test_integration(self, client: FlaskClient, json: dict, score: int):
        """Integration test with examples"""
        res = client.post(
            '/receipts/process',
            json=json
        )

        assert res.status_code == 200
        assert 'id' in res.json
        id = res.json['id']

        res2 = client.get(f'/receipts/{id}/points')

        assert res2.status_code == 200
        assert res2.json == dict(points=score)


class TestProcess:
    """Test /receipts/procss endpoint"""

    @pytest.mark.parametrize('json', stubs.bad_syntax)
    def test_bad_syntax(self, client: FlaskClient, json: dict):
        """Test unhappy case when body has bad syntax"""

        res = client.post(
            '/receipts/process',
            json=json
        )

        assert res.status_code == 400


class TestPoints:
    """Test /receipts/<id>/points endpoint"""

    def test_404(self, client: FlaskClient):
        """Test unhappy case when object does not exist"""

        res = client.get('/receipts/does_not_exist/points')

        assert res.status_code == 404
