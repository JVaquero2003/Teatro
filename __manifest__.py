# -*- coding: utf-8 -*-
{
    'name': "teatro",
    'summary': """Gestion de un teatro""",
    'description': """
        Aplicacion para gestionar un teatro
    """,
    'author': "Jose Vaquero",
    'website': "https://github.com/JVaquero2003",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}