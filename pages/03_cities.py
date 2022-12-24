import pandas as pd
import streamlit as st
from utils import process_cities as pc

def read_processed_data():
    return pd.read_csv("./data/processed/data.csv")

def build_sidebar( df ):
    st.sidebar.markdown('## Filtro')
    country_options = st.sidebar.multiselect( 'Escolha os Países que Deseja visualizar as Informações',
                                              list( df['country_code'].unique() ),
                                              default = ['Brazil', 'Australia', 'United States of America']
                                            )
    st.sidebar.markdown("""---""")
    
    return list(country_options)

def main():
    st.set_page_config( 
                        page_title = 'Visão Cidades',
                        page_icon = '🌆',
                        layout = 'wide'
    )

    df = read_processed_data()
    
    st.markdown('# 🏙 Visão Cidades')
    
    country_options = build_sidebar( df )
    
    fig = pc.top_restaurants_by_city( df, country_options )
    st.plotly_chart( fig, use_container_width = True )
    
    col1, col2 = st.columns( 2 )
    with col1:
        fig = pc.top_or_worst_restaurants_by_average_rating( df, country_options )
        st.plotly_chart( fig, use_container_width = True )
    with col2:
        fig = pc.top_or_worst_restaurants_by_average_rating( df, country_options, option = 'worst' )
        st.plotly_chart( fig, use_container_width = True )
        
    fig = pc.top_cities_cuisines( df, country_options )
    st.plotly_chart( fig, use_container_width = True )
    
    return None
    
if __name__ == "__main__":
    main()