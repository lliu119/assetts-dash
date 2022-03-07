#2. Display the plot in a dash app that displays a stacked bar plot of country GDPs stacked within regions. Allow the user to select between the IMF, UN and World Bank reported numbers.

import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import os
import requests as rq
import bs4
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
page = rq.get(url)
## print out the first 200 characters just to see what it looks like
page.text[0 : 99]

bs4page = bs4.BeautifulSoup(page.text, 'html.parser')
tables = bs4page.find('table',{'class':"wikitable"})
bs4page = bs4page.findAll("sup",{"class":"reference"})
if bs4page:
    for ref in bs4page:
        ref.extract()
                    
GDP = pd.read_html(str(tables))[0]
GDP =GDP.dropna()
GDP.columns=["Country", "Region","IMF_Estimate","IMF_Year", "UN_Estimate", "UN_Year", "WB_Estimate", "WB_Year"]
GDP.head()

GDP= GDP[['Country', 'Region', 'IMF_Estimate','UN_Estimate', 'WB_Estimate']]
GDP.tail()

GDP= GDP.melt(id_vars= ['Country', 'Region'])
GDP.head()

## Define the app
app = dash.Dash(__name__)

## Read in our data
GDP.head()


## Define the app
app = dash.Dash(__name__)

## This creates the layout of the page
app.layout = html.Div([
    dcc.Dropdown(options = [
        {'label' :'IMF_Estimate', 'variable' :'IMF_Estimate'},
        {'label' :'UN_Estimate', 'variable' :'UN_Estimate'},
        {'label' :'WB_Estimate', 'variable' :'WB_Estimate'}
    ],
        value=1, id = 'input-level'),
    dcc.Graph(id= 'output-graph')
])
@app.callback(
    Output('output-graph', 'figure'),
    Input('input-level', 'value'))

def update_output_div(selected_level):
    subdat = GDP.loc[dat['variable'] == int('selected level')].sort_values(by = ['value'])
    fig= px.bar(subdat, x = 'Region', y = 'IMF_Estimate', color = 'Country')

    return fig


## This runs the server
if __name__ == '__main__':
    app.run_server(debug=True)