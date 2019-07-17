"""
transaction.py
Comments: Data objects for Transaction and sub-Transaction information
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from . import JsonDict, JsonList


class SubTransaction(JsonDict):
    """
    Single Sub-Transaction object
    """

    fields = {
        "id": str(),
        "transaction_id": str(),
        "amount": int(),
        "memo": str(),
        "payee_id": str(),
        "category_id": str(),
        "transfer_account_id": str(),
        "deleted": bool()
    }

    def __init__(self):
        super().__init__()


class SubTransactions(JsonList):
    """
    An object that includes a list of single sub-transaction objects
    """

    def __init__(self):
        super().__init__()


class Transaction(JsonDict):
    """
    Single Transaction object
    """

    def __index__(self):
        super().__init__()

    def from_json_dict(self, json_data):

        d = super().from_json_dict(json_data)

        if json_data["subtransactions"]:
            setattr(self, "subtransactions", SubTransactions().from_json_list(SubTransaction,
                                                                              json_data["subtransactions"]))

        return d

    fields = {
        "id": str(),
        "date": str(),
        "amount": int(),
        "memo": str(),
        "cleared": str(),
        "approved": bool(),
        "flag_color": str(),
        "account_id": str(),
        "payee_id": str(),
        "category_id": str(),
        "transfer_account_id": str(),
        "transfer_transaction_id": str(),
        "matched_transaction_id": str(),
        "import_id": str(),
        "deleted": bool(),
        "account_name": str(),
        "payee_name": str(),
        "category_name": str(),
        "subtransactions": list()
    }

    def __init__(self):
        super().__init__()


class Transactions(JsonList):
    """
    An object that includes a list of single transaction objects
    """

    def __init__(self):
        super().__init__()
