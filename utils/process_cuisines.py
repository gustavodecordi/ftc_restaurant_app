import pandas as pd
import plotly.express as px 
import streamlit as st

def info(df, culinaria):
    df_line = ( df.loc[df['cuisines'] == culinaria,:]
                  .sort_values(by=['aggregate_rating','restaurant_id'], ascending = [False,True])
                  .reset_index().head(1)
              ) 
    nome_do_restaurante = df_line['restaurant_name'][0]
                          
    nota_do_restaurante = df_line['aggregate_rating'][0]
    
    pais = df_line['country_code'][0]
    
    cidade = df_line['city'][0]              
    media_prato_para_dois = round( df_line['average_cost_for_two'][0], 2 )
    
    moeda_local = df_line['currency'][0]
    
    metrica = st.metric(   label = f'{culinaria}: {nome_do_restaurante}', 
                           value = str(nota_do_restaurante) +" / 5.0",
                           help=f"""
                                    País: {pais}\n
                                    Cidade: {cidade}\n
                                    Média Prato para dois: {media_prato_para_dois} ({moeda_local})
                                 """
                       )
    return metrica
    
def show_dataframe( df, country_options, top_restaurants_slider, cuisines_options ):
    sel_lines = (df['country_code'].isin(country_options)) & (df['cuisines'].isin(cuisines_options))
    cols = ['restaurant_id','restaurant_name','country_code','city','price_in_dollar','cuisines','aggregate_rating','votes']
    sel = df.loc[ sel_lines, cols].sort_values(by=['aggregate_rating','restaurant_id'], ascending = [False, True])
    return sel.head(top_restaurants_slider)

def top_best_or_worst_cuisines( df, country_options, top_restaurants_slider, ascending_index ):
    cols = ['cuisines','aggregate_rating']
    sel = ( df.loc[df['country_code'].isin(country_options), cols].groupby(['cuisines'])
                                                                  .mean()
                                                                  .sort_values('aggregate_rating', ascending = ascending_index )
                                                                  .reset_index()
          )
    if ascending_index == False:
        title=f'Top {top_restaurants_slider} melhores tipos de culinárias'
    else:
        title=f'Top {top_restaurants_slider} piores tipos de culinárias'
    sel.columns = ['Tipo de culinária','Média da avaliação média']
    fig = px.bar(
                 sel.head(top_restaurants_slider), 
                 x='Tipo de culinária', 
                 y='Média da avaliação média',
                 title=title, 
                 text_auto=".2f"
    )
    return fig