# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api
 
class MaintenanceEquipmenteLine(models.Model):
    _name = 'maintenance.equipment.line'
    _description = 'maintenance.equipment.line'

    name = fields.Char()
    equipment_id = fields.Many2one('maintenance.equipment')
    equipment_ids_count = fields.Integer('maintenance.equipment', String='Nº Equipment', compute= '_compute_equipment_ids_count', store=True)
    cost = fields.Float('Cost')
    serial_no = fields.Char('maintenance.equipment', related='equipment_id.serial_no', String='Serial Number')
    category_id = fields.Many2one('maintenance.equipment.category', related='equipment_id.category_id')
    assign_date = fields.Date('maintenance.equipment', related='equipment_id.assign_date', String='Assigned Date')
    cost = fields.Float('maintenance.equipment', related='equipment_id.cost', String='Cost')
    # equipment_brand = fields.Many2one('maintenance.equipment.brand', related='equipment_id.equipment_brand', String='Brand')
    # equipment_status_id = fields.Many2one('maintenance.equipment.status', related='equipment_id.equipment_status_id', String='Status')
    technician_user_id = fields.Many2one('res.users', related='equipment_id.technician_user_id', String='Technician')
    # ticket_ids = fields.Many2many('helpdesk.ticket', related='equipment_id.ticket_ids', String='Tickets Number')
    # ticket_count = fields.Integer('helpdesk.ticket', related='equipment_id.ticket_count', String='Tickets Number')
    create_date = fields.Datetime(String='Creation Date', index=True)


    @api.depends('equipment_id')
    def _compute_equipment_ids_count(self):
        for equipment in self:
            equipment.equipment_ids_count = len(equipment.equipment_id)

