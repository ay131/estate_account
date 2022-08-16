# -*- coding: utf-8 -*-
{
    'name': "estate_account",

    'summary': " ",

    'description': "",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'sequence': -100,

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','real-estate'],
    'application': 'Ture',

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
}
