
{
    "name": "Dark Mode Ultimate",
    "summary": "Switch between Light and Dark themes for a better user experience",
    "license": "OPL-1",
    "version": "19.0.1.0.0",
    "author": "CloudAddons Technologies",
    'category': 'Settings/Display',
    "depends": ["web"],
    "installable": True,
    'price': 1.00,
    'currency': 'USD',
    'images': ['static/description/main_screenshot.png'],
     "data": [
        "views/res_users_views.xml",
        "views/web_layout.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "dark_mode_ultimate/static/src/js/switch_item.esm.js",       
        ],
        "web.assets_backend_lazy_dark": [
            ("include", "web.assets_variables_dark"),
            ("include", "web.assets_backend_helpers_dark"),
            
        ],
        "web.assets_variables_dark": [
            (
                "before",
                "web/static/src/scss/primary_variables.scss",
                "dark_mode_ultimate/static/src/scss/primary_variables.dark.scss",
            ),
            (
                "before",
                "web/static/src/scss/secondary_variables.scss",
                "dark_mode_ultimate/static/src/scss/secondary_variables.dark.scss",
            ),
            (
                "before",
                "web/static/src/**/*.variables.scss",
                "dark_mode_ultimate/static/src/**/*.variables.dark.scss",
            ),
        ],
        "web.assets_backend_helpers_dark": [
            (
                "before",
                "web/static/src/scss/bootstrap_overridden.scss",
                "dark_mode_ultimate/static/src/scss/bootstrap_overridden.dark.scss",
            ),
            (
                "after",
                "web/static/lib/bootstrap/scss/_functions.scss",
                "dark_mode_ultimate/static/src/scss/bs_functions_overrides.dark.scss",
            ),
        ],
        "web.assets_web_dark": [
            ("include", "web.assets_variables_dark"),
            ("include", "web.assets_backend_helpers_dark"),
            "dark_mode_ultimate/static/src/**/*.dark.scss",
        ],
    },
   
}
