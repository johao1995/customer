{
    'name':'Sales of Management',
    'autor':'Johao Marcos Maldonado Roman',
    'description':'Module of Sales Management',
    'depends':[
        'base'
    ],
    'data':[
        'views/commercial_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
        'views/menu.xml',
        #security
        'security/res_groups.xml',
        'security/ir_model_access.xml',
        #report
        'report/report_order.xml',
        'report/report_customer.xml'
    ]
}