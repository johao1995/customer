{
    'name':'list of movies',
    'autor':'Johao Marcos Maldonado Roman',
    'description':'Peliculas',
    'depends':[
        'contacts'
    ],
    'data':[
        #security
        'security/res_groups.xml',
        'security/ir_model_access.xml',
        #vistas
        'views/view_presupuesto.xml',
        'views/view_genero.xml',
        'views/view_categoria_operarios.xml',
        'views/menu.xml',
        #data
        'data/genero.xml',
        'data/categoria_operarios.xml',
        'data/ir_sequence.xml'
    ]
}