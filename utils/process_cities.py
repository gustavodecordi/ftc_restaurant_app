import pandas as pd
import plotly.express as px 

# Top 10 cidades com mais restaurantes registrados na base de dados
def top_restaurants_by_city( df, country_options ):
    cols = ['country_code','city','restaurant_id']
    sel = ( df.loc[ df['country_code'].isin( country_options ), cols].groupby(['country_code','city'])
                                                                     .count()
                                                                     .sort_values('restaurant_id', ascending = False )
                                                                     .reset_index() 
          )
    sel.columns = ['Paises','Cidade','Quantidade de restaurantes']
    fig = px.bar(
                 sel.head(10), 
                 x = 'Cidade', 
                 y = 'Quantidade de restaurantes',
                 title = 'Top 10 cidades com mais restaurantes', 
                 color = 'Paises',
                 text_auto=True   # Inclui os números nas barras
                )
    return fig
    
# Top 7 cidades com media de avaliacao acima de 4.0 ou abaixo de 2.5    
def top_or_worst_restaurants_by_average_rating( df, country_options, option = 'top' ):
    if option == 'top':
        filtro = (df['aggregate_rating'] > 4.0) & ( df['country_code'].isin(country_options) )
        title = 'Top 7 cidades com média de avaliação acima de 4'
    else: 
        filtro = (df['aggregate_rating'] < 2.5) & ( df['country_code'].isin(country_options) )
        title = 'Top 7 cidades com média de avaliação abaixo de 2.5'
        
    cols = ['country_code','city','restaurant_id']
    sel = ( df.loc[filtro, cols].groupby(['country_code','city'])
                                .count()
                                .sort_values('restaurant_id', ascending = False )
                                .reset_index()
          )
    sel.columns = ['paises','Cidade','Quantidade de restaurantes']
    fig = px.bar(
                 sel.head(7), 
                 x = 'Cidade', 
                 y = 'Quantidade de restaurantes',
                 title = title, 
                 color = 'paises',
                 text_auto = True
    )
    return fig

# Top 10 cidades com restaurantes com tipos de culinarias distintas
def top_cities_cuisines( df, country_options ):
    cols = ['country_code','city','cuisines']
    sel = ( df.loc[ df['country_code'].isin(country_options), cols].groupby(['country_code','city'])
                                                                   .nunique()
                                                                   .sort_values('cuisines', ascending = False)
                                                                   .reset_index() 
          )
    sel.columns = ['paises','Cidade','Quantidade de restaurantes']
    fig = px.bar(
                 sel.head(10), 
                 x = 'Cidade', 
                 y = 'Quantidade de restaurantes',
                 title = 'Top 10 cidades com restaurantes com tipos de culinárias distintas', 
                 color = 'paises',
                 text_auto = True
    )  
    return fig    