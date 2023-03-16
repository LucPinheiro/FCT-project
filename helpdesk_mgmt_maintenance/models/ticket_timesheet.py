# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import  models, fields, api
from datetime import datetime, time
import logging
import re
import babel.dates
from dateutil.relativedelta import SU, relativedelta
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

empty_name = "/"
# ---------------------------------
# Ticket Timesheet:
# ---------------------------------
# Class 1
# class TicketTimesheet(models.Model):
#     _name = 'ticket.timesheet'
#     _description = 'Ticket Timesheet'
#     _inherit = ["mail.thread", "mail.activity.mixin", "portal.mixin"]
#     _table = "ticket_timesheet"
#     _order = "id desc"


#     name = fields.Char()
#     employee_id = fields.Many2one(
#         "hr.employee",
#         String="Employee",
#         default=lambda self: self._default_employee(),
#         required=True,
#         states={"new": [("readonly", False)]},
#     )
#     user_id = fields.Many2one(
#         "res.users",
#         related="employee_id.user_id",
#         string="User",
#         store=True,
#     )
#     department_id = fields.Many2one(
#         "hr.department",
#         string="Department",
#         default=lambda self: self._default_department_id(),
#         states={"new": [("readonly", False)]},
#     )
#     company_id = fields.Many2one(
#         "res.company",
#         String="Company",
#         default=lambda self: self.env.company,
#         required=True,
#         readonly=True,
#     )
    
#     # ticket_ids_timesheet_line = fields.One2many(
#     #     'ticket.timesheet.line',
#     #     'timesheet_ids',
#     #     String='Timesheet Lines')
    

#     ticket_id = fields.Many2one('helpdesk.ticket')
#     ticket_ids = fields.Many2many('helpdesk.ticket')
#     ticket_count = fields.Integer('helpdesk.ticket', compute='_compute_ticket_count')
#     assigned_date = fields.Datetime('helpdesk.ticket')
#     # ticket_line_ids = fields.One2many(
#     #     'helpdesk.ticket',
#     #     String='Ticket Lines'
#     # )


#     # date_start = fields.Date(
#     #     String="Date From",
#     #     default=lambda self: self._default_date_start(),
#     #     required=True,
#     #     index=True,
#     #     readonly=True,
#     #     states={"new": [("readonly", False)]},
#     # )
#     # date_end = fields.Date(
#     #     string="Date To",
#     #     default=lambda self: self._default_date_end(),
#     #     required=True,
#     #     index=True,
#     #     readonly=True,
#     #     states={"new": [("readonly", False)]},
#     # )
    
#     # tickets_hours = fields.Float(string="Quantity", default=0.0)
#     total_time = fields.Float(compute="_compute_total_time", store=True)

#     stage_id = fields.Many2one(
#         comodel_name="helpdesk.ticket.stage",
#         string="Stage"
#     )
#     # state = fields.Selection(
#     #     [
#     #         ("new", "New"),
#     #         ("draft", "Open"),
#     #         ("confirm", "Waiting Review"),
#     #         ("done", "Approved"),
#     #     ],
#     #     default="new",
#     #     tracking=True,
#     #     string="Status",
#     #     required=True,
#     #     readonly=True,
#     #     index=True,
#     # )

#     def _default_date_start(self):
#         return self._get_period_start(
#             self.env.user.company_id, fields.Date.context_today(self)
#         )

#     def _default_date_end(self):
#         return self._get_period_end(
#             self.env.user.company_id, fields.Date.context_today(self)
#         )
    
#     def _default_employee(self):
#         company = self.env.company
#         return self.env["hr.employee"].search(
#             [("user_id", "=", self.env.uid), ("company_id", "in", [company.id, False])],
#             limit=1,
#             order="company_id ASC",
#         )

#     def _default_department_id(self):
#         return self._default_employee().department_id
   
#     @api.model
#     def _get_period_start(self, company, date):
#         r = company and company.sheet_range or "WEEKLY"
#         if r == "WEEKLY":
#             if company.timesheet_week_start:
#                 delta = relativedelta(weekday=int(company.timesheet_week_start), days=6)
#             else:
#                 delta = relativedelta(days=date.weekday())
#             return date - delta
#         elif r == "MONTHLY":
#             return date + relativedelta(day=1)
#         return date

#     @api.model
#     def _get_period_end(self, company, date):
#         r = company and company.sheet_range or "WEEKLY"
#         if r == "WEEKLY":
#             if company.timesheet_week_start:
#                 delta = relativedelta(
#                     weekday=(int(company.timesheet_week_start) + 6) % 7
#                 )
#             else:
#                 delta = relativedelta(days=6 - date.weekday())
#             return date + delta
#         elif r == "MONTHLY":
#             return date + relativedelta(months=1, day=1, days=-1)
#         return date
#    # @api.depends("timesheet_ids.tickets_hours")
#     def _compute_total_time(self):
#         for sheet in self:
#             sheet.total_time = sum(sheet.mapped("timesheet_ids.tickets_hours"))
    
#     @api.depends('ticket_ids')
#     def _compute_ticket_count(self):
#        for  ticket in self:
#             ticket.ticket_count = len(ticket.ticket_ids)



# Class 2
class TicketTimesheetLine(models.Model):
    _name = 'ticket.timesheet.line'
    _description = 'Ticket Timesheet Line'

    # _table = "ticket_timesheet"
    # _order = "id desc"

    name = fields.Char()
    # timesheet_ids = fields.Many2one(
    #     string="Timesheets",
    #     readonly=True,
    #     # states={"new": [("readonly", False)], "draft": [("readonly", False)]},
    # )
    ticket_id = fields.Many2one('helpdesk.ticket')
    date_start = fields.Date('helpdesk.ticket')
    date_end = fields.Date('helpdesk.ticket')