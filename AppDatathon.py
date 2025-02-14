import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import h2o
from h2o.automl import H2OAutoML
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error  # Importação do erro quadrático médio

# Configuração da página (deve ser o primeiro comando relacionado ao Streamlit)
st.set_page_config(page_title="Projeto de Previsão dados ONG Passos Mágicos", page_icon="📊", layout="wide")

# Configuração do título do aplicativo
st.markdown("<p style='font-size:40px; color:#B40C40;'>Datathon | Fiap</p>", unsafe_allow_html=True)

# Criando um menu de navegação com `selectbox` ou `radio`
pagina = st.sidebar.radio("Escolha a Página", ["Introdução", "Metodologia", "Dashboard Interativo", "MVP", "Análise", "Referências"])

# Conteúdo de cada página
if pagina == "Introdução":
    st.image('imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Introdução</h3>", unsafe_allow_html=True)
    st.write('''Este trabalho tem como objetivo trazer uma proposta preditiva para mostrar o impacto das ações da ONG Passos Mágicos sobre a comunidade que atendem.
    Os impactos a serem analisados terão como base o perfil dos estudantes atendidos, informações educacionais, informações socioeconômicas e as respostas da pesquisa realizada pela ONG.''')

    st.markdown("<h3 style='color:#0367B0;'>Ferramentas utilizadas</h3>", unsafe_allow_html=True)
    st.write('Para a realização deste trabalho, foi utilizado as seguintes ferramentas:')
    st.write('Python: utilizado para toda a tratativa inicial das bases como organização das colunas, remoção de espaços e duplicidades e valores nulos, assim como para a realização da previsão dos preços do petróleo por meio do modelo de machine learning PROPHET.')
    st.write('PowerBI: utilizado para a criação de um dashboard interativo compilando as informações disponíveis do preço do petróleo, previsão e acontecimentos que influenciam na explicação da variação do preço.')
    st.write('Streamlit: utilizado para desenvolvimento do MVP (Minimum Viable Product, ou Produto Mínimo Viável) e disponibilização das etapas e informações do projeto.')

elif pagina == "Metodologia":
    st.image('imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:#0367B0;'>Metodologia</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#145089;'>Origem e análise dos dados</h3>", unsafe_allow_html=True)
    st.write('''Os dados utilizados nesta análise foram extraídos do Drive disponibilizado pela FIAP. 
    Após a extração, os dados foram salvos em um arquivo excel, passaram por um tratamento inicial onde foi ajustado as acentuações em algumas palavras e importados no python para demais tratamentos necessários conforme abaixo:''')
    st.image('imagens/1.1 Leitura e tratamento de Dados.png')
    st.image('imagens/1.2 Leitura e tratamento de Dados.png')

    st.markdown("<h3 style='color:#145089;'>Análises iniciais</h3>", unsafe_allow_html=True)
    st.write('Análise de desempenho escolar')
    st.image('imagens/2.1 Análise desempenho escolar.png')
    st.image('imagens/2.2 Análise desempenho escolar - defasagem.png')
    st.write('Correlações')
    st.image('imagens/3.1 Visualização de Dados - Notas vs frequência.png')
    st.image('imagens/3.1 Gráfico - Distribuição das notas vs Frequência.png')
    st.image('imagens/3.2 Visualização de Dados - Idade vs frequência.png')
    st.image('imagens/3.2 Gráfico - Distribuição de idades vs Frequência.png')
    st.image('imagens/3.3 Gráfico - Média de notas vs Faixa etária.png')
    st.image('imagens/3.4 Gráfico - Notas vs Faixa etária.png')
    st.image('imagens/3.5 Gráfico - Nota vs Aprovação.png')
    st.image('imagens/3.6 Gráfico - Desempenho vs tipo de escola.png')
    st.image('imagens/3.7 Gráfico - Desempenho vs Idade.png')
    st.image('imagens/3.8 Visualização de Dados - Faltas vs Reprovação.png')
    st.image('imagens/3.8 Gráfico - Idade vs reprovação.png')
    st.image('imagens/3.9 Visualização de Dados - Previsão de comportamento - Feedbacks.png')
    st.image('imagens/3.9 Gráfico - Previsão de comportamento - Feedbacks.png')
    st.image('imagens/3.9 Visualização de Dados - Previsão de comportamento.png')
    st.image('imagens/3.9 Gráfico - Previsão.png')
    st.image('imagens/3.9 Visualização de Dados - Previsão de comportamento - Correlação e treinamento.png')
    st.image('imagens/3.9 Gráfico - Previsão de comportamento - Correlação e treinamento.png')
    st.image('imagens/4.1 Gráfico - Pedra vs Idade.png')
    st.image('imagens/5.1 Gráfico - Qtd Feedbacks vs Tipo de comportamento.png')
    st.image('imagens/6.1 Visualização de Dados - Feedback vs tempo de estudo.png')
    st.image('imagens/6.1 Gráfico - Feedback vs tempo de estudo.png')
    st.image('imagens/7.1 Gráfico - Matriz de confusão.png')
    st.image('imagens/8.1 Gráfico - Previsão vs Feedback.png')
    st.image('imagens/9.1 Visualização de Dados - Acurácia do modelo.png')
    st.image('imagens/9.1 Gráfico - Acurácia do modelo.png')

elif pagina == "Dashboard Interativo":
    # URL do painel do Power BI
    powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiNzFkOTBjMGMtYmM3ZC00YzE0LWI1YjYtNjdhNTE0MzE0NWIyIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9&pageName=cb3dc97fa06772a0514d'

    # HTML com iframe para incorporar
    iframe_html = f"""<iframe title="DataThon2025" width="100%" height="800" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>"""
    
    # Exibe o painel do Power BI usando markdown com HTML
    st.markdown(iframe_html, unsafe_allow_html=True)

elif pagina == "MVP":
    # Caixas para o usuário inserir os valores das variáveis
    st.write("Insira os valores das variáveis:")

    IDA = st.number_input("IDA", min_value=0.0, max_value=10.0, step=0.1)
    IPV = st.number_input("IPV", min_value=0.0, max_value=10.0, step=0.1)
    IAA = st.number_input("IAA", min_value=0.0, max_value=10.0, step=0.1)
    IEG = st.number_input("IEG", min_value=0.0, max_value=10.0, step=0.1)
    IPS = st.number_input("IPS", min_value=0.0, max_value=10.0, step=0.1)
    IPP = st.number_input("IPP", min_value=0.0, max_value=10.0, step=0.1)
    IAN = st.number_input("IAN", min_value=0.0, max_value=10.0, step=0.1)

    # Dados de exemplo (para treino do modelo)
    example_data = {
        "IDA": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "IPV": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "IAA": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "IEG": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "IPS": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "IPP": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "IAN": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "target": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Variável alvo
    }

    # Criar DataFrame
    data = pd.DataFrame(example_data)

    # Verificar se as colunas necessárias estão presentes
    features = ["IDA", "IPV", "IAA", "IEG", "IPS", "IPP", "IAN"]
    if all(feature in data.columns for feature in features):
        # Separar as features e a variável alvo
        X = data[features]
        y = data["target"]

        # Dividir os dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Treinar o modelo
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)

        # Predição com base nos valores fornecidos pelo usuário
        if st.button("Fazer Previsão"):
            user_input = np.array([[IDA, IPV, IAA, IEG, IPS, IPP, IAN]])
            prediction = model.predict(user_input)[0]

            # Classificar a predição
            if 2.405 <= prediction <= 5.506:
                categoria = "Quartzo"
            elif 5.506 < prediction <= 6.868:
                categoria = "Ágata"
            elif 6.868 < prediction <= 8.230:
                categoria = "Ametista"
            elif 8.230 < prediction <= 9.294:
                categoria = "Topázio"
            else:
                categoria = "Fora dos intervalos"

            # Exibir os resultados
            st.write(f"Predição: {prediction:.2f}")
            st.write(f"Categoria: {categoria}")
    else:
        st.error("As colunas necessárias não estão presentes no DataFrame!")

elif pagina == "Análise":
    st. image ('imagens/Passos-magicos-icon-cor.png')
    st.markdown("<h3 style='color:##0367B0;'>Análise PM</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#145089;>Dados da ONG:</h3>", unsafe_allow_html=True)
    st.write('''A ONG disponibiliza em seu site dados desde 2016, a partir desses dados foi possível entender que a onde está em uma constante crescente, tanto em quantidade de pessoas atendidas quanto em profissionais contratados, a tendência para os próximos três anos que é a ONG tenha crescimento, principalmente em crianças atendidas e professores contratados, já que são variáveis totalmente relacionadas. 
Porém para o futuro é bom ter como alerta a taxa de fecundidade que vem diminuindo desde 2017, o que futuramente pode causar um impacto, uma vez que a quantidade de nascidos vivos em Embu-guaçu também acompanha esse declínio.''')

    st.markdown("<h3 style='color:#145089;'>Análise alunos 2020:</h3>", unsafe_allow_html=True)
    st.write('''Com base no arquivo disponibilizado segue o panorama de atuação da ONG:
    44% dos alunos deste ano estavam matriculados em escola pública. Somente 7% dos alunos foi avaliado como Topázio (melhor nota). 6% dos alunos estavam em alfabetização, 37% dos alunos estavam no ensino fundamental e 9% dos alunos estavam no ensino médio e 2% em nível superior.
Alunos de 11 - 15 anos representam 28% dos alunos atendidos, dos alunos dessa faixa etária 81% estavam matriculados em escola pública e 17% foram avaliados como Quartzo (a menor nota) e somente 8% como Topázio (maior nota). 
Alunos de 16 - 19 anos representam 9% dos alunos atendidos, 65% dos alunos estavam matriculados em escola pública, 35% foram avaliados como Quartzo (menor nota). 
Aluno de 20 - 22 apenas um aluno tinha mais de 20 anos que ingressou na PM em 2016 e foi avaliado como Ágata.''')
    
    st.markdown("<h3 style='color:#145089;'>Análise alunos 2021:</h3>", unsafe_allow_html=True)
    st.write('''Com base no arquivo disponibilizado segue o panorama de atuação da ONG:
    41% dos alunos deste ano estavam matriculados em escola pública. Somente 7% dos alunos foi avaliado como Topázio (melhor nota). 35% dos alunos estavam no ensino fundamental e 7% dos alunos estavam no ensino médio.
Alunos de 11 - 15 anos representam 32% dos alunos atendidos, dos alunos dessa faixa etária 52% estavam matriculados em escola pública e 15% foram avaliados como Quartzo (a menor nota) e somente 8% como Topázio (maior nota).
Alunos de 16 - 19 anos representam 13% dos alunos atendidos, 20% dos alunos estavam matriculados em escola particular, 4% foram avaliados como Quartzo (menor nota) e 19% deles foram avaliados como Ametista (segunda maior nota).''')

st.markdown("<h3 style='color:#145089;'>Análise alunos 2022:</h3>", unsafe_allow_html=True)
    st.write('''Com base no arquivo disponibilizado segue o panorama de atuação da ONG:
    Não há informação sobre o tipo de instituição de nenhum aluno nesse ano. Somente 10% dos alunos foi avaliado como Topázio (melhor nota). 42% dos alunos estavam no ensino fundamental e 7% dos alunos estavam no ensino médio.
Alunos de 11 - 15 anos representam 32% dos alunos atendidos, dos alunos dessa faixa etária 9% foram avaliados como Quartzo (a menor nota) e somente 8% como Topázio (maior nota).
Alunos de 16 - 19 anos representam 16% dos alunos atendidos, 9% foram avaliados como Quartzo (menor nota) e 8% deles foram avaliados como Ametista (segunda maior nota).''')

st.markdown("<h3 style='color:##0367B0;'>Análise pedras</h3>", unsafe_allow_html=True)
    st.write('''A distribuição de pedras a cada ano não mostra uma enorme evolução, afinal é uma condição variável de diversos fatores, assim como a quantidade de alunos sempre se alterará pelo ingresso e formação dos mesmos, dessa forma não nos mostrando uma linha de evolução constante.
Apesar disso é possível notar que houve um aumento considerável nos alunos avaliados como topázio em 2022, bem como a diminuição da quantidade de informações não informadas.''')

st.markdown("<h3 style='color:##0367B0;'>Desafios e melhorias identificadas</h3>", unsafe_allow_html=True)
    st.write('''A ONG com toda certeza sabe o impacto na comunidade, isso é explicado não só pelo aumento constante de alunos ingressantes como também a permanencia dos mesmos a longo prazo, porém como toda grande organização existem desafios e melhorias a serem tratados:''')
    st.markdown("<h3 style='color:#145089;'>Desafios:</h3>", unsafe_allow_html=True)
    st.write('''Como alerta, deixamos a situação da taxa de fecundidade em queda, pois é um movimento crescente assim como a escolha de não ter filhos, o que afeta o público alvo da ONG, uma forma de seguir impactando a comunidade sem perder a intenção valorosa do ensino, seria ir em busca de adultos sem formação para a regularização dos estudos, a profissionalização e o suporte emocional que a essa altura da vida é algo que mutios não buscam e que se faz necessário nesse momento de equalização educacional. ''')
    st.markdown("<h3 style='color:#145089;'>Melhorias:</h3>", unsafe_allow_html=True)
    st.write('''Percebemos que a base de dados disponível é bem falha, tendo informações faltantes de um ano para o outro e informações novas a cada ano, para uma análise a longo prazo isso é algo extremamente prejudicial para tomadas de decisões, pois com as informações irregulares disponibilizadas pode prejudicar a predição e acompanhamento de tendências do negócio. Portanto fazer um mapeamento de informações primordiais e mantê-las como obrigatórias no momento do preenchimento dos relatórios se faz fundamental, deixaremos abaixo algumas informações que se mostram primordiais para nós avaliadores:
    Data de nascimento, Data de ingresso na PM, ID do aluno (código único de cada aluno para ter rastreio sem o nome vinculado), raça, instituição de ensino, todas as notas de avaliação utilizadas, INDE e Pedras''')

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














