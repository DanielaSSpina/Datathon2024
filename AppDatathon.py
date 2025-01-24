import streamlit as st
import pandas as pd
import numpy as np

# Configuração do título do aplicativo
st.set_page_config(page_title="Projeto de Previsão dados ONG Passos Mágicos", page_icon="📊", layout="wide")

st.markdown("<p style='font-size:40px; color:#B40C40;'>Datathon | Fiap</p>", unsafe_allow_html=True)

# Criando um menu de navegação com `selectbox` ou `radio`
pagina = st.sidebar.radio("Escolha a Página", ["Introdução", "Metodologia", "Análise", 
                                               "Dashboard Interativo", "MVP", "Referências"])

# Conteúdo de cada página
if pagina == "Introdução":
    st. image ('imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Introdução</h3>", unsafe_allow_html=True)
    st.write('''Este trabalho tem como objetivo trazer uma proposta preditiva para mostrar o impacto das ações da ONG Passos Mágicos sobre a comunidade que atendem
    Os impactos a serem analisados terão como base o perfil dos estudantes atendidos,  informações educacionanais, informações socioeconômicas e as respostas da pesquisa realizada pela ONG.''')

    st.markdown("<h3 style='color:#0367B0;'>Ferramentas utilizadas</h3>", unsafe_allow_html=True)
    st.write('Para a realização deste trabalho, foi utilizado as seguintes ferramentas:')
    st.write('Python: utilizado para toda a tratativa inicial das bases como organização das colunas, remoção de espaços e duplicidades e valores nulo, assim como para a realização da previsão dos preços do petróleo por meio do modelo de machine learning PROPHET.')
    st.write('PowerBI: utilizado para a criação de um dashboard interativo compilando as informações disponíveis do preço do petróleo, previsão e acontecimentos que influenciam na explicação da variação do preço.')
    st.write('Streamlit: utilizado para desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) e disponibilização das etapas e informações do projeto.')

elif pagina == "Metodologia":
    st. image ('Imagens/abraco-meninos.jpg')
    st.markdown("<h3 style='color:#0367B0;'>Metodologia</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#145089;'>Origem e análise dos dados</h3>", unsafe_allow_html=True)
    st.write('''Os dados utilizados nesta análise foram extraídos do Drive disponibilizado pela FIAP. 
    Após a extração, os dados foram salvos em um arquivo excel, passado por um tratamento inicial onde foi ajustado as acentuações em algumas palavras e importados no python para demais tratamenots necessários conforme abaixo:''')
    st. image ('Imagens/1.1 Leitura e tratamento de Dados.png')
    st. image ('Imagens/1.2 Leitura e tratamento de Dados.png', caption='importando e instalando bibliotecas necessárias')

    st.markdown("<h3 style='color:#145089;'>Análises iniciais</h3>", unsafe_allow_html=True)

  
    st.write('Para realizar o machine learning dos nossos dados, utilizamos o modelo X, pois ?????w.')
    st. image ('Imagens/2.1 Análise desempenho escolar.png')
    st. image ('Imagens/2.2 Análise desempenho escolar - defasagem.png')
    st. image ('Imagens/2.3 Análise desempenho escolar - defasagem.png')
    st. image ('Imagens/3.1 Visualização de Dados - Notas vs frequência.png')
    st. image ('Imagens/3.2 Visualização de Dados - Idade vs frequência.png')
    st. image ('Imagens/3.3 Visualização de Dados - Desempenho vs Idade.png')
    st. image ('Imagens/3.4 Visualização de Dados - Idade vs Desempenho acadêmico.png')
    st. image ('Imagens/3.5 Visualização de Dados - Frequencia vs Desempenho escolar.png')
    st. image ('Imagens/3.6 Visualização de Dados - Taxa de aprovação vs Idade.png')
    st. image ('Imagens/3.7 Visualização de Dados - Notas vs Tipo de escola.png')
    st. image ('Imagens/3.8 Visualização de Dados - Desempenho vs idade vs frequência vs tipo de institu.png')
    st. image ('Imagens/3.9 Visualização de Dados - Faltas vs Idade.png')
    st. image ('Imagens/3.11 Visualização de Dados - Reprovados vs Idade.png')

  
    st.markdown("<h3 style='color:#145089;'>Machine Learning</h3>", unsafe_allow_html=True)
  
  
    st. image ('Imagens/4.1 Previsão de comportamento - Treinamento.png')
    st. image ('Imagens/4.1 Previsão de comportamento.png')
    st. image ('Imagens/4.2 Previsão de comportamento - Comparação entre variáveis.png')
    st. image ('Imagens/4.3 Previsão de comportamento - Idade vs INDE.png')
    st. image ('Imagens/4.4 Previsão de comportamento - NLP.png')
    st. image ('Imagens/4.5 Previsão de comportamento - Feedbacks.png')
    st. image ('Imagens/4.6 Previsão de comportamento - Gráfico Matriz de confusão.png')
    st. image ('Imagens/4.6 Previsão de comportamento - Matriz de confusão.png')
    st. image ('Imagens/4.7 Previsão de comportamento - Distribuição da previsão.png')
    st. image ('Imagens/4.7 Previsão de comportamento - Gráfico de Distribuição da previsão.png')
    st. image ('Imagens/5.1 Acurácia de modelo - Gráfico.png')
    st. image ('Imagens/5.1 Acurácia de modelo.png')


elif pagina == "Análise":
    st. image ('Imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:##0367B0;'>Principais Acontecimentos</h3>", unsafe_allow_html=True)

    st.markdown("<h3 style='color:#145089;'>Crise econômica de 2008:</h3>", unsafe_allow_html=True)
    st.write('''A crise financeira de 2008, a mais grave desde a Grande Depressão, começou nos Estados Unidos e rapidamente se espalhou globalmente, afetando bancos, mercados financeiros e milhões de pessoas. A bolha imobiliária foi alimentada por empréstimos de alto risco, chamados "subprime", e pela especulação de que imóveis seriam investimentos seguros. Quando os preços dos imóveis caíram, muitos proprietários ficaram com dívidas maiores do que o valor das casas. Isso causou grandes perdas em instituições financeiras, como Lehman Brothers, que faliu em setembro de 2008. O congelamento do crédito afetou empresas e consumidores, gerando uma recessão global. O preço do petróleo inicialmente subiu devido a preocupações geopolíticas, mas caiu drasticamente no final de 2008, devido à queda na demanda causada pela desaceleração econômica.''')
    st.image('Imagens/Python/6. Python - visualização do impacto - Crise econômica.png', caption='Crise econômica de 2008')

    st.markdown("<h3 style='color:#145089;'>Impacto do acordo da OPEP:</h3>", unsafe_allow_html=True)
    st.write('''A OPEP (Organização dos Países Exportadores de Petróleo e Aliados) que foi criada em 1960 inicialmente por 5 países que exportam petróleos e ao longo dos anos outros paises foram convidados a participar.
Ela foi criada com o objetivo de estabelecer uma política comum em relação à produção e à venda de petróleo, de forma a influenciar os preços do petróleo no mercado internacional. Por serem grandes produtores, seus membros são capazes mexer com as cotações, ao aumentar ou cortar a produção de forma coordenada.
Em 2016, quando os preços do petróleo estavam particularmente baixos, a Opep uniu forças com outros dez grandes produtores de petróleo para criar a Opep+, que tinha como missão reduzir a produção de petróleo e estabilizar o mercado global de energia. A decisão inicial ocorreu em setembro de 2016, durante a reunião em Argel, onde membros da OPEP concordaram em limitar a produção pela primeira vez desde 2008. Em novembro, a OPEP finalizou o acordo, e em dezembro, países não-membros (incluindo Rússia, México e outros) se comprometeram voluntariamente a cortes de produção, formando uma coalizão inédita para controlar o excesso de oferta global de petróleo.
Essas restrições resultaram em aumentos moderados nos preços do petróleo e ajudaram a recuperar parte da estabilidade do mercado.O acordo se mostrou crucial para amortecer impactos de oscilações no preço do petróleo nos anos seguintes, especialmente durante crises.''')
    st.image('Imagens/Python/7. Python - Visualização do impacto - Acordo opep.png', caption='Imapacto acordo da OPEP - 2016')

elif pagina == "Dashboard Interativo":
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiODljNzU2NjUtNTQzNS00ODhhLWIyYTgtMDY0NzczY2M1MDE0IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"
    iframe_code = f'<iframe width="80%" height="700px" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>'

    st.components.v1.html(iframe_code, height=600)

elif pagina == "MVP":
    st. image ('Imagens/Banner/MVP GG 2048x733.jpeg')
    st.markdown("<h3 style='color:#0367B0;'>MVP</h3>", unsafe_allow_html=True)

    # Corrigindo a indentação do decorador e da função
    @st.cache
    def load_data():
        data_path = "Documentos/Dados  petroleo Forecasting .xlsx"  # Substitua com o nome correto ao fazer upload
        data = pd.read_excel(data_path)
        data['data'] = pd.to_datetime(data['data'])
        return data

    # Configuração inicial
        st.markdown("<h3 style='color:#145089;'>Previsão do Preço do Petróleo</h3>", unsafe_allow_html=True)
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
    st.markdown("<h3 style='color:#145089;'>Comparação: Preço Realizado vs. Previsão</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(filtered_data['data'], filtered_data['Fechamento realizado'], label="Fechamento Realizado", color="blue")
    ax.plot(filtered_data['data'], filtered_data['preco_previsto'], label="Preço Previsto", color="orange")
    ax.set_title("Preço do Petróleo: Realizado vs. Previsto")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preço (US$)")
    ax.legend()
    st.pyplot(fig)

    # Insights resumidos
    st.markdown("<h3 style='color:#145089;'>Insights</h3>", unsafe_allow_html=True)
    st.write("1. A previsão segue a tendência geral dos preços realizados com desvios ocasionais.")
    st.write("2. As maiores diferenças entre previsão e valores reais ocorrem em períodos de maior volatilidade.")
    st.write("3. O modelo mostra boa performance em períodos de estabilidade.")
    st.write("4. Eventos econômicos ou geopolíticos específicos podem impactar a precisão.")

    # Download dos dados filtrados
    st.markdown("<h3 style='color:#145089;'>Exportar Dados Filtrados</h3>", unsafe_allow_html=True)
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="Baixar dados filtrados como CSV",
        data=csv,
        file_name="dados_filtrados_petroleo.csv",
        mime="text/csv"
    )

elif pagina == "Referências":
    st. image ('Imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Referências</h3>", unsafe_allow_html=True)
   
    st.markdown("<h3 style='color:#145089;'>Dados da ONG</h3>", unsafe_allow_html=True)
    st.write('''https://passosmagicos.org.br/''')
