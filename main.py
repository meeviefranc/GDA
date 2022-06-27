from app import app
from layout import sidebar, content, dash_layout, cl_layout
from dataviz import al_layout, rt_layout, ls_layout, ave_layout, day_layout, week_layout, month_layout, geo_layout
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dash_layout
    elif pathname == "/analysis":
        return al_layout
    elif pathname == "/ridetype":
        return rt_layout
    elif pathname == "/longshort":
        return ls_layout
    elif pathname == "/ave":
        return ave_layout
    elif pathname == "/day":
        return day_layout
    elif pathname == "/week":
        return week_layout
    elif pathname == "/month":
        return month_layout
    elif pathname == "/geomap":
        return geo_layout
    elif pathname == "/conclusion":
        return cl_layout
    return dbc.Jumbotron([
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."), ])


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port='8050')
