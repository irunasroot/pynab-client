"""
payee.py
Comments: Data objects for Payee information
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from . import JsonDict, JsonList


class Payee(JsonDict):
    """
    Single payee object
    """

    fields = {
        "id": str(),
        "name": str(),
        "transfer_account_id": str(),
        "deleted": bool()
    }

    def __init__(self):
        super().__init__()


class Payees(JsonList):
    """
    An object that includes a list of single payee objects
    """

    def __init__(self):
        super().__init__()
