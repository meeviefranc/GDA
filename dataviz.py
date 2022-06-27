import plotly.express as px
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from pandas.api.types import CategoricalDtype
from layout import txt_me
from plotly.subplots import make_subplots


# LOAD AND TRANSFORM DATA
df = pd.read_csv("CyclisticBikeData.csv", parse_dates=['started_at', 'ended_at'])
# Transform for Month, Day of Week, Time of Day, Length of Ride and coordinate systems
df['year'] = df['started_at'].dt.year
# month
cat_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
df['month'] = df['started_at'].dt.month_name()
df['month'] = df['month'].astype(CategoricalDtype(categories=cat_month, ordered=False))
# day of week
cat_dow = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
df['dweek'] = df['started_at'].dt.day_name()
df['dweek'] = df['dweek'].astype(CategoricalDtype(categories=cat_dow, ordered=False))
# time of day
df['hr_time'] = df['started_at'].dt.hour
df = df.astype(
    {'year': 'int16', 'hr_time': 'int8', 'length_mins': 'int32', 'start_lat': 'float', 'start_lng': 'float',
     'end_lat': 'float', 'end_lng': 'float'})


# DASHBOARD LAYOUT
# object functions
def dash_hdr(display):
    hdr = html.H4(html.B(display),
                  className="text-center mt-4 mb-5",
                  style={'color': '#503D36', "text-decoration": "None",
                         "border-radius": "2%", "background": "white",
                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 1)",
                         }, )
    return hdr


# DATA DISTRIBUTION
def dash_dist():
    dfg = df.groupby('member_casual')['ride_id'].agg(['count']).reset_index()
    cont = dbc.Container([dash_hdr("DATA VISUALIZATION"),
                          dbc.Row([
                                  dbc.Col([dcc.Graph(figure=px.histogram(dfg,
                                                     x="member_casual", y="count").update_layout(xaxis_title='riders', yaxis_title='count')),
                                           ], align='end'),
                                  dbc.Col([html.Hr(),
                                           html.H4(['DATA DISTRIBUTION', html.Br(), html.Hr()]),
                                           txt_me('Enough data is available for Member and Casual Riders after data went through the Process phase:'),
                                           txt_me('- Drop columns: station id columns for the start_station_name, start station id and end station id.'),
                                           txt_me('- Remove missing values: row has incomplete data.'),
                                           txt_me('- Remove duplicate records.'),
                                           txt_me('- Calculate for distance between rides and remove short rides less than a minute.'),
                                           txt_me('- Calculate what month, day of week and time of day the bike was used.'),
                                           html.Hr(),], align='center'),
                                  ], justify='between',
                                  style={"background-color": "white", "height": "450px", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)",}
                                  )
                          ], fluid=True)
    return cont


def dash_pie_fig(dfg):
    fig = px.pie(dfg, values='count', names='rideable_type', width=400)
    return fig


def dash_pie():
    dfg = df.groupby(['member_casual', 'rideable_type'])['ride_id'].count().reset_index(name="count")
    dfg_casual = dfg[dfg.member_casual =='casual']
    dfg_member = dfg[dfg.member_casual =='member']
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'RIDE TYPES DISTRIBUTION', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('Both casual riders and annual members prefer the Classic Bike.')])
                                  ], justify='between',
                                  style={"background-color": "white", "height": "500",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)"}
                                 ),
                          html.Br(),
                          dbc.Row([dbc.Col([html.Hr(), html.H6('CASUAL RIDERS'), html.Hr(),
                                            dcc.Graph(figure=dash_pie_fig(dfg_casual).update_layout(showlegend=False)), html.Br()
                                            ], align='end'),
                                   dbc.Col([html.Hr(), html.H6('ANNUAL MEMBERS'), html.Hr(),
                                            dcc.Graph(figure=dash_pie_fig(dfg_member)), html.Br()
                                            ], align='end'),
                                   ], justify='between',
                                   style={"background-color": "#761607", "height": "500", "border-radius": "2%",
                                          "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)"}
                                  )
                          ], fluid=True)
    return cont


def dash_ls_fig(dfg):
    fig = px.scatter(dfg, x="length_mins", y="rideable_type",
                       size="count", color="rideable_type",
                       hover_name="rideable_type", log_x=True, size_max=60).update_layout(xaxis_range=[-0.1, 2.5], showlegend=False)
    return fig


