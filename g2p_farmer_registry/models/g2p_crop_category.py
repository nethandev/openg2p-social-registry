from odoo import fields, models, api


class G2pCropCategory(models.Model):
    _name = 'g2p.crop.category'
    _description = 'G2P Crop Category'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
