from odoo import api, fields, models, tools, _


class G2PRegion(models.Model):
    _inherit = 'g2p.region'
    _rec_name = 'name'

    province_id = fields.Char(string='Capitol')
    # year_created = fields.Char(string='Created')
    # area_km2 = fields.Float(string='Area')
    # population = fields.Integer(string='Population')
    # pop_density = fields.Float(string='Population Density', compute='_compute_pop_density', store=True)
    sinhala_name = fields.Char(string='Sinhala Name')
    tamil_name = fields.Char(string='Tamil Name')
    active = fields.Boolean(string="Is Active", default=True)

    @api.depends('population', 'area_km2')
    def _compute_pop_density(self):
        for rec in self:
            rec.pop_density = rec.population / rec.area_km2 if rec.area_km2 else 0
