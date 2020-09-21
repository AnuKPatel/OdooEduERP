# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Transport Management',
    'version': '3.0',
    'author': 'Serpent Consulting Services PVT. LTD.',
    'website': 'http://www.serpentcs.com',
    'license': '',
    'category': 'School Management',
    'complexity': 'easy',
    'summary': 'A Module For Transport & Vehicle Management In School',
    'depends': ['hr', 'school'],
    'demo': ['demo/transport_demo.xml'],
    'data': [
        'security/ir.model.access.csv',
        'views/transport_view.xml',
        'views/report_view.xml',
        'views/vehicle.xml',
        'views/participants.xml',
        'wizard/transfer_vehicle.xml',
    ],
    'test': [
        'test/transport.yml',
        'test/transport_report.yml',
    ],
    'installable': True,
    'application': True,
}
