# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# ---------------------------------
# Helpdesk Ticket: 
# ---------------------------------
# Class 1

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    equipment_id = fields.Many2one('maintenance.equipment', String= 'Equipments', required=True)
    employee_id_hr = fields.Many2one('hr.employee', String= 'Equipments')
    equipment_ids = fields.Many2many('maintenance.equipment', String= 'Equipments')
    equipment_ids_count = fields.Integer('maintenance.equipment', compute= '_compute_equipment_ids_count', store=True)
    employee_id = fields.Many2one('hr.employee', related='equipment_id.employee_id')
    departament_id = fields.Many2one('hr.department')
    serial_no = fields.Char('maintenance.equipment', related='equipment_id.serial_no', String='Serial Number')
    model_equipament = fields.Char('maintenance.equipment', related='equipment_id.model', String ='Modal')
    # equipment_brand = fields.Many2one('maintenance.equipment.brand', related='equipment_ids.equipment_brand', String='Brand')
    category_id = fields.Many2one('maintenance.equipment.category', related='equipment_id.category_id')
    cost = fields.Float('maintenance.equipment', related='equipment_id.cost', String='Cost')
    description_equipment = fields.Html(String='Description')
    assigned_date = fields.Datetime()
    closed_date = fields.Datetime()
    project_id = fields.Many2one('project.project', string='Project')
    project_id_count = fields.Integer('project.project', compute= '_compute_project_id_count', store=True)
    task_id = fields.Many2one('project.task', string='Task')
    task_id_count = fields.Integer('project.task', compute= '_compute_task_id_count', store=True)
    
    progress = fields.Float("Progress", compute='_compute_progress_hours', store=True, group_operator="avg", help="Display progress of current task.")
    progress_percentage = fields.Float(compute='_compute_progress_percentage')
    planned_hours = fields.Float()
    initially_hours = fields.Float()

    tracking = fields.Selection([
        ('serial', 'By Unique Serial Number'),
        ('lot', 'By Lots'),
        ('none', 'No Tracking')], String="Tracking", default='serial', required=True)
    
    


    # total_hours_spent = fields.Float("Total Hours", compute='_compute_total_hours_spent', store=True, help="Time spent on this task, including its sub-tasks.")
    # remaining_hours = fields.Float("Remaining Hours", compute='_compute_remaining_hours', store=True, readonly=True, help="Total remaining time, can be re-estimated periodically by the assignee of the task.")
    # effective_hours = fields.Float("Hours Spent", compute='_compute_effective_hours', compute_sudo=True, store=True, help="Time spent on this task, excluding its sub-tasks.")
    # subtask_effective_hours = fields.Float("Sub-tasks Hours Spent", compute='_compute_subtask_effective_hours', recursive=True, store=True, help="Time spent on the sub-tasks (and their own sub-tasks) of this task.")
    # planned_hours = fields.Float("Initially Planned Hours", help='Time planned to achieve this task (including its sub-tasks).', tracking=True)

    # @api.depends('effective_hours', 'subtask_effective_hours', 'planned_hours')
    # def _compute_progress_hours(self):
    #     for task in self:
    #         if (task.planned_hours > 0.0):
    #             task_total_hours = task.effective_hours + task.subtask_effective_hours
    #             task.overtime = max(task_total_hours - task.planned_hours, 0)
    #             if task_total_hours > task.planned_hours:
    #                 task.progress = 100
    #             else:
    #                 task.progress = round(100.0 * task_total_hours / task.planned_hours, 2)
    #         else:
    #             task.progress = 0.0
    #             task.overtime = 0


    # ---------------------------------
    # DEPENDS METHODS
    # ---------------------------------
    @api.depends('progress','planned_hours','initially_hours')
    def _compute_progress_percentage(self):
        for u in self:
            u.progress_percentage = u.progress / 100

    @api.depends('planned_hours','initially_hours','equipment_ids')
    def _compute_progress_hours(self):
        for u in self:
            u.progress = u.planned_hours * u.initially_hours
   
    @api.depends('equipment_ids')
    def _compute_equipment_ids_count(self):
        for equipment in self:
            equipment.equipment_ids_count = len(equipment.equipment_ids)

    @api.depends('project_id')
    def _compute_project_id_count(self):
        for project in self:
            project.project_id_count = len(project.project_id)

    @api.depends('task_id')
    def _compute_task_id_count(self):
        for tack in self:
            tack.task_id_count = len(tack.task_id)

    # _sql_constraints = [
    #     ('model', 'unique(model)', "Another asset already exists with this model number!"),
    # ]

    @api.constrains('assigned_date')
    def _check_assigned_date(self):
        for record in self:
            if record.assigned_date < fields.Date.today():
                raise ValidationError("The end date cannot be set in the past")
            
    # ---------------------------------
    # CRUD overrides
    # ---------------------------------




    # ---------------------------------
    # Helpdesk Ticket Team: 
    # ---------------------------------

    # Class 2
    class HelpdeskTicketTeam(models.Model):
        _inherit = "helpdesk.ticket.team"


    # ---------------------------------
    # Helpdesk Ticket Stage: 
    # ---------------------------------
    # Class 3
    class HelpdeskTicketStage(models.Model):
        _inherit = "helpdesk.ticket.stage"


    # ---------------------------------
    # Helpdesk Category: 
    # ---------------------------------
    # Class 4
    class HelpdeskCategory(models.Model):
        _inherit = "helpdesk.ticket.category"


    # ---------------------------------
    # Helpdesk Ticket Channel: 
    # ---------------------------------
    # Class 5
    class HelpdeskTicketChannel(models.Model):
        _inherit = "helpdesk.ticket.channel"


    # ---------------------------------
    # Helpdesk Ticket Tag: 
    # ---------------------------------
    # Class 5
    class HelpdeskTicketTag(models.Model):
        _inherit = "helpdesk.ticket.tag"
