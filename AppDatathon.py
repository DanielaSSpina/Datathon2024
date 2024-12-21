import streamlit as st
import pandas as pd
import numpy as np

# Configuração do título do aplicativo
st.set_page_config(page_title="Projeto de Previsão de Preço de Petróleo", page_icon="📊", layout="wide")

st.markdown("<p style='font-size:40px; color:#B40C40;'>Tech Challenge 4 | Fiap</p>", unsafe_allow_html=True)

# Criando um menu de navegação com `selectbox` ou `radio`
pagina = st.sidebar.radio("Escolha a Página", ["Introdução", "Metodologia", "Principais Acontecimentos", 
                                               "Dashboard Interativo", "MVP", "Referências"])

# Conteúdo de cada página
if pagina == "Introdução":
    st. image ('Imagens/Banner/Página inicial - GG.jpeg')
    st.markdown("<h3 style='color:#264CAC;'>Introdução</h3>", unsafe_allow_html=True)
    st.write('''Este trabalho tem como foco apresentar a análise do preço do petróleo brent, trazendo quatro acontecimentos que auxiliem a explicação das variação do preço e podem variar desde fatores geopolíticos até avanços tecnológicos. 
Traremos além dos acontecimentos, uma análise por meio de um dashboard dinâmico dos dados, previsão analisada e MVP.''')

    st.markdown("<h3 style='color:#264CAC;'>Ferramentas utilizadas</h3>", unsafe_allow_html=True)
    st.write('Para a realização deste trabalho, foi utilizado as seguintes ferramentas:')
    st.write('Python: utilizado para toda a tratativa inicial das bases como organização das colunas, remoção de espaços e duplicidades e valores nulo, assim como para a realização da previsão dos preços do petróleo por meio do modelo de machine learning PROPHET.')
    st.write('PowerBI: utilizado para a criação de um dashboard interativo compilando as informações disponíveis do preço do petróleo, previsão e acontecimentos que influenciam na explicação da variação do preço.')
    st.write('Streamlit: utilizado para desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) e disponibilização das etapas e informações do projeto.')

elif pagina == "Metodologia":
    st. image ('Imagens/Banner/Metodologia GG 2048x733.jpeg')
    st.markdown("<h3 style='color:#264CAC;'>Metodologia</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#6C778A;'>Origem e análise dos dados</h3>", unsafe_allow_html=True)
    st.write('Os dados utilizados nesta análise foram extraídos do site do Instituto de Pesquisa Econômica Aplicada (Ipea). Após a extração, os dados foram salvos em um arquivo excel, e importados no python para tratamentos iniciais mostrados abaixo:')
    st. image ('Imagens/Python/1. Pyhton - importanto bibliotecas.png', caption='importando e instalando bibliotecas necessárias')
    st. image ('Imagens/Python/2. Python - importando bibliotecas.png', caption='importando e instalando bibliotecas necessárias')
    st.image('Imagens/Python/3. Python - tratamento de dados.png', caption='importação da base de dados e tratamento inicial')

    st.markdown("<h3 style='color:#6C778A;'>Modelo de Machine Learning</h3>", unsafe_allow_html=True)
    st.write('Para realizar o machine learning dos nossos dados, utilizamos o modelo Prophet, pois é uma ferramenta que se destaca em cenários onde previsões de longo prazo e ajustes a tendências e sazonalidades complexas são necessários.')
    st. image ('Imagens/Python/9. Python - Estrutura do dado para previsão.png', caption='preparando os dados para o Prophet')
    st. image ('Imagens/Python/10. Python - Preparação para previsão.png', caption='preparando os dados para o Prophet')
    st. image ('Imagens/Python/11. Python - Visualização da previsão.png', caption='gráficos plotados de tendência e sazonalidade')
    st. image ('Imagens/Python/12. Python - Forecasting.png', caption='criação do forecast')
    st. image ('Imagens/Python/13. Python - Unindo bases para previsão.png', caption='unindo bases para a criação do arquivo de previsão')
    st. image ('Imagens/Python/14. Python - Acurácia do modelo.png', caption='validando acurácia do modelo')

