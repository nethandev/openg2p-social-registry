from odoo import api, fields, models


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    bank_id = fields.Many2one('res.bank', string='Bank')
    branch_id = fields.Many2one('g2p.bank.branch', "Branch")
    # branch_code = fields.Char(related="branch_id.branch_code",string='Branch Code')
    partner_id = fields.Many2one(tracking=True, domain="[('is_farmer', '=', True)]")
    country = fields.Many2one('res.country', default=lambda self: self.env.company.country_id)
    account_no =fields.Char(string="Account Number")
    account_sn =fields.Char(string="Account Serial Number")
    active = fields.Boolean(default=True)
    invalid = fields.Boolean(default=False)

    # account number, account serial number, invalid, status