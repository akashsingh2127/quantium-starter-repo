import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("processed_sales_data.csv")


df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

daily_sales = df.groupby("date", as_index=False)["sales"].sum()


fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales"}
)


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])


if __name__ == "__main__":
    app.run(debug=True)
