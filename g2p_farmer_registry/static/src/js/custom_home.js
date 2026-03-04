/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { AppsMenu } from "@muk_web_theme/webclient/appsmenu/appsmenu";

patch(AppsMenu.prototype, {
    setup() {
        super.setup();

        // Force your custom background image
        // (this overrides both company upload and Muk default)
        this.backgroundImageUrl = "/g2p_farmer_registry/static/src/img/bgg.png";

        // Optional: you can still check company image if you want fallback logic
        // if (this.companyService.currentCompany.has_background_image) {
        //     this.backgroundImageUrl = url('/web/image', {
        //         model: 'res.company',
        //         field: 'background_image',
        //         id: this.companyService.currentCompany.id,
        //     });
        // }
    }
});