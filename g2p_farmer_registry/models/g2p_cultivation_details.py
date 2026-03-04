from odoo import api, fields, models, _, exceptions


class G2PCultivationDetails(models.Model):
    _name = 'g2p.cultivation.details'

    season_id = fields.Many2one('g2p.season', string=_('Season'))
    partner_id = fields.Many2one('res.partner', string=_('Farmer'))
    land_id = fields.Many2one(comodel_name='g2p.land.details', string=_('Land details'),
                              domain="[('partner_id', '=', partner_id)]")
    district_id = fields.Many2one('g2p.district', string=_('District'))
    district_approve =fields.Boolean(string=_('Approve'))
    asc_id = fields.Many2one('g2p.agrarian.service.center', string=_("ASC"), domain="[('district_id', '=', district_id)]")
    asc_approve = fields.Boolean(string=_('ASC Approve'))
    # code = fields.Char(related='asc_id.asc_code', string=_('ASC Code'))
    plr_number = fields.Char(string=_('PLR Number'))
    irrigation = fields.Selection([
        ('1-Major', '1-Major'),
        ('2-Minor', '2-Minor'),
        ('3-Rainfed', '3-Rainfed'), ], string=_("Irrigation"))
    land_extent = fields.Float(string=_('Land Extent (HA)'))
    cultivated_extend = fields.Float(string=_('Cultivated Extent (HA)'))
    cultivated_date = fields.Date(string=_('Cultivated Date'))
    data_entered = fields.Datetime(string=_('Data Enter'))
    last_update = fields.Datetime(string=_('Last Update'))
    status_id = fields.Many2one('status.cultivation', string=_('Status'))
    harvested_extent = fields.Float(string='Harvested Extent (HA)')
    harvested_yield = fields.Float(string='Harvested Yield (kg/HA)')  # or total kg if preferred
    harvested_date = fields.Date(string='Harvested Date')
    invalid = fields.Boolean(string=_('Invalid'))
    crop_id = fields.Many2one('g2p.crop', string=_('Crop'))
    crop_type_id = fields.Many2one('g2p.crop.type', string='Crop Type')
    crop_category_id = fields.Many2one('g2p.crop.category', string='Crop Category')
    damage_id = fields.One2many('g2p.damage','cultivation_details_id', string=_('Damage'))
    paddy_damage = fields.Float(string=_('Paddy Damage'))
    slip_generate = fields.Boolean(string=_('Slip Generate'))
    remark = fields.Char(string=_('Remark'))

    @api.onchange('land_id')
    def _onchange_land_id(self):
        if self.land_id:
            # Copy values from the selected land record
            self.district_id = self.land_id.district_id
            self.asc_id = self.land_id.asc_id  # if it matches the district
            self.plr_number = self.land_id.plr_number
            self.irrigation = self.land_id.irrigation
            self.land_extent = self.land_id.land_extent

            # Optional: force domain refresh if needed (usually not necessary)
            # return {'domain': {'asc_id': [('district_id', '=', self.district_id.id)]}}
        else:
            # Optional: clear fields when land is removed
            self.district_id = False
            self.asc_id = False
            self.plr_number = False
            self.irrigation = False
            self.land_extent = 0.0
