import pandas as pd
import streamlit as st
from utils import process_countries as pcs

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
                        page_title = 'Visão Países',
                        page_icon = '🌎',
                        layout = 'wide'
    )

    df = read_processed_data()
    
    st.markdown('# 🌎 Visão Países')
    
    country_options = build_sidebar( df )
    
    fig = pcs.restaurants_by_country( df, country_options )
    st.plotly_chart( fig, use_container_width = True )
    
    fig = pcs.cities_by_country( df, country_options )
    st.plotly_chart( fig, use_container_width = True )
    
    col1, col2 = st.columns( 2 )
    with col1:
        fig = pcs.avg_rating_or_avg_price_by_country( df, 'votes', country_options )
        fig.update_yaxes(dtick=100)
        st.plotly_chart( fig, use_container_width = True )
    with col2:
        fig = pcs.avg_rating_or_avg_price_by_country( df, 'price_in_dollar', country_options )
        st.plotly_chart( fig, use_container_width = True )
        
    return None
        
if __name__ == "__main__":
    main()