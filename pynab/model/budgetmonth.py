"""
budgetmonth.py
Comments: Data objects for Budget Month information
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from . import JsonDict, JsonList


class BudgetMonth(JsonDict):
    """
    BudgetMonth object is a single month's collection of data returned by the API.

    This object is subclasses JasonDict which is a universal dictionary object
    """

    fields = {
        "month": str(),
        "note": str(),
        "income": int(),
        "budgeted": int(),
        "activity": int(),
        "to_be_budgeted": int(),
        "age_of_money": int(),
        "deleted": bool()
    }

    def __init__(self):
        super().__init__()

    def extend(self):
        # TODO: Figure out how to extend self with a categories attr if this was a summary obj
        # if hasattr(self, "categories"):
        # self._set_categories(????)
        pass


class BudgetMonths(JsonList):
    """
    BudgetMonths is a collection list of BudgetMonth objects containing multiple months.

    This object is subclasses JasonList which is a universal list object
    """

    def __init__(self):
        super().__init__()
