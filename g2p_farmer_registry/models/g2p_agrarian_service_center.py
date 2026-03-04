from odoo import models, fields, api, _


class AgrarianServiceCenter(models.Model):
    _name = 'g2p.agrarian.service.center'
    _description = 'Agrarian Service Center'
    _rec_name = 'asc_name'

    # asc_id = fields.Char(string='ASC ID', size=6, required=True)
    asc_sequence = fields.Char(
        string='Sequence',
        copy=False,
        readonly=True,
        index=True,
    )
    asc_code = fields.Char(string='Code', size=6, required=True)
    asc_name = fields.Char(string='Name', size=100, required=True)
    sinhala_name = fields.Char(string='Sinhala Name', size=100)
    tamil_name = fields.Char(string='Tamil Name', size=100)

    asc_latitude = fields.Char(string='Latitude', size=100)
    asc_longitude = fields.Char(string='Longitude', size=100)
    active = fields.Boolean(default=True)

    # asc_status = fields.Selection(
    #     [('A', 'Active'), ('I', 'Inactive')],
    #     string='Status',
    #     default='A'
    # )
    district_id = fields.Many2one('g2p.district', string='District')

    # Reverse One2many – shows all land details linked to this ASC
    land_detail_ids = fields.One2many(
        'g2p.land.details',
        'asc_id',
        string="Land Details",
        readonly=True,  # optional
    )
    # Computed fields – count & total extent
    land_count = fields.Integer(
        string="Number of Land Lots",
        compute='_compute_land_stats',
        store=True,  # store = True → searchable, filterable, groupable
        help="Total number of land records linked to this ASC"
    )

    total_land_extent = fields.Float(
        string="Total Land Extent (HA)",
        compute='_compute_land_stats',
        store=True,
        digits=(16, 3),  # optional – adjust precision
        help="Sum of land extent (HA) for all linked land records"
    )

    @api.depends('land_detail_ids', 'land_detail_ids.land_extent')
    def _compute_land_stats(self):
        for asc in self:
            lands = asc.land_detail_ids
            asc.land_count = len(lands)
            asc.total_land_extent = sum(lands.mapped('land_extent'))  # or .filtered('is_paddy_land') if needed

    _sql_constraints = [
        ('asc_code_unique', 'unique(asc_code)', 'ASC code must be unique!')
    ]


    @api.model
    def create(self, vals):
        if not vals.get('asc_sequence'):
            vals['asc_sequence'] = self.env['ir.sequence'].next_by_code('g2p.agrarian.service.center') or _('New')
        return super(AgrarianServiceCenter, self).create(vals)
