"""
account.py - desc
Comments: 
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright © 2019, iRunAsRoot 
"""

from . import JsonDict, JsonList


class Account(JsonDict):
    """
    Single account object
    """

    fields = {
        "id": str(),
        "name": str(),
        "type": str(),
        "on_budget": bool(),
        "closed": bool(),
        "note": str(),
        "balance": int(),
        "cleared_balance": int(),
        "uncleared_balance": int(),
        "transfer_payee_id": str(),
        "deleted": int()
    }

    def __init__(self):
        super().__init__()


class Accounts(JsonList):
    """
    An object that includes a list of single account objects
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        d = ", ".join([i.name for i in self._data])
        return f"<{self.__class__.__name__} [{len(self._data)}]: {d}>"
