# © 2023 Lucia Pinero Consultoría Informática (<http://www.luciapinero.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


# class Maintenance(models.Model):
#     _name = 'fcd.document.line'
#     _description = 'fcd.document.line'

#     name = fields.Char()
#     fcd_document_id = fields.Many2one('fcd.document')
#     lot_id = fields.Many2one('stock.production.lot')
#     box_count = fields.Integer()
#     notes_cost = fields.Text()


###########################################
# Maintenance Equipment Line: 
###########################################    
class MaintenanceEquipmenteLine(models.Model):
    _name = 'maintenance.equipment.line'
    _description = 'maintenance.equipment.line'

    name = fields.Char()
    equipment_id = fields.Many2one('maintenance.equipment')
    cost = fields.Float('Cost')

