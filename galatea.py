# This file is part galatea_manufacturer module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta
from .tools import slugify

__all__ = ['GalateaWebSiteManufacturer', 'GalateaWebSite']


class GalateaWebSiteManufacturer(ModelSQL, ModelView):
    'Galatea Web Site Manufacturer'
    __name__ = "galatea.website.manufacturer"
    _rec_name = 'party'
    website = fields.Many2One('galatea.website', 'Website', ondelete='CASCADE',
        required=True, select=True)
    party = fields.Many2One('party.party', 'Manufacturer', ondelete='CASCADE',
        required=True, domain=[('manufacturer', '=', True)])
    slug = fields.Char('slug', required=True,
        help='Cannonical uri.')
    description = fields.Text('Description', translate=True,
        help='You could write wiki markup to create html content. Formats text following '
        'the MediaWiki (http://meta.wikimedia.org/wiki/Help:Editing) syntax.')

    @classmethod
    def __setup__(cls):
        super(GalateaWebSiteManufacturer, cls).__setup__()
        cls._order.insert(0, ('party', 'ASC'))

    @classmethod
    def default_website(cls):
        Website = Pool().get('galatea.website')
        websites = Website.search([('active', '=', True)])
        if len(websites) == 1:
            return websites[0].id

    @fields.depends('party', 'slug')
    def on_change_party(self):
        if self.party and not self.slug:
            self.slug = slugify(self.party.name)

    @classmethod
    def copy(cls, manufacturers, default=None):
        new_manufacturers = []
        for manufacturer in manufacturers:
            if manufacturer.slug:
                default['slug'] = '%s-copy' % manufacturer.slug
            new_manufacturer, = super(GalateaWebSiteManufacturer, cls).copy(
                [manufacturer], default=default)
            new_manufacturers.append(new_manufacturer)
        return new_manufacturers


class GalateaWebSite:
    __metaclass__ = PoolMeta
    __name__ = "galatea.website"
    manufacturers = fields.One2Many('galatea.website.manufacturer', 'website',
        'Manufacturers')
