from odoo.http import request
from odoo import http, fields

class WebSiteDireccion(http.Controller):
    @http.route('/equipments/<model("maintenance.request"):equipment>', type='http', auth='none')
    def fun_equipment(self, equipment):
        return http.request.render('maintenance_request', {
            "equipment": equipment
        })