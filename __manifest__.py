{
    'name': 'Web Themer',
    'description': 'Change Odoo color scheme and styles.',
    'category': 'Customizations',
    'website': 'yahyaanwar.github.io',
    'support': 'k3ic8zwya@mozmail.com',
    'version': '1.0',
    'license': 'OPL-1',
    'price': 0, 'currency': 'USD',
    'author': 'Yahya Anwar Ramadhan',
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': [
        'base',
        'web',
    ],
    'external_dependencies': {
        'python': [
        ],
        'bin': [
        ],
    },
    'data': [
    ],
    'demo': [
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('replace', 'web/static/src/scss/primary_variables.scss', '/web_themer/static/src/components/theme.scss'),
        ],
    },
    'images': [
    ],
    'post_load': 'apply_patch',
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
}