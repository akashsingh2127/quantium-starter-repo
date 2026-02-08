import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div(className="container", children=[

    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    html.Div(className="radio-group", children=[
        dcc.RadioItems(
            id="region-selector",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        )
    ]),

    dcc.Graph(id="sales-line-chart")

])


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    daily_sales = (
        filtered_df
        .groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        },
        title="Pink Morsel Sales Over Time"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
