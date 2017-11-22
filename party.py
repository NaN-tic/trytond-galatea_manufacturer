from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Party']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'
    website_manufacturer = fields.One2Many('galatea.website.manufacturer',
        'party', 'Website Manufacturer')
