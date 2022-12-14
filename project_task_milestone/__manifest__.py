# Copyright 2018 Gontzal Gomez - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Project Task Milestone",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "project",
        "project_timeline",
    ],
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/project-addons",
    "category": "Project",
    "data": [
        "security/ir.model.access.csv",
        "views/project_task_view.xml",
        "views/project_task_phase_view.xml",
        "views/project_project_view.xml",
        "report/project_task_plan_view.xml",
    ],
    "installable": True,
}