elif pagina == "Principais Acontecimentos":
    st. image ('Imagens/Banner/Acontecimentos GG 2048x733.jpeg')
    st.markdown("<h3 style='color:#264CAC;'>Principais Acontecimentos</h3>", unsafe_allow_html=True)

    st.markdown("<h3 style='color:#6C778A;'>Crise econômica de 2008:</h3>", unsafe_allow_html=True)
    st.write('''A crise financeira de 2008, a mais grave desde a Grande Depressão, começou nos Estados Unidos e rapidamente se espalhou globalmente, afetando bancos, mercados financeiros e milhões de pessoas. A bolha imobiliária foi alimentada por empréstimos de alto risco, chamados "subprime", e pela especulação de que imóveis seriam investimentos seguros. Quando os preços dos imóveis caíram, muitos proprietários ficaram com dívidas maiores do que o valor das casas. Isso causou grandes perdas em instituições financeiras, como Lehman Brothers, que faliu em setembro de 2008. O congelamento do crédito afetou empresas e consumidores, gerando uma recessão global. O preço do petróleo inicialmente subiu devido a preocupações geopolíticas, mas caiu drasticamente no final de 2008, devido à queda na demanda causada pela desaceleração econômica.''')
    st.image('Imagens/Python/6. Python - visualização do impacto - Crise econômica.png', caption='Crise econômica de 2008')

    st.markdown("<h3 style='color:#6C778A;'>Impacto do acordo da OPEP:</h3>", unsafe_allow_html=True)
    st.write('''A OPEP (Organização dos Países Exportadores de Petróleo e Aliados) que foi criada em 1960 inicialmente por 5 países que exportam petróleos e ao longo dos anos outros paises foram convidados a participar.
Ela foi criada com o objetivo de estabelecer uma política comum em relação à produção e à venda de petróleo, de forma a influenciar os preços do petróleo no mercado internacional. Por serem grandes produtores, seus membros são capazes mexer com as cotações, ao aumentar ou cortar a produção de forma coordenada.
Em 2016, quando os preços do petróleo estavam particularmente baixos, a Opep uniu forças com outros dez grandes produtores de petróleo para criar a Opep+, que tinha como missão reduzir a produção de petróleo e estabilizar o mercado global de energia. A decisão inicial ocorreu em setembro de 2016, durante a reunião em Argel, onde membros da OPEP concordaram em limitar a produção pela primeira vez desde 2008. Em novembro, a OPEP finalizou o acordo, e em dezembro, países não-membros (incluindo Rússia, México e outros) se comprometeram voluntariamente a cortes de produção, formando uma coalizão inédita para controlar o excesso de oferta global de petróleo.
Essas restrições resultaram em aumentos moderados nos preços do petróleo e ajudaram a recuperar parte da estabilidade do mercado.O acordo se mostrou crucial para amortecer impactos de oscilações no preço do petróleo nos anos seguintes, especialmente durante crises.''')
    st.image('Imagens/Python/7. Python - Visualização do impacto - Acordo opep.png', caption='Imapacto acordo da OPEP - 2016')

    st.markdown("<h3 style='color:#6C778A;'>Tensões geopolíticas do Oriente Médio:</h3>", unsafe_allow_html=True)
    st.write('''As tensões geopolíticas no Oriente Médio em 2020 foram intensificadas pela rivalidade entre os EUA e o Irã, além do conflito no Iêmen, que envolvia potências regionais. O assassinato do general iraniano Qassem Soleimani pelos EUA em janeiro de 2020 gerou uma resposta militar do Irã, com ataques a bases americanas no Iraque. Além disso, o Irã atacou instalações petrolíferas sauditas, elevando a volatilidade no mercado de petróleo. O apoio iraniano a grupos no Iêmen, Síria e Iraque intensificou as rivalidades, agravando a crise humanitária no Iêmen. A pandemia de COVID-19 também complicou as relações, embora houvesse tentativas de reaproximação entre países do Golfo. Essas tensões aumentaram a incerteza e volatilidade nos preços de energia, destacando a importância da estabilidade na região para a segurança econômica global.''')
    st.image('Imagens/Python/5. Python - visualização do impacto - Tensões no oriente.png', caption='Tensão geopolítica do oriente médio - 2020')

    st.markdown("<h3 style='color:#6C778A;'>Pandemia covid-19</h3>", unsafe_allow_html=True)
    st.write('''A pandemia de COVID-19, que começou no final de 2019 e se espalhou globalmente em 2020, resultou em uma crise de saúde sem precedentes que afetou todos os aspectos da vida cotidiana, levando a bloqueios, restrições de viagem e mudanças significativas nos padrões de consumo e produção. As economias foram severamente impactadas, com muitos setores enfrentando quedas drásticas na demanda.
Com a implementação de lockdowns e restrições de movimentação em todo o mundo, a demanda por petróleo caiu drasticamente. Indústrias, transporte e aviação sofreram com reduções severas no consumo. A demanda global de petróleo caiu cerca de 20% em abril de 2020, o que levou a um excesso de oferta significativo.
Em abril de 2020, o preço do petróleo alcançou um marco histórico com o petróleo WTI (West Texas Intermediate) chegando a valores negativos pela primeira vez, refletindo que os produtores estavam dispostos a pagar para que as pessoas retirassem o petróleo de seus estoques, dado o colapso da demanda e a falta de capacidade de armazenamento.''')
    st.image('Imagens/Python/4. Python - visualização de impacto - pandemia.png', caption='Pandemia Covid19 2020 - 2021')

