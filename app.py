import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


rfm = pd.read_csv('output/rfm_results.csv')


app = Dash(__name__)


fig = px.scatter(
    rfm,
    x='Recency',
    y='Monetary',
    size='Frequency',
    color='Segment',
    hover_data=['CustomerID', 'RFM_Score'],
    title='Interactive Customer Segmentation (RFM)',
    template='plotly_dark'
)

fig.update_layout(
    xaxis_title='Recency (days)',
    yaxis_title='Total Spend ($)',
    legend_title='Customer Segment'
)

# 4️⃣ Layout – გვერდის სტრუქტურა
app.layout = html.Div([
    html.H1('E-commerce Customer Analysis Dashboard', style={'textAlign': 'center'}),
    html.P('Explore customer behavior and segmentation using RFM methodology.', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# 5️⃣ აპის გაშვება
if __name__ == '__main__':
    app.run(debug=True)
