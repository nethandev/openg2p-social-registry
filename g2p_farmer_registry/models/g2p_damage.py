from odoo import api, fields, models, tools, _


class G2PDamage(models.Model):
    _name = 'g2p.damage'
    _description = 'G2P Damage'

    name = fields.Char(string='Name')
    type_id = fields.Many2one('g2p.damage_type')
    stage_id = fields.Many2one('g2p.stage')
    percentage = fields.Float(string='Percentage')
    extent = fields.Float(string='Extent')
    date = fields.Date(string='Date')
    cultivation_details_id = fields.Many2one('g2p.cultivation.details', string='Cultivation Details')
