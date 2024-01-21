import pandas as pd
import streamlit as st
from PIL import Image
import time
import datetime as datetime
import webbrowser
import sqlite3
import openpyxl
import altair as alt
from datetime import datetime
from io import BytesIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header

timenow = datetime.now().replace(microsecond=0).time()
datenow = datetime.now().date()
monthnow = datetime.now().strftime('%B')
monthnumbernow = datetime.now().month

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title=('MANUTENÇÃO SSM SOLAR DO BRASIL'),
    page_icon='S.M.M.I',
    layout='wide',
    
    initial_sidebar_state='expanded',
    menu_items={""
        'Get Help': 'http://www.meusite.com.br',
        'Report a bug': "http://www.meuoutrosite.com.br",
        'About': "Na duvida,duvide!"
    }
)

style_metric_cards()
# --- Criar o dataframe
df = pd.read_excel(
    io = './Datasets/system_extraction.xlsx',
    engine='openpyxl',
    sheet_name='salesreport',
    usecols='A:D',
    nrows=12
)
senha = ()
with st.sidebar:
    logo_teste = Image.open('./Midia/sales.jpeg')
    st.image(logo_teste, width=300)
    st.subheader('MANUTENÇÃO SSM SOLAR DO BRASIL')
    img = Image.open('./Midia/user.png')
    with st.form('Logon'):
        st.image(img,width=100)
        fLIDERES = st.selectbox(
        "LIDER:",
        options=df['LIDERES'].unique()
        )
        fSETOR = st.selectbox(
        "SETOR:",
        options=df['SETOR'].unique()
        )
        if senha == '1409':
           st.write('ok')
        else:
            senha = st.text_input('Ensira sua senha',type="password")
        st.form_submit_button('Entrar')
        
    with st.spinner("Carregando..."):
                st.success("Pronto!")
    st.write("Bem Vindo")

    with st.expander('#$#$'):
        st.success('Nada além de um homem comum,com pensamentos comuns')


if fLIDERES == 'Selecione' and fSETOR == 'Selecione' and senha == '47297913':
    col,col1,col2,col3 = st.columns([1,1,1,1])
    with open("./Data/Setores", 'rb') as file:
        with col:
            st.write('Dados de O.S de todos setores:')
            st.download_button(
                label="BAIXAR DADOS",
                key= "download_button",
                data= file,
                file_name="Setores",
                mime='application/octet-stream'
                )
    
    with open("./Data/Materiais", 'rb') as file:
        with col1:
            st.write('Dados da tabela de materiais:')
            st.download_button(
                label="BAIXAR DADOS ",
                key= "download_button ",
                data= file,
                file_name="Materiais ",
                mime='application/octet-stream '
                )
     
if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'BANCOS' == 'BANCOS':
    conn = sqlite3.connect('./Data/Setores')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ELETRICA (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        ESPECIALIDADE,
        Local,
        MÊS,           
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)
                
        )
'''   )
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ferramentaria (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,           
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)
                   
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCAO(
                   
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,           
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)           
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Administrativo (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,           
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)        
       
                   
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comercial (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,           
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)
       
                   
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EXPEDICAO (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,           
        Local,
        MÊS,         
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)
                          
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Serralharia (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,           
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)
       
                   
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MECANICA (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        ESPECIALIDADE,           
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)   
       
                   
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TI (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        PARADA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR,
        ESPECIALIDADE,
        Local,
        MÊS,
        FOREIGN KEY (OS) REFERENCES ids (ID_UNIC)
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ids (
        ID_UNIC INTEGER PRIMARY KEY,
        HORA TIME,
        HORAF TIME,
        DATA DATE
                
    )
''')
    

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS imagens (
        id INTEGER PRIMARY KEY,
        imagem BLOB,
        mes TEXT,
        FOREIGN KEY (id) REFERENCES ids (ID_UNIC)
        
    )
