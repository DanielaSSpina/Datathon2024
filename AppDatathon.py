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
    st.image('imagens/Passos-magicos-icon-cor.png')  # Agora somente aparece na página MVP
    st.markdown("<h3 style='color:#0367B0;'>MVP</h3>", unsafe_allow_html=True)

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
    st.markdown("<h3 style='color:##0367B0;'>Análise PM</h3>", unsafe_allow_html=True)

    st.markdown("<h3 style='color:#145089;>Dados da ONG:</h3>", unsafe_allow_html=True)
    st.write('''A ONG disponibiliza em seu site dados desde 2016, a partir desses dados foi possível entender que a onde está em uma constante crescente, tanto em quantidade de pessoas atendidas quanto em profissionais contratados, a tendência para os próximos três anos que é a ONG tenha crescimento, principalmente em crianças atendidas e professores contratados, já que são variáveis totalmente relacionadas. 
Porém para o futuro é bom ter como alerta a taxa de fecundidade que vem diminuindo desde 2017, o que futuramente pode causar um impacto, uma vez que a quantidade de nascidos vivos em Embu-guaçu também acompanha esse declínio.''')

    st.markdown("<h3 style='color:#145089;'>Análise alunos 2020:</h3>", unsafe_allow_html=True)
    st.write('''Com base no arquivo disponibilizado segue o panorama de atuação da ONG:
Alunos de 11 - 15 anos representam 28% dos alunos atendidos, dos alunos dessa faixa etária 80% estavam matriculados em escola pública e 48% foram avaliados como Ametista. A maior parte desses alunos fazem parte das fases 2 e 3.''')

    

elif pagina == "Referências":
    st. image ('Imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Referências</h3>", unsafe_allow_html=True)
   
    st.markdown("<h3 style='color:#145089;'>Dados da ONG</h3>", unsafe_allow_html=True)
    st.write('''https://passosmagicos.org.br/''')
    st.markdown("<h3 style='color:#145089;'>Dados disponibilizados pela FIAP</h3>", unsafe_allow_html=True)
    st.write('''https://drive.google.com/drive/folders/1Z1j6uzzCOgjB2a6i3Ym1pmJRsasfm7cD''')
    st.markdown("<h3 style='color:#145089;'>Dados nascimento em SP</h3>", unsafe_allow_html=True)
    st.write('''https://spdemografico.seade.gov.br/integra/?analise=a-fecundidade-no-estado-de-sao-paulo-e-em-suas-regioes-administrativas-2000-a-2023&utm_source=chatgpt.com''')
    st.markdown("<h3 style='color:#145089;'>Dados nascimento em Embu-guaçu</h3>", unsafe_allow_html=True)
    st.write('''https://primeirainfanciaprimeiro.fmcsv.org.br/municipios/embu-guacu-sp/''')
