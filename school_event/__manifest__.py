# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{'name': 'School Event Management',
 'version': '1.0',
 'author': 'Serpent Consulting Services PVT. LTD.',
 'website': 'http://www.serpentcs.com',
 'category': 'School Management',
 'license': '',
 'complexity': 'easy',
 'summary': 'A Module For Event Management In School',
 'depends': ['school'],
 'data': ['views/event_view.xml',
          'views/event_workflow.xml',
          'security/event_security.xml',
          'security/ir.model.access.csv',
          'views/participants.xml',
          'views/report_view.xml'],
 'demo': ['demo/event_demo.xml'],
 'installable': True,
 'application': True}
