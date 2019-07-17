"""
__init__.py
Comments: Base classes for all other models
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""


class JsonDict(object):
    """
    Custom dict blueprint class for upstream objects to inherit.
    """

    fields = dict()

    def __init__(self):
        super().__setattr__("_keys",  list())

    def __str__(self):
        d = ", ".join([f"{k} : {v}" for k, v in self.items()])
        return f"<{self.__class__.__name__} [{len(self._keys)}]: {d}>"

    __repr__ = __str__

    def __getattr__(self, item):
        return self.__getattribute__(item)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key not in self._keys:
            self._keys.append(key)

    def __delattr__(self, item):
        if item in self:
            self._keys.remove(item)
            delattr(self, item)

    def __contains__(self, item):
        return hasattr(self, item)

    def __len__(self):
        return len(self._keys)

    def from_json_dict(self, json_data):
        """
        Class method for creating the proper incoming Ynab object. The incoming data needs to be a dict type object

        :param json_data: The json data provided by the Ynab API
        :return: Returning he proper calling Ynab single data object. See objects defined in pynab.model.*
        """

        for k, v in list(self.fields.items()):
            setattr(self, k, json_data[k])

        return self

    def items(self):
        return iter([(k, getattr(self, k)) for k in self._keys if not k.startswith("_")])


class JsonList(object):
    """
    Custom list blueprint class for upstream objects to inherit.
    """

    def __init__(self):
        self._data = list()

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        return f"<{self.__class__.__name__} [{len(self._data)}]>"

    __repr__ = __str__

    def __len__(self):
        return len(self._data)

    def from_json_list(self, cls, initlist):
        """
         Class method for creating the proper incoming Ynab object. The incoming data needs to be a list type object.
         This method would also be provided a single type object for generating a list of these singular items.

        :param cls: The single item Ynab object type to to return as a list.
        :param initlist: The list of json objects to create objects from.
        :return: Returning a list of singular Ynab data type objects.
        """

        for item in initlist:
            obj = cls()
            obj.from_json_dict(item)
            self._data.append(obj)
        return self

    def append(self, item):
        self._data.append(item)
