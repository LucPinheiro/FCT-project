# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Helpdesk Maintenance",
    "summary": """
        Helpdesk Maintenance
    """,
    "author": "Luciana Pinheiro",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Inventory/Maintenance/Helpdesk",
    "website": "https://github.com/solvosci/slv-hr",
    "depends": [
        "maintenance",
        "helpdesk_mgmt",
        "helpdesk_mgmt_project",
        "project", 
        "helpdesk_mgmt_project",
        "hr_maintenance",
        "stock",
    ],
    "data": [
        # "security/ir.model.access.csv",
        # "security/maintenance.xml",
        "report/equipment_traceability_report.xml",
        "views/menus.xml",     
        "views/maintenance_views.xml",
        "views/helpdesk_mgmt_views.xml",
        "views/project_views.xml",
        "views/traceability.xml",


        # "wizard/wizard.xml",
       
    ],
    'installable': True,
}
