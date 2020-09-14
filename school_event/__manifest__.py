# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{'name': 'School Event Management',
 'version': "10.0.1.0.0",
 'author': "Serpent Consulting Services Pvt. Ltd., Odoo SA",
 'website': 'http://www.serpentcs.com',
 'category': 'School Management',
 'license': "AGPL-3",
 'complexity': 'easy',
 'summary': 'A Module For Event Management In School',
 'depends': ['school'],
 'data': ['views/event_view.xml',
          'views/event_workflow.xml',
          'security/event_security.xml',
          'security/ir.model.access.csv',
          'views/participants.xml',
          'views/report_view.xml'],
 'installable': True,
 'application': True}
