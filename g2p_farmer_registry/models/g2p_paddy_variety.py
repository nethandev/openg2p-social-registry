from odoo import models, fields


class PaddyVariety(models.Model):
    _name = 'g2p.paddy.variety'
    _description = 'Paddy Variety'

    category_id = fields.Many2one('g2p.crop.category', string="Category")
    age_group = fields.Selection(
        [
            ('short', 'Short Duration'),
            ('medium', 'Medium Duration'),
            ('long', 'Long Duration'),
        ], string="Age Group")
    cultivation_days = fields.Integer(string="Cultivation Days")
    variety_name = fields.Char(string="Variety Name", required=True)
    variety_type = fields.Selection(
        [
            ('hybrid', 'Hybrid'),
            ('traditional', 'Traditional'),
            ('organic', 'Organic'),
        ], string="Variety Type")
    active = fields.Boolean(default=True)