def dash_ls():
    dfg_casual = df[df['member_casual'] == 'casual'].groupby(['member_casual', 'rideable_type'])['length_mins'].value_counts().reset_index(name='count')
    dfg_member = df[df['member_casual'] == 'member'].groupby(['member_casual','rideable_type'])['length_mins'].value_counts().reset_index(name='count')
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'Type of Bikes Casual and Annual Members Prefer for Long Rides vs Short Rides', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('There is no clear indication from the data on how the riders, '
                                                   'both casual and member types, will prefer the type of their bikes to use based on the length of ride.')])
                          ], justify='between',
                              style={"background-color": "white", "height": "500",
                                     "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                          ),
                          html.Br(),
                          dbc.Row([dbc.Col([html.Hr(), html.H6('CASUAL RIDERS'), html.Hr(), dcc.Graph(figure=dash_ls_fig(dfg_casual)),
                                            html.Br()], align='end'),
                                   dbc.Col([html.Hr(), html.H6('ANNUAL MEMBERS'), html.Hr(), dcc.Graph(figure=dash_ls_fig(dfg_member)),
                                            html.Br()], align='end'),
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          ], fluid=True)
    return cont

def dash_ave():
    dfg = df.groupby(['member_casual'])[['length_mins','Distance']].mean().reset_index()
    fig1 = px.bar(dfg, x="member_casual", y="length_mins", color='member_casual',
                  color_discrete_map={'casual': '#FF934F', 'member': '#F2F283'}).update_layout(showlegend=False)
    fig2 = px.bar(dfg, x="member_casual", y="Distance", color='member_casual',
                  color_discrete_map={'casual': '#FF934F', 'member': '#F2F283'}).update_layout(showlegend=False)
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'Average Travel Time vs Average Distance by Member Type', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('Average time vs Average distance shows casual riders tend to ride the bikes leisurely.'),
                                            txt_me('Members on the other hand use bikes for longer distance on shorter rides.')])
                          ], justify='between',
                              style={"background-color": "white", "height": "500",
                                     "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                          ),
                          html.Br(),
                          dbc.Row([dbc.Col([html.Hr(), html.H6('AVERAGE TRAVEL TIME'), html.Hr(), dcc.Graph(figure=fig1),
                                            html.Br()], align='end'),
                                   dbc.Col([html.Hr(), html.H6('AVERAGE TRAVEL DISTANCE'), html.Hr(), dcc.Graph(figure=fig2),
                                            html.Br()], align='end'),
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          ], fluid=True)
    return cont


def dash_day():
    dfg = df.groupby(['hr_time','member_casual'])['ride_id'].count().reset_index(name='rides')
    fig = px.line(dfg, x='hr_time', y='rides', range_y=[0, 550000],
                     color='member_casual',
                     line_shape='spline',
                     markers=True,
                     labels={'rides': 'No. of Rides', 'hr_time': 'TimeOfDay', 'member_casual': 'Member/Casual'},
                     color_discrete_map={'casual': '#FF934F', 'member': '#3236A8'})
    fig.update_layout(xaxis_range=[0, 24], yaxis_range=[0, 300000])
    fig.update_layout(xaxis={"dtick": 1}, margin={"t": 0, "b": 0}, height=400)
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'Frequency of rides per Time of Day', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('Rides for both members and casual riders tend to peak during 5pm.'),
                                            txt_me('The trend for the Members to use the bikes is between the usual working hours,'
                                                   ' suggesting the use for transport.'),
                                            txt_me('The trend for the Casual riders to use the bikes starts to peak midday afternoon'
                                                   ' until early in the evening.')])
                          ], justify='between',
                              style={"background-color": "white", "height": "500",
                                     "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                          ),
                          html.Br(),
                          dbc.Row([html.Hr(), dcc.Graph(figure=fig), html.Hr()
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          ], fluid=True)
    return cont


def dash_wk():
    cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dfg = df.groupby(['dweek', 'member_casual'])['ride_id'].count().reset_index(name='rides')
    dfg['dweek'] = pd.Categorical(dfg['dweek'], categories=cats, ordered=True)
    dfg = dfg.sort_values('dweek')
    fig1 = px.line(dfg, x='dweek', y='rides', range_y=[0, 550000],
                   color='member_casual',
                   line_shape='spline',
                   markers=True,
                   labels={'rides': 'No. of Rides', 'dweek': 'Weekdays', 'member_casual': 'Member/Casual'},
                   color_discrete_map={'casual': '#FF934F', 'member': '#F2F283'})
    fig2 = px.bar(dfg, x='dweek', y='rides', color='member_casual',
                  hover_name='member_casual', hover_data={'member_casual': False, 'rides': True},
                  height=400)
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(fig1['data'][0], row=1, col=1)
    fig.add_trace(fig1['data'][1], row=1, col=1)
    fig.add_trace(fig2['data'][0], row=1, col=1)
    fig.add_trace(fig2['data'][1], row=1, col=1)
    fig.update_layout(title_text='ride frequency throughout the week', title_x=0.5)
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'Frequency of rides per Day of Week', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('Casual riders can be seen using the bikes more often during weekends. '),
                                            txt_me('Annual members use the bikes consistently throughout the week.'),
                                           ])
                          ], justify='between',
                              style={"background-color": "white", "height": "500",
                                     "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                          ),
                          html.Br(),
                          dbc.Row([html.Hr(), dcc.Graph(figure=fig), html.Hr()
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          ], fluid=True)
    return cont


def dash_mo():
    dfg = df.groupby(['month','member_casual'])['ride_id'].count().reset_index(name='rides')
    fig = px.line(dfg, x='month', y='rides', range_y=[0, 550000],
                       color='member_casual',
                       line_shape='spline',
                       markers=True,
                       labels={'rides': 'No. of Rides', 'month': 'Month', 'member_casual': 'Member/Casual'},
                       color_discrete_map={'casual': '#FF934F', 'member': '#3236A8'})
    fig.update_layout(yaxis_range=[0, 400000])
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'Frequency of rides per Month', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('Casual riders tend to use the bikes during spring and summer.'),
                                            txt_me('Annual members tend to ride less during the coldest time of the year')])
                          ], justify='between',
                              style={"background-color": "white", "height": "500",
                                     "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                          ),
                          html.Br(),
                          dbc.Row([html.Hr(), dcc.Graph(figure=fig), html.Hr()
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          ], fluid=True)
    return cont

def dash_geo_map(dfg):
    fig = px.scatter_mapbox(dfg, lat="end_lat", lon="end_lng",
                            hover_name="end_station_name",
                            hover_data=["end_station_name"],
                            color_discrete_sequence=["#3236A8"], zoom=9, height=600)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

def dash_geo():
    dfg = df[['member_casual','end_station_name','end_lat', 'end_lng']].drop_duplicates()
    dfg_casual = dfg[dfg['member_casual'] == 'casual']
    dfg_member = dfg[dfg['member_casual'] == 'member']

    fig1 = dash_geo_map(dfg_casual)
    fig2 = dash_geo_map(dfg_member)
    cont = dbc.Container([dbc.Row([html.H4([html.Hr(),'Casual Riders vs Annual Members Density Map', html.Br(), html.Hr(),
                                            html.B(txt_me('ANALYSIS:')),
                                            txt_me('Majority of the routes of both riders are mostly in the central area.'),
                                            txt_me('Casual riders have routes mostly on scenic sites like parks and landmarks.'),
                                            txt_me('Annual members have routes scattered in the outskirts and residential areas which indicates the use of the bikes for usual commute.')])
                          ], justify='between',
                              style={"background-color": "white", "height": "500",
                                     "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                          ),
                          html.Br(),
                          dbc.Row([html.Hr(), html.H6('CASUAL RIDERS'), html.Hr(),
                                   dcc.Graph(figure=fig1), html.Hr()
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          html.Br(),
                          dbc.Row([html.Hr(), html.H6('ANNUAL MEMBERS'), html.Hr(),
                                   dcc.Graph(figure=fig2), html.Hr()
                                   ], justify='between',
                                  style={"background-color": "#761607", "height": "600", "border-radius": "2%",
                                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)", }
                                  ),
                          ], fluid=True)
    return cont


al_layout = html.Div(children=[dash_dist(), html.Hr(), html.Br(),])
rt_layout = html.Div(children=[dash_pie(), html.Hr(), html.Br(),])
ls_layout = html.Div(children=[dash_ls(), html.Hr(), html.Br(),])
ave_layout = html.Div(children=[dash_ave(), html.Hr(), html.Br(),])
day_layout = html.Div(children=[dash_day(), html.Hr(), html.Br(),])
week_layout = html.Div(children=[dash_wk(), html.Hr(), html.Br(),])
month_layout = html.Div(children=[dash_mo(), html.Hr(), html.Br(),])
geo_layout = html.Div(children=[dash_geo(), html.Hr(), html.Br(),])

