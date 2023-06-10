<p align="center">
  <img src= img/logo.png alt="logo da empresa" width="200" height="200"/>
</p>

# Problema de Negócio

A App Company é uma empresa de tecnologia que desenvolveu um aplicativo para conectar restaurantes e pessoas. Através do aplicativo, é possível pedir refeições de qualquer restaurante cadastrado e recebê-las no conforto da sua casa por meio de entregadorores também cadastrados.

A empresa funcinona como um marketplace de restaurantes, sendo seu principal objetivo facilitar o encontro e as negociações entre clientes e estabelecimentos gastronômicos. Os restaurantes se cadastram na plataforma da App Company, fornecendo informações como endereço, tipo de culinária oferecida, disponibilidade de reserva, opções de entrega e também uma avaliação dos serviços e produtos do restaurante, entre outros detalhes.
Neste momento, a tarefa principal é identificar e fornecer ao CEO os principais indicadores-chave de desempenho (KPIs) estratégicos organizados em um único produto de dados: um painel interativo. Esse painel ajudará o CEO na tomada de decisões com base em três perspectivas do negócio.

# Premissas assumidas para a análise

1. O modelo de negócio adotado foi o Marketplace.
2. Foram estabelecidas três principais perspectivas de negócio: Visão por Países, Visão por Cidades e Visão por Culinárias (ou Cuisines).
3. Com o objetivo de facilitar a comparação dos preços dos pratos nos restaurantes dos 15 países que utilizam a plataforma, foi realizada a conversão dos valores para dólares.

# Estratégia da solução

O painel estratégico foi desenvolvido utilizando uma página principal que mostra algumas métricas gerais e três outras páginas que refletem as três visões do modelo de negócios da empresa, bem como suas métricas mais detalhadas.
1. Visão Geral;
2. Visão por Países;
3. Visão por Cidades;
4. Visão por Culinárias;

Cada visão é representada pelo seguinte conjunto de métricas:

1. Visão Geral:

	* Restaurantes cadastrados;
	* Países cadastrados;
	* Cidades cadastradas;
	* Avaliações;
	* Tipos de culinárias;
	* Filtro que permite acessar as localizações dos restaurantes de cada país em um mapa
	
2. Visão por Países:
	* Quantidade de restaurantes registrados por país; 
	* Quantidade de cidades registradas por país; 
	* Média de avaliações feitas por país;
	* Preço médio de prato para duas pessoas por país em dólares
		
3. Visão por Cidades
* Top 10 cidades com mais restaurantes cadastrados na base;
* Top 7 cidades com média de avaliação acima de 4;
* Top 7 cidades com média de avaliação abaixo de 2.5;
* Top 10 cidades com restaurantes com tipos de culinárias distintas

4. Visão por Culinárias
* Melhor restaurante de culinária indiana;
* Melhor restaurante de culinária americana;
* Melhor restaurante de culinária italiana;
* Melhor restaurante de culinária do tipo cafe;
* Melhor restaurante de culinária do tipo pizza;
* Top melhores restaurantes de acordo com os países e culinárias selecionadas com os filtros;
* Top melhores tipos de culinárias selecionadas com os filtros;
* Top piores tipos de culinárias selecionadas com os filtros

# Top 3 insights de dados
	
1. Embora a Índia tenha o maior número de restaurantes registrados na base, com um total de 3110 estabelecimentos, ela não detém o recorde de avaliações. Surpreendentemente, a Indonésia, mesmo com apenas 80 restaurantes registrados, possui uma média impressionante de 1112,82 avaliações, em comparação com as 887,08 da Índia;
2. Outro fenômeno interessante ocorre com os restaurantes americanos. Embora os Estados Unidos tenham um número expressivo de restaurantes registrados, com 1374 estabelecimentos, a Austrália, com apenas 179 restaurantes, supera significativamente a quantidade de avaliações feitas na plataforma. Os restaurantes australianos possuem uma média de 727,12 avaliações, quase o dobro da média dos restaurantes americanos, que é de 380,17;
3. Essas informações revelam que o número de restaurantes registrados nem sempre corresponde ao número de avaliações recebidas, demonstrando diferenças surpreendentes entre países com menos estabelecimentos, mas altas taxas de avaliação, e países com maior presença de restaurantes, mas menor envolvimento dos usuários na plataforma.

# O Produto final do projeto

Painel online, hospedado em uma Cloud e disponível para qualquer dispositivo conectado à internet através do link: 

https://gustavodecordi-ftc-restaurant-app-01-main-page-c1w8u0.streamlit.app/cuisines

# Conclusão

O objetivo dessse projeto foi criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.
O número de restaurantes registrados em um país não necessariamente reflete o número de avaliações recebidas. Isso indica que fatores como engajamento dos usuários e popularidade dos restaurantes podem ter um impacto significativo no número de avaliações. Além disso, os insights destacam a necessidade de analisar a qualidade e relevância das avaliações, além da quantidade, para obter uma imagem mais completa e precisa sobre a experiência dos usuários nos restaurantes.

# Próximos passos

1. Reduzir o numero de métricas;
2. Criar novos filtros;
3. Adicionar novas visões de negócios.

