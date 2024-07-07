# -*- coding: utf-8 -*-
{
    'name': "Student Management System",

    'summary': "A module for managing students and their information.",

    'description': """
This module helps in managing student data, courses, and other related information.
    """,

    'author': "Laplacesoftware company",
    'website': "https://www.laplacesoftware.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True
}

