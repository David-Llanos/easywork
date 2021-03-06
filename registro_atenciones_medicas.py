import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
nav = Navbar()

body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Resgitrs Atenciones Medicas"),
                     html.P(
                         """\
                            Donec id elit non mi porta gravida at eget metus.Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentumnibh,\n
                            ut fermentum massa justo sit amet risus. Etiam porta semmalesuada magna mollis euismod. Donec sed odio dui. \n
                            Donec id elit nonmi porta gravida at eget metus. Fusce dapibus, tellus ac cursuscommodo, tortor mauris condimentum nibh, \n
                            ut fermentum massa justo sitamet risus. Etiam porta sem malesuada magna mollis euismod. Donec sedodio dui."""
                           ),
                           dbc.Button("View details", color="secondary"),
                   ],
                  md=6,
               ),
              dbc.Col(
                 [
                     html.H2("Graph"),
                     dcc.Graph(
                         figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                            ),
                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)

def registroAtencionMedica():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = registroAtencionMedica()
if __name__ == "__main__":
    app.run_server()

