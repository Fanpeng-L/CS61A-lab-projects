def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"
    t = []
    if odd == True:
        for item in lst:
            if item % 2 != 0:
                t.append(item)
        return t
    else:
        for item in lst:
            if item % 2 == 0:
                t.append(item)
        return t



class SmartFridge:
    """"
    The SmartFridge class is used by smart refrigerators to track which items 
    are in the fridge and let owners know when an item has run out.

    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Uh oh, buy more Mayo!'
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        self.items[item]
        self.quantity = quantity

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
