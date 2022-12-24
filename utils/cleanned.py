import pandas as pd
import inflection

# Preenchimento do nome dos paises
def country_name(country_id):
    '''
        Esta funcao recebe um 'id' do pais e retorna o nome com base em um dicionario.
        Input: country_id
        Output: nome do pais
    '''
    COUNTRIES = {
                    1: "India",
                    14: "Australia",
                    30: "Brazil",
                    37: "Canada",
                    94: "Indonesia",
                    148: "New Zeland",
                    162: "Philippines",
                    166: "Qatar",
                    184: "Singapure",
                    189: "South Africa",
                    191: "Sri Lanka",
                    208: "Turkey",
                    214: "United Arab Emirates",
                    215: "England",
                    216: "United States of America",
                }
    
    return COUNTRIES[country_id]

# Criacao do Tipo de Categoria de Comida
def create_price_tye(price_range):
    '''
        Esta funcao categoriza o custo do prato de acordo com a faixa de preco.
        Input: faixa de preco 'price_range';
        Output: categoria
    '''
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"
    
# Criacao do nome das Cores
def color_name(color_code):
    '''
        Esta funcao recebe um codigo de cores e decodifica em uma cor de acordo com um dicionario.
        Input: codigo de cores;
        Output: cor correspondente
    '''
    COLORS = {
                "3F7E00": "darkgreen",
                "5BA829": "green",
                "9ACD32": "lightgreen",
                "CDD614": "orange",
                "FFBA00": "red",
                "CBCBC8": "darkred",
                "FF7800": "darkred",
              }
    return COLORS[color_code]

# Renomear as colunas do DataFrame
def rename_columns(dataframe):
    '''
        Esta funcao reescreve os titulos das colunas transformando todas as letras maiusculas em minisculas,
        unindo as palavras atraves do 'underscore' e eliminando os espacos em branco.
    '''
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

# Limpeza dos dados
def clean_data( file_path ):
    # Carregamento dos dados
    df = pd.read_csv( file_path )
    
    # Elimina as linhas duplicadas
    df = df.drop_duplicates()
    
    # Remove todos os dados faltantes NaN na coluna 'cuisines'
    df = df.dropna()
    
    # Remove a coluna 'Switch to order menu' -> nao adiciona informacao alguma
    df = df.drop('Switch to order menu', axis=1)

    # Aplicamos a funcao de renomar as 'features' 
    df = rename_columns(df)

    # Este cmd basicamente categoriza o tipo de culinaria somente pela primeira palavra.           
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    # Transformacao da coluna 'country_code' para os nomes dos paises.
    df['country_code'] = df['country_code'].apply( lambda x: country_name(x) )

    # Transformacao da coluna 'rating_color' para as cores.
    df['rating_color'] = df['rating_color'].apply( lambda x: color_name(x) )
    
    # Adicao de uma coluna extra com uma categorizacao pelo preco
    df['price_tye'] = df['price_range'].apply( lambda x: create_price_tye(x) )
    
    # Criacao de uma coluna adicional que converte os valores na coluna 'average_cost_for_two' para dollar
    cols = ['currency', 'average_cost_for_two']
    df['price_in_dollar'] = ( df[cols].apply( lambda x: 
                                                ( x['average_cost_for_two'] / 12.85  ) if x['currency'] == 'Botswana Pula(P)'  else
                                                ( x['average_cost_for_two'] / 5.31  ) if x['currency'] == 'Brazilian Real(R$)' else
                                                ( x['average_cost_for_two'] / 1  ) if x['currency'] == 'Dollar($)' else
                                                ( x['average_cost_for_two'] / 3.67  ) if x['currency'] == 'Emirati Diram(AED)' else
                                                ( x['average_cost_for_two'] / 82.68  ) if x['currency'] == 'Indian Rupees(Rs.)' else
                                                ( x['average_cost_for_two'] / 15608.45  ) if x['currency'] == 'Indonesian Rupiah(IDR)' else
                                                ( x['average_cost_for_two'] / 1.57  ) if x['currency'] == 'NewZealand($)' else
                                                ( x['average_cost_for_two'] / 0.819257  ) if x['currency'] == 'Pounds(£)' else
                                                ( x['average_cost_for_two'] / 3.64  ) if x['currency'] == 'Qatari Rial(QR)' else
                                                ( x['average_cost_for_two'] / 17.59  ) if x['currency'] == 'Rand(R)' else
                                                ( x['average_cost_for_two'] / 366.86  ) if x['currency'] == 'Sri Lankan Rupee(LKR)' else
                                                ( x['average_cost_for_two'] / 18.65  ) if x['currency'] == 'Turkish Lira(TL)' else 0, 
                                               axis=1 ) 
                             )
    # Arredondamento para duas casas decimais dos dados
    df['price_in_dollar'] = df['price_in_dollar'].round(decimals = 2)
    
    # Elimina duas linhas que contem outliers: 'average_cost_for_two' de 25000017.0 e 'votes' de 41333
    filtros = ( df['price_in_dollar'] < df['price_in_dollar'].max() ) & ( df['votes'] < df['votes'].max() )
    df = df.loc[filtros, :]
    
    df.to_csv("./data/processed/data.csv", index=False)
    
    return df