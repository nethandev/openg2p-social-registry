from odoo import models, fields, _


class FloodDamageSubsidy(models.Model):
    _name = "g2p.flood.damage.subsidy"
    _description = "Flood Damage Subsidy Details"

    partner_id = fields.Many2one("res.partner", string="Farmer", required=True, ondelete="cascade")
    land_id = fields.Many2one(comodel_name='g2p.land.details', string=_('Land details'))
    plr_number = fields.Char(string=_("PLR Number"))

    # change here,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    farmer_bank_id = fields.Many2one(comodel_name='res.partner.bank', string=_('Farmer Bank'), domain="[('partner_id', '=', partner_id)]")
    branch_id = fields.Many2one('g2p.bank.branch', related="farmer_bank_id.branch_id")
    bank_id = fields.Many2one('res.bank', related="branch_id.bank_id")
    # bank_code = fields.Char(string=_("Bank Code"), related="farmer_bank_id.bank_code")
    # branch_code = fields.Char(string=_("Branch Code"), related="farmer_bank_id.branch_code")
    account_no = fields.Char(string=_("Account No"))
    damage_type = fields.Char(string=_("Damage Type"))
    full_damage_extent = fields.Float(string=_("Full Damage Extent"))
    partial_damage = fields.Float(string=_("Partial Damage"))
    not_cultivated_extent = fields.Float(string=_("Not Cultivated Extent"))
    recommended_extent = fields.Float(string=_("Recommended Extent"))
    amount = fields.Float(string=_("Amount"))
    transaction_date = fields.Datetime(string=_("Transaction Date"))
    status_id = fields.Many2one('status.flood', string=_('Status'))
