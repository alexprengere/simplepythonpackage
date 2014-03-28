Simple Python Package
=====================

This is a simple Python package containing everything:
documentation, tests, packaging.

Examples
--------

This is an aggregation module:

.. code-block:: python

    >>> from aggregation import aggregate, _read_file

This is an example:

.. code-block:: python

    >>> from StringIO import StringIO
    >>> a = StringIO("""ORY^CDG^2
    ...                 ORY^CDG^3""")
    >>> aggregate(_read_file(a))
    {'ORY': 5.0}

Packaging
---------

Source distribution may be created using:

.. code-block:: bash

 $ python setup.py sdist

Installation may be performed with:

.. code-block:: bash

 $ python setup.py install --user

Tests
-----

.. code-block:: bash

 $ python test.py  -v

