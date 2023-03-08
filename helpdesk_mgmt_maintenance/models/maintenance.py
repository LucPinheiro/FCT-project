# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
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

    helpdesk = fields.Char()
    ticket_id = fields.Char(String='Tickets Number')
    ticket_active = fields.Boolean()
    ticket_ids = fields.Many2many('helpdesk.ticket', String='Tickets Number')
    ticket_count = fields.Integer('helpdesk.ticket', compute='_compute_ticket_count', store=True)
    name_ticket = fields.Char(String='Ticket Name')
    description_ticket = fields.Html(String='Description')
    user_id_ticket = fields.Many2one('helpdesk.ticket')
    project_id_ticket = fields.Many2one('project.project', String='Projects') #es heredado de helpdesk
    create_date_ticket = fields.Date()
    last_stage_update_ticket = fields.Datetime(default=fields.Datetime.now)
    category_id_ticket = fields.Many2one('helpdesk.ticket.category', String='Ticket category')
    stage_id_ticket = fields.Many2one('helpdesk.ticket.stage')
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
    # status_id = fields.Many2one('equipment.status', String='Status', tracking=True)

    model = fields.Char('Model Number', copy=False)
    schedule_date = fields.Datetime('Scheduled Date', help="Date the maintenance team plans the maintenance.  It should not differ much from the Request Date. ")
    create_date = fields.Datetime()

    equipment_line_ids = fields.One2many('maintenance.equipment.line', inverse_name='equipment_id')
    # order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)



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
    