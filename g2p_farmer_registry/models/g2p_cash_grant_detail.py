from odoo import models, fields, _


class CashGrantDetail(models.Model):
    _name = "g2p.cash.grant.detail"
    _description = "Cash Grant Details"

    partner_id = fields.Many2one("res.partner", string="Farmer", required=True, ondelete="cascade", )
    nic_number = fields.Char(string='NIC Number', related="partner_id.nic_number", )
    address = fields.Char(string='Address', related="partner_id.address", )
    tp = fields.Char(string='TP', related="partner_id.tp", )

    cultivation_id = fields.Many2one("g2p.cultivation.details", string=_("Cultivation Details"))
    land_id = fields.Many2one(comodel_name='g2p.land.details', string=_('Land details'),
                              domain="[('partner_id', '=', partner_id)]")
    irrigation = fields.Selection(related="land_id.irrigation", string=_("Irrigation"))
    season_id = fields.Many2one('g2p.season', string=_('Season'))
    subsidy_type = fields.Char(string=_("Subsidy Type"))
    district_id = fields.Many2one('g2p.district', string=_('District'))
    asc_id = fields.Many2one('g2p.agrarian.service.center', string=_("ASC"), domain="[('district_id', '=', district_id)]")
    # asc_code = fields.Char(string="ASC Code", size=6, related="asc_id.asc_code")
    plr_number = fields.Char(string=_("PLR Number"))
    land_extent = fields.Float(string=_("Land Extent (HA)"))
    farmer_bank_id = fields.Many2one(comodel_name='res.partner.bank', string=_('Farmer Bank'), domain="[('partner_id', '=', partner_id)]")
    branch_id = fields.Many2one('g2p.bank.branch', related="farmer_bank_id.branch_id")
    bank_id = fields.Many2one('res.bank', related="branch_id.bank_id")
    # bank_code = fields.Char(string=_("Bank Name"), related="farmer_bank_id.bank_code")
    # branch_code = fields.Char(string=_("Branch Name"), related="farmer_bank_id.branch_code")
    account_detail = fields.Char(string=_("Account Detail"))
    slip_number = fields.Char(string=_("Slip Number"))
    amount_quantity = fields.Float(string=_("Amount/Quantity"))
    status_id = fields.Many2one('status.grant', string=_('Status'))
    gn_division_id = fields.Many2one(comodel_name='g2p.gn.division', string=_('GN Division'))
    # gn_division = fields.Char(related="gn_division_id.code", string=_(' Code'))
    old_dos = fields.Char(string=_('Old DOS'))
    nic_check = fields.Boolean(string=_('NIC Check'))
    trance_date = fields.Date(string=_('Trance Date'))
    reject_date = fields.Date(string=_('Reject Date'))
    is_paddy = fields.Boolean(string=_('Is Paddy Land'))

