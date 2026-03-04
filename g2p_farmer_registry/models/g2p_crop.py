from odoo import api, fields, models


class G2PCrop(models.Model):
    _name = 'g2p.crop'
    _description = 'G2P Crop'
    _order = 'name'

    name = fields.Char(required=True)
    crop_type_id = fields.Many2one('g2p.crop.type', string='Crop Type')
    crop_category_id = fields.Many2one('g2p.crop.category', string='Crop Category')
    active = fields.Boolean(default=True)
