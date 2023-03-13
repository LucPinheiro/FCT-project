# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import  models, fields, api
from odoo.exceptions import ValidationError

# ---------------------------------
# Maintenance Equipment:
# ---------------------------------
# Class 1
class MaintenanceEquipment(models.Model):
    _inherit = ["maintenance.equipment", "image.mixin"]
    _name = "maintenance.equipment"

    equipment_ids= fields.Many2many()
    request_id = fields.Many2one('maintenance.request')
    request_ids = fields.Many2many('maintenance.request')
    request_stage_id = fields.Many2one('maintenance.stage', related='request_id.request_stage_id', String='Request Stage')

    ticket_id = fields.Char(String='Tickets Number')
    ticket_active = fields.Boolean()
    ticket_ids = fields.Many2many('helpdesk.ticket', String='Tickets Number')
    ticket_count = fields.Integer('helpdesk.ticket', compute='_compute_ticket_count', store=True)
    name_ticket = fields.Char(String='Ticket Name')
    description_ticket = fields.Html(String='Description')
    user_id_ticket = fields.Many2one('helpdesk.ticket')
    stage_id_ticket = fields.Many2one('helpdesk.ticket.stage', String='Stage')
    project_id_ticket = fields.Many2one('project.project', String='Projects') #es heredado de helpdesk
    create_date_ticket = fields.Date()
    last_stage_update_ticket = fields.Datetime(default=fields.Datetime.now)
    category_id_ticket = fields.Many2one('helpdesk.ticket.category', String='Ticket category')
    priority_ticket = fields.Selection(
        selection=[
            ("0", "Low"),
            ("1", "Medium"),
            ("2", "High"),
            ("3", "Very High"),
        ],
        default="1",
    )
    tracking = fields.Selection([
        ('serial', 'By Unique Serial Number'),
        ('lot', 'By Lots'),
        ('none', 'No Tracking')], String="Tracking", default='serial', required=True)
    model = fields.Char('Model Number', copy=False)
    equipment_brand = fields.Many2one('maintenance.equipment.brand', String='Brand')
    equipment_status_id = fields.Many2one('maintenance.equipment.status', String='Status')
    schedule_date = fields.Datetime('Scheduled Date', help="Date the maintenance team plans the maintenance.  It should not differ much from the Request Date. ")
    create_date = fields.Datetime(String='Creation Date', index=True)
    equipment_line_ids = fields.Many2many('maintenance.equipment.line', inverse_name='equipment_id')


    # ---------------------------------
    # DEPENDS METHODS: compute function
    # ---------------------------------

    @api.depends('ticket_ids')
    def _compute_ticket_count(self):
       for  ticket in self:
            ticket.ticket_count = len(ticket.ticket_ids)

    # _sql_constraints = [
    #         ('name_uniq', 'UNIQUE (name)',  'You can not have two users with the same name !')
    #     ]

    # def _check_name(self, cr, uid, ids, context=None):
    #         for val in self.read(cr, uid, ids, ['name'], context=context):
    #             if val['name']:
    #                 if len(val['name']) < 6:
    #                     return False
    #         return True

    # _constraints = [
    #     (_check_name, 'Name must have at least 6 characters.', ['name'])
    # ]


    # ------------------------------------
    # CONSTRAINS METHODS: compute function
    # ------------------------------------

    # @api.constrains('create_date_ticket')
    # def _check_create_date_ticket(self):
    #     for record in self:
    #         if record.create_date_ticket < fields.Date.today():
    #             raise ValidationError("Creation date cannot be created in the past")


    # ---------------------------------
    # CRUD
    # ---------------------------------
#    def name_get(self):
#         result = []
#         for record in self:
#             if record.name and record.serial_no:
#                 result.append((record.id, record.name + '/' + record.serial_no))
#             if record.name and not record.serial_no:
#                 result.append((record.id, record.name))
#         return result



class Department(models.Model):
    _inherit = 'hr.department'

    # def name_get(self):
    #     # Get department name using superuser, because model is not accessible
    #     # for portal users
    #     self_sudo = self.sudo()
    #     return super(Department, self_sudo).name_get()


    # def name_get(self):
    #     res = super()._get_name()
    #     for record in self:
    #         if record.name and record.serial_no:
    #             res.append((record.id, record.name + '/' + record.serial_no + '-' + record.ticket_ids))
    #         if record.name and record.serial_no and not record.ticket_ids:
    #             res.append((record.id, record.name))
    #         if record.name and not record.serial_no:
    #             res.append((record.id, record.name))
    #     return res
    
    # def _compute_access_url(self):
    #     res = super()._compute_access_url()
    #     for item in self:
    #         item.access_url = "/my/ticket/%s" % (item.id)
    #     return res


    
    # ---------------------------------
    # CRUD
    # ---------------------------------
    