from odoo import api, fields, models


class G2PCropType(models.Model):
    _name = 'g2p.crop.type'
    _description = 'G2P Crop Type'

    name = fields.Char(required=True)
