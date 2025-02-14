import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import h2o
import os
from h2o.automl import H2OAutoML

# Verifica se o ambiente não é o Streamlit Cloud
if "STREAMLIT_CLOUD" not in os.environ:
    h2o.init()
else:
    st.write("H2O não suportado neste ambiente.")

# Limpar o cache de dados do Streamlit
st.cache_data.clear()

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

# Inicializar o ambiente H2O
h2o.init()

# Função para carregar e processar os dados
def load_and_process_data(file_path):
    df = pd.read_excel(file_path, sheet_name="VF")

    # Seleção de colunas relevantes
    columns = ['IAA', 'IPS', 'IPP', 'IPV', 'IAN', 'PONTO_VIRADA']
    df = df[[col for col in columns if col in df.columns]]

    # Remover valores inconsistentes e preencher NaN
    df = df[df['PONTO_VIRADA'] != 'Sem dados']
    df = df.fillna(0)

    return h2o.H2OFrame(df)

# Treinamento do modelo
def train_model(data):
    # Definir a coluna de resposta e preditores
    response = 'PONTO_VIRADA'
    predictors = ['IAA', 'IPS', 'IPP', 'IPV', 'IAN']

    # Executar o AutoML
    aml = H2OAutoML(max_runtime_secs=300, seed=42)
    aml.train(x=predictors, y=response, training_frame=data)

    return aml.leader

# Carregar dados
st.title("MVP de Previsão - Índices")
uploaded_file = st.file_uploader("Faça upload do dataset (Excel)", type=["xlsx"])

if uploaded_file:
    st.success("Dataset carregado com sucesso!")

    # Processar os dados
    data = load_and_process_data(uploaded_file)

    # Treinar o modelo
    st.info("Treinando o modelo... Isso pode levar alguns minutos.")
    model = train_model(data)
    st.success("Modelo treinado com sucesso!")

    # Inputs do usuário
    st.header("Insira os índices para prever")
    indicator_iaa = st.number_input("IAA", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ips = st.number_input("IPS", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ipp = st.number_input("IPP", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ipv = st.number_input("IPV", min_value=0.0, max_value=10.0, step=0.1)
    indicator_ian = st.number_input("IAN", min_value=0.0, max_value=10.0, step=0.1)

    # Fazer previsão
    if st.button("Prever"):
        input_data = h2o.H2OFrame.from_python({
            'IAA': [indicator_iaa],
            'IPS': [indicator_ips],
            'IPP': [indicator_ipp],
            'IPV': [indicator_ipv],
            'IAN': [indicator_ian],
        })
        
        prediction = model.predict(input_data)
        result = prediction.as_data_frame().iloc[0, 0]  # Pega o resultado

        # Exibir o resultado
        if result == 1:
            st.success("Resposta: Sim")
        else:
            st.error("Resposta: Não")


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
    44% dos alunos deste ano estavam matriculados em escola pública. Somente 7% dos alunos foi avaliado como Topázio (melhor nota). 37% dos alunos estavam no ensino fundamental e 9% dos alunos estavam no ensino médio.
Alunos de 6 - 10 anos representam 16% dos alunos atendidos, 51% dos alunos foram avaliados como Ametista (segunda maior nota) e 25% receberam avaliação Topázio (maior nota).
Alunos de 11 - 15 anos representam 28% dos alunos atendidos, dos alunos dessa faixa etária 81% estavam matriculados em escola pública e 17% foram avaliados como Quartzo (a menor nota) e somente 8% como Topázio (maior nota). A maior parte desses alunos fazem parte das fases 2 e 3 que são alunos do 5º ao 8º ano.
Alunos de 16 - 19 anos representam 9% dos alunos atendidos, 65% dos alunos estavam matriculados em escola pública, 35% foram avaliados como Quartzo (menor nota). 
Aluno de 20 - 22 apenas um aluno tinha mais de 20 anos que ingressou na PM em 2016 e foi avaliado como Ágata.''')
    
    st.markdown("<h3 style='color:#145089;'>Análise alunos 2021:</h3>", unsafe_allow_html=True)
    st.write('''Com base no arquivo disponibilizado segue o panorama de atuação da ONG:
    44% dos alunos deste ano estavam matriculados em escola pública. Somente 7% dos alunos foi avaliado como Topázio (melhor nota). 37% dos alunos estavam no ensino fundamental e 9% dos alunos estavam no ensino médio.
Alunos de 6 - 10 anos representam 16% dos alunos atendidos, 51% dos alunos foram avaliados como Ametista (segunda maior nota) e 25% receberam avaliação Topázio (maior nota).
Alunos de 11 - 15 anos representam 28% dos alunos atendidos, dos alunos dessa faixa etária 81% estavam matriculados em escola pública e 17% foram avaliados como Quartzo (a menor nota) e somente 8% como Topázio (maior nota). A maior parte desses alunos fazem parte das fases 2 e 3 que são alunos do 5º ao 8º ano.
Alunos de 16 - 19 anos representam 9% dos alunos atendidos, 65% dos alunos estavam matriculados em escola pública, 35% foram avaliados como Quartzo (menor nota). 
Aluno de 20 - 22 apenas um aluno tinha mais de 20 anos que ingressou na PM em 2016 e foi avaliado como Ágata.''')

    

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
