from odoo import fields, models, api


class G2PDamageStage(models.Model):
    _name = 'g2p.damage.stage'
    _description = 'G2P Damage Stage'
    _order = 'name'

    name = fields.Char(required=True)
