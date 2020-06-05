class Shotdetails(object):
    """ Examples of built-in methods.
    """
    def __init__(self, value=None):
        self._shot_details =value if value.__class__ == dict else {}

    def __repr__(self):
        return "{}.{}({})".format(self.__module__, self.__class__.__name__, self._shot_details)

    def __contains__(self, key):
        return True if key in self._shot_details else False

    def __setitem__(self, key, value):
        self._shot_details[key] = value

    def __getitem__(self, key):
        return self._shot_details[key]
