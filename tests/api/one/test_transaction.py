import pytest

import tests.api.one.env as env_v1
import tests.env as env

from ark.client import ArkClient


ARK = ArkClient(
    env.HOST,
    env.PORT,
    env.NETHASH,
    env_v1.VERSION,
    api_version=env_v1.API_VERSION
)


def test_transaction():
    res = ARK.transaction.transaction(env.TRANSACTION_ID)
    assert res['success'] is True
    assert 'transaction' in res


def test_transactions():
    res = ARK.transaction.transactions()
    assert res['success'] is True
    assert 'transactions' in res
    assert len(res['transactions']) > 1


def test_transactions_with_parameters():
    parameters = {'limit': 1, 'offset': 0}
    res = ARK.transaction.transactions(parameters)
    assert res['success'] is True
    assert 'transactions' in res
    assert len(res['transactions']) == 1


@pytest.mark.skip('Need to create transaction to test unconrfirmed transaction')
def test_unconfirmed_transaction():
    parameters = {'orderBy': 'timestamp:desc',
                  'limit': 1}
    res = ARK.transaction.transactions(parameters)
    assert res['success'] is True
    id_ = res['transactions'][0]['id']
    res = ARK.transaction.unconfirmed_transaction(id_)
    assert res['success'] is True
    assert 'transaction' in res


def test_unconfirmed_transactions():
    res = ARK.transaction.unconfirmed_transactions()
    assert res['success'] is True
    assert 'transactions' in res


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_create():
    assert False