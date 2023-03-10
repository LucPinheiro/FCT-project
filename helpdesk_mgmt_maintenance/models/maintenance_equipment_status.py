# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class MaintenanceEquipmentStatus(models.Model):
    _name = "maintenance.equipment.status"
    _description = "Maintenance Equipment Status"

    name = fields.Char('Status', required=True, translate=True)
    color = fields.Integer('Color Index')
    partner_id = fields.Char('res.partner', String= 'Suppliers')
    