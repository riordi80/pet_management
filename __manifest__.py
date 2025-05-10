# -*- coding: utf-8 -*-
{
    'name': "pet_management",

    'summary': "Gestión de mascotas y sus vacunas",

    'description': """
Este módulo permite gestionar mascotas, sus propietarios y el historial de vacunación.
Incluye vistas personalizadas y permisos de acceso.
    """,

    'author': "ordiDev",
    'website': "https://www.ordidev.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/views_weight_log.xml',
    'views/views_pets.xml', 
    'views/views_vaccinations.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

