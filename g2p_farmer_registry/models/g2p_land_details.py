from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class G2pLandDetails(models.Model):
    _name = 'g2p.land.details'
    _description = 'G2p Land Details'
    _rec_name = 'land_number'

    land_sequence = fields.Char(
        string='Sequence',
        copy=False,
        readonly=True,
        index=True,
    )
    name = fields.Char(string=_('Land Name'), required=True)
    land_number = fields.Char(string=_('Land Number'), required=True)
    district_id = fields.Many2one('g2p.district', string=_('District'))
    asc_id = fields.Many2one('g2p.agrarian.service.center', string=_("ASC"), domain="[('district_id', '=', district_id)]")
    # code = fields.Char(related='asc_id.asc_code', string=_('ASC Code'))
    plr_number = fields.Char(string=_('PLR Number'))
    irrigation = fields.Selection([
        ('1-Major', '1-Major'),
        ('2-Minor', '2-Minor'),
        ('3-Rainfed', '3-Rainfed'), ], string=_("Irrigation"))
    land_extent = fields.Float(default=False, string=_("Land Extent (HA)"))
    partner_id = fields.Many2one(comodel_name='res.partner', string=_('Farmer'))
    is_paddy_land = fields.Boolean(default=True, string=_('Is Paddy Land'))
    land_owner = fields.Many2one(comodel_name='res.partner', string=_('Land Owner'))
    gn_division_id = fields.Many2one(comodel_name='g2p.gn.division', string=_('GN Division'))
    # gn_division = fields.Char(related="gn_division_id.code", string=_(' Code'))
    status_id = fields.Many2one('status.land.details', string=_('Status'))
    land_type = fields.Selection([
        ('paddy', 'Paddy Land'),
        ('other', 'Other Land'),
    ], default='paddy', string=_('Land Type'))
    new_dos = fields.Char(string=_('New DOS'))
    old_dos = fields.Char(string=_('Old DOS'))

    _sql_constraints = [
        ('land_number_unique', 'UNIQUE(land_number)', 'This Land Number is already in use.'),
        ('plr_number_unique', 'UNIQUE(plr_number)', 'This PLR Number is already in use.'),
    ]

    @api.model
    def create(self, vals):
        if not vals.get('land_sequence'):
            prefix = 'L'

            if 'asc_id' in vals and vals.get('asc_id'):
                asc = self.env['g2p.agrarian.service.center'].browse(vals['asc_id'])
                if asc.asc_sequence and '/' in asc.asc_sequence:
                    asc_prefix = asc.asc_sequence.split('/')[0]
                    if asc_prefix.startswith('L') and len(asc_prefix) == 6:
                        prefix = asc_prefix

            if prefix == 'L' and 'district_id' in vals and vals.get('district_id'):
                district = self.env['g2p.district'].browse(vals['district_id'])
                if district.district_sequence and '/' in district.district_sequence:
                    prefix = district.district_sequence.split('/')[0]
                elif district.code:
                    prefix += district.code.zfill(5)[:5]

            if prefix == 'L':
                raise ValidationError(
                    _("Cannot generate Land Code: "
                      "Please select ASC or ensure District has a valid code.")
                )

            next_num = self.env['ir.sequence'].next_by_code('g2p.land.details')
            if not next_num:
                raise UserError(_("Failed to generate land sequence number."))

            vals['land_sequence'] = f"{prefix}/{next_num}"

        return super().create(vals)