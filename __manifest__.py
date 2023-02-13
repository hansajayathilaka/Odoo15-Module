# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital_Management',
    'version': '0.1',
    'category': '',
    'summary': 'Patient management',
    'author': 'Hansa Jayathilaka',
    'description': """Manage Hosppitals""",
    'sequence': -100,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
