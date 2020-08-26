import dash
import dash_core_components as dcc
import dash_html_components as html
import math
import pandas as pd
import plotly.graph_objs as go

##################################################################################

feature_ind = 0  # The only thing needs to be modified: 0 -> PM25, 1 -> PM10. 2 -> O3, 3 -> NO2

##################################################################################

app = dash.Dash()
variables = ['PM25', 'PM10', 'O3', 'NO2']

df = pd.read_csv("./" + variables[feature_ind] + "_importance.csv")

unique_stations = list(df["station"].unique())

app.layout = html.Div([
    html.H2(children=variables[feature_ind] + ' Air Pollution Feature Importance Visualization'),
    dcc.Dropdown(
        id="station-dropdown",
        options=[
            {'label': i, 'value': i} for i in unique_stations
        ],
        value=unique_stations,
        multi=True
    ),
    dcc.Graph(id='gapminder'),
    dcc.Slider(
        id='hour-slider',
        min=df['hour'].min(),
        max=df['hour'].max(),
        value=df['hour'].min(),
        step=None,
        marks={str(hour): str(hour) for hour in df['hour'].unique()}
    ),
])


@app.callback(
    dash.dependencies.Output('gapminder', 'figure'),
    [dash.dependencies.Input('hour-slider', 'value'),
     dash.dependencies.Input('station-dropdown', 'value')])
def update_figure(selected_hour, selected_station):
    hour_filtered_df = df[df.hour == selected_hour]
    filtered_df = hour_filtered_df[df.station.isin(selected_station)]
    traces = []
    tmp_max = 0
    for i in filtered_df.station.unique():
        df_by_station = filtered_df[filtered_df['station'] == i].sort_values(['importance'], ascending=[0])[:20]
        tmp_max = max(tmp_max, df_by_station['importance'].max())
        traces.append(go.Scatter(
            x=df_by_station['feature'],
            y=df_by_station['importance'],
            text=df_by_station['feature'],
            mode='markers',
            opacity=0.7,
            marker={
                'line': {'width': 0.5, 'color': 'white'},
                'symbol': 'circle',
                'sizemode': 'area'
            },
            name=i,
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'category', 'title': 'feature'},
            yaxis={'title': 'importance', 'range': [0, tmp_max + 0.05]},
            margin={'l': 40, 'b': 150, 't': 10, 'r': 40},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050 + ind * 10)