elif pagina == "Dashboard Interativo":
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiODljNzU2NjUtNTQzNS00ODhhLWIyYTgtMDY0NzczY2M1MDE0IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"
    iframe_code = f'<iframe width="80%" height="700px" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>'

    st.components.v1.html(iframe_code, height=600)

elif pagina == "MVP":
    st. image ('Imagens/Banner/MVP GG 2048x733.jpeg')
    st.markdown("<h3 style='color:#264CAC;'>MVP</h3>", unsafe_allow_html=True)

    # Corrigindo a indentação do decorador e da função
    @st.cache
    def load_data():
        data_path = "Documentos/Dados  petroleo Forecasting .xlsx"  # Substitua com o nome correto ao fazer upload
        data = pd.read_excel(data_path)
        data['data'] = pd.to_datetime(data['data'])
        return data

    # Configuração inicial
        st.markdown("<h3 style='color:#6C778A;'>Previsão do Preço do Petróleo</h3>", unsafe_allow_html=True)
    st.write("Utilizando dados do modelo Prophet para análise e visualização interativa.")

    data = load_data()

    # Filtro por intervalo de datas
    st.sidebar.header("Filtro de Datas")
    start_date = st.sidebar.date_input("Data Inicial", data['data'].min())
    end_date = st.sidebar.date_input("Data Final", data['data'].max())

    filtered_data = data[(data['data'] >= pd.to_datetime(start_date)) & (data['data'] <= pd.to_datetime(end_date))]

    # Exibir dados filtrados
    st.write(f"Exibindo dados entre {start_date} e {end_date}")
    st.dataframe(filtered_data)

    # Visualização do Preço Realizado e Previsão
    st.markdown("<h3 style='color:#6C778A;'>Comparação: Preço Realizado vs. Previsão</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['data'], filtered_data['Fechamento realizado'], label="Fechamento Realizado", color="blue")
    ax.plot(filtered_data['data'], filtered_data['preco_previsto'], label="Preço Previsto", color="orange")
    ax.set_title("Preço do Petróleo: Realizado vs. Previsto")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preço (US$)")
    ax.legend()
    st.pyplot(fig)

    # Insights resumidos
    st.markdown("<h3 style='color:#6C778A;'>Insights</h3>", unsafe_allow_html=True)
    st.write("1. A previsão segue a tendência geral dos preços realizados com desvios ocasionais.")
    st.write("2. As maiores diferenças entre previsão e valores reais ocorrem em períodos de maior volatilidade.")
    st.write("3. O modelo mostra boa performance em períodos de estabilidade.")
    st.write("4. Eventos econômicos ou geopolíticos específicos podem impactar a precisão.")

    # Download dos dados filtrados
    st.markdown("<h3 style='color:#6C778A;'>Exportar Dados Filtrados</h3>", unsafe_allow_html=True)
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="Baixar dados filtrados como CSV",
        data=csv,
        file_name="dados_filtrados_petroleo.csv",
        mime="text/csv"
    )

