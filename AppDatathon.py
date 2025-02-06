import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuração do título do aplicativo
st.set_page_config(page_title="Projeto de Previsão dados ONG Passos Mágicos", page_icon="📊", layout="wide")

st.markdown("<p style='font-size:40px; color:#B40C40;'>Datathon | Fiap</p>", unsafe_allow_html=True)

# Criando um menu de navegação com `selectbox` ou `radio`
pagina = st.sidebar.radio("Escolha a Página", ["Introdução", "Metodologia","Dashboard Interativo", "MVP", "Análise", "Referências"])

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
    st. image ('imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Metodologia</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#145089;'>Origem e análise dos dados</h3>", unsafe_allow_html=True)
    st.write('''Os dados utilizados nesta análise foram extraídos do Drive disponibilizado pela FIAP. 
    Após a extração, os dados foram salvos em um arquivo excel, passado por um tratamento inicial onde foi ajustado as acentuações em algumas palavras e importados no python para demais tratamenots necessários conforme abaixo:''')
    st. image ('imagens/1.1 Leitura e tratamento de Dados.png')
    st. image ('imagens/1.2 Leitura e tratamento de Dados.png')

    st.markdown("<h3 style='color:#145089;'>Análises iniciais</h3>", unsafe_allow_html=True)

  
    st.write('Análise de desempenho escolar')
    st. image ('imagens/2.1 Análise desempenho escolar.png')
    st. image ('imagens/2.2 Análise desempenho escolar - defasagem.png')
    st.write('Correlações')
    st. image ('imagens/3.1 Visualização de Dados - Notas vs frequência.png')
    st. image ('imagens/3.1 Gráfico - Distribuição das notas vs Frequência.png')
    st. image ('imagens/3.2 Visualização de Dados - Idade vs frequência.png')
    st. image ('imagens/3.2 Gráfico - Distribuição de idades vs Frequência.png')
    st. image ('imagens/3.3 Gráfico - Média de notas vs Faixa etária.png')
    st. image ('imagens/3.4 Gráfico - Notas vs Faixa etária.png')
    st. image ('imagens/3.5 Gráfico - Nota vs Aprovação.png')
    st. image ('imagens/3.6 Gráfico - Desempenho vs tipo de escola.png')
    st. image ('imagens/3.7 Gráfico - Desempenho vs Idade.png')
    st. image ('imagens/3.8 Visualização de Dados - Faltas vs Reprovação.png')
    st. image ('imagens/3.8 Gráfico - Idade vs reprovação.png')
    st. image ('imagens/3.9 Visualização de Dados - Previsão de comportamento - Feedbacks.png')
    st. image ('imagens/3.9 Gráfico - Previsão de comportamento - Feedbacks.png')
    st. image ('imagens/3.9 Visualização de Dados - Previsão de comportamento.png')
    st. image ('imagens/3.9 Gráfico - Previsão.png')
    st. image ('imagens/3.9 Visualização de Dados - Previsão de comportamento - Correlação e treinamento.png')
    st. image ('imagens/3.9 Gráfico - Previsão de comportamento - Correlação e treinamento.png')
    st. image ('imagens/4.1 Gráfico - Pedra vs Idade.png')
    st. image ('imagens/5.1 Gráfico - Qtd Feedbacks vs Tipo de comportamento.png')
    st. image ('imagens/6.1 Visualização de Dados - Feedback vs tempo de estudo.png')
    st. image ('imagens/6.1 Gráfico - Feedback vs tempo de estudo.png')
    st. image ('imagens/7.1 Gráfico - Matriz de confusão.png')
    st. image ('imagens/8.1 Gráfico - Previsão vs Feedback.png')
    st. image ('imagens/9.1 Visualização de Dados - Acurácia do modelo.png')
    st. image ('imagens/9.1 Gráfico - Acurácia do modelo.png')

elif pagina == "Dashboard Interativo":
    # URL do painel do Power BI
    powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiNzFkOTBjMGMtYmM3ZC00YzE0LWI1YjYtNjdhNTE0MzE0NWIyIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9&pageName=cb3dc97fa06772a0514d'

    # HTML com iframe para incorporar
    iframe_html = f"""<iframe title="DataThon2025" width="100%" height="800" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>"""
    
    # Exibe o painel do Power BI usando markdown com HTML
    st.markdown(iframe_html, unsafe_allow_html=True)

elif pagina == "MVP":
    st. image ('imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:##0367B0;'>MVP</h3>", unsafe_allow_html=True)

  # Carregar os dados limpos
data = pd.read_csv("Arquivos_Apoio/cleaned_data.csv")

# Criar o gráfico de importância
with st.container():
    fig = go.Figure()

    # Ordenar por importância (exemplo: IPV como proxy)
    data_sorted = data.mean().sort_values(ascending=False)

    fig.add_trace(
        go.Bar(
            x=data_sorted.values,
            y=data_sorted.index,
            orientation='h',
            marker=dict(color='#0367B0'),  # Azul
            name="Feature Importance",
        )
    )

    fig.update_layout(
        title="Feature Importance in Random Forest Model",
        xaxis_title="Importance",
        yaxis_title="Feature",
        yaxis=dict(autorange="reversed"),
        height=600,
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)

# Inputs de indicadores
with st.container():
    col0, col1, col2, col3, col4 = st.columns(5)
    indicator_ian = col0.number_input("IAN", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ipv = col1.number_input("IPV", min_value=0.0, max_value=10.0, step=0.1)
    indicator_iaa = col2.number_input("IAA", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ips = col3.number_input("IPS", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ipp = col4.number_input("IPP", min_value=0.0, max_value=10.0, step=0.1)

# Criar dataframe de entrada para o modelo
student_data = pd.DataFrame({
    'IAA': [indicator_iaa],
    'IPS': [indicator_ips],
    'IPP': [indicator_ipp],
    'IPV': [indicator_ipv],
    'IAN': [indicator_ian],
})

# Botão de previsão
if st.button("Prever"):
    st.dataframe(student_data)
    # Aqui você adicionaria o scaler e o modelo para realizar a previsão
    # Exemplo fictício:
    st.success("Previsão realizada com sucesso!")
    
elif pagina == "Análise":
    st. image ('imagens/Passos-magicos-icon-cor.png')
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

elif pagina == "Referências":
    st. image ('Imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Referências</h3>", unsafe_allow_html=True)
   
    st.markdown("<h3 style='color:#145089;'>Dados da ONG</h3>", unsafe_allow_html=True)
    st.write('''https://passosmagicos.org.br/''')
    st.markdown("<h3 style='color:#145089;'>Dados disponibilizados pela FIAP</h3>", unsafe_allow_html=True)
    st.write('''https://drive.google.com/drive/folders/1Z1j6uzzCOgjB2a6i3Ym1pmJRsasfm7cD''')
