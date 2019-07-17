"""
helpers.py
Comments: Helper variables, classes, etc to make this API go
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

_endpoints = {
    "base_url": {
        "url": "https://api.youneedabudget.com/v1"
    },
    "budgets": {
        "path": "/budgets/{budget_id}"
    },
    "accounts": {
        "path": "/budgets/{budget_id}/accounts/{account_id}"
    },
    "budgetmonths": {
        "path": "/budgets/{budget_id}/months/{month}"
    },
    "categories": {
        "path": "/budgets/{budget_id}/categories/{category_id}"
    },
    "payees": {
        "path": "/budgets/{budget_id}/payees/{payee_id}"
    },
    "transactions": {
        "path": "/budgets/{budget_id}/transactions/{transaction_id}"
    }
}
