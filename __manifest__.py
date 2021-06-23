# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Medical Center',
    'author': 'Odoo S.A',
    'version' : '1.1',
    'summary': 'Medical Center Management System',
    'sequence': 10,
    'description': """Medical Center Management System""",
    'category': 'Productivity',
    'website': '',
    'images' : [],
    'depends' : [],
    'data': [
        'data\mc_data.xml',
        'views\mc_patient_view.xml',
        'views\mc_doctor_view.xml',
        'views\mc_category_view.xml',
        'views\mc_room_view.xml',
        'views\mc_rmcategory_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
