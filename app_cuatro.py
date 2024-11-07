


from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Load the data
a = pd.read_csv(r'C:\Users\pablo\OneDrive\Escritorio\forage\quantium\1\quantium-task-1-model-answer\formated_data.csv')
a['date'] = pd.to_datetime(a['date'])
a['year'] = a['date'].dt.year
a['month'] = a['date'].dt.month_name()    
a = a.drop(columns=['Unnamed: 0'])

# Initialize the Dash app
app = Dash(__name__)

colors = {
    'background': '#012E40',
    'text': '#F2E3D5',
    'bar_color': '#3CA6A6'
    
}

# Define the layout of the app
app.layout = html.Div(style={'backgroundColor': colors['background'],}, children=[
    html.Div(style={'flex': '1', 'padding': '10px'}, children=[
        html.H1(
            children='Sales per Region',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
    ]),
    
    html.Div(style={'flex': '0 0 auto', 'padding': '10px', 'textAlign': 'right'}, children=[
        html.Label('Select Regions',
                   style={
                       'color': colors['text']
                   }),
        dcc.Checklist(
            options=[{'label': region, 'value': region} for region in a['region'].unique()],
            id='yaxis-column',
            value=a['region'].unique().tolist(),  # Default to all regions selected
            style={
                'color': colors['text'],
            },
        ),
    ]),
    dcc.Graph(id='fig'),
])

# Callback to update the figure
@callback(
    Output('fig', 'figure'),
    Input('yaxis-column', 'value'),
)
def update_figure(selected_regions):
    if not selected_regions:  
        return px.histogram()

    filtered_a = a[a['region'].isin(selected_regions)]

    fig = px.histogram(
        filtered_a,
        x='region', 
        y='sales', 

        histfunc='sum',
        text_auto=True
    )
    fig.update_traces(marker_color=colors['bar_color'])
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    

    fig.update_layout(transition_duration=500)

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)