from odoo.http import request
from odoo import http, fields

class WebSiteDireccion(http.Controller):
    @http.route('/productos/<model("product.template"):product>', type='http', auth='none')
    def fun_product(self, product):
        return http.request.render('academy.product', {
            "product": product
        })