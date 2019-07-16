"""
category.py
Comments: Data objects for Budget Category information
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from . import JsonDict, JsonList


class BudgetCategoryGroup(JsonDict):
    fields = {
        "id": str(),
        "name": str(),
        "hidden": bool(),
        "deleted": bool()
    }

    def __init__(self):
        super().__init__()


class BudgetCategoryGroups(JsonList):

    def __init__(self):
        super().__init__()


class BudgetCategory(JsonDict):

    fields = {
            "id": str(),
            "category_group_id": str(),
            "name": str(),
            "hidden": bool(),
            "original_category_group_id": str(),
            "note": str(),
            "budgeted": int(),
            "activity": int(),
            "balance": int(),
            "goal_type": str(),
            "goal_creation_month": str(),
            "goal_target": int(),
            "goal_target_month": str(),
            "goal_percentage_complete": int(),
            "deleted": bool()
    }

    def __init__(self):
        super().__init__()

    def set_category(self):
        pass


class BudgetCategories(JsonList):

    def __init__(self):
        super().__init__()

    def from_json_list(self, cls, initlist):
        """
         Class method for creating the proper incoming Ynab object. The incoming data needs to be a list type object.
         This method would also be provided a single type object for generating a list of these singular items.

        :param cls: The single item Ynab object type to to return as a list.
        :param initlist: The list of json objects to create objects from.
        :return: Returning a list of singular Ynab data type objects.
        """

        if isinstance(initlist, dict):
            initlist = [initlist]

        for group in initlist:
            for cat in group["categories"]:
                obj = cls()
                obj.from_json_dict(cat)

                if "id" in group:
                    setattr(obj, "group", BudgetCategoryGroup().from_json_dict(group))

                self.append(obj)
        return self
