from . import models



def uninstall_hook(env):
    """
    Runs after the module is uninstalled.
    Trigger upgrade of 'base' to restore original menu names from XML.
    """
    base_module = env['ir.module.module'].search([('name', '=', 'base')])
    if base_module and base_module.state == 'installed':
        base_module.button_upgrade()  # or button_immediate_upgrade() if you prefer immediate reload
