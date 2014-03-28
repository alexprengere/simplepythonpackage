#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import doctest

import aggregation as agg


class AggregationTest(unittest.TestCase):

    def test_aggregation(self):

        flights = [
            ('ORY', 'CDG', 2),
            ('ORY', 'CDG', 3)
        ]
        self.assertEquals(agg.aggregate(flights), {'ORY': 5.0})


def main():

    s = unittest.TestSuite()

    s.addTests(unittest.makeSuite(AggregationTest))
    s.addTests(doctest.DocTestSuite(agg))
    s.addTests(doctest.DocFileSuite('README.rst'))

    return s


if __name__ == '__main__':

    unittest.main(defaultTest='main')

