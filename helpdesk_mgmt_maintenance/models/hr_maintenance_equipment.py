# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import  models, fields, api
from odoo.exceptions import ValidationError

# ---------------------------------
# Hr Maintenance Equipment:
# ---------------------------------
# Class 1

class MaintenanceEquipment(models.Model):
    # _inherit = "maintenance.equipment"
    _name = 'maintenance.equipment'
    _inherits ={'maintenance.equipment': 'equipment_id'}

 
    # class User(models.Model): 
    # _name = 'res.users' 
    # _inherits = {'res.partner': 'partner_id'} 
    # partner_id = fields.Many2one('res.partner')

# class MixinAccountPaymentGroup(models.Model):
#     _name = 'account.payment.group'
#     _inherit = ['account.payment.group','portal.mixin']

# employee_id = fields.Many2one('hr.employee', compute='_compute_equipment_assign',
#         store=True, readonly=False, string='Assigned Employee', tracking=True)
# department_id = fields.Many2one('hr.department', compute='_compute_equipment_assign',
#         store=True, readonly=False, string='Assigned Department', tracking=True)
# equipment_assign_to = fields.Selection(
#     [('department', 'Department'), ('employee', 'Employee'), ('other', 'Other')],
#     string='Used By',
#     required=True,
#     default='employee')

# assign_date = fields.Date(compute='_compute_equipment_assign', store=True, readonly=False, copy=True)

# @api.depends('equipment_assign_to')
#     def _compute_equipment_assign(self):
#         for equipment in self:
#             if equipment.equipment_assign_to == 'employee':
#                 equipment.department_id = False
#                 equipment.employee_id = equipment.employee_id
#             elif equipment.equipment_assign_to == 'department':
#                 equipment.employee_id = False
#                 equipment.department_id = equipment.department_id
#             else:
#                 equipment.department_id = equipment.department_id
#                 equipment.employee_id = equipment.employee_id
#             equipment.assign_date = fields.Date.context_today(self)