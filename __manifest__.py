# -*- coding: utf-8 -*-
{
    'name': "PedidosYa Odoo Connector",

    'summary': """
        Connector Odoo-PedidosYa""",

    'description': """
        Connector Odoo-PedidosYa for Sale Orders
    """,

    'author': "Codize",
    'website': "https://www.codize.ar",

    'category': 'Sales',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'views/res_company.xml',
    ]
}
