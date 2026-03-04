from odoo import api, fields, models, tools, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _rec_name = "farmer_id"

    name = fields.Char(string='Farmers Name', required=True)
    farmer_id = fields.Char(string='Farmers ID', required=True)
    nic_number = fields.Char(string='NIC Number', required=True)
    nic_check =fields.Boolean(string='NIC Check')
    address = fields.Char(string='Address')
    tp = fields.Char(string='Tele Phone Number')
    is_farmer = fields.Boolean(string="Is Farmer", default=False, index=True)
    land_details_ids = fields.One2many('g2p.land.details', 'partner_id', 'Land Details')
    cultivation_details_ids = fields.One2many('g2p.cultivation.details', 'partner_id', 'Cultivation Details')
    cash_grand_detail_ids = fields.One2many("g2p.cash.grant.detail", "partner_id", string="Cash Grant Details")
    subsidy_detail_ids = fields.One2many("g2p.subsidy.detail", "partner_id", string="Subsidy Details")
    flood_damage_subsidy_ids = fields.One2many("g2p.flood.damage.subsidy", "partner_id",
                                               string="Flood damage subsidy Details")
    active =fields.Boolean(string="Is Active", default=True)
    verify = fields.Boolean(string="Is Verify", default=True)
    verified_by = fields.Many2one('res.users', string="Verified By")


    def _message_auto_subscribe_notify(self, partner_ids, template_id=None):
        # Call super first
        res = super(ResPartner, self)._message_auto_subscribe_notify(partner_ids, template_id)

        # Override creation log only for new farmers
        if self.is_farmer and self.env.context.get('default_is_farmer'):
            # Find the creation message and change text
            creation_msg = self.message_ids.filtered(
                lambda m: m.message_type == 'notification' and 'created' in m.body
            )
            if creation_msg:
                creation_msg.body = creation_msg.body.replace("Contact created", "Farmer created")

        return res

    def action_view_farmer_bank_accounts(self):
        self.ensure_one()
        return {
            'name': 'Bank Accounts / Branches',
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner.bank',
            'view_mode': 'tree,form',  # tree first, then form
            'domain': [('partner_id', '=', self.id)],
            'context': {
                'default_partner_id': self.id,  # pre-fill partner when creating new
            },
            'target': 'current',
        }
