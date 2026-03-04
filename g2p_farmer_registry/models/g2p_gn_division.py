from odoo import fields, models, _


class G2PGNDivision(models.Model):
    _name = "g2p.gn.division"
    _description = "G2P GN Division"
    _rec_name = "code"

    district_id = fields.Many2one('g2p.district', string=_('District'))
    # district_code = fields.Char(string="District Code", size=2, related="district_id.code")

    asc_id = fields.Many2one('g2p.agrarian.service.center', string="ASC")
    # asc_code = fields.Char(string="ASC Code", size=6, related="asc_id.asc_code")

    o_code = fields.Char(string="Old Code", size=20)

    code = fields.Char(string="Code", size=11, required=True, index=True)

    lcode = fields.Char(string="Local Code", size=10)

    name = fields.Char(string="Name", size=100, required=True)

    sinhala_name = fields.Char(string="Sinhala Name", size=100)

    tamil_name = fields.Char(string="Tamil Name", size=100)
    active = fields.Boolean(default=True)

    # status = fields.Selection(
    #     [
    #         ('A', 'Active'),
    #         ('I', 'Inactive'),
    #     ], string="Status", default='A')