''')
    
    conn14 = sqlite3.connect('./Data/Meses')
    cursor14 = conn14.cursor()

#cl = st.button("DELETAR TABELAS")
#if cl:
   #cursor.execute("DROP TABLE ELETRICA")
   #cursor.execute("DROP TABLE MECANICA")
   #cursor.execute("DROP TABLE imagens")
   #cursor.execute("DROP TABLE Ferramentaria")
   #cursor.execute("DROP TABLE PRODUCAO")
   #cursor.execute("DROP TABLE Administrativo")
   #cursor.execute("DROP TABLE Comercial")
   #cursor.execute("DROP TABLE EXPEDICAO")
   #cursor.execute("DROP TABLE TI")
   #cursor.execute("DROP TABLE Serralharia")
   #cursor.execute("DROP TABLE ids")
   #conn.commit()

#leitura do banco ELETRICA
allln = pd.read_sql_query("SELECT * FROM ELETRICA", conn)
allln1 = allln.shape[0]
consulta1 = "SELECT * FROM ELETRICA"
allinhas = pd.read_sql_query(consulta1, conn)

#O.S ABERTAS  NÃO FINALIZADAS

consulta2 = "SELECT * FROM ELETRICA WHERE FINALIZADA = 'Não'"
whrlinhas1 = pd.read_sql_query(consulta2, conn)
whrlinhas2 = whrlinhas1.shape[0] 

#O.S FINALIZADAS
consulta3 = "SELECT * FROM ELETRICA WHERE FINALIZADA = 'Sim'"
whrlinhas3 = pd.read_sql_query(consulta3, conn)
whrlinhas4 = whrlinhas3.shape[0]

if 'Ferramentaria' == 'Ferramentaria':
    #feedback Ferramentaria
    allln13 = pd.read_sql_query("SELECT * FROM Ferramentaria", conn)
    allln14 = allln13.shape[0]

    query = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Não'"
    rd2 = pd.read_sql_query(query, conn)
    rd3 = rd2.shape[0]

    query1 = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Sim'"
    rd = pd.read_sql_query(query1, conn)
    rd1 = rd.shape[0]

    query = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
    rd25 = pd.read_sql_query(query, conn)
    rd26 = rd25.shape[0]

    query1 = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
    rd27 = pd.read_sql_query(query1, conn)
    rd28 = rd27.shape[0]

    query = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
    rd29 = pd.read_sql_query(query, conn)
    rd30 = rd29.shape[0]

    query1 = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
    rd31 = pd.read_sql_query(query1, conn)
    rd32 = rd31.shape[0]

if 'Produção'=='Produção':
    #FEEDBACK Produção
    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não'"
    rd6 = pd.read_sql_query(query, conn)
    rd7 = rd6.shape[0]

    query1 = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim'"
    rd4 = pd.read_sql_query(query1, conn)
    rd5 = rd4.shape[0]

    allln15 = pd.read_sql_query("SELECT * FROM PRODUCAO", conn)
    allln16 = allln15.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
    rd33 = pd.read_sql_query(query, conn)
    rd34 = rd33.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
    rd35 = pd.read_sql_query(query, conn)
    rd36 = rd35.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
    rd37 = pd.read_sql_query(query, conn)
    rd38 = rd37.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
    rd39 = pd.read_sql_query(query, conn)
    rd40 = rd39.shape[0]

    allln15 = pd.read_sql_query("SELECT * FROM PRODUCAO", conn)
    allln16 = allln15.shape[0]
    consulta9 = "SELECT * FROM PRODUCAO"
    allinhas16 = pd.read_sql_query(consulta9, conn)

    #O.S ABERTAS  NÃO FINALIZADAS
    consulta10 = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não'"
    whrlinhas18 = pd.read_sql_query(consulta10, conn)
    whrlinhas19 = whrlinhas18.shape[0]

    #O.S FINALIZADAS
    cursor.execute("SELECT * FROM PRODUCAO WHERE FINALIZADA = ?;", ('Sim',))
    whrlinhas20 = cursor.fetchall()
    whrlinhas21 = pd.DataFrame(whrlinhas20)
    whrlinhas22 = whrlinhas21.shape[0]

if 'Administrativo' == 'Administrativo':
    #FEEDBACK Administrativo
    query = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Não'"
    rd10 = pd.read_sql_query(query, conn)
    rd11 = rd10.shape[0]

    query1 = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Sim'"
    rd8 = pd.read_sql_query(query1, conn)
    rd9 = rd8.shape[0]

    allln17 = pd.read_sql_query("SELECT * FROM Administrativo", conn)
    allln18 = allln17.shape[0]

    query = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
    rd41 = pd.read_sql_query(query, conn)
    rd42 = rd41.shape[0]

    query = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
    rd43 = pd.read_sql_query(query, conn)
    rd44 = rd43.shape[0]

    query = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
    rd45 = pd.read_sql_query(query, conn)
    rd46 = rd45.shape[0]

    query = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
    rd47 = pd.read_sql_query(query, conn)
    rd48 = rd47.shape[0]

if 'Comercial' == 'Comercial':
    #FEEDBACK Comercial
    query = "SELECT * FROM Comercial WHERE FINALIZADA = 'Não'"
    rd14 = pd.read_sql_query(query, conn)
    rd15 = rd14.shape[0]

    query1 = "SELECT * FROM Comercial WHERE FINALIZADA = 'Sim'"
    rd12 = pd.read_sql_query(query1, conn)
    rd13 = rd12.shape[0]

    allln19 = pd.read_sql_query("SELECT * FROM Comercial", conn)
    allln20 = allln19.shape[0]

    query = "SELECT * FROM Comercial WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
    rd49 = pd.read_sql_query(query, conn)
    rd50 = rd49.shape[0]

    query = "SELECT * FROM Comercial WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
    rd51 = pd.read_sql_query(query, conn)
    rd52 = rd51.shape[0]

    query = "SELECT * FROM Comercial WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
    rd53 = pd.read_sql_query(query, conn)
    rd54 = rd53.shape[0]

    query = "SELECT * FROM Comercial WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
    rd55 = pd.read_sql_query(query, conn)
    rd56 = rd55.shape[0]

if 'Expedição' == 'Expedição':
    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não'"
    rd18 = pd.read_sql_query(query, conn)
    rd19 = rd18.shape[0]

    query1 = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim'"
    rd16 = pd.read_sql_query(query1, conn)
    rd17 = rd16.shape[0]

    allln21 = pd.read_sql_query("SELECT * FROM EXPEDICAO", conn)
    allln22 = allln21.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
    rd57 = pd.read_sql_query(query, conn)
    rd58 = rd57.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
    rd59 = pd.read_sql_query(query, conn)
    rd60 = rd59.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
    rd61 = pd.read_sql_query(query, conn)
    rd62 = rd61.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
    rd63 = pd.read_sql_query(query, conn)
    rd64 = rd63.shape[0]

if 'Serralharia' == 'Serralharia':
    #FEEDBACK Serralharia
    query = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Não'"
    rd22 = pd.read_sql_query(query, conn)
    rd23 = rd22.shape[0]

    query1 = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Sim'"
    rd20 = pd.read_sql_query(query1, conn)
    rd21 = rd20.shape[0]

    allln23 = pd.read_sql_query("SELECT * FROM Serralharia", conn)
    allln24 = allln23.shape[0]

    query = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
    rd65 = pd.read_sql_query(query, conn)
    rd66 = rd65.shape[0]

    query = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
    rd67 = pd.read_sql_query(query, conn)
    rd68 = rd67.shape[0]

    query = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
    rd69 = pd.read_sql_query(query, conn)
    rd70 = rd69.shape[0]

    query = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
    rd71 = pd.read_sql_query(query, conn)
    rd72 = rd71.shape[0]

if 'PCM' == 'PCM':
   consulta3 = "SELECT * FROM PCM WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Elétrica'"
   pcm = pd.read_sql_query(consulta3, conn)
   pcm_id = pcm.shape[0]

   consulta3 = "SELECT * FROM PCM WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Elétrica'"
   pcm1 = pd.read_sql_query(consulta3, conn)
   pcm_id1 = pcm1.shape[0]

   consulta3 = "SELECT * FROM PCM WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'Mecânica'"
   pcm2 = pd.read_sql_query(consulta3, conn)
   pcm_id2 = pcm2.shape[0]

   consulta3 = "SELECT * FROM PCM WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'Mecânica'"
   pcm3 = pd.read_sql_query(consulta3, conn)
   pcm_id3 = pcm3.shape[0]

if 'OI' == 'OI':
   consulta3 = "SELECT * FROM ids"
   ids = pd.read_sql_query(consulta3, conn)
   ids_shape = ids.shape[0]

if 'OS' not in st.session_state:
    st.session_state.OS = 0
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

query = "SELECT * FROM TI WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
rd74 = pd.read_sql_query(query, conn)
rd75 = rd74.shape[0]

query = "SELECT * FROM TI WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
rd76 = pd.read_sql_query(query, conn)
rd77 = rd76.shape[0]

query = "SELECT * FROM TI WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
rd78= pd.read_sql_query(query, conn)
rd79 = rd78.shape[0]

query = "SELECT * FROM TI WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
rd80 = pd.read_sql_query(query, conn)
rd81 = rd80.shape[0]

caminho_imagem = './Midia/empty.png'
with open(caminho_imagem, 'rb') as arquivo_imagem:
    bytes_imagem = arquivo_imagem.read()
#ELÉTRICA
if fLIDERES == 'Equipe de ELÉTRICA':
    if fSETOR == 'Elétrica':
        if senha == '1409':
            #cl1 = st.button("DELETAR TABELA")
            #if cl1:
                #cursor.execute("DROP TABLE ELETRICA")
                #conn.commit()
            #image = Image.open('./Midia/ssmm.jpg')
            col1,col2 = st.columns([10,1])
            with col1:
            
                st.title('Status e informações de O.S')
            tab6, tab7,tab8,tab9,tab10= st.tabs(["| Cadastro |", "| Finalizar |","| O.S Em aberto |","| O.S Finalizadas |","| Geral |"])
            with tab6:
                st.header("Cadastro de ocorrência")
        
                colibrim,neymar= st.columns([5,5])  
                with colibrim:
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln1 == 0:
                           numros = 0
                           numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln1,value=allln1,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM ELETRICA"
                        ros_oc = pd.read_sql_query(consulta1, conn)

                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            preenchimento = 'NONE'
            
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Filipe leite','Jameson Sales','Maurilio Sales','Bruno Kappaun','Adriely Lemos','Gilson Freitas','Willian Oliveira','Cesar Augusto'),index=None,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Filipe leite','Jameson Sales','Maurilio Sales','Bruno Kappaun','Adriely Lemos','Gilson Freitas','Willian Oliveira','Cesar Augusto'),index=None,placeholder='Atualize')
                        
                    if not atd1:
                        Rstatus = container.text_area('Atualize o tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                    
                    if not atd1:
                        Rsetor = container.selectbox('Setor solicitante:', ('Tecnologia da Informação','Comercial','Administrativo','Expedição','Ferramentaria','Serralharia','Utilidades','Estampo,corte e furo','Extrusão'),index=None,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Tecnologia da Informação','Comercial','Administrativo','Expedição','Ferramentaria','Serralharia','Utilidades','Estampo,corte e furo','Extrusão'),index=None,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva','Confecção'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva','Confecção'),index=None,placeholder='Atualize')

                    if not atd1:
                        parada = container.selectbox('Gerou parada de maquina?:', ('Sim','Não'),index=None,placeholder='Selecione')
                    if atd1:
                        parada = container.selectbox('Gerou parada de maquina?: ', ('Sim','Não'),index=None,placeholder='Selecione')
                    
                    if not atd1: 
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if Rsetor == 'Extrusão' or RUsetor == 'Extrusão':
                        Local = container.selectbox('Local:',('Prensa - P8','Puller - 01','Puller - 02','Quench','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts'),index=None,placeholder= 'Selecione')
                        
                    if Rsetor == 'Estampo,corte e furo' or RUsetor == 'Estampo,corte e furo':
                        Local = container.selectbox('Local:',('Prensa Excentrica - 01','Prensa Excentrica - 02','Serra Automatica','Serra Manual','Serra fita - FRANHO','Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Embaladora Automatica','Seladora manual - KT001','Seladora manual - KT002'),index=None,placeholder= 'Selecione')
                        
                    if Rsetor == 'Utilidades' or RUsetor == 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione')
                            
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades' and Rsetor != 'Serralharia' and RUsetor != 'Serralharia' and Rsetor != 'Ferramentaria' and RUsetor != 'Ferramentaria'  and Rsetor != 'Geral' and RUsetor != 'Geral':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione')
                    elif Rsetor == 'Serralharia' or RUsetor == 'Serralharia':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Serra fita - FRANHO'),index=None,placeholder= 'Selecione')
                    elif Rsetor == 'Ferramentaria' or RUsetor == 'Ferramentaria':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Maquina de jatear','Talha Elétrica','Recuperação de ferramentas'),index=None,placeholder= 'Selecione')
                    elif Rsetor == 'Geral' or RUsetor == 'Geral':
                        Local = container.selectbox('Local:',('Prensa - P8 - Puller - 1 - Puller - 2 - Esticadeira - HEAD - Esticadeira - TAIL - Forno de Tarugo - Serra Fria - Forno de Envelhecimento - Prensa Excentrica - 1 - Prensa Excentrica - 2 - Serra Automatica - Serra Manual - Serra fita - FRANHO - Rosqueadeira - MACHO 01 - Rosqueadeira - COSSINETE 01 - Rosqueadeira - COSSINETE 2 - Maquina de jatear - Talha Elétrica - Embaladora Automatica - Elétrica Predial - Artífice - Recuperação de ferramentas - Casa de Bombas - Caixa D.Agua - Subestação - 1 - Subestação - 2 -  Seladora manual - KT001 - Seladora manual - KT002 - Portão de automoveis - Portão de pedestres - Interfone',), placeholder='Selecione')
    
                    if atd1:
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        agree = container.checkbox('Selecione á caixa para enviar a imagem em outro momento:')
                        if agree:
                            uploaded_files = bytes_imagem
                            bytes_data = bytes_imagem
                        else:
                             uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                             for uploaded_file in uploaded_files:
                                 bytes_data = uploaded_file.read()
            
                with neymar:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln1)
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=int(preenchimento[0]),value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM ELETRICA WHERE OS = {numero_da_os};')
                                conn.commit()

                if fLIDERES == 'Equipe de ELÉTRICA':

                    if fSETOR == 'Elétrica':
                        if senha == '1409':
                            if atd1: 
                                atl = st.button('Atualize ↻')
                                if atl:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{numero_da_os}] Atualizada!')
                                    cursor.execute("UPDATE ELETRICA SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, AÇÃO = ?, LOCAL = ?, ESPECIALIDADE = ? WHERE OS = ?",(RUsolicitante, RUsetor, RUstatus,RUniveldaocorrencia,RUacao,Local,especialidades,int(preenchimento[0])))
                                    cursor.execute("UPDATE imagens SET imagem = ? WHERE id = ?",(bytes_data,numros))
                                    conn.commit()
                                                                          
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files,parada]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[8] == True:
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_elétrica = ids_shape + 1
                                        st.balloons()
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_elétrica}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_elétrica,str(timenow),datenow))
                                        cursor.execute("INSERT INTO ELETRICA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,ESPECIALIDADE,LOCAL,MÊS,PARADA) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (ids_shape_elétrica , Rsolicitante, Rsetor,Rstatus,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,especialidades,Local,monthnow,parada))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_elétrica,bytes_data,monthnow))
                                        conn.commit()
                                                               
            with tab7:
                st.header('Finalizar O.S ✔')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    containerx = st.container(border=True)
                    setorescolhido = containerx.selectbox('Setor', ('PCM','Tecnologia da Informação','Comercial','Administrativo','Expedição','Produção','Ferramentaria','Serralharia','Elétrica'),index=None,placeholder='Selecione')
                    fnlz2 = containerx.number_input("Selecione o numero da OS que deseja Finalizar",min_value=1,max_value=1000,value=1,placeholder="Selecione")
                    fnlz3 = fnlz2-1
                    finalizar = containerx.selectbox('O.S finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                    #datainput = containerx.date_input("Data", value=None)
                    #containerx.write(datainput)
                    #timeinput = containerx.time_input('HORA', value=None)
                    #containerx.write(timeinput)
                   
                if fLIDERES == 'Equipe de ELÉTRICA':
                    if fSETOR == 'Elétrica':
                        if senha == '1409':
                            if setorescolhido == 'Ferramentaria':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Ferramentaria SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()

                            if setorescolhido == 'Elétrica':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE ELETRICA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit() 

                            if setorescolhido == 'Produção':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                            
                            if setorescolhido == 'Administrativo':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Administrativo SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit() 
                            
                            if setorescolhido == 'Comercial':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Comercial SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit() 

                            if setorescolhido == 'Expedição':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()  

                            if setorescolhido == 'Serralharia':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Serralharia SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()

                            if setorescolhido == 'Tecnologia da Informação':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE TI SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()

                            if setorescolhido == 'PCM':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor14.execute("UPDATE PCM SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()   
            with tab8:
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    st.header('Manutenção', divider='rainbow')
                    with st.expander("Filtros"):
                        genre = st.radio(
                          "Selecione",
                        ["ELÉTRICA","Por Data"],
                        index=0,
                        )
          
                with st.expander(f"Minhas OS ({whrlinhas2})"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'Por Data':
                        with diferent1:
                            cls = st.date_input('Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM ELETRICA WHERE FINALIZADA = 'Não' AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn)
                            whrlinhas91 = whrlinhas90.shape[0]
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas2)
                            numros3 = numros2-1
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width2")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width2)
                        with diferent2:
                            st.button('↻')
                    
                    else:
                        if not whrlinhas2 == 0:
                            numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=whrlinhas2,value=whrlinhas2,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas2)
                            numros3 = numros2-1
                        if whrlinhas2 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = whrlinhas1.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width3")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width3)
                
                with st.expander("PCM" f' ({pcm_id})'):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if pcm_id == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da k OS",min_value=1,max_value=pcm_id,value=pcm_id,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=pcm_id)
                            numros5 = numros4-1
                            osespec = pcm.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width6")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width6)

                #Ferramentaria   
                st.markdown('----------')
                with st.expander("Ferramentaria"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd28 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=rd28,value=rd28,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd28)
                            numros5 = numros4-1
                            osespec = rd27.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width4")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width4)
                
                #Produção
                with st.expander("Produção"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd34 == 0:
                           st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero   da   OS",min_value=1,max_value=rd34,value=rd34,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd34)
                            numros5 = numros4-1
                            osespec = rd33.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width5")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width5)
            
                #Administrativo
                with st.expander("Administrativo"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd42 == 0:
                           st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione   o  numero   da   OS",min_value=1,max_value=rd42,value=rd42,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd42)
                            numros5 = numros4-1
                            osespec = rd41.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width7")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width7)
            
                with st.expander("Comercial"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd50 == 0:
                           st.success('Não há pendências')
                        else:
                            numros4 = st.number_input(" Selecione   o  numero   da   OS",min_value=1,max_value=rd50,value=rd50,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd50)
                            numros5 = numros4-1
                            osespec = rd49.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width9")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width9)

                #Expedição
                with st.expander("Expedição"):
                  if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd58 == 0:
                           st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("  Selecione   o  numero   da   OS",min_value=1,max_value=rd58,value=rd58,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd58)
                            numros5 = numros4-1
                            osespec = rd57.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width11")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width11)
            
                #Serralharia
                with st.expander("Serralharia"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd66 == 0:
                           st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da OS                                ",min_value=1,max_value=rd66,value=rd66,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd66)
                            numros5 = numros4-1
                            osespec = rd65.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width13")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width13)
                
                #Tecnologia da Informação
                with st.expander("Tecnologia da Informação"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd79 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS          ",min_value=1,max_value=rd79,value=rd79,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd79)
                            numros5 = numros4-1
                            osespec = rd78.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width15")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width15)       
            #FINALIZADAS   
            with tab9:
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    st.header('Manutenção', divider='rainbow')
                    with st.expander("Filtros"):
                        genre = st.radio("Selecione ",["ELÉTRICA", "Por Data"],index=0)

                with st.expander(f"Minhas O.S  ({whrlinhas4})"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'Por Data':
                        with diferent1:
                            cls = st.date_input('Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM ELETRICA WHERE FINALIZADA = 'Sim'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn)
                            whrlinhas91 = whrlinhas90.shape[0]
                        
                        if whrlinhas4 == 0:
                            st.success('Não há pendências')
                        else:
                            numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=whrlinhas4,value=whrlinhas4,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas4)
                            numros3 = numros2-1
                            osespec = whrlinhas3.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width17")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width17)
                        with diferent2:
                            st.button('↻')
                    
                    else:
                        if whrlinhas4 == 0:
                           st.success('Não há pendências')
                        else:
                            numros2 = st.number_input("Selecione o numero da            OS",min_value=1,max_value=whrlinhas4,value=whrlinhas4,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas4)
                            numros3 = numros2-1
                            osespec = whrlinhas3.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width19")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width19)



                with st.expander("PCM" f' ({pcm_id1})'):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if pcm_id1 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input(" Selecione  o numero da    OS",min_value=1,max_value=pcm_id1,value=pcm_id1,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=pcm_id1)
                            numros5 = numros4-1
                            osespec = pcm1.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width30")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width30)

                
                #Ferramentaria
                st.markdown('------')
                with st.expander("Ferramentaria"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd32 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione  o  numero  da  OS ",min_value=1,max_value=rd32,value=rd32,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd32)
                            numros5 = numros4-1
                            osespec = rd31.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width21")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width21)
                
                with st.expander("Produção"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd38 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS  ",min_value=1,max_value=rd38,value=rd38,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd38)
                            numros5 = numros4-1
                            osespec = rd37.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width23")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width23)

                with st.expander("Administrativo"):
                    if genre == 'ELÉTRICA':
                        if rd46 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS    ",min_value=1,max_value=rd46,value=rd46,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd46)
                            numros5 = numros4-1
                            osespec = rd45.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width24")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width24)

                with st.expander("Comercial"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd54 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS     ",min_value=1,max_value=rd54,value=rd54,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd54)
                            numros5 = numros4-1
                            osespec = rd53.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width25")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width25)
                    
                with st.expander("Expedição"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd62 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS        ",min_value=1,max_value=rd62,value=rd62,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd62)
                            numros5 = numros4-1
                            osespec = rd61.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width26")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width26)
                
                with st.expander("Serralharia"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd70 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS         ",min_value=1,max_value=rd70,value=rd70,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd70)
                            numros5 = numros4-1
                            osespec = rd69.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width27")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width27)
                
                with st.expander("Tecnologia da Informação"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if rd75 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS            ",min_value=1,max_value=rd75,value=rd75,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd75)
                            numros5 = numros4-1
                            osespec = rd74.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width28")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width28)
            #GERAL
            with tab10:
                st.header('Manutenção', divider='rainbow')
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:
                    with st.expander("Geral"):
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            numros10 = st.number_input(" Selecione o  numero da     OS",min_value=1,max_value=allln1,value=allln1,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= allln1)
                            numros11 = numros10-1
                            osespec = allinhas.loc[numros11]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width29")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width29)
#MECÂNICA
allln = pd.read_sql_query("SELECT * FROM MECANICA", conn)
allln1 = allln.shape[0]
consulta4 = "SELECT * FROM MECANICA"
allinhas = pd.read_sql_query(consulta4, conn)

#O.S ABERTAS  NÃO FINALIZADAS
consulta5 = "SELECT * FROM MECANICA WHERE FINALIZADA = 'Não'"
MECANICAdados = pd.read_sql_query(consulta5, conn)
MECANICAvalores = MECANICAdados.shape[0] 

#O.S FINALIZADAS
consulta6 = "SELECT * FROM MECANICA WHERE FINALIZADA = 'Sim'"
MECANICAdados1 = pd.read_sql_query(consulta6, conn)
MECANICAvalores1= MECANICAdados1.shape[0]

if fLIDERES == 'Equipe de MECÂNICA':
    if fSETOR == 'Mecânica':
        if senha == '1400':
            #cl1 = st.button("DELETAR TABELA")
            #if cl1:
                #cursor.execute("DROP TABLE MECANICA")
                #conn.commit()
            image = Image.open('./Midia/ssmm.jpg')
            col1,col2 = st.columns([5,5])
            with col1:
                st.title('Status e informações de O.S')
           
            tab6, tab7,tab8,tab9,tab10= st.tabs(["| Cadastro |", "| Finalizar |","| O.S Em aberto |","| O.S Finalizadas |","| Geral |"])
            with tab6:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln1 == 0:
                           numros = 0
                           numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln1,value=allln1,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM MECANICA"
                        ros_oc = pd.read_sql_query(consulta1, conn)

                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]

                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Filipe leite','Jameson Sales','Cesar Filho','Ivson Paulino','Maurilio Sales','Bruno Kappaun','Adriely Lemos','Gilson Freitas','Willian Oliveira','Cesar Augusto'),index=None,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Filipe leite','Jameson Sales','Cesar Filho','Maurilio Sales','Bruno Kappaun','Adriely Lemos','Gilson Freitas','Willian Oliveira','Cesar Augusto'),index=None,placeholder='Atualize')
                        
                    if not atd1:
                        Rstatus = container.text_area('Atualize o tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                        
                    if not atd1:
                        Rsetor = container.selectbox('Setor solicitante:', ('Tecnologia da Informação','Comercial','Administrativo','Expedição','Ferramentaria','Serralharia','Utilidades','Estampo,corte e furo','Extrusão','Geral'),index=None,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Tecnologia da Informação','Comercial','Administrativo','Expedição','Ferramentaria','Serralharia','Utilidades','Estampo,corte e furo','Extrusão','Geral'),index=None,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva','Confecção'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva','Confecção'),index=None,placeholder='Atualize')

                    if not atd1:
                        parada = container.selectbox('Gerou parada de maquina?:', ('Sim','Não'),index=None,placeholder='Selecione')
                    if atd1:
                        parada = container.selectbox('Gerou parada de maquina?: ', ('Sim','Não'),index=None,placeholder='Selecione')

                    if not atd1: 
                    
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                        
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if Rsetor == 'Extrusão' or RUsetor == 'Extrusão':
                        Local = container.selectbox('Local:',('Prensa - P8','Puller - 01','Puller - 02','Quench','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts'),index=None,placeholder= 'Selecione')
                        
                    if Rsetor == 'Estampo,corte e furo' or RUsetor == 'Estampo,corte e furo':
                        Local = container.selectbox('Local:',('Prensa Excentrica - 01','Prensa Excentrica - 02','Serra Automatica','Serra Manual','Serra fita - FRANHO','Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Embaladora Automatica','Seladora manual - KT001','Seladora manual - KT002'),index=None,placeholder= 'Selecione')
                        
                    if Rsetor == 'Utilidades' or RUsetor == 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione')
                            
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades' and Rsetor != 'Serralharia' and RUsetor != 'Serralharia' and Rsetor != 'Ferramentaria' and RUsetor != 'Ferramentaria'  and Rsetor != 'Geral' and RUsetor != 'Geral':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione')
                    elif Rsetor == 'Serralharia' or RUsetor == 'Serralharia':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Serra fita - FRANHO'),index=None,placeholder= 'Selecione')
                    elif Rsetor == 'Ferramentaria' or RUsetor == 'Ferramentaria':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Maquina de jatear','Talha Elétrica','Recuperação de ferramentas'),index=None,placeholder= 'Selecione')
                    elif Rsetor == 'Geral' or RUsetor == 'Geral':
                        Local = container.selectbox('Local:',('Prensa - P8 - Puller - 01 - Puller - 02 - Esticadeira - HEAD - Esticadeira - TAIL - Forno de Tarugo - Serra Fria - Forno de Envelhecimento - Prensa Excentrica - 01 - Prensa Excentrica - 02 - Serra Automatica - Serra Manual - Serra fita - FRANHO - Rosqueadeira - MACHO 01 - Rosqueadeira - COSSINETE 01 - Rosqueadeira - COSSINETE 2 - Maquina de jatear - Talha Elétrica - Embaladora Automatica - Elétrica Predial - Artífice - Recuperação de ferramentas - Casa de Bombas - Caixa D.Agua - Subestação - 1 - Subestação - 2 -  Seladora manual - KT001 - Seladora manual - KT002 - Portão de automoveis - Portão de pedestres - Interfone',), placeholder='Selecione')

                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        agree = container.checkbox('Selecione á caixa para enviar a imagem em outro momento:')
                        if agree:
                            uploaded_files = bytes_imagem
                            bytes_data = bytes_imagem
                        else:
                             uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                             for uploaded_file in uploaded_files:
                                 bytes_data = uploaded_file.read()

                with neymar:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln1)
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=int(preenchimento[0]),value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM MECANICA WHERE OS = {numero_da_os};')
                                conn.commit()
                
                if fLIDERES == 'Equipe de MECÂNICA':
                    if fSETOR == 'Mecânica':
                        if senha == '1400':
                            if atd1: 
                                atl = st.button('Atualize  ↻')
                                if atl:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.01)
                                    cursor.execute("UPDATE MECANICA SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, AÇÃO = ?,Local = ? WHERE OS = ?",(RUsolicitante, RUsetor, RUstatus,RUniveldaocorrencia,RUacao,Local,int(preenchimento[0])))
                                    conn.commit()
                                    
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files,parada]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[8] == True:
                                    insdds = st.button("Envia O.S 📤")

                                    if insdds:
                                        ids_shape_mecanica = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_mecanica}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_mecanica,str(timenow),datenow))
                                        cursor.execute("INSERT INTO MECANICA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,ESPECIALIDADE,MÊS,Local,PARADA) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (ids_shape_mecanica, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,especialidades,monthnow,Local,parada))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn.commit()

            with tab7:
                st.header('Finalizar O.S')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    containerx = st.container(border=True)
                    setorescolhido = containerx.selectbox('Setor', ('PCM','Tecnologia da Informação','Comercial','Administrativo','Expedição','Produção','Ferramentaria','Serralharia','Mecânica'),index=None,placeholder='Selecione')
                    fnlz2 = containerx.number_input("Selecione o numero da OS que deseja Finalizar",min_value=1,max_value=1000,value=1,placeholder="Selecione")
                    fnlz3 = fnlz2-1
                    finalizar = containerx.selectbox('O.S finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                    #datainput = containerx.date_input("Data", value=None)
                    #containerx.write(datainput)
                    #timeinput = containerx.time_input('HORA', value=None)
                    #containerx.write(timeinput)

                if fLIDERES == 'Equipe de MECÂNICA':
                    if fSETOR == 'Mecânica':
                        if senha == '1400':

                            if setorescolhido == 'Ferramentaria':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Ferramentaria SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()

    
                            if setorescolhido == 'Produção':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                            
                            if setorescolhido == 'Administrativo':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Administrativo SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit() 
                            
                            if setorescolhido == 'Comercial':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Comercial SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit() 

                            if setorescolhido == 'Expedição':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()  

                            if setorescolhido == 'Serralharia':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Serralharia SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()

                            if setorescolhido == 'Tecnologia da Informação':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE TI SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()

                            if setorescolhido == 'PCM':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor14.execute("UPDATE PCM SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn14.commit() 


                            if setorescolhido == 'Mecânica':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE MECANICA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()  

            with tab8:
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    st.header('Manutenção', divider='rainbow')
                    with st.expander("Filtros"):
                        genre = st.radio(
                          "Selecione",
                        ["MECÂNICA","Por Data"],
                        index=0,
                        )
                with st.expander(f"Minhas OS  ({MECANICAvalores})"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'Por Data':
                        with diferent1:
                            cls = st.date_input('Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM MECANICA WHERE FINALIZADA = 'Não' AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn)
                            whrlinhas91 = whrlinhas90.shape[0]
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= MECANICAvalores)
                            numros3 = numros2-1
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width2")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width2)
                        with diferent2:
                            st.button('↻')
                    else:
                        if MECANICAvalores == 0:
                           st.success('Não há pendências')
                        else:
                            numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=MECANICAvalores,value=MECANICAvalores,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= MECANICAvalores)
                            numros3 = numros2-1
                            osespec = MECANICAdados.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width2")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width2)

                
                with st.expander("PCM" f' ({pcm_id2})'):
                    if 'MECÂNICA' == 'MECÂNICA':
                        if pcm_id2 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da k OS",min_value=1,max_value=pcm_id2,value=pcm_id2,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=pcm_id2)
                            numros5 = numros4-1
                            osespec = pcm2.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width16")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width16)

                #Ferramentaria   
                st.markdown('------')
                with st.expander("Ferramentaria"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd30 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS ",min_value=1,max_value=rd30,value=rd30,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd30)
                            numros5 = numros4-1
                            osespec = rd29.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width17")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width17)
                    
                #Produção
                with st.expander("Produção"):
                    if 'MECÂNICA' == 'MECÂNICA':
                            if rd36 == 0:
                               st.success('Não há pendências')
                            else:
                                numros4 = st.number_input(" Selecione  o  numero  da   OS",min_value=1,max_value=rd36,value=rd36,placeholder="Selecione")
                                st.metric(label="O.S Existentes", value=rd36)
                                numros5 = numros4-1
                                osespec = rd35.loc[numros5]
                                def load_data():
                                    return pd.DataFrame(osespec)
                                st.checkbox("Estender", value=True, key="use_container_width5")
                                lddt = load_data()
                                st.dataframe(lddt, use_container_width=st.session_state.use_container_width5)

                #Administrativo
                with st.expander("Administrativo"):
                    if 'MECÂNICA' == 'MECÂNICA':
                            if rd44 == 0:
                               st.success('Não há pendências')
                            else:
                                numros4 = st.number_input("Selecione  o numero  da    OS",min_value=1,max_value=rd44,value=rd44,placeholder="Selecione")
                                st.metric(label="O.S Existentes", value=rd44)
                                numros5 = numros4-1
                                osespec = rd43.loc[numros5]
                                def load_data():
                                    return pd.DataFrame(osespec)
                                st.checkbox("Estender", value=True, key="use_container_width7")
                                lddt = load_data()
                                st.dataframe(lddt, use_container_width=st.session_state.use_container_width7)
                #Comercial
                with st.expander("Comercial"):
                    if 'MECÂNICA' == 'MECÂNICA':
                            if rd52 == 0:
                               st.success('Não há pendências')
                            else:
                                numros4 = st.number_input("Selecione  o  numero   da    OS",min_value=1,max_value=rd52,value=rd52,placeholder="Selecione")
                                st.metric(label="O.S Existentes", value=rd52)
                                numros5 = numros4-1
                                osespec = rd51.loc[numros5]
                                def load_data():
                                    return pd.DataFrame(osespec)
                                st.checkbox("Estender", value=True, key="use_container_width9")
                                lddt = load_data()
                                st.dataframe(lddt, use_container_width=st.session_state.use_container_width9)

                #Expedição
                with st.expander("Expedição"):
                  if 'MECÂNICA' == 'MECÂNICA':
                        if rd60 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione  o  numero   da     OS",min_value=1,max_value=rd60,value=rd60,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd60)
                            numros5 = numros4-1
                            osespec = rd59.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width11")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width11)
                
                #Serralharia
                with st.expander("Serralharia"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd68 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione  o    numero   da    OS",min_value=1,max_value=rd68,value=rd68,placeholder="Selecione")
                            oi = st.metric(label="O.S Existentes", value=rd68)
                            numros5 = numros4-1
                            osespec = rd67.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width13")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width13)
                
            with tab9:
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    st.header('Manutenção', divider='rainbow')
                    with st.expander("Filtros"):
                        genre = st.radio("Selecione ",["MECÂNICA","Por Data"],index=0)
                    
                with st.expander(f"Minhas OS ({MECANICAvalores1})"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'Por Data':
                        with diferent1:
                            cls = st.date_input(' Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM MECANICA WHERE FINALIZADA = 'Sim' AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn)
                            whrlinhas91 = whrlinhas90.shape[0]
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            numros2 = st.number_input(" Selecione   o  numero da  OS ",min_value=1,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas91)
                            numros3 = numros2-1
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width14")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width14)
                        with diferent2:
                            st.button('↻    ')
                    else:
                        numros2 = st.number_input("Selecione   o   numero  da      OS      ",min_value=1,max_value=1000,value=1,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= MECANICAvalores1)
                        numros3 = numros2-1
                        if MECANICAvalores1 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = MECANICAdados1.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width15")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width15)
                
                with st.expander("PCM" f' ({pcm_id3})'):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        if pcm_id3 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da O.S    ",min_value=1,max_value=100,value=1,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=pcm_id3)
                            numros5 = numros4-1
                            osespec = pcm3.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width16")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width16)

                #Ferramentaria
                st.markdown('------')
                with st.expander("Ferramentaria"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd30 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input(" Selecione  o  numero  da  OS ",min_value=1,max_value=rd30,value=rd30,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd30)
                            numros5 = numros4-1
                            osespec = rd29.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width18")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width18)
                
                with st.expander("Produção"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd40 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS   ",min_value=1,max_value=rd40,value=rd40,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd40)
                            numros5 = numros4-1
                            osespec = rd39.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width19")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width19)
                            
                with st.expander("Administrativo"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd48 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS     ",min_value=1,max_value=rd48,value=rd48,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd48)
                            numros5 = numros4-1
                            osespec = rd47.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width21")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width21)

                with st.expander("Comercial"):            
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd56 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS       ",min_value=1,max_value=rd56,value=rd56,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd56)
                            numros5 = numros4-1
                            osespec = rd55.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width23")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width23)

                with st.expander("Expedição"):            
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd64 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS        ",min_value=1,max_value=rd64,value=rd64,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd64)
                            numros5 = numros4-1
                            osespec = rd63.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width25")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width25)
                
                with st.expander("Serralharia"):                
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd72 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS          ",min_value=1,max_value=rd72,value=rd72,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd72)
                            numros5 = numros4-1
                            osespec = rd71.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width27")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width27)
                
                with st.expander("Tecnologia da Informação"):    
                    if 'MECÂNICA' == 'MECÂNICA':
                        if rd77 == 0:
                            st.success('Não há pendências')
                        else:
                            numros4 = st.number_input("Selecione o numero da  OS           ",min_value=1,max_value=rd77,value=rd77,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value=rd77)
                            numros5 = numros4-1
                            osespec = rd76.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width29")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width29)

            with tab10:
                st.header('Manutenção', divider='rainbow')
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:
                    with st.expander("GERAL"):
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            numros10 = st.number_input("Selecione o numero da     OS",min_value=1,max_value=allln1,value=allln1,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= allln1)
                            numros11 = numros10-1
                            osespec = allinhas.loc[numros11]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width30")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width30) 

#Ferramentaria
allln13 = pd.read_sql_query("SELECT * FROM Ferramentaria", conn)
allln14 = allln13.shape[0]
consulta7 = "SELECT * FROM Ferramentaria"
allinhas15 = pd.read_sql_query(consulta7, conn)

#O.S ABERTAS  NÃO FINALIZADAS
consulta8 = "SELECT * FROM Ferramentaria WHERE FINALIZADA = 'Não'"
whrlinhas12 = pd.read_sql_query(consulta8, conn)
whrlinhas13 = whrlinhas12.shape[0]

#O.S FINALIZADAS
cursor.execute("SELECT * FROM Ferramentaria WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas15 = cursor.fetchall()
whrlinhas16 = pd.DataFrame(whrlinhas15)
whrlinhas17 = whrlinhas16.shape[0]

if fLIDERES == 'Ivson Paulino':
    if fSETOR == 'Ferramentaria':
        if senha == '70':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl5 = st.button("DELETAR TABELA")
            #if cl5:
                #cursor.execute("DROP TABLE Ferramentaria")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab26,tab27,tab28,tab29= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral |"])
            with tab26:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col9,col10= st.columns([5,5])  
                with col9:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas13 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln14,value=allln14,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM Ferramentaria"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                           [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
                        
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Ivson Paulino',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Ivson Paulino',),index=0,placeholder='Atualize')
                        
                    if not atd1:
                        Rstatus = container.text_area('Atualize o tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                        
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Ferramentaria',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Ferramentaria',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                                                
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Maquina de jatear','Talha Elétrica','Recuperação de ferramentas'),index=None,placeholder= 'Selecione')
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                
                with col10:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln14)
                        if allln14 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec4 = allinhas15.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec4)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM Ferramentaria WHERE OS = {numero_da_os};')
                                conn.commit()
                
                if fLIDERES == 'Ivson Paulino':
                    if fSETOR == 'Ferramentaria':
                        if senha == '70':
                            if atd1: 
                                atl1 = st.button('Atualize')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE Ferramentaria SET OCORRENCIA = ?,GRAU = ?, AÇÃO = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,int(preenchimento[0])))
                                    conn.commit()
                                                                           
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[7] == True:
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_Ferramentaria = ids_shape + 1
                                    if insdds:
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Ferramentaria}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_Ferramentaria,str(timenow),datenow))    
                                        cursor.execute("INSERT INTO Ferramentaria (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?,?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_Ferramentaria , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_Ferramentaria,bytes_data,monthnow))
                                        conn.commit()
                                        
            with tab27:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Ferramentaria', divider='rainbow')
                    st.button(' Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas13 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas13,value=whrlinhas13,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas13)
                            numros23 = numros22-1
                            osespec5 = whrlinhas12.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec5)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab28:
                st.header('Ferramentaria', divider='rainbow')
                st.button(' Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd1 == 0:
                        st.success('Não há pendências')
                    else:
                        numros16 = st.number_input("Selecione o numero da   O.S",min_value=1,max_value=rd1,value=rd1,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd1)
                        numros17 = numros16-1
                        osespec6 = rd.loc[numros17]
                        def load_data():
                            return pd.DataFrame(osespec6)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab29:
                st.header('Ferramentaria', divider='rainbow')
                st.button(' Atualize ↻  ')
                with st.expander("Geral"):
                    if allln14 == 0:
                        st.success('Não há pendências')
                    else:
                        numros20 = st.number_input("Selecione o numero da    O.S",min_value=1,max_value=allln14,value=allln14,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln14)
                        numros21 = numros20-1
                        osespec7 = allln13.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec7)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)
#PRODUCAO
if fLIDERES == 'Maurilio Sales':
    if fSETOR == 'Produção':
        if senha == '1405':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl6 = st.button("DELETAR TABELA")
            #if cl6:
                #cursor.execute("DROP TABLE PRODUCAO")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab30,tab31,tab32,tab33= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral |"])
            with tab30:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col11,col12= st.columns([5,5])  
                with col11:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if rd7 == 0:
                           numros = 0
                           numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=rd7,value=rd7,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM PRODUCAO"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
                            
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Maurilio Sales',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Maurilio Sales',),index=0,placeholder='Atualize')
                        
                    if not atd1:
                        Rstatus = container.text_area('Atualize o tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                        
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Produção',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Produção',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                                                
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Prensa - P8','Puller - 01','Puller - 02','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts','Prensa Excentrica - 01','Prensa Excentrica - 02','Serra Automatica','Serra Manual','Serra fita  - FRANHO','Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Maquina de jatear','Talha Elétrica','Embaladora Automatica','Elétrica Predial','Artífice','Recuperação de ferramentas','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Seladora manual - KT001','Seladora manual - KT002','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione')
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()

                with col12:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln16)
                        if allln16 == 0:
                            st.success('Não há Ordens')
                        else:
                            osespec8 = allinhas16.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec8)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM PRODUCAO WHERE OS = {numero_da_os};')
                                conn.commit()
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                                    
                if fLIDERES == 'Maurilio Sales':
                    if fSETOR == 'Produção':
                        if senha == '1405':
                            if atd1:
                                atl1 = st.button('Atualize ↻')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE PRODUCAO SET  OCORRENCIA = ?,GRAU = ?, AÇÃO = ?, MANUTENTOR = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,manutentor,int(preenchimento[0])))
                                    conn.commit()                           
                                                            
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[7] == True:
                    
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_producao = ids_shape + 1
                                    if insdds:
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_producao}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_producao,str(timenow),datenow))                      
                                        cursor.execute("INSERT INTO PRODUCAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)", (ids_shape_producao , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_producao,bytes_data,monthnow))
                                        conn.commit()

            with tab31:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Produção', divider='rainbow')
                    st.button(' Atualize  ↻ ')
                    with st.expander("Abertas"):
                        if whrlinhas19 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas19,value=whrlinhas19,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas19)
                            numros23 = numros22-1
                            osespec9 = whrlinhas18.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec9)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)


            with tab32:
                st.header('Produção', divider='rainbow')
                st.button(' Atualize   ↻ ')
                with st.expander("Finalizadas"):
                    if rd5 == 0:
                        st.success('Não há pendências')
                    else:
                        numros18 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd5,value=rd5,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd5)
                        numros19 = numros18-1
                        osespec10 = rd4.loc[numros19]
                        def load_data():
                            return pd.DataFrame(osespec10)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab33:
                st.header('Produção', divider='rainbow')
                st.button('Atualize ↻    ')
                with st.expander("Geral"):
                    if allln16 == 0:
                        st.success('Não há pendências')
                    else:
                        numros20 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln16,value=allln16,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln16)
                        numros21 = numros20-1
                        osespec11 = allln15.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec11)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)
#Administrativo
#GERAL Administrativo
allln17 = pd.read_sql_query("SELECT * FROM Administrativo", conn)
allln18 = allln17.shape[0]
consulta2 = "SELECT * FROM Administrativo"
allinhas17 = pd.read_sql_query(consulta2, conn)

#O.S ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM Administrativo WHERE FINALIZADA = 'Não'"
whrlinhas23 = pd.read_sql_query(consulta3, conn)
whrlinhas24 = whrlinhas23.shape[0]

#O.S FINALIZADAS
cursor.execute("SELECT * FROM Administrativo WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas25 = cursor.fetchall()
whrlinhas26 = pd.DataFrame(whrlinhas25)
whrlinhas27 = whrlinhas26.shape[0]

if fLIDERES == 'Gilson Freitas':
    if fSETOR == 'Administrativo':
        if senha == '1404':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl7 = st.button("DELETAR TABELA")
            #if cl7:
                #cursor.execute("DROP TABLE Administrativo")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab34,tab35,tab36,tab37= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral |"])
            with tab34:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col13,col14= st.columns([5,5])  
                with col13:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln18 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln18 ,value=allln18 ,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM Administrativo"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
                        
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Gilson Freitas',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante', ('Gilson Freitas',),index=0,placeholder='Atualize')
                    
                    if not atd1:
                        Rstatus = container.text_area('Tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Atualize o tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                    
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Administrativo',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Administrativo',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                                        
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione')
                    
    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()

                with col14:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln18)
                        if allln18 ==0:
                            st.success('Não há pendências')
                        else:
                            osespec12 = allinhas17.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec12)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM Administrativo WHERE OS = {numero_da_os};')
                                conn.commit()
                
                if fLIDERES == 'Gilson Freitas':
                    if fSETOR == 'Administrativo':
                        if senha == '1404':
                            if atd1: 
                                atl1 = st.button('Atualize ↻')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE Administrativo SET OCORRENCIA = ?,GRAU = ?, AÇÃO = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,int(preenchimento[0])))
                                    conn.commit()
                                                               
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[7] == True:
                    
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_Administrativo = ids_shape + 1
                                    if insdds:
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Administrativo}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_Administrativo,str(timenow),datenow))
                                        cursor.execute("INSERT INTO Administrativo (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?, ?,  ?,?, ?, ?,?,?,?,?,?,?)", (ids_shape_Administrativo , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_Administrativo,bytes_data,monthnow))
                                        conn.commit()
                                        
            with tab35:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Administrativo', divider='rainbow')
                    st.button(' Atualize ↻  ')
                    with st.expander("Abertas"):
                        if whrlinhas24 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  O.S",min_value=1,max_value=whrlinhas24,value=whrlinhas24,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas24)
                            numros23 = numros22-1
                            osespec13 = whrlinhas23.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec13)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab36:
                st.header('Administrativo', divider='rainbow')
                st.button('Atualize ↻        ')
                with st.expander("Finalizadas"):
                    if rd9 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        numros20 = st.number_input("Selecione o numero da   O.S",min_value=1,max_value=rd9,value=rd9,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd9)
                        numros21 = numros20-1
                        osespec14 = rd8.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec14)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab37:
                st.header('Administrativo', divider='rainbow')
                st.button('Atualize ↻   ')
                with st.expander("Geral"):
                    if allln18 == 0:
                        st.success('Não há pendências')
                    else:
                        numros20 = st.number_input("Selecione o numero da    O.S",min_value=1,max_value=allln18,value=allln18,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln18)
                        numros21 = numros20-1
                        osespec15 = allln17.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec15)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

#Comercial
#GERAL Comercial
allln19 = pd.read_sql_query("SELECT * FROM Comercial", conn)
allln20 = allln19.shape[0]
consulta2 = "SELECT * FROM Comercial"
allinhas18 = pd.read_sql_query(consulta2, conn)

#O.S ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM Comercial WHERE FINALIZADA = 'Não'"
whrlinhas28 = pd.read_sql_query(consulta3, conn)
whrlinhas29 = whrlinhas28.shape[0]

#O.S FINALIZADAS
cursor.execute("SELECT * FROM Comercial WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas30 = cursor.fetchall()
whrlinhas31 = pd.DataFrame(whrlinhas30)
whrlinhas32 = whrlinhas31.shape[0]

if fLIDERES == 'Adriely Lemos':
    if fSETOR == 'Comercial':
        if senha == '1403':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl8 = st.button("DELETAR TABELA")
            #if cl8:
                #cursor.execute("DROP TABLE Comercial")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')
            st.markdown("---")
            tab38,tab39,tab40,tab41= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral |"])
            with tab38:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col15,col16= st.columns([5,5])  
                with col15:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas29 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=whrlinhas29 ,value=whrlinhas29 ,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM Comercial"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]

                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Adriely Lemos',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Adriely Lemos',),index=0,placeholder='Atualize')
                    
                    if not atd1:
                        Rstatus = container.text_area('Tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Atualize o tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                    
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Comercial',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Comercial',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                                        
                            
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice'),index=None,placeholder= 'Selecione')
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()

                with col16:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln20)
                        if allln20 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec16 = allinhas18.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec16)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM Comercial WHERE OS = {numero_da_os};')
                                conn.commit()
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                            
                if fLIDERES == 'Adriely Lemos':
                    if fSETOR == 'Comercial':
                        if senha == '1403':
                            if atd1: 
                                atl1 = st.button('Atualize ↻')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE Comercial SET OCORRENCIA = ?,GRAU = ?, AÇÃO = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,int(preenchimento[0])))
                                    conn.commit()
                                                       
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[7] == True:
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_Comercial = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Comercial}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_Comercial,str(timenow),datenow))
                                        cursor.execute("INSERT INTO Comercial (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?, ?,?,?,? ,?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_Comercial , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_Comercial,bytes_data,monthnow))
                                        conn.commit()
                                             
            with tab39:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Comercial', divider='rainbow')
                    st.button('  Atualize ↻ ')
                    with st.expander("Abertas"):
                        if whrlinhas29 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas29,value=whrlinhas29,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas29)
                            numros23 = numros22-1
                            osespec17 = whrlinhas28.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec17)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab40:
                st.header('Comercial', divider='rainbow')
                st.button(' Atualize ↻  ' )
                with st.expander("Finalizadas"):
                    if rd13 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        numros22 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd13,value=rd13,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd13)
                        numros23 = numros22-1
                        osespec18 = rd12.loc[numros23]
                        def load_data():
                            return pd.DataFrame(osespec18)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab41:
                st.header('Comercial', divider='rainbow')
                st.button(' Atualize ↻ ')
                with st.expander("Geral"):
                    if allln20 == 0:
                        st.success('Não há pendências')
                    else:
                        numros22 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln20,value=allln20,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln20)
                        numros23 = numros22-1
                        osespec19 = allln19.loc[numros23]
                        def load_data():
                            return pd.DataFrame(osespec19)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

#EXPEDICAO
#GERAL EXPEDICAO
allln21 = pd.read_sql_query("SELECT * FROM EXPEDICAO", conn)
allln22 = allln21.shape[0]
consulta2 = "SELECT * FROM EXPEDICAO"
allinhas19 = pd.read_sql_query(consulta2, conn)

#O.S ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não'"
whrlinhas33 = pd.read_sql_query(consulta3, conn)
whrlinhas34 = whrlinhas33.shape[0]

#O.S FINALIZADAS
cursor.execute("SELECT * FROM EXPEDICAO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas35 = cursor.fetchall()
whrlinhas36 = pd.DataFrame(whrlinhas35)
whrlinhas37 = whrlinhas36.shape[0]

if fLIDERES == 'Willian Oliveira':
    if fSETOR == 'Expedição':
        if senha == '1402':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl9 = st.button("DELETAR TABELA")
            #if cl9:
                #cursor.execute("DROP TABLE EXPEDICAO")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab42,tab43,tab44,tab45= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral| "])
            with tab42:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col17,col18= st.columns([5,5])  
                with col17:
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas34 == 0:
                            numros1 = 0
                            numros = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln22,value=allln22,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM EXPEDICAO"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
                        
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Willian Oliveira',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Willian Oliveira',),index=0,placeholder='Atualize')
                    
                    if not atd1:
                        Rstatus = container.text_area('Tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Atualize o tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                    
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Expedição',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Expedição',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                   
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice'),index=None,placeholder= 'Selecione')
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()

                with col18:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln22)
                        if allln22 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec20 = allinhas19.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec20)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM EXPEDICAO WHERE OS = {numero_da_os};')
                                conn.commit()
            
                if fLIDERES == 'Willian Oliveira':
                    if fSETOR == 'Expedição':
                        if senha == '1402':  
                            if atd1: 
                                atl1 = st.button('Atualize  ↻')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE EXPEDICAO SET OCORRENCIA = ?,GRAU = ?,AÇÃO = ? WHERE OS = ?",(Rstatus,RUniveldaocorrencia,RUacao,int(preenchimento[0])))
                                    conn.commit()                                            
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[7] == True:
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_expedicao = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_expedicao}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_expedicao,str(timenow),datenow))
                                        cursor.execute("INSERT INTO EXPEDICAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?, ?,?, ?, ?, ?,?,?,?,?,?,?)", (ids_shape_expedicao, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_expedicao,bytes_data,monthnow))
                                        conn.commit()
                                    
            with tab43:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Expedição', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas34 == 0:
                            st.success('Não há pendências')
                        else:
                            numros24 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas34,value=whrlinhas34,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas34)
                            numros25 = numros24-1
                            osespec21 = whrlinhas33.loc[numros25]
                            def load_data():
                                return pd.DataFrame(osespec21)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab44:
                st.header('Expedição', divider='rainbow')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd17 == 0:
                        st.success('Não há pendências')
                    else:
                        numros24 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd17,value=rd17,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd17)
                        numros25 = numros24-1
                        osespec22 = rd16.loc[numros25]
                        def load_data():
                            return pd.DataFrame(osespec22)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab45:
                st.header('Expedição', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    if allln22 == 0:
                        st.success('Não há pendências')
                    else:
                        numros24 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln22,value=allln22,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln22)
                        numros25 = numros24-1
                        osespec23 = allln21.loc[numros25]
                        def load_data():
                            return pd.DataFrame(osespec23)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

#Serralharia
#GERAL Serralharia
allln23 = pd.read_sql_query("SELECT * FROM Serralharia", conn)
allln24 = allln23.shape[0]
consulta2 = "SELECT * FROM Serralharia"
allinhas20 = pd.read_sql_query(consulta2, conn)

#O.S ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM Serralharia WHERE FINALIZADA = 'Não'"
whrlinhas38 = pd.read_sql_query(consulta3, conn)
whrlinhas39 = whrlinhas38.shape[0]

#O.S FINALIZADAS
cursor.execute("SELECT * FROM Serralharia WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas40 = cursor.fetchall()
whrlinhas41 = pd.DataFrame(whrlinhas40)
whrlinhas42 = whrlinhas41.shape[0]

if fLIDERES == 'Cesar Augusto':
    if fSETOR == 'Serralharia':
        if senha == '1401':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl10 = st.button("DELETAR TABELA")
            #if cl10:
                #cursor.execute("DROP TABLE Serralharia")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab46,tab47,tab48,tab49= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral |"])
            with tab46:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col19,col20= st.columns([5,5])  
                with col19:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas39 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln24 ,value=allln24 ,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM Serralharia"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]

                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Cesar Augusto',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Cesar Augusto',),index=0,placeholder='Atualize')
                    
                    if not atd1:
                        Rstatus = container.text_area('Tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Atualize o tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                    
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Serralharia',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Serralharia',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:',('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                                          
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Serra fita - FRANHO'),index=None,placeholder= 'Selecione')
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()

                with col20:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln24)
                        if allln24 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec24 = allinhas20.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec24)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=preenchimento[0],placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM Serralharia WHERE OS = {numero_da_os};')
                                conn.commit()
 
                if fLIDERES == 'Cesar Augusto':
                    if fSETOR == 'Serralharia':
                        if senha == '1401':
                            if atd1: 
                                atl1 = st.button('Atualize ↻       ')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE Serralharia SET OCORRENCIA = ?,GRAU = ?, AÇÃO = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,int(preenchimento[0])))
                                    conn.commit()
                                     
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[7] == True:
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_Serralharia = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Serralharia}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_Serralharia,str(timenow),datenow))
                                        cursor.execute("INSERT INTO Serralharia (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?, ?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_Serralharia, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_Serralharia,bytes_data,monthnow))
                                        conn.commit()
                                                    
            with tab47:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Serralharia', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas39 == 0:
                            st.success('Não há pendências')
                        else:
                            numros26 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas39,value=whrlinhas39,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas39)
                            numros27 = numros26-1
                            osespec25 = whrlinhas38.loc[numros27]
                            def load_data():
                                return pd.DataFrame(osespec25)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab48:
                st.header('Serralharia', divider='rainbow')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd21 == 0:
                        st.success('Não há pendências')
                    else:
                        numros26 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd21,value=rd21,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd21)
                        numros27 = numros26-1
                        osespec26 = rd20.loc[numros27]
                        def load_data():
                            return pd.DataFrame(osespec26)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab49:
                st.header('Serralharia', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    if allln24 == 0:
                        st.success('Não há pendências')
                    else:
                        numros26 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln24,value=allln24,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln24)
                        numros27 = numros26-1
                        osespec27 = allln23.loc[numros27]
                        def load_data():
                            return pd.DataFrame(osespec27)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

query = "SELECT * FROM TI WHERE FINALIZADA = 'Não'"
rd70 = pd.read_sql_query(query, conn)
rd71 = rd70.shape[0]

query1 = "SELECT * FROM TI WHERE FINALIZADA = 'Sim'"
rd72 = pd.read_sql_query(query1, conn)
rd73 = rd72.shape[0]

allln25 = pd.read_sql_query("SELECT * FROM TI", conn)
allln26 = allln25.shape[0]

#O.S ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM TI WHERE FINALIZADA = 'Não'"
whrlinhas43 = pd.read_sql_query(consulta3, conn)
whrlinhas44 = whrlinhas43.shape[0]

#O.S FINALIZADAS
cursor.execute("SELECT * FROM TI WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas45 = cursor.fetchall()
whrlinhas46 = pd.DataFrame(whrlinhas45)
whrlinhas47 = whrlinhas46.shape[0]

if fLIDERES == 'Filipe Leite':
    if fSETOR == 'Tecnologia da Informação':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl11 = st.button("DELETAR TABELA")
            #if cl11:
                #cursor.execute("DROP TABLE TI")
                #conn.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab50,tab51,tab52,tab53= st.tabs(["| Cadastro |","| O.S Abertas |","| O.S Finalizadas |","| Geral |"])
            with tab50:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col21,col22= st.columns([5,5])  
                with col21:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas44 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln26 ,value=allln26 ,placeholder="Selecione")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM TI"
                        ros_oc = pd.read_sql_query(consulta1, conn)
                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox('Solicitante:', ('Filipe Leite',),index=0,placeholder='Selecione')
                    if atd1:
                        RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Filipe Leite',),index=0,placeholder='Atualize')
                    
                    if not atd1:
                        Rstatus = container.text_area('Tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
                    if atd1:
                        RUstatus = container.text_area('Atualize o tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                    
                    if not atd1:
                        Rsetor = container.selectbox('Setor:', ('Tecnologia da Informação',),index=0,placeholder='Selecione')
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox('Aualize o Setor:', ('Tecnologia da Informação',),index=0,placeholder='Atualize')
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione')
                    if atd1:
                        RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize')

                    if not atd1:
                        Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                    if atd1:
                        RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize')

                    if not atd1:
                        especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
                    if atd1:
                        especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')
                    
                    if not atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                    if atd1:
                        manutentor = container.selectbox('Tipo de manutenção:', ('Elétrica','Mecânica'),index=None,placeholder='Selecione')
                                        
                    if Rsetor != 'Extrusão' and Rsetor != 'Estampo,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,corte e furo' and RUsetor != 'Utilidades':
                        Local = container.selectbox('Local:',('Elétrica Predial','Artífice'),index=None,placeholder= 'Selecione')
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()

                with col22:
                    if atd1:
                        st.metric(label="O.S Existentes", value= allln26)
                        if allln26 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec28 = allln25.loc[numros1]
                            def load_dataa():
                                return pd.DataFrame(osespec28)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM TI WHERE OS = {numero_da_os};')
                                conn.commit()
                                     
                if fLIDERES == 'Filipe Leite':
                    if fSETOR == 'Tecnologia da Informação':
                        if senha == '69':
                            if atd1: 
                                atl1 = st.button('  Atualize ↻  ')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE TI SET OCORRENCIA = ?,GRAU = ?, AÇÃO = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,int(preenchimento[0])))
                                    conn.commit()
                                    conn.close()
                                                                                     
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[8] == True:
                                    insdds = st.button("Envia O.S 📤")
                                    if insdds:
                                        ids_shape_ti = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_ti}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA) VALUES (?,?,?)", (ids_shape_ti,str(timenow),datenow))
                                        cursor.execute("INSERT INTO TI (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?,?, ?, ?, ?, ?,?,?,?,?,?,?)", (ids_shape_ti, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        cursor.execute("INSERT INTO imagens (id,imagem,mes) VALUES (?,?,?)", (ids_shape_ti,bytes_data,monthnow))
                                        conn.commit()
                                        conn.close()

            with tab51:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('T.I', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas44 == 0:
                            st.success('Não há pendências')
                        else:
                            numros28 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas44,value=whrlinhas44,placeholder="Selecione")
                            st.metric(label="O.S Existentes", value= whrlinhas44)
                            numros29 = numros28-1
                            osespec29 = whrlinhas43.loc[numros29]
                            def load_data():
                                return pd.DataFrame(osespec29)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab52:
                st.header('T.I', divider='rainbow')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd73 == 0:
                        st.success('Não há pendências')
                    else:
                        numros28 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd73,value=rd73,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= rd73)
                        numros29 = numros28-1
                        osespec30 = rd72.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec30)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)
            
            with tab53:
                st.header('T.I', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):  
                    if allln26 == 0:
                        st.success('Não há pendências')
                    else:
                        numros28 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln26,value=allln26,placeholder="Selecione")
                        st.metric(label="O.S Existentes", value= allln26)
                        numros29 = numros28-1
                        osespec31 = allln25.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec31)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

