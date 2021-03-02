import dash_bootstrap_components as dbc

def Navbar():
        navbar = dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink(u'Gestión administrativa', href="/gestion-administrativa")),
                dbc.NavItem(dbc.NavLink(u'Gestión médica', href="/gestion-medica")),
                dbc.NavItem(dbc.NavLink(u'Gestión de relaciones tablas', href="/gestion-tablas")),
                dbc.NavItem(dbc.NavLink(u'Registro atenciones médicas', href="/registro-atencion-medica")),
                dbc.NavItem(dbc.NavLink(u'Registro atenciones administrativas', href="/registro-atencion-administrativa")),
                dbc.NavItem(dbc.NavLink(u'Gestión de reportes administrativos', href="/gestion-reporte-administrativo")),
                dbc.NavItem(dbc.NavLink(u'Gestión de reportes médicos', href="/gestion-reporte-medico")),
                dbc.NavItem(dbc.NavLink(u'Gestión telemedicina', href="/gestion-telemedicina")),





                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Menu",
                    children=[
                        dbc.DropdownMenuItem("Entry 1"),
                        dbc.DropdownMenuItem("Entry 2"),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem("Entry 3"),
                            ],
                        ),
                        ],
            brand=u'Gestión del sistema',
            brand_href="/gestion-sistema",
            sticky="top",
            )
        return navbar