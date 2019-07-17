"""
budget.py
Comments: Data objects for Budget information
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from .account import *
from .payee import *
from .category import *
from .budgetmonth import *
from . import JsonDict, JsonList


class CurrencyFormat(JsonDict):

    fields = {
        "iso_code": str(),
        "example_format": str(),
        "decimal_digits": int(),
        "decimal_separator": str(),
        "symbol_first": bool(),
        "group_separator": str(),
        "currency_symbol": str(),
        "display_symbol": bool()
    }

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"<{self.__class__.__name__} [{len(self._keys)}]>"


class Budget(JsonDict):

    fields = {
        "id": str(),
        "name": str(),
        "last_modified_on": str(),
        "first_month": str(),
        "last_month": str(),
        "date_format": object(),
        "currency_format": object()
    }

    expand_fields = {
        "accounts": object(),
        "payees": object(),
        "category_groups": object(),
        "categories": object(),
        "months": object()
    }

    def from_json_dict(self, json_data, expand=False):

        d = super().from_json_dict(json_data)

        setattr(d, "date_format", json_data["date_format"]["format"])
        setattr(d, "currency_format", CurrencyFormat().from_json_dict(json_data["currency_format"]))

        if expand:
            setattr(d, "accounts", Accounts().from_json_list(Account, json_data["accounts"]))
            setattr(d, "payees", Payees().from_json_list(Payee, json_data["payees"]))
            setattr(d, "category_groups", BudgetCategoryGroups().from_json_list(BudgetCategoryGroup,
                                                                                json_data["category_groups"]))
            setattr(d, "categories", BudgetCategories().from_json_list(BudgetCategory,
                                                                       {"categories": json_data["categories"]}))
            setattr(d, "months", BudgetMonths().from_json_list(BudgetMonth, json_data["months"]))

        return d

    def __init__(self):
        super().__init__()


class Budgets(JsonList):

    def __init__(self):
        super().__init__()

