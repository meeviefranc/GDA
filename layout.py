import dash_bootstrap_components as dbc
import base64
from dash import html


# intro layout
def dash_hdr(display):
    hdr = html.H4(html.B(display),
                  className="text-center mt-4 mb-5",
                  style={'color': '#503D36', "text-decoration": "None",
                         "border-radius": "2%", "background": "white",
                         "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 1)",
                         }, )
    return hdr


def txt_me(display):
    s = html.P(display,
               style={'textAlign': 'left', 'fontSize': '14px', 'color': 'black'})
    return s


dash_layout = dbc.Container([
    dbc.Row([
        dash_hdr("GOOGLE DATA ANALYTICS - Cyclistic Bike Share Program"),
        html.Div([
            html.H4(['INTRODUCTION:',html.Br()]),
            txt_me('This is a case study to identify and explore differences on how annual members '
                    'and casual riders use the Cyclistics Bike Share program.'),
            txt_me('The Marketing Director believes that the company’s future success depends on the number of the '
                    'program’s annual memberships. This is based on the report of the finance analysts who have concluded '
                    'that annual members are more profitable than casual riders. Furthermore, the MD believes that there is '
                    'a good chance that casual riders can convert to annual membership because they have already experienced '
                    'the program and have chosen Cyclistics bikes at some point for their mobility needs.'),
            txt_me('Addressing the following will guide the future marketing strategy:'),
            txt_me('- How annual members and casual riders differ in using the bikes'),
            txt_me('- Why casual riders would buy an annual membership'),
            txt_me('- How digital media can affect their marketing tactics to influence casual riders to become members'),
            txt_me('- What are the trends on the historical bike trip data'),
            txt_me('The MD, Lily Moreno, has assigned me as a Data Analyst to address the first question. '),
            html.H4('PROBLEM:'),
            txt_me('This case study aims to address - How do annual members and casual riders use Cyclistic bikes differently?'),
            html.H4('SOLUTION:'),
            txt_me('In the course of this case study, I used the Data Analysis Phase - Ask, Prepare, Process, Analyze, Share and Act. '
                   'The solution is presented below using each of the phases.'),
        ])
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([html.Hr(),
        html.H6('JUPYTER NOTEBOOK:'),
        html.A("Link to Jupyter Notebook", href='https://www.kaggle.com/code/mvmlfranc/cyclistic-bike-share', target="_blank"),
        dbc.Col([
            txt_me('A Jupyter Notebook version of this analysis is available in the repository.'),
            txt_me('The notebook was used to collect data from the Month-Year csv files and store it into one csv file.'),
            txt_me('Refer to Step 2: Prepare under Data Organisation for more details on these csv files.'),
            txt_me('The resulting csv file is the source data for this dash application.'),
            txt_me('The notebook also shows how the collected data was processed, cleaned and transform to support the analyze phase.'),
            txt_me('Refer to Step 3: Process under Data Cleaning & Integrity Check section for more details.')
        ], style={"box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)",
                  "border-radius": "2%"}),
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([html.Hr(),
        html.H5('STEP 1: ASK'),
        html.H6('BUSINESS OBJECTIVE'),
        txt_me('Analyze the historical data from the Cyclistics Bike Share program to identify the key differences '
               'on how casual riders and annual members use Cyclistics bikes for their mobility needs.'),
        html.H6('BUSINESS TASK'),
        txt_me('Identify how casual riders and annual members use Cyclistic bikes differently. Specifically, '
               'find key differences that can help support a future marketing strategy geared towards converting casual riders to annual members.'),
        html.H6('STAKEHOLDERS'),
        txt_me(
            '- Lily Moreno (my Manager): The director of marketing. Moreno is responsible for the development of campaigns and initiatives to '
            'promote the bike-share program.'),
        txt_me(
            '- Cyclistic marketing analytics team (my team): A team of data analysts who are responsible for collecting, analyzing, and reporting '
            'data that helps guide Cyclistic marketing strategy.'),
        txt_me(
            '- Cyclistic executive team (decision-maker): The notoriously detail-oriented executive team will decide whether to approve the '
            'recommended marketing program.'),
        html.H6('DATA METRICS TO ACHIEVE OBJECTIVES'),
        txt_me(
            '- Is there a difference on the preference on the bikes they used - What type of bikes do casual and annual members use? '
            'E.g. electric vs classic bikes'),
        txt_me(
            '- Does the data indicate any difference on how they use the bikes - What type of rides do casual and annual members use '
            'for long and short rides?'),
        txt_me(
            '- Is there any difference in the frequency that they used the bikes depending on the time of day and day of week?'),
        txt_me(
            '- Is there any difference on how they use the bikes during the seasons? E.g. between summer and winter'),
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([html.Hr(),
        html.H5('STEP 2: PREPARE'),
        html.H6('DATA COLLECTION AND STORAGE'),
        txt_me(
            'Data used for this case study is from the Chicago Bike Share program from date period Nov 2020 to Nov 2021:'),
        html.A('https://divvy-tripdata.s3.amazonaws.com/index.html](https://divvy-tripdata.s3.amazonaws.com/index.html',
               target='blank',
               href='https://divvy-tripdata.s3.amazonaws.com/index.html](https://divvy-tripdata.s3.amazonaws.com/index.html'),
        html.Br(), html.Br(),
        txt_me('The behaviour of the customers might have changed '
               'towards the years so it is important to use a recent date period to draw observations based on the latest trends.'),
        html.H6('DATA ORGANISATION'),
        txt_me(
            'Data is stored and published using csv files. Each file represent month and year when the data was collected. '
            'I have collated data from the date period on each csv files and combine them into a single data source for the data analysis.'),
        html.H6('DATA CREDIBILITY'),
        txt_me('Data is from the Divvy bike-sharing program:'),
        html.A(
            'https://www.ideo.com/case-study/bringing-bikes-to-the-streets-of-chicago](https://www.ideo.com/case-study/bringing-bikes-to-the-streets-of-chicago',
            target='blank',
            href='https://www.ideo.com/case-study/bringing-bikes-to-the-streets-of-chicago](https://www.ideo.com/case-study/bringing-bikes-to-the-streets-of-chicago'),
        html.Br(), html.Br(), html.Br(),
        txt_me('Divvy is in charge of running the case study with the City of Chicago. '),
        txt_me(
            'Data can address the business objective because it is large scale covering use of classic and electric bikes '
            'by both members and casual users. There is enough information to attempt to answer the mission statement using this data. '),
        txt_me('Data is published by the Chicago government for public use.'),
        html.H6('PROBLEMS WITH THE DATA'),
        txt_me(
            '- Data is stored in different csv files. They need to be stored in one dataframe to make sure data is consistent.'),
        txt_me('- Some of the ride_ids, which identifies each ride, have duplicate ids.'),
        txt_me('- There are missing information for some of the rides.'),
        txt_me('- There are rides that are less than a minute which does not represent a valid usual ride for casual or annual members.'),
        txt_me('These problems were resolved during the Process phase.'),
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([html.Hr(),
        html.H5('STEP 3: PROCESS'),
        html.H6('TOOLS'),
        txt_me('I used the following tools during the case study :'),
        txt_me('- Excel: to review the initial source data which are in csv format and check for Data Integrity.'),
        txt_me('- Jupyter Notebook: to process and analyze data, checking further for data integrity and present my analysis report.'),
        txt_me('- Python Data Analytics libraries e.g. Pandas, Plotly, Seaborn: to create charts and graphs.'),
        txt_me('- PyCharm IDE and related Dash libraries: to present the data visualization using a Dash application. '),
        html.H6('DATA CLEANING &  INTEGRITY CHECK'),
        txt_me('I used the following steps to clean data, check for errors and transform data: '),
        txt_me('- Drop the columns that I don\'t need for the analysis: station id columns for the start_station_name, start station id and end station id for each ride.'),
        txt_me('- Remove missing values: remove all rows with NaN values in column. This mean the row has incomplete data.'),
        txt_me('- Remove duplicate records'),
        txt_me('- Length_mins column added to store the ride period in minutes calculated based on'
               'Start Date/Time and End Date/Time columns. Both date fields converted to datetime64.'),
        txt_me('- Remove all ride duration less than 1 minute. This can indicate misrecording of actual ride start and end time.'),
        txt_me('- Calculate what month, day of week and time of day the bike was used to compare data on how annual and casual bikers'
               'use the bikes during each time period.'),
        txt_me('- Calculate distance per ride for member and casual riders'),
        txt_me('- Determine if there is enough distribution for annual and casual members in the remaining data'),
        txt_me('- Store the data into one csv file as a source data for presenting the data visualization'),
        txt_me('Refer to the Jupyter Notebook in the repository on how the above process was implemented on the data.')
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([html.Hr(),
        html.H5('STEP 4: ANALYZE'),
        html.H6('ORGANIZE AND AGGREGATE DATA'),
        txt_me('With the available data, the following information can be derived:'),
        txt_me('- Type of bikes casual and annual members used'),
        txt_me('- Length of time to determine if rides were used leisurely or otherwise'),
        txt_me('- Time of Day, Day of Week and Month rides were taken'),
        html.H6('PERFORM CALCULATIONS'),
        txt_me('The following calculations were made'),
        txt_me('- percentage of ride types for casual and annual members'),
        txt_me('- average rides per time of day for casual and annual members'),
        txt_me('- average rides per day of week for casual and annual members'),
        txt_me('- average rides per month for casual and annual members'),
        html.H6('IDENTIFY TRENDS AND RELATIONSHIPS'),
        txt_me('- The following were determined using these calculations'),
        txt_me('- what type of bikes casual and annual members prefer in general'),
        txt_me('- what type of bikes casual and annual members prefer for long vs short rides'),
        txt_me('- on what time of day do they prefer to use the bikes'),
        txt_me('- on what day of week do they prefer to use the bikes'),
        txt_me('- difference on the use of bikes between seasons (rides per month)'),
        txt_me('Go to the Analysis page for the data visualization of these results.'),
        txt_me('The following Share and Act summarizes the findings based on these data metrics and visualization.'),
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([html.Hr(),
        html.H5('STEP 5: SHARE AND ACT'),
        html.H6('PUBLISH FINDINGS'),
        txt_me('The complete set of findings, data visualization, analysis results and conclusion can be found in the Jupyter notebook and on this Dash application.'),
        html.H6('WHAT STORY DOES YOUR DATA TELL'),
        txt_me('Both riders prefer the Classic Bike over Electric Bikes and Docked Bikes. But there is no clear indication from the data '
               'if the length of the ride (the longer it takes) affects their decision to use any bike type.'),
        txt_me('Comparing the average time spent on the ride vs the average distance, casual riders tend to ride the bikes leisurely whilst '
               'members will cover more distance in a shorter amount of time.'),
        txt_me('Looking at the frequency of rides per hour of day, rides for both riders tend to peak at 5pm. Moreover, the trend for the Members '
               'is to use the bikes between the usual working hours whilst rides from Casual riders starts to peak midday afternoon until early evening.'),
        txt_me('Looking at the frequency of rides per day of week, Casual riders can be seen using bikes more often during weekends. Annual members use '
               'the bikes throughout the week.'),
        txt_me('Looking at the frequency of rides per month, Casual riders tend to use the bikes during spring and summer. Annual members tend to ride '
               'less during the coldest time of the year.'),
        txt_me('Looking at the map density for the coordinates of their rides, the majority of the routes of both riders are mostly in the central area. '
               'But it looks like Casual riders have routes mostly on scenic sites like parks and landmarks. Whilst, Annual members have routes that include '
               'trips to outskirts and residential areas. This may indicate the use of the bikes for usual commute/transportation.'),
        txt_me('Go to the Conclusion page for the assumptions and insights on the Analysis Results and recommended next steps.')
    ], justify='center', style={"background-color": "white"}),
], fluid=True)


cl_layout = dbc.Container([
    dbc.Row([
        dash_hdr("CONCLUSION"),
        html.Div([
            html.H4(['ANALYSIS RESULTS', html.Br()]),
            html.H5(['How do annual members and casual riders use Cyclistic bikes differently?',html.Br()]),
            html.H6(['Based on the data analysis results, it can be assumed that:']),
            txt_me('- Classic Bike is the popular choice.'),
            txt_me('- Peak time for both riders on average will start late in the afternoon and ends in the early evening. '
                   'But most Casual riders are most likely to start using them in the afternoon for a leisurely ride.'),
            txt_me('- Both riders prefer using bikes during Spring and Summer. Annual members use the bikes mostly throughout the year except for colder months.'),
            txt_me('- Rides are popular for both bikers in the Central and Downtown area. But routes seem to differ - '
                   'Annual members are likely to include residential and outskirt areas whilst Casual riders includes scenic spots.'),
            html.H6('Based on these results, my insights are as follows:'),
            txt_me('- Peak time for casual riders starts in the afternoon til early evenings. Bikes also are popular to them during '
                   'the weekends and during summer and spring.'),
            txt_me('- Annual members will mostly use the bike share for commute and transportation.'),
            txt_me('- Casual riders will mostly use the bike for leisure activity.'),
        ])
    ], justify='center', style={"background-color": "white"}),
    html.Hr(),
    dbc.Row([
        html.Div([
            html.H4('NEXT STEP'),
            html.H5('Recommendations based on analysis'),
            txt_me(
                'Additional data can be added to map the route of the casual riders and members and further examine the riders\' routes. Aside from commute, '
                'transportation and tourist activities, there might be other activities that can be observed from the data (for example, exercise).'),
            txt_me(
                'To apply insights, marketing campaign can use this information to promote the popularity of the bikes for commute and leisure activities. '
                'The campaign can be held during the peak time when casual riders are using the bikes. Those casual riders might be more keen to convert '
                'to membership, especially those who use the bikes during the weekend.'),
            txt_me(
                'Next Steps to recommend includes further step on the data analysis process: another survey can be conducted and time time focused on the casual '
                'riders during peak hours to gain more information that can support the marketing campaign.'),
        ])
    ], justify='center', style={"background-color": "white"}),
], fluid=True)


# SIDEBAR LAYOUT
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 1)",
    "border-radius": "2%"
}
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "3rem 2rem",
}

png = base64.b64encode(open('bikeshare.png', 'rb').read()).decode('ascii')
sidebar = html.Div([html.H5("CYCLISTICS BIKE ANALYSIS",
                            style={'textAlign': 'center', 'color': '#503D36', 'font-family': 'open sans,sans-serif'}),
                    html.Hr(),
                    html.P("MENU", className="lead", style={'textAlign': 'center', 'color': '#503D36'}),
                    dbc.Nav(
                        [
                            dbc.NavLink("Introduction", href="/", active="exact"),
                            dbc.NavLink("Analysis Visualization", href="/analysis", active="exact"),
                            dbc.NavLink("- ride type distribution", href="/ridetype", active="exact"),
                            dbc.NavLink("- long vs short rides", href="/longshort", active="exact"),
                            dbc.NavLink("- average ride vs distance", href="/ave", active="exact"),
                            dbc.NavLink("- ride frequency in a day", href="/day", active="exact"),
                            dbc.NavLink("- ride frequency on a week", href="/week", active="exact"),
                            dbc.NavLink("- ride frequency on a month", href="/month", active="exact"),
                            dbc.NavLink("- geo map", href="/geomap", active="exact"),
                            dbc.NavLink("Conclusion", href="/conclusion", active="exact"),
                        ], style={"background-color": "#4e5d6c",
                                  "box-shadow": "0 2px 5px 0 rgba(0, 0, 0, .25), 0 3px 10px 5px rgba(0, 0, 0, 0.75)",
                                  "border-radius": "2%"},
                        vertical=True,
                        pills=True,
                    ),
                    html.Hr(),
                    html.Div([html.Img(alt='I have an image here.',
                                       # src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPkAAADKCAMAAABQfxahAAAAwFBMVEX///8Al6fu/0EAlqjx/z4AlakAlaosoqDL61uOy34AlKTy/z4Ak6oMl6iazdX0/zvi8PP3+/zW8VVKqrjy+fpasLzG6WB1wIpuvIvq9fbf7/L3/zjn+kZnuY7I5Oil13O12uAooKF6wobV8VV3vcem09qRydEwobBIrJlFq5mx32tjtMDR6OyEx4KFw8y44mfi+EtTsJWp2nCa0nhftZEXm6SIyYA9p5wqoaC14Wnc9lCVz3rP7lm/5mP//y693+PaZfXfAAAX7ElEQVR4nO1dB5uiyhK90IAKImZFMGDCnNEZ1Ov//1evGwHJWWf2vj377e4EQA7VXamri3/++Yu/+Iu/yB6VSp3vrB6DyaQ0faI0mQweqw5fr/z0vb0NFb7TG0zHy0ZNllkWwzD0F/4D/5PlWm05Lk16Hf6/xr9SfpTGkDKG0TSNYZjB+/UFDWgWPoHGuPTo/FfEj1gvIWnE2aTrA+25yMspZP/Tt50W9dVkrLEOoWwFkn5tXFr9weQh7WVM1i/hY3Kj1ON/mkIilAdjmQUJWJuyZ+XlpPPTNOKC741ryaRt4w4lP378SYLnB2iUp6T9BOS+nPwp3DulWka0dfKgtun8AYauDHmnmd2e3LHa9LdP+M5Upukwq52EOy1vfjP3+qSRubxN7ljt1873+qCR6fx2cWd/KffVRn6XvE3u2Hj10zRd4Cfym2k/ucvTXyb21fKtA91CHVs+fpqsBXxJ/gxvjbtcKv80YQOr8YcErlPHGr9jtlcGtQS3T1IUmVgh0rXJLwhh+SkbX+CAvbTX60tS5lDsmx8f8Z1xAo8NKOu8SDDXxMwhlj884h+1BDOc/OrjnNrcntIwp+XBT0YxjyTOCyALIn7Y56Q0xBH1yY/xrkzjGDOSNL7Y7+BALyZXcAZ1bPNDXk29FCM8YUFO0o9mz8ztQpm/SEN+/CMqno9lxdlWNX/SpM4qB+5gPDMWU9Iwp8c/ELrymzi3COkKwlVnvhAM5gA79y9pRj27/PiAL4/jjVMo89uJepI8Cvncc9KTFxU/UUHnhYH+tHXjx2zMCarM5tCOA3gW2cbxofYQWGrIVC9k6LmBWH7Up+FjShwB6vbzvQ0HOCnduWoXo6AD270x/XQ6Dkn9g3O9vklyu0C5C9VukcWKXZVTr/vLbK0KzXlKkUN8bq7Xp7EIQ+hfDnfcaE/Cp9aqcrh6U3Hmtk/NG+Jjdj2OHYeqvHVG+owi4VlrUWjuKWjc9wtIW6we51QmidrNZ+z6IFYagpzf8INCsbMLi5HKUSTu8DmwQNm3hu2ZklHmjp18wod/xMu/AOnAEVdprW6/kHI7EtwCaXNAFYuUW+A0QvxhAMOX9xPv1GLKibzkmd1WFfpIwKS0JeAQ8NFqgJUby2WSpUi61ns38fIytkio2Z1h8P7TbadyC445eo5yWt48+HqlzvemcmzbQdfebdtiqfUnyK8FQ4itou6wzm+cePa8dzPFVHk0YksdvFnLDeITx4pHZrdj1K4+xIv7prCbuVxWYBMav4z/OdN3El/FT8GwgBo2W0NRyBtswSm/zTlnOpAfKT+Jlt/owfPLuLdDAkVSMIUk1zsuDy05/AGE5J7noOSwS/FHF91431SfxLwXtvi1PtwPUMBAueLMNlcszs8z+J2LuFtgfFwbArF5F/FezJUUgHWbBMepyDUHyhEnmufCjTsAD71NL136KVb8r+NNC0+xxzrVHXHqodB9fvN1wAUcF8S1lzGn3eppksChedN4L0X7eGCkFqHfyt33CiBJCv2MlM43cZdvK16MWHcedZBgcZbdvMOLjahtgTQzUo1HJj8rAoqct85tCQUsuf0+557jGkpu5kkCYewNrlx9HO2zpb560KiDXJMpQHHPjiOREJGaw0jSL9VMu5VTKUkOgH5DrB7RypBz9V9xhqYymcszh8usAEPx0QgnroFEPDRctCftAOsxbVIiqnqDMt8tJCRaVukz4k2FGr11mX1zTSkw+eKyauVktSfZ+++RTTlQLhKpoPFOXhYiLjZbEkVRBS7vcttgSAYwoAeltGPRoDJNuCRPT7NVclFiU5J6JlQBeTkc0CIKyHWHJ6TSqNydWzj9NpqWl9NSaVwDGkfHKtkgablR1k7sNFzdgMvh+gy8qdNOaGoaDWUf4AORFoR6cogc1ErPkk7+WXkAMEs1QCXRUqVOPVPL1olg0cgWI661DB34OnBM/zmvAank2luCKTjMOF3rmTe4egZmslkNwJdSFJhlKvRIkw5aMRR4o1smlW8CPzypr0cqLqhrZ9JyaY9JwfOex4PeajUYy3Sa/Bw9zk7o0TJQ1OnGqW0tt0bN7wJewFCk8v3vv+K965jktKPG5xURyLLMplxgzVLoERMx5KnKqV3NSaMueUYsQL7s6XjeS1SQxBFKWVYJZzfT+YhZApYc7rjbXktAoAGwa0G7zsIfO5SbxypgJ376KYB5LSuhR7blLFpFyc+equ2kwrHvue7oFVElSXP5wiPyS4QY0SnACjiz1QoiABoAI6ctg0/He923vsywXJiuZeO9P6KFi4CkSGjDjjix1bQ6HACicHDnnXxi6Lhpj2AMMmEeKXQARWV+OkkwCu8TBLLlaHaf82vHYazvmm+llKXQMymgiRQ6AOz0PdqhPDqZ+ybEPlbEvqBZzzmrYAKyJkkSb76Qs4jTBxEWVeD83gm4Wm1hyKBtObx/uo6g90I6Tg1c5Y+b3wxCFjquPo7iv7VE7t6azTURk7M8h+/E50KaFWxwnoyP8klRmWeg41YRNA85u3ELqUjpIqbmhx0hNmfO0QtC6jpWWW6LSD/co3hX5Bqv7osWilJ33XJWModIHCFRGsYb6cP0eiTnagHNl/GEUHEIWh13WHI2QhFThp5c+txM6GCHHGFYIrxKnLrrnOcasd9Q5y0zMkMlJ6dddZiEECf3/TaLHbj715MuebmJ3aL7OOAn8fLSYnvrsRfufOGRzY2FUM1evDJ3qbjGd+0n3WJbVPfuqkZfiZfHNofrIdN2JGdeS+fMhCZjii1RPBUveeE2R85rEVq0g2sVxX+O80uo+SyhVaXUsCOFuk8XsIX67NTlxlwxMMS5ZlvBpFOTU/fuldIAiaOnZBnvFd6GeKV39g8dpGIe+sGoZruZo7DrjhPz2/wORqautVLglyQpL3W96L88UEo83tPlJyrhsSPZwncnqN5bN1wQBHF7cqWSWI9FMw0dQ4kEpBJSMG+kKQV2T3MUiz4TrPoaGXkZcVeSBeDSvh4LXcnpqvub1vKrFgaM/ZzN5MzTRS0P59UoZb8+9k8ou96eKchbAdhBuEvaciFgAeWxhER7Vy11rBbMdzksBfOAORQOhzVnyTmqV0Xamz2K1UU7B/V5cYjv9k/C3lOD9izNLNuqn3zzpSmYp7HoFbs1B6A1EphqcwFlzg5HjCDerieleBkxhcB1Uq9n33H4LLTPeE/DvJHcovN2PxpodemzZ7pBma+3okCoi9ZlwW2DFkppZ9mTRtx5FOutBtMwl5OruI7NaSdPI+E2IyndalEUNjs3IfnRiFBPHg6reQceqaGeS3XScq/sgSR1QiaS+zI9qx8DlANT7VrLk2FQluseVEEg8HMQcw+bVVktXWUjcs0DaUJ2OnnQYgudqNOOWTvvliyCr/ZC5e5BlerAS9XUXRscAe2BVAtsHtMsImweHHl+VrY5aQGgFAiv37wO8bSs9Xg7BBIguRdnU+1wsAs+ki3Oq9w6ULvXPMfdavy27jPPj3UX30SELVoG0lZYOO60+AxHgbLlFlJg1kr2bBLAb95KnW4kTUPaMuAo8WJnziqnuZ6OQHm4wK2GNNboeQy9yiPLJLsTQE6akerYmR+Epm0bBnna3Z92nNyrgdodgZY9m16tEuz5i4zEnvvKtrpCnhnDS9XAYlchr5eESAth4VPcaDnBs/lRxArDREici7OnJaj9jjtahjt5aXIHvd0h6G5b1uHAYl4mifZsDuFf66hfJTFxlh0kZG5f0wbKglHb5phmyYK4a5uT27KAhqq8NK9ElpGNtl1Ddm8nLHlVfT8boMrPy7BJ+yomLoh0rOaT+5Ew2usFECTVVYWDZErV+IKm5cYGNetFWD0m4xprvW3a3Qqm5FFdQNNsbTN5PK/S6U02NTkReZ+USCgc2W+0IM7d1goFUVSGI051rx9htemjbFXilfJjY7trwDr6fbmZw8ezeXTsV+ltkrRYTLquOHHMQICdVQFvXtun7vkuCreuw5ABrDHxCo86E1uXIajlrUc5mQO6Vip7WEB+Erv9HEjK3LWWD5T2iONwcbfDOabp3EbsYGTFamO/6cbjRc3BnGZ9212W4zbmSpybcMfGgMoN76ooiuq2JTl3lQb2sXo0bLeEvVpj2JiztKfHY2AVbxtbhszRNP3ad1vdmeQw3zQd0qHSkYQBptq1MQ9rIFCO1dAkcTWkd80nWictOkv74EgP+5C6LclAm2rXwpzFpmExRiXOomNi5tEzQQAr2W653BtMJpNBzzbv+Y3VvHky33hexTYMKtPoUs90tPvAIvFKp4RWw7SqdblhbUltdVS9mNNWiZdLS+RCwquwcmNqUXoxpJ44QI+4TcueOO1MZYwGuj2EyqBWenG3VAZ4MLcGlfy09trJCC9Xs2iRSmRPP7HMnfbc9wNeiyh1aLpttVQsjdUGpihfMZCbuSVdV3FeBRn5l+/nzFj7I7knExED4wx+49EgkJZf09cMTzyYm/3e6h5TmbV2BnMt/WTNPOJeOWBmlX13jZuzwayhdTF/pY54vyTVy+JFHe9J/fZHJOa0Gf/7F7Sx5sMxxOVibsbSFd8U+0udrKLt9kgcq/UiJbtfCjRoVcBIANcbwJP5aznCf46xpgnxfzq24xPH59GerCnyR8BbGWhTpPoWY5fMjd8H1TzTJpUo9YkpcjKRtq8AwxYFl8Gb01hfkncwN6s1K4ElSabhi1ZElXhDCx+lMM9cCQyzBAOd2saTuaGFQ3SLuS4bxe4krwasRHmwxogKKywxJ/Iz0+Mc7cZzCalCM/caR9FByfPtlU34aKdrum++Clk0MMuEOpr2sDM3vZjQ+Ws8aL4RfJx2b8nr+yO4r6YQwoolzeKNujbR7cxNZRHeYkE/rzKOIJXk1VGD8JaHRk1xfRPG3LyPpVvmwAgnQ60VvXweWZmGOxuexRrREGEyGVcP3+BkaneNnWO0688vXLOYRiCCikuxfh5hI67BvBx6qKkRNGk5NJz+XT38KkYJyCA0nAJY8kLvCDvVwCDqQzJtjKY9HMz18qnw3ZDmKmH41r40OzoqoZOXTcJcM+AOmUdlTr+Yh76mbpmi/HMSpuLYJKPdreEM5uE7KOKM9jT7l8JVnMHg92m45PGKxifUczdsVfjEAIZV0yzxy+KgFcUYVm0c2aql2oYenvJ6OaUhzE0RVLQRTU+NEvYpkrnhyYQmQ9jInkzKpjqhY8rUW50Qv9NyoHbPsgHE9eXahg0yIyaOoAuT14QhhE/0V8QSwtwYHN5JtIF+lZBJEyNiSeHHIEQIVA0NGtLbi9WF5d2tw5zoYZuxDTqhbV7SVL1q9xmuuMzMRGCACQzNXvZ8lqbJyywzkcqaI0RI8A70Q4MizFcy3UdzmCYoaKa/iikjRBRJ864GwhSXNQr23+4DzP0FFZ/E9Gs/x8R/3cxskxkhA5l6j+I/oVujX4Lw32LFmutu/mNoYHyib1bg1cw2gn5L3ygufInpJXQ41T0nMW2+Ds5fGbx2INQ3nlIHr3R7hJW1lDYNIUrLKNMfq3vVc9Dy6y78szzsa7tLZeJ1FctCdXiclrzw84XwZIttLXDQoB0rirbeWEFK0FKr+VgC+4oiTTder1mK0JEyeZmzBb2wT0Gf87Kd/ORVAQdoYCv5DN5fDmqvq9QnDdasoYRf1Eqvq9SjFMtk0RQxQu8kFrOWZZQH45rMog70cm0zsCgaPmR62vYv8YON/rp4x1XqG++iSduVsumfFGFTrKPApVJe9QaDQW9lq2urh5oi1rZ1S7/Kw36VyibCOmdGPbOirWGF5rbDJK7d8TjM5eSjEM+ivwZCPUJqG8krrCos0i2HV4VFQPLFFQd6Ue6ZtepwFyqDWrS3HNCW2hL3VR4Rr5JV09do/UVQCbd/9Wf0fWey7+ApR7xKhj1fo5aN0PJm5ZZ7pbeJ1diRlscrt9wr6L3LEa+SXZ9f78jSC6y8edjvmh+MY+8zBPL4YZ+p/CP6VegM/DcT0Tv2IfvbmA5WnXK53FkNtJL8+HXp2lU2r6s05BjbGui08akVkWoITABM24chy2n7QMErxL9Kxp2dY7ZpfO69Sdm91NzBE/Mq2Xbzjv9Wjp9C5s28UzRa/ixSrax4IayA5bfgDU37w4rjAEl9AmHvHkyffnMjuGgGXAofQSv4ZXTZtjDXUW4EfSbVxj8Boulu/W8lnqUT80Jg9yyqTXAEBMMR6A4ZBt4l+gf9R6C/TzAmB4bDRVw7GB2A45Yv9BOfZ3GcdrR+PhfMPGOLZiAwyQ1lvm1BDA87ePvicUEQu+sdfsmMCjdmdG498W0SV4/tU7ePDm5eVY0xAY/UnoR6bWo/2B3hGectDp9cf6id3i58BzH3a0qTGkHuO9UWW9TlcsmBk0owVamLc01ljYjPlKbQx6T5BeEo6uK9z7H5aY7Bg/GCcn+OkwXWR8Jm+qCNnghzyymXi8QOVUacAe30y+kQwPxNYx3h4V/nCJm3c3e1eisoR5zTmN8hc656gt9D5le1Wq2ORjpxXOxKB3WnnsmCSDiYE+KpmLvDMc7kpfaomm9hR06cX/LaBXaBo/2Nr4L3T8kh5pcRQ3DqvCuazAko8QOOmB80LUAYikq9nESGYMQ+/K2DObdVTtKQ0JgPcUZQc3sRn892XNg89+nMlQ3Kvk6sxlwVhH/zX0OT+VmTOPFkznGGJkNTeH8ZCfoPIHMOQdBH+1D6Pl3gLEDMRfiwZjONuYCUZ4Buf/M7JH0XGBFzZX0tDHP7kT7P79JpDyVOaDI/NyGqL+u0zX0NF000nSHzY1PDFTEn8rm2eMD6usw5ZqtAgzm/bOEBeZHxZU5n0sQ6AF4LPzrzFupHQBb3eYP5F1bEFoib0NdaEkDFhawZpxmq7UlhsT00AXjhxQUxP6IuTfPTjmDyuf3xeL5I39zzTU6ssg1g/u7X5FZ8XDlNw21Ho9tidmkKusy/CjNNV0GZtw79fr8JGTe/v7+bIlJkarN/wRZI5oUFwvcaMifU+X4ncFdlwUHmmKIUv+7w2FnuCC+w2Pkyf4vzZodPtYKh4QjuoFwN5kN8oUDhafMczWkCqbYiBclwAvyaYO5f0H6hea5pLzTPuQPWvt+bR6yFc/mv7v2+l5oEIcJ5zmjn+zD/yEvQvXcIPpmjOX1XCoJp1fACVhAR876h3baHQ/9brB5UxGR32qs2q8aJXVKRIFjpxmnz/P51gvZ8Pt8xAd7r+9+Qq8FzKdPQ7YK4VhYv5oTahdMWyVzQAOfxU7zKUITf3qWnzE3mQlM6bSHuBXAkbki342cW2fOZ+LyAJ/O3azcDXlkKxBxrD4etPXozSVUxZE7ccrkRZL4fatjqqn03xPbn41pCpF/M2T6zxuAEZxhOnc1UxBw+u7k0wudKSzv/6uW9fuRN2AZ1l9Sh337MIeyPO+iynwoEMzr1EZ/DPi/c99rvcpLpve76e0mRuvBJEIfT7cm8ud/i59buOS/6p5F6OmoPZN8khvr5e0/v9Y2+mxMTl9Qhc7E6gn92yIDj6g7986Spor+jqs17hQept+ZN+1ZUjR/CE3Y7w7+FP90Zvyd2Ve0CVdVrtKcvDIlFnXYx1wNJnZjxz/M/wvpL/cev6PT1OOzfvH5PBESpHyX+T2Xi2IoJ43Mjhn4nPJi/+e3fbjikTp7yn8Dt8OWYZ5+VOAKUuo26kvsIJIfEM35fZDQ4OliSH4FN4jQ7+Ani6DWPP5uDp+V3Rym+WGX5Prj4xGsf8ty8kOmr8P4k4qjvS4KubVkAYKFlVG+GZ6Xr+0Fj0zclmGOg986WrX7E5cdP6TYrOrE6l2XB2/tVjD+Aul9y7j0A8i8Y6QZW3iX9b+EdWHH4eXxM0dGsb7PJn8JHZjuNLX/UiHuDH9TePORp6K7+nhluBT+ppXq7QBhxufQ7eSOUSx794TLijYU0F/1p8KVkHZjDePt30f096Eyz5k7TYPNLXJcQaM0gs6INp89vnt9O1AfLdK9SMYA2bA1+/zi3oVOyd25PAEBjtT9kmNtRR3sZ6GgbT7xo0676/j8I9cc4keTRLr9xwFaePwL13mQZa18DGiaNae+PlbYVFb43bcgsCKvSR2/zAHJj8+B/UzCWGvxqMF0+d5ra3zVivmKLrS03g/+GrF2o1PnOY7IZNyy7U9BelcZyU3qs+Pp/StR+gA+B58s8X///oPsXf/FT+B9YdKVTOf329wAAAABJRU5ErkJggg==')
                                       src="data:image/png;base64,{}".format(png),
                                       style={'height': '50%','width': '50%'})
                              ], style={'textAlign': 'center'}),
                    html.Br(),
                    html.Footer([html.P(['A Capstone Project for',html.Br(),'Google Data Analytics',html.Br(),
                                        'Certificate Program'],
                                        className="card-text", style={'textAlign': 'center', 'color': '#503D36'}),
                                 html.A('by mvf 2021', target='blank',
                                        href='mailto:meeviefranc@gmail.com'),html.Hr(),
                                 html.I(
                                 txt_me('My 4th wall: This case study is originally intended for R. My personal goal however is to specialize in Python.'
                                        ' I have deviated from using R so I can explore the python libraries.')
                                 )], style={'textAlign': 'center'})
                    ], style=SIDEBAR_STYLE, )

content = html.Div(id="page-content", style=CONTENT_STYLE)

