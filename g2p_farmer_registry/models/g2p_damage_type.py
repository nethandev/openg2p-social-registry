from odoo import api, fields, models


class G2PDamageType(models.Model):
    _name = 'g2p.damage.type'
    _description = 'G2P Damage Type'

    name = fields.Char(required=True)
