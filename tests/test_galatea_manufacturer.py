# This file is part of the galatea_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class GalateaManufacturerTestCase(ModuleTestCase):
    'Test Galatea Manufacturer module'
    module = 'galatea_manufacturer'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        GalateaManufacturerTestCase))
    return suite