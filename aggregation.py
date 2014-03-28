#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This is the main documentation.

    >>> from StringIO import StringIO
    >>> a = StringIO('''ORY^CDG^2
    ...                 ORY^CDG^3''')
    >>> aggregate(_read_file(a))
    {'ORY': 5.0}

"""

# For with keyword retro-compatibility
# >= 2.6: not needed
#    2.5: needed
#from __future__ import with_statement


def _read_file(filelike):
    """This reads a filelike and yields flights.

    >>> from StringIO import StringIO
    >>> a = StringIO('''ORY^CDG^2
    ...                 ORY^CDG^3''')
    >>> list(_read_file(a))
    [('ORY', 'CDG', 2.0), ('ORY', 'CDG', 3.0)]
    """
    for row in filelike:
        if not row or row.startswith('#'):
            continue

        row = row.strip().split('^')

        yield row[0], row[1], float(row[2])



def aggregate(flights):
    """This aggregate flights data by origin.

    >>> aggregate([('ORY', 'CDG', 1), ('ORY', 'CDG', 2.0)])
    {'ORY': 3.0}
    """
    data = {}

    for origin, _, volume in flights:
        if origin not in data:
            data[origin] = 0
        data[origin] += volume

    return data


def _test():

    import doctest
    doctest.testmod()


if __name__ == '__main__':

    _test()

    #import sys
    #with open(sys.argv[1]) as fl:
    #    print aggregate(_read_file(fl))

