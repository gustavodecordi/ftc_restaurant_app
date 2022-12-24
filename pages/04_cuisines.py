import pandas as pd
import streamlit as st
from utils import process_cuisines as pci

def read_processed_data():
    return pd.read_csv("./data/processed/data.csv")

def build_sidebar( df ):
    st.sidebar.markdown('## Filtro')
    country_options = st.sidebar.multiselect( 'Escolha os Países que Deseja visualizar as Informações',
                                              list( df['country_code'].unique() ),
                                              default = ['Brazil', 'Australia', 'United States of America']
                                            )
    
    top_restaurants_slider = st.sidebar.slider(
                                                'Selecione a quantidade de Restaurantes que deseja visualizar?',
                                                value = 10,
                                                min_value = 0,
                                                max_value = 20
                                              )

    cuisines_options = st.sidebar.multiselect( 'Escolha os Tipos de Culinária',
                                               list(df['cuisines'].unique()),
                                               default = ['Italian', 'European','Brazilian']
                                             )
    
    st.sidebar.markdown("""---""")
    
    return list(country_options), top_restaurants_slider, list(cuisines_options) 

def main():
    df = read_processed_data()
    
    st.set_page_config( 
                        page_title = 'Visão Cuisines',
                        page_icon = '👩‍🍳',
                        layout = 'wide'
                      )
    
    country_options, top_restaurants_slider, cuisines_options = build_sidebar( df )
    
    st.markdown( '### Melhores Restaurantes dos Principais tipos Culinários' )
    col1, col2, col3, col4, col5 = st.columns( 5 ) 
    with col1:
        pci.info(df, 'North Indian')
    with col2:
        pci.info(df, 'American')
    with col3:
        pci.info(df, 'Cafe')
    with col4:
        pci.info(df, 'Italian')
    with col5:
        pci.info(df, 'Pizza')
    
    st.dataframe( pci.show_dataframe( df, country_options, top_restaurants_slider, cuisines_options ) )
    
    col1, col2 = st.columns( 2 )
    with col1:
        fig = pci.top_best_or_worst_cuisines( df, country_options, top_restaurants_slider, False )
        st.plotly_chart( fig, use_container_width = True )
    with col2:
        fig = pci.top_best_or_worst_cuisines( df, country_options, top_restaurants_slider, True )
        st.plotly_chart( fig, use_container_width = True )
        
    return None
        
if __name__ == "__main__":
    main()