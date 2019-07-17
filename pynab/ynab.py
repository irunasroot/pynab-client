"""
ynab.py
Comments: Main Ynab API
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

import requests
import re

from .helpers import _endpoints
from .exceptions import *

from .model.budget import *
from .model.budgetmonth import *
from .model.category import *
from .model.account import *
from .model.payee import *
from .model.transaction import *

re_month_format = re.compile("20[0-9]{2}-[0|1][0-9]-[0|1][0-9]")


class YnabClient:

    def __init__(self, token):
        self.headers = {"Accept": "application/json"}

        if token:
            self._token = token
            self._auth_header = {"Authorization":  f"Bearer {self._token}"}
        else:
            raise YnabException("Personal token not specified")

        self.headers.update(self._auth_header)
        self.url = _endpoints["base_url"]["url"]

    def _request_stuff(self, endpoint, headers=None):

        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint

        if endpoint.endswith("/"):
            endpoint = endpoint.rstrip("/")

        if headers and type(headers) == dict:
            headers.update(self.headers)
        else:
            headers = self.headers.copy()

        api_call = requests.get(f"{self.url}{endpoint}", headers=headers)

        if api_call.status_code != 200:
            raise YnabConnectionError("Unable to call API endpoint: {}".format(api_call.status_code))

        d = api_call.json()["data"]

        return d

    def get_account(self, account_id=None, budget_id="last-used"):
        """
        Get budget account or accounts.

        :param account_id: Provide account_id to retrieve a single known account.
            :default: None
        :param budget_id: The budget id of the budget you want to view data from.
            :default: last-used which is your last opened budget.
        :return: Returns Accounts object as a list of Account objects or a single Account object
        """

        d = self._request_stuff(_endpoints["accounts"]["path"].format(budget_id=budget_id,
                                                                      account_id=account_id if account_id else ""))

        acc = None

        if account_id:
            acc = Account().from_json_dict(d["account"])
        elif not account_id:
            acc = Accounts().from_json_list(Account, d["accounts"])

        return acc

    def get_budget(self, summary=True, budget_id="last-used"):
        """
        The mother load. By default you'll get a summary list of all Budgets you have on your account. If you're looking
        for a single budget you can specify the budget_id or by default it will pull data for the last opened budget.

        :param summary: Set summary to False if you want an entire payload of a single budget
            :default: True
        :param budget_id: The budget id of the budget you want to view data from.
            :default: last-used which is your last opened budget.
        :return: Returns Budgets object as a list of Budget objects or a single Budget object
        """

        d = self._request_stuff(_endpoints["budgets"]["path"].format(budget_id=budget_id if not summary else ""))

        bud = None

        if summary:
            bud = Budgets().from_json_list(Budget, d["budgets"])
        elif not summary:
            bud = Budget().from_json_dict(d["budget"], True)

        return bud

    def get_budgetmonth(self, month=None, budget_id="last-used"):
        """
        Get budget month or months. If specifying the month then a list of categories are also provided.

        :param month: Provide month to retrieve a single known month.
            :default: None
        :param budget_id: The budget id of the budget you want to view data from.
            :default: last-used which is your last opened budget.
        :return: Returns BudgetMonths object as a list of BudgetMonth objects or a single BudgetMonth object
        """

        if month and not re_month_format.match(month):
            raise YnabValueError(f"Invalid Date format for {month}. Please use format yyyy-MM-dd")

        d = self._request_stuff(_endpoints["budgetmonths"]["path"].format(budget_id=budget_id,
                                                                          month=month if month else ""))

        bm = None

        if month:
            bm = BudgetMonth().from_json_dict(d["month"])
            bm.categories = BudgetCategories().from_json_list(BudgetCategory, d["month"])
        elif not month:
            bm = BudgetMonths().from_json_list(BudgetMonth, d["months"])

        return bm

    def get_category(self, category_id=None, month=None, budget_id="last-used"):
        """
        Get budget category or categories. If specifying the month then you also need to specify a category_id

        :param category_id: The category ID of the specific category you want to retrieve
            :default: None
        :param month: The month of the category you want to retrieve format: yyyy-MM-dd
            :default: None
        :param budget_id: The budget id of the budget you want to view data from.
            :default: last-used which is your last opened budget.
        :return: Returns BudgetCategories object as a list of BudgetCategory objects or a single BudgetCategory object
        """

        if month and not re_month_format.match(month):
            raise YnabValueError(f"Invalid Date format for {month}. Please use format yyyy-MM-dd")

        cat = None
        endpoint = None

        if month:
            if not category_id:
                YnabValueError("Category ID not specified")

            endpoint = (_endpoints["budgetmonths"]["path"] + "/categories/{category_id}")\
                .format(budget_id=budget_id, month=month, category_id=category_id)
        elif not month:
            endpoint = _endpoints["categories"]["path"].format(budget_id=budget_id,
                                                               category_id=category_id if category_id else "")

        d = self._request_stuff(endpoint)

        if category_id or month:
            cat = BudgetCategory().from_json_dict(d["category"])
        elif not month:
            cat = BudgetCategories().from_json_list(BudgetCategory, d["category_groups"])

        return cat

    def get_payee(self, payee_id=None, budget_id="last-used"):
        """
        Get budget payee or payees.

        :param payee_id: Provide payee_id to retrieve a single known payee.
        :param budget_id: The budget id of the budget you want to view data from.
            :default: last-used which is your last opened budget.
        :return: Returns Payees object as a list of Payee objects or a single Payee object
        """

        d = self._request_stuff(_endpoints["payees"]["path"].format(budget_id=budget_id,
                                                                    payee_id=payee_id if payee_id else ""))

        pay = None

        if payee_id:
            pay = Payee().from_json_dict(d["payee"])
        elif not payee_id:
            pay = Payees().from_json_list(Payee, d["payees"])

        return pay

    def get_transaction(self, transaction_id=None, budget_id="last-used"):
        """
        Get budget transaction or transactions.

        :param transaction_id: Provide transaction_id to retrieve a single known transaction.
            :default: None
        :param budget_id: The budget id of the budget you want to view data from.
            :default: last-used which is your last opened budget.
        :return: Returns Transactions object as a list of Transaction objects or a single Transaction object
        """

        d = self._request_stuff(_endpoints["transactions"]["path"].format(budget_id=budget_id,
                                                                          transaction_id=transaction_id if
                                                                          transaction_id else ""))

        tran = None

        if transaction_id:
            tran = Transaction().from_json_dict(d["transaction"])
        elif not transaction_id:
            tran = Transactions().from_json_list(Transaction, d["transactions"])

        return tran



