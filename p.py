import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

 

df = pd.read_csv('data/01_District_wise_crimes_committed_IPC_2001_2012.csv')
df = df[df['DISTRICT'] == "TOTAL"]
app = dash.Dash()

 


# https://dash.plot.ly/dash-core-components/dropdown
# We need to construct a dictionary of dropdown values for the years
year_options = []
for state in df['STATE/UT'].unique():
    year_options.append({'label':str(state),'value':state})

 

app.layout = html.Div([
    dcc.Graph(id='graph1'),
    dcc.Dropdown(id='year-picker1',options=year_options,value='BIHAR'),
    dcc.Graph(id='graph2'),
    dcc.Dropdown(id='year-picker2',options=year_options,value='BIHAR'),
    dcc.Graph(id='graph3'),
    dcc.Dropdown(id='year-picker3',options=year_options,value='BIHAR'),
    dcc.Graph(id='graph4'),
    dcc.Dropdown(id='year-picker4',options=year_options,value='BIHAR'),
    dcc.Graph(id='graph5'),
    dcc.Dropdown(id='year-picker5',options=year_options,value='BIHAR')
    
   
           
])

 

@app.callback(Output('graph1', 'figure'),
              [Input('year-picker1', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['STATE/UT'] == selected_year]
    traces = []
    for continent_name in filtered_df['DISTRICT'].unique():
        df_by_continent = filtered_df[filtered_df['DISTRICT'] == continent_name]
        print(df_by_continent)
        #print(x,y)
        traces.append(go.Scatter(
            x=df_by_continent['YEAR'],
            y=df_by_continent['MURDER'],
            text=df_by_continent['DISTRICT'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},

 

            name=continent_name
        ))
        return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'YEAR'},
            yaxis={'title': 'MURDER'},
            hovermode='closest'
        )
    }

 

@app.callback(Output('graph2', 'figure'),
              [Input('year-picker2', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['STATE/UT'] == selected_year]
    traces = []
    for continent_name in filtered_df['DISTRICT'].unique():
        df_by_continent = filtered_df[filtered_df['DISTRICT'] == continent_name]
        print(df_by_continent)
        #print(x,y)
        traces.append(go.Scatter(
            x=df_by_continent['YEAR'],
            y=df_by_continent['THEFT'],
            text=df_by_continent['DISTRICT'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},

 

            name=continent_name
        ))
        return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'YEAR'},
            yaxis={'title': 'THEFT'},
            hovermode='closest'
        )
    }

@app.callback(Output('graph3', 'figure'),
              [Input('year-picker3', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['STATE/UT'] == selected_year]
    traces = []
    for continent_name in filtered_df['DISTRICT'].unique():
        df_by_continent = filtered_df[filtered_df['DISTRICT'] == continent_name]
        print(df_by_continent)
        #print(x,y)
        traces.append(go.Scatter(
            x=df_by_continent['YEAR'],
            y=df_by_continent['RAPE'],
            text=df_by_continent['DISTRICT'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},

 

            name=continent_name
        ))
        return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'YEAR'},
            yaxis={'title': 'RAPE'},
            hovermode='closest'
        )
    }

@app.callback(Output('graph4', 'figure'),
              [Input('year-picker4', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['STATE/UT'] == selected_year]
    traces = []
    for continent_name in filtered_df['DISTRICT'].unique():
        df_by_continent = filtered_df[filtered_df['DISTRICT'] == continent_name]
        print(df_by_continent)
        #print(x,y)
        traces.append(go.Scatter(
            x=df_by_continent['YEAR'],
            y=df_by_continent['DACOITY'],
            text=df_by_continent['DISTRICT'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},

 

            name=continent_name
        ))
        return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'YEAR'},
            yaxis={'title': 'DACOITY'},
            hovermode='closest'
        )
    }

@app.callback(Output('graph5', 'figure'),
              [Input('year-picker5', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['STATE/UT'] == selected_year]
    traces = []
    for continent_name in filtered_df['DISTRICT'].unique():
        df_by_continent = filtered_df[filtered_df['DISTRICT'] == continent_name]
        print(df_by_continent)
        #print(x,y)
        traces.append(go.Scatter(
            x=df_by_continent['YEAR'],
            y=df_by_continent['RIOTS'],
            text=df_by_continent['DISTRICT'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},

 

            name=continent_name
        ))
        return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'YEAR'},
            yaxis={'title': 'RIOTS'},
            hovermode='closest'
        )
    }

 

if __name__ == '__main__':
    app.run_server()
 