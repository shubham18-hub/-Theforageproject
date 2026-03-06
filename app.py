from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
#Your task is to create a Dash app to visualise the data you generated in the last task. Lean on the resources linked below to learn more about the basics of working with Dash. Your application must incorporate the following elements:
#A header which appropriately titles the visualiser
#A line chart which visualises the sales data generated in the last task, sorted by date. Be sure to include appropriate axis labels for the chart.
#Soul Foods would like a way to dig into region-specific sales data for Pink Morsels. To this end, they’d like a radio button in your visualiser which allows them to filter sales data by region. Leaning on the resources linked below, add a radio button with five options to narrow which data appear in the line chart: “north,” “east,” “south,” “west,” and “all.”
#Now it’s time to dress up your Dash app! Apply some CSS to each element to make your application more visually appealing. There are no requirements for this step other than that you put effort into making your visualiser interesting. The model answer contains an example styling, but the possibilities are infinite — make your visualiser your own!
# Load data
df = pd.read_csv("formatted_data.csv")
#Convert Sales into float
df["sales"] = df["sales"].astype(float)
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")
daily_sales = df.groupby("date")["sales"].sum().reset_index()
# Create line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales",
    template="plotly_white",
    font=dict(family="Arial, sans-serif", size=12, color="#333"),
    title=dict(font=dict(size=24, color="#ff69b4")),
    plot_bgcolor="rgba(240, 240, 240, 0.5)",  # light gray background
    paper_bgcolor="white",
    hovermode="x unified"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "textAlign": "center", "color": "#120d10", "fontSize": "48px","fontFamily": "Arial, sans-serif", "marginBottom": "30px"},
            id = "header"
        ),

        dcc.Graph(
            id="sales-graph",
            figure=fig,
            style={"width": "90%", "margin": "auto"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin-right": "20px"},
            style={"textAlign": "center", "margin-top": "20px"}
        )
    ]
)

@app.callback(
    Output("sales-graph", "figure"),      # what will change
    Input("region-filter", "value")       # what drives the change
)
def update_figure(selected_region):
    if selected_region == "all":
        filtered = df
    else:
        # boolean indexing or query to keep just that region
        filtered = df[df["region"] == selected_region]

    # recompute the time‑series exactly as you did before
    daily = filtered.groupby("date")["sales"].sum().reset_index()

    # recreate the Plotly figure
    fig = px.line(daily, x="date", y="sales", title="Pink Morsel Sales Over Time")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales",
        template="plotly_white"
    )
    return fig
#Run app
if __name__ == "__main__":
      #No longer uses app run server now just uses run  
    app.run(debug=True)

