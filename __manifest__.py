{
    'name': 'BUZON DE IAP',
    'version': '1.0',
    'category': 'Modulo de JAP',
    'sequence': 15,
    'author':'DTIC - JAPDF',
    'summary': 'BUZON DE NOTIFICACIONES DE AUTORIZACION Y RECHAZO DE TRAMITE',
    'description': 'MODULO QUE LLEVA A CABO LA CONSULTA DEL BUZON DE LAS IAP',


    'depends': ['base','mail','gestiontramites'],

    'data': [


        'views/gestion_tramite_view.xml',
        'security/tools_jap_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view_admon.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}