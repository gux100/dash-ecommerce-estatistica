import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# 1. Ler o arquivo CSV dentro de um dataframe
df = pd.read_csv('ecommerce_estatistica.csv')

# 2. Inicializar a aplicação Dash
app = dash.Dash(__name__)

# 3. Layout da aplicação
app.layout = html.Div([
    html.H1("Dashboard de Estatísticas de E-commerce"),

    # Dropdown para seleção de gráfico
    dcc.Dropdown(
        id='graph-selector',
        options=[
            {'label': 'Gráfico de Vendas por Categoria', 'value': 'vendas_categoria'},
            {'label': 'Gráfico de Receita por Região', 'value': 'receita_regiao'},
            # Adicione mais opções de gráficos conforme necessário
        ],
        value='vendas_categoria'  # Valor inicial
    ),

    # Div para exibir o gráfico
    dcc.Graph(id='main-graph')
])


# 4. Callback para atualizar o gráfico com base na seleção do dropdown
@app.callback(
    Output('main-graph', 'figure'),
    [Input('graph-selector', 'value')]
)
def update_graph(selected_graph):
    if selected_graph == 'vendas_categoria':
        fig = px.bar(df, x='Categoria', y='Vendas', title="Vendas por Categoria")
    elif selected_graph == 'receita_regiao':
        fig = px.pie(df, names='Região', values='Receita', title="Receita por Região")
    # Adicione outras condições para diferentes gráficos aqui

    return fig


# 5. Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
