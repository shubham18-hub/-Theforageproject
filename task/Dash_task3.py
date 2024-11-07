import pandas as pd
import dash
from dash import dcc, html
import datetime as dt 
import plotly.express as px

a = pd.read_csv(r'C:\Users\pablo\OneDrive\Escritorio\forage\quantium\1\quantium-task-1-model-answer\formated_data.csv')
a['date'] = pd.to_datetime(a['date'])
a['year'] = a['date'].dt.year
a['month'] = a['date'].dt.month_name()
def get_quarter(month):
    if month in ['January', 'February', 'March',]:
        return 'Q1'
    elif month in ['April','May', 'June']:
        return 'Q2'
    elif month in ['July', 'August','September']:
        return 'Q3'
    else:
        return 'Q4'
a['quarter'] = a["month"].apply(get_quarter)    
a = a.drop(columns=['Unnamed: 0'])
b = a[['year','sales','quarter',]].groupby(['year','quarter']).agg({'sales':'sum'}).reset_index()
b = b.pivot_table(values='sales', index='year', columns='quarter', aggfunc='sum', fill_value=0)
c = a[['year','sales','month',]].groupby(['year','month']).agg({'sales':'sum'}).reset_index()
c['month'] = pd.Categorical(c['month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)
c = c.sort_values(by=['year', 'month']).reset_index(drop=True)
c =c.pivot_table(values='sales', index='month', columns='year', aggfunc='sum', observed=False)

app = dash.Dash(__name__)

# Crear el gráfico de barras apiladas
bar_fig = px.bar(b,
             x=b.index, 
             y=b.columns, 
             title='Sales per quarter and year',
             labels={'x': 'year', 'value': 'sales', 'variable': 'quarter'},
             text_auto=True)
line_fig = px.line(c, 
                   x=c.index, 
                   y=c.columns, 
                   title='Sales trends by year and month',
                   labels={'x': 'month', 'value': 'sales', 'variable': 'year'},
                   markers=True)

# Configuración del gráfico
bar_fig.update_traces(textposition='inside')
bar_fig.update_layout(barmode='stack')

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Sales Chart"),
    dcc.Graph(figure=bar_fig),
    dcc.Graph(figure=line_fig)
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)