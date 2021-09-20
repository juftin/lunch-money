"""
Run Tests on the Crypto Endpoint
"""

import logging

from conftest import lunchable_cassette
from lunchable import LunchMoney
from lunchable.models.crypto import CryptoObject

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_crypto(lunch_money_obj: LunchMoney):
    """
    Get Crypto and assert its Crypto
    """
    cryptos = lunch_money_obj.get_crypto()
    assert len(cryptos) >= 1
    for crypto in cryptos:
        assert isinstance(crypto, CryptoObject)
    logger.info("%s Crypto Accounts returned", len(cryptos))


@lunchable_cassette
def test_update_crypto(lunch_money_obj: LunchMoney):
    """
    Update a Crypto Object
    """
    crypto = lunch_money_obj.update_crypto(crypto_id=2939,
                                           balance=0.50)
    assert isinstance(crypto, CryptoObject)
    logger.info("Crypto Asset Updated: %s", crypto.id)
