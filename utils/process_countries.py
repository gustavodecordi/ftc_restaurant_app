import pandas as pd
import plotly.express as px 

def restaurants_by_country( df, country_options ):
    cols = ['country_code','restaurant_id']
    sel = ( df.loc[ df['country_code'].isin(country_options),cols].groupby(['country_code'])
                                                                  .count()
                                                                  .sort_values('restaurant_id', ascending = False )
                                                                  .reset_index()
          )
    fig = px.bar(
                 sel, 
                 x='country_code', 
                 y='restaurant_id',
                 title='Quantidade de Restaurantes registrados por país', 
                 labels = {'country_code': 'Países', 'restaurant_id': 'Número de restaurantes registrados'},
                 text_auto=True   
                )
    return fig
    
def cities_by_country( df, country_options ):
    sel = ( df.loc[ df['country_code'].isin(country_options),['city','country_code']].groupby('country_code')
                                                                                     .nunique()
                                                                                     .sort_values('city', ascending = False )
                                                                                     .reset_index()
          )
    fig = px.bar(
                 sel, 
                 x='country_code', 
                 y='city',
                 title='Quantidade de cidades registradas por país', 
                 labels = {'country_code': 'Países', 'city': 'Número de cidades registradas'},
                 text_auto=True
    )
    return fig
    
def avg_rating_or_avg_price_by_country( df, col, country_options ):
        sel = ( df.loc[ df['country_code'].isin(country_options),['country_code', col]].groupby(['country_code'])
                                                                                       .mean()
                                                                                       .sort_values(col, ascending = False)
                                                                                       .reset_index()
              )
        sel[col] = sel[col].round(decimals = 2)
        if col == 'votes':
            title='Média de avaliações feitas por país'
            labels = {'country_code': 'Países', 'votes': 'Número de avaliações'}
        else: 
            title='Preço de prato para duas pessoas por país em dollares'
            labels = {'country_code': 'Países', 'price_in_dollar': 'Preço de prato para duas pessoas'}
        fig = px.bar(
                 sel, 
                 x='country_code', 
                 y=col,
                 title=title, 
                 labels=labels,
                 text_auto=True
        )
        return fig
        
    