# This file is part galatea_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .galatea import *
from .party import *

def register():
    Pool.register(
        GalateaWebSiteManufacturer,
        GalateaWebSite,
        Party,
        module='galatea_manufacturer', type_='model')
