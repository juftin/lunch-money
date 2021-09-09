# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money Python SDK - This Module Leverages Class Inheritance to
Distribute API Methods Across a series of files. Ultimately, everything
inherits from the lunchmoney.sdk.core.LunchMoneyCore class which facilitates
interacting with the API.

For example: to see source code on interactions with the "transactions" API endpoint you
will refer to the LunchMoneyTransactions object.
"""

from .assets import LunchMoneyAssets
from .budgets import LunchMoneyBudgets
from .plaid_accounts import LunchMoneyPlaidAccounts
from .recurring_expenses import LunchMoneyRecurringExpenses
from .transactions import LunchMoneyTransactions


class LunchMoney(
    LunchMoneyAssets,
    LunchMoneyBudgets,
    LunchMoneyPlaidAccounts,
    LunchMoneyRecurringExpenses,
    LunchMoneyTransactions,
):
    """
    Core Lunch Money SDK.
    """

    pass
