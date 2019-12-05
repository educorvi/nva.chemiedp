import doctest
import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import nva.chemiedp

OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS

ptc.setupPloneSite(products=['nva.chemiedp'])


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            zcml.load_config('configure.zcml',
              nva.chemiedp)

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='nva.chemiedp',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='nva.chemiedp.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'INTEGRATION.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

        # -*- extra stuff goes here -*-

        # Integration tests for ReinigungsmittelEtiketten
        ztc.ZopeDocFileSuite(
            'ReinigungsmittelEtiketten.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for ReinigungsmittelManuell
        ztc.ZopeDocFileSuite(
            'ReinigungsmittelManuell.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Druckbestaeubungspuder
        ztc.ZopeDocFileSuite(
            'Druckbestaeubungspuder.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Produktdatenblatt
        ztc.ZopeDocFileSuite(
            'Produktdatenblatt.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Maschine
        ztc.ZopeDocFileSuite(
            'Maschine.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Hersteller
        ztc.ZopeDocFileSuite(
            'Hersteller.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for ProduktOrdner
        ztc.ZopeDocFileSuite(
            'ProduktOrdner.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for MaschinenOrdner
        ztc.ZopeDocFileSuite(
            'MaschinenOrdner.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for HerstellerOrdner
        ztc.ZopeDocFileSuite(
            'HerstellerOrdner.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for DatenbankChemieDP
        ztc.ZopeDocFileSuite(
            'DatenbankChemieDP.txt',
            package='nva.chemiedp',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
