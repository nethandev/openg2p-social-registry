from odoo import models, fields, _


class SubsidyDetail(models.Model):
    _name = "g2p.subsidy.detail"
    _description = "Subsidy Details"

    partner_id = fields.Many2one("res.partner", string=_("Farmer"), required=True, ondelete="cascade", )
    cultivation_id = fields.Many2one("g2p.cultivation.details", string=_("Cultivation Details"))
    season_id = fields.Many2one('g2p.season', string=_('Season'))
    subsidy_type = fields.Char(string=_("Subsidy Type"))
    district_id = fields.Many2one('g2p.district', string=_('District'))
    asc_id = fields.Many2one('g2p.agrarian.service.center', string=_("ASC"), domain="[('district_id', '=', district_id)]")
    plr_number = fields.Char(string=_("PLR Number"))
    land_extent = fields.Float(string=_("Land Extent (HA)"))
    amount_quantity = fields.Char(string=_("Amount/Quantity"))
    # status = fields.Char(string=_("Status"))
    status_id = fields.Many2one('status.subsidy', string=_('Status'))
