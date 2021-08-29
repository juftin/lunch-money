# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Transactions

https://lunchmoney.dev/#transactions
"""

import datetime
import logging
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class TransactionsObject(BaseModel):
    """
    https://lunchmoney.dev/#transaction-object
    """
    id: Optional[int]
    date: str
    amount: float
    payee: Optional[str]
    currency: Optional[str]
    status: Optional[str]
    category_id: Optional[int]
    asset_id: Optional[int]
    parent_id: Optional[int]
    plaid_account_id: Optional[int]
    is_group: Optional[bool]
    group_id: Optional[int]
    external_id: Optional[str]
    tags: Optional[List[str]]
    notes: Optional[str]


class TransactionInsertObject(BaseModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """
    date: datetime.date
    amount: float
    category_id: Optional[int]
    payee: Optional[str]
    currency: Optional[str]
    asset_id: Optional[int]
    recurring_id: Optional[int]
    notes: Optional[str]
    status: Optional[str]
    external_id: Optional[str]
    tags: Optional[List[Any]]


class TransactionUpdateObject(BaseModel):
    """
    https://lunchmoney.dev/#update-transaction
    """
    date: Optional[datetime.date]
    amount: Optional[float]
    category_id: Optional[int]
    payee: Optional[str]
    currency: Optional[str]
    asset_id: Optional[int]
    recurring_id: Optional[int]
    notes: Optional[str]
    status: Optional[str]
    external_id: Optional[str]
    tags: Optional[List[Any]]


class TransactionParamsGet(BaseModel):
    """
    https://lunchmoney.dev/#get-all-transactions
    """
    start_date: Optional[datetime.date]
    end_date: Optional[datetime.date]


class TransactionInsertParamsPost(BaseModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """
    transactions: List[TransactionInsertObject]
    apply_rules: bool = False
    skip_duplicates: bool = False
    check_for_recurring: bool = False
    debit_as_negative: bool = False
    skip_balance_update: bool = True


class TransactionUpdateParamsPut(BaseModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """
    split: Optional[bool]
    transaction: TransactionUpdateObject
    debit_as_negative: bool = False
    skip_balance_update: bool = True


class LunchMoneyTransactions(LunchMoneyCore):
    """
    Lunch Money Transactions Interactions
    """

    def get_transactions(self,
                         start_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
                         end_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
                         params: Optional[dict] = None
                         ) -> List[TransactionsObject]:
        """
        Use this to retrieve all transactions between a date range. Returns list of Transaction
        objects. If no query parameters are set, this will return transactions for the
        current calendar month. If either start_date or _end_date are datetime.datetime objects,
        they will be reduced to dates. If a string is provided, it will be attempted to be parsed
        as YYYY-MM-DD format

        Parameters
        ----------
        start_date: Optional[Union[datetime.date, datetime.datetime, str]]:
            start date for search
        end_date: Optional[Union[datetime.date, datetime.datetime, str]]
            end date for search
        params: Optional[dict]
            additional parameters to pass to the API

        Returns
        -------
        List[TransactionsObject]
        """
        search_params = TransactionParamsGet(start_date=start_date,
                                             end_date=end_date).dict(exclude_none=True)
        if params is not None:
            search_params.update(params)
        response_data = self._make_request(method="GET",
                                           url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
                                           params=search_params)
        transactions = response_data[APIConfig.LUNCHMONEY_TRANSACTIONS]
        transaction_objects = [TransactionsObject(**item) for item in transactions]
        return transaction_objects

    def get_transaction(self, transaction_id: int) -> TransactionsObject:
        """
        Returns a single Transaction object

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID

        Returns
        -------
        Dict[str, Any]
        """
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     transaction_id])
        return TransactionsObject(**response_data)

    def update_transaction(self, transaction_id: int,
                           transaction: TransactionUpdateObject,
                           split: Optional[object] = None,
                           debit_as_negative: bool = False,
                           skip_balance_update: bool = True) -> Dict[str, Any]:
        """
        Returns a single Transaction object

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID
        transaction: TransactionUpdateObject
            Object to update with
        split: object
            Defines the split of a transaction. You may not split an already-split
            transaction, recurring transaction, or group transaction.
        debit_as_negative: bool
            If true, will assume negative amount values denote expenses and
            positive amount values denote credits. Defaults to false.
        skip_balance_update: bool
            If false, will skip updating balance if an asset_id
            is present for any of the transactions.

        Returns
        -------
        Dict[str, Any]
        """
        response_data = TransactionUpdateParamsPut(transaction=transaction,
                                                   split=split,
                                                   debit_as_negative=debit_as_negative,
                                                   skip_balance_update=skip_balance_update
                                                   ).dict(exclude_unset=True)
        response_data = self._make_request(method="PUT",
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     transaction_id],
                                           json=response_data)
        return response_data
