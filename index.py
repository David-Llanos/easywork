import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from gestion_administrativa import gestionAdministrativa, build_graph
from gestion_sistema import gestionSistema
from gestion_medica import gestionMedica
from gestion_tablas import gestionTablas
from registro_atenciones_medicas import registroAtencionMedica
from registro_atenciones_administrativas import registroAtencionAdministrativa
from gestion_reportes_administrativos import gestionReportesAdministrativos
from gestion_reportes_medicos import gestionReportesMedicos
from gestion_telemedicina import gestionTelemedicina


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
    )
def display_page(pathname):
    if pathname == '/gestion-administrativa':
        return gestionAdministrativa()
    elif pathname == '/gestion-medica':
        return gestionMedica()
    elif pathname == '/gestion-tablas':
        return gestionTablas()
    elif pathname == '/registro-atencion-medica':
        return registroAtencionMedica()
    elif pathname == '/registro-atencion-administrativa':
        return registroAtencionAdministrativa()
    elif pathname == '/gestion-reporte-medico':
        return gestionReportesMedicos()
    elif pathname == '/gestion-reporte-administrativo':
        return gestionReportesAdministrativos()
    elif pathname == '/gestion-telemedicina':
        return gestionTelemedicina()
    else:
        return gestionSistema()

@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = build_graph(city)
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)