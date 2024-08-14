# -*- coding: utf-8 -*-
{
    'name': "Task Flow",

    'summary': "This module is used to manage tasks in a project.",

    'description': """
This module is used to manage tasks in a project.
    """,

    'author': "Wilson Contreras",
    'website': "https://www.koidevs.vercel.app/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'views/task.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
}

