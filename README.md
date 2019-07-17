# pynab-client
Python API module for interfacing with You Need a Budget's (YNAB) v1 API

Only runs on python >3.6 .....#sorrynotsorry

## installation
Easy way
```bash
pip install pynab-client
```

Less easy way
```bash
git clone https://github.com/irunasroot/pynab-client.git
cd pynab-client
python setup.py install
```

## Usage
```python
from pynabapi import YnabClient

client = YnabClient("my-api-token")

my_budgets = client.get_budget()
```

## API

YnabClient.get_budget()
```text
The mother load. By default you'll get a summary list of all Budgets you have on your account. If you're looking
for a single budget you can specify the budget_id or by default it will pull data for the last opened budget.

:param summary: Set summary to False if you want an entire payload of a single budget
    :default: True
:param budget_id: The budget id of the budget you want to view data from.
    :default: last-used which is your last opened budget.
:return: Returns Budgets object as a list of Budget objects or a single Budget object
```

YnabClient.get_account()  
```text
:param account_id: Provide account_id to retrieve a single known account.  
    :default: None
:param budget_id: The budget id of the budget you want to view data from.  
    :default: last-used which is your last opened budget.  
:return: Returns Accounts object as a list of Account objects or a single Account object  
```

YnabClient.get_budgetmonth()
```text
Get budget month or months. If specifying the month then a list of categories are also provided.

:param month: Provide month to retrieve a single known month.
    :default: None
:param budget_id: The budget id of the budget you want to view data from.
    :default: last-used which is your last opened budget.
:return: Returns BudgetMonths object as a list of BudgetMonth objects or a single BudgetMonth object
```

YnabClient.get_category()
```text
Get budget category or categories. If specifying the month then you also need to specify a category_id

:param category_id: The category ID of the specific category you want to retrieve
    :default: None
:param month: The month of the category you want to retrieve format: yyyy-MM-dd
    :default: None
:param budget_id: The budget id of the budget you want to view data from.
    :default: last-used which is your last opened budget.
:return: Returns BudgetCategories object as a list of BudgetCategory objects or a single BudgetCategory object
```

YnabClient.get_payee()
```text
Get budget payee or payees.

:param payee_id: Provide payee_id to retrieve a single known payee.
:param budget_id: The budget id of the budget you want to view data from.
    :default: last-used which is your last opened budget.
:return: Returns Payees object as a list of Payee objects or a single Payee object
```

YnabClient.get_transaction()
```text
Get budget transaction or transactions.

:param transaction_id: Provide transaction_id to retrieve a single known transaction.
    :default: None
:param budget_id: The budget id of the budget you want to view data from.
    :default: last-used which is your last opened budget.
:return: Returns Transactions object as a list of Transaction objects or a single Transaction object
```
