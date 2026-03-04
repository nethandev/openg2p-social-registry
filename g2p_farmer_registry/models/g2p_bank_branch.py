from odoo import models, fields


class BankBranch(models.Model):
    _name = 'g2p.bank.branch'
    _description = 'Bank Branch'
    _rec_name = 'branch_code'

    bank_id = fields.Many2one('res.bank', string='Bank', required=True, ondelete='restrict')
    # bank_code = fields.Char( related='bank_id.bic', store=True, readonly=True, string="Bank Code")
    branch_code = fields.Char(string='Branch Code', size=3, required=True)
    branch_name = fields.Char(string='Branch Name', size=1000, required=True)
    branch_address = fields.Char(string='Address', size=1000)

    tel_01 = fields.Char(string='Telephone 1', size=10)
    tel_02 = fields.Char(string='Telephone 2', size=10)
    tel_03 = fields.Char(string='Telephone 3', size=10)
    tel_04 = fields.Char(string='Telephone 4', size=10)

    fax_no = fields.Char(string='Fax No', size=100)

    district_id = fields.Many2one('g2p.district', string='District')

    # branch_status = fields.Selection(
    #     [('A', 'Active'), ('I', 'Inactive')],
    #     string='Status',
    #     default='A'
    # )
    active = fields.Boolean(default=True)