elif pagina == "Referências":
    st. image ('Imagens/Banner/Referência GG.jpg')
    st.markdown("<h3 style='color:#264CAC;'>Referências</h3>", unsafe_allow_html=True)
   
    st.markdown("<h3 style='color:#6C778A;'>Crise financeira asiática 1997 - 1998</h3>", unsafe_allow_html=True)
    st.write('''https://iwofr.org/crise-financeira-asi%C3%A1tica/
    https://www.suno.com.br/artigos/crise-asiatica/''')

    st.markdown("<h3 style='color:#6C778A;'>Ataque 11 de setembro de 2001 </h3>", unsafe_allow_html=True)
    st.write('''https://einvestidor.estadao.com.br/mercado/11-de-setembro-mercado-financeiro/
    https://clicrdc.com.br/gestao-e-negocios/11-de-setembro-o-dia-que-mudou-a-historia-e-a-economia-global/''')

    st.markdown("<h3 style='color:#6C778A;'>Invasão ao Iraque - 2003</h3>", unsafe_allow_html=True)
    st.write('''https://www.greelane.com/pt/humanidades/problemas/oil-drive-us-invasion-of-iraq-3968261/''')

    st.markdown("<h3 style='color:#6C778A;'>Furacão Katrina - 2005</h3>", unsafe_allow_html=True)
    st.write('''https://pt.facts.net/historia/eventos-historicos/36-fatos-sobre-furacao-katrina/''')

    st.markdown("<h3 style='color:#6C778A;'>Primavera Árabe e Guerra Civil na Líbia - 2011</h3>", unsafe_allow_html=True)
    st.write('''https://revistas.ufpr.br/conjgloblal/article/download/74925/43315
    https://sites.ufpe.br/oci/2022/06/13/guerra-civil-na-libia-2011/''')

    st.markdown("<h3 style='color:#6C778A;'>Tensões entre EUA e Irã - 2014</h3>", unsafe_allow_html=True)
    st.write('''https://areferencia.com/oriente-medio/do-alinhamento-a-rivalidade-entenda-a-relacao-de-eua-e-ira-nos-ultimos-50-anos/
    https://conteudos.xpi.com.br/acoes/relatorios/quais-os-impactos-da-tensao-entre-ira-e-estados-unidos/
    https://www.terra.com.br/noticias/mundo/por-que-a-tensao-entre-eua-e-ira-no-estreito-de-ormuz-pode-fazer-disparar-o-preco-do-petroleo,3480d9d3c15dd3c6045aebbee253f0e87igg1e62.html''')
  
    st.markdown("<h3 style='color:#6C778A;'>Crise financeira 2008</h3>", unsafe_allow_html=True)
    st.write('''https://www.investopedia.com/ask/answers/052715/how-did-financial-crisis-affect-oil-and-gas-sector.asp
    https://cepr.org/voxeu/columns/oil-prices-and-economic-recession-2007-08
    https://www.investopedia.com/articles/economics/09/financial-crisis-review.asp''')
    
    st.markdown("<h3 style='color:#6C778A;'>Informações OPEP 2017 - 2018</h3>", unsafe_allow_html=True)
    st.write('''https://www.ecb.europa.eu/pub/pdf/other/eb201608_focus01.en.pdf
    https://www.opec.org/opec_web/en/press_room/6748.htm
    https://oglobo.globo.com/economia/noticia/2023/11/30/o-que-e-a-opep-como-ela-funciona-e-o-que-o-brasil-tem-a-ganhar-caso-se-torne-um-membro.ghtml''')
    
    st.markdown("<h3 style='color:#6C778A;'>Tensões geopolíticas do oriente médio 2017 - 2018</h3>", unsafe_allow_html=True)
    st.write('''https://www.wilsoncenter.org/article/explainer-roots-and-realities-10-conflicts-middle-east
    https://www.iemed.org/publication/geopolitical-trends-shifts-challenges-and-fractures-of-the-post-arab-spring-2020-2021/
    https://www.brookings.edu/articles/the-middle-east-and-north-africa-over-the-next-decade-key-challenges-and-policy-options/''')

    st.markdown("<h3 style='color:#6C778A;'>Conflito Rússia e Ucrânia 2022 - 2023</h3>", unsafe_allow_html=True)
    st.write('''https://assets.kpmg.com/content/dam/kpmg/br/pdf/2022/9/conflito_russia_ucrania_impactos_sobre_o_preco_da_energia.pdf
    https://veja.abril.com.br/economia/o-impacto-da-tensao-da-russia-e-da-ucrania-no-preco-dos-combustiveis/''')

    st.markdown("<h3 style='color:#6C778A;'>Instabilidade regional e decisões da OPEP+ 2024</h3>", unsafe_allow_html=True)
    st.write('''https://br.investing.com/news/commodities-news/o-que-esperar-do-petroleo-em-2024-especialista-traca-cenarios-1191005
    https://clickpetroleoegas.com.br/petroleo-em-foco-tensoes-e-expectativas-nos-investimentos-para-2024/
    https://exame.com/economia/opep-mantem-previsao-para-alta-na-demanda-global-por-petroleo-em-2023-e-2024/''')
