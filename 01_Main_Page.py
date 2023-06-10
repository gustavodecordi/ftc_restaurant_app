import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

from utils import cleanned as cl

raw_data_path = './data/raw/data.csv'

def create_map(dataframe):
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(max_bounds=True).add_to(f)
    
    marker_cluster = MarkerCluster().add_to(m)
    
    for _, line in dataframe.iterrows():
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["rating_color"]}'
        
        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggregate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
                            )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
                     ).add_to(marker_cluster)

    folium_static(m, width=1024, height=768)
    
def build_sidebar( df ):
    st.sidebar.markdown('## App Company')
    
    image_path = './img/'
    image = Image.open(image_path + 'logo.png')
    st.sidebar.image( image, width = 50 )
    
    st.sidebar.markdown('## Filtro')
    country_options = st.sidebar.multiselect( 'Escolha os Países que Deseja visualizar as Informações',
                                              list( df['country_code'].unique() ),
                                              default = ['Brazil', 'Australia', 'United States of America']
                                            )
    st.sidebar.markdown("""---""")
    st.sidebar.markdown("### Dados Tratados")

    processed_data = pd.read_csv("./data/processed/data.csv")

    st.sidebar.download_button(
        label = "Download",
        data = processed_data.to_csv(index=False),
        file_name = "data.csv",
        mime = "text/csv",
    )
    
    return list(country_options)
    
def main():
    df = cl.clean_data( raw_data_path )
    
    st.set_page_config( 
                        page_title = 'Home',
                        page_icon = '📈',
                        layout = 'wide'
    )
    
    country_options = build_sidebar( df )
    
    st.markdown(
                """
                    ## App Company
                    ### O Melhor lugar para encontrar seu mais novo restaurante favorito!
                    ##### Temos as seguintes visões dentro da nossa plataforma:
                    - Visão Países:
                        - Distribuição dos restaurantes por país.
                    - Visão Cidades:
                        - Distribuição dos melhores e piores restaurantes por país e cidade.
                    - Visão "Cuisines":
                        - Distribuição dos Melhores Restaurantes e dos Principais tipos Culinários por país.
                    #####
                """ 
    )

    st.markdown( '### Métricas gerais' )
    col1, col2, col3, col4, col5 = st.columns( 5 ) 
    with col1:
        col1.metric( 'Restaurantes cadastrados:', df.shape[0] )
        
    with col2:
        col2.metric( 'Países cadastrados:', df['country_code'].nunique() )

    with col3:
        col3.metric( 'Cidades cadastradas:', df['city'].nunique() )
        
    with col4:
        col4.metric( 'Avaliações:',f"{df['votes'].sum():,}".replace(",", ".") )
    with col5:
        col5.metric( 'Tipos de culinárias:', df['cuisines'].nunique() )
    
    df = df.loc[ df['country_code'].isin(country_options), : ]
    create_map(df)
    
    st.markdown(
                """
                    ##
                    ##
                    ##### Ask for Help
                    - Time de Data Science no Discord
                        - @gustavo
                """ 
    )
    return None

if __name__ == "__main__":
    main()
