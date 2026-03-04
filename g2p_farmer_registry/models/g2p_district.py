from odoo import api, fields, models, tools, _


class G2PDistrict(models.Model):
    _inherit = 'g2p.district'
    _rec_name = 'code'

    district_sequence = fields.Char(
        string='Sequence',
        copy=False,
        readonly=True,
        index=True,
    )
    code = fields.Char(string='Code')
    region_id = fields.Many2one('g2p.region', string='Province')
    area_km2 = fields.Float(string='Area')
    pop_density = fields.Float(string='Population Density')
    sinhala_name = fields.Char(string='Sinhala Name')
    tamil_name = fields.Char(string='Tamil Name')
    bank_id = fields.Many2one('res.bank', string='Bank')
    # bank_code = fields.Char(string='Bank Code', related='bank_id.bic')
    branch_id = fields.Many2one('g2p.bank.branch', string='Branch')
    # branch_code = fields.Char(string='Branch Code', related='branch_id.branch_code')
    account_no = fields.Char(string='Account Number')
    active = fields.Boolean(default=True)

    secretariat_ids = fields.One2many(
        'g2p.divisional.secretariat',
        'district_id',
        string='Divisional Secretariats'
    )

    secretariat_count = fields.Integer(
        string='Secretariats Count',
        compute='_compute_secretariat_count',
        store=False
    )

    @api.depends('secretariat_ids')
    def _compute_secretariat_count(self):
        for district in self:
            district.secretariat_count = len(district.secretariat_ids)

    @api.model
    def create(self, vals):
        if not vals.get('district_sequence'):
            vals['district_sequence'] = self.env['ir.sequence'].next_by_code('g2p.district') or _('New')
        return super(G2PDistrict, self).create(vals)
