from odoo import models, fields

class Bank(models.Model):
    _inherit = 'res.bank'
    _rec_name = 'bic'

    bic = fields.Char(string='Bank Code', size=4, required=True)
    name = fields.Char(string='Bank Name', size=100, required=True)
    code = fields.Char(string='Bank Code', size=100, required=True)
    active = fields.Boolean(default=True)
    # bank_status = fields.Selection(
    #     [('A', 'Active'), ('I', 'Inactive')],
    #     string='Status',
    #     default='A'
    # )

    _sql_constraints = [
        ('bank_code_unique', 'unique(bank_code)', 'Bank code must be unique!')
    ]
