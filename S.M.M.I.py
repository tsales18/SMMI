
import pandas as pd
import streamlit as st
from PIL import Image
import time
import datetime as datetime
import webbrowser
import sqlite3
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import PyPDF2
import altair as alt
from datetime import datetime
import pytz
from io import BytesIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header
from streamlit_extras.dataframe_explorer import dataframe_explorer

novo_fuso_horario = pytz.timezone('America/Sao_Paulo')
hora_atual = datetime.now().replace(microsecond=0)
hora_atual_no_novo_fuso = hora_atual.astimezone(novo_fuso_horario)
data_hora_com_fuso = str(hora_atual_no_novo_fuso)
data_hora_obj = datetime.strptime(data_hora_com_fuso, "%Y-%m-%d %H:%M:%S%z")
horas = data_hora_obj.strftime("%H")
minutos = data_hora_obj.strftime("%M")
segundos = data_hora_obj.strftime("%S")
timenow = (f"{horas}:{minutos}:{segundos}")

#timenow = datetime.now().replace(microsecond=0).time()
datenow = datetime.now().date()
monthnow = datetime.now().strftime('%B')
monthnumbernow = datetime.now().month

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title=('MANUTENÇÃO SSM SOLAR DO BRASIL'),
    page_icon='🦾',
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
        "Lideres:",
        options=df['LIDERES'].unique()
        ,placeholder='Selecione!')
        fSETOR = st.selectbox(
        "Setores:",
        options=df['SETOR'].unique()
        ,placeholder='Selecione!')
        if senha == '1409':
           st.write('ok')
        else:
            senha = st.text_input('Ensira sua senha:',type="password")
        st.form_submit_button('Entrar')
    with st.spinner("Carregando..."):
        st.write("Bem Vindo!")
    with st.expander('#$#$'):
        st.success('Nada além de um homem comum,com pensamentos comuns!')

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
        SEGMENTO TEXT,  
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
        SEGMENTO TEXT,
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
        SEGMENTO TEXT,
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
        DATA DATE,
        Mês TEXT,
        MAQUINA
                
    )
                   
''') 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS checklist (
        ID_UNIC INTEGER PRIMARY KEY,
        Tag,
        Local,
        Equipamento,
        Situação,
        Check_1,     
        Check_2,
        Check_3,
        Check_4,
        Check_5,
        Check_6,
        Check_7,
        Check_8,
        Check_9,
        Relatorio,
        Hora TIME,
        Data DATE,
        Mês TEXT
             
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS checklistM(
        ID_UNIC INTEGER PRIMARY KEY,
        Tag,
        Local,
        Equipamento,
        Situação,
        Check_1,     
        Check_2,
        Check_3,
        Check_4,
        Check_5,
        Check_6,
        Check_7,
        Check_8,
        Check_9,
        Relatorio,
        Hora TIME,
        Data DATE,
        Mês TEXT
             
    )
''')

    conn1 = sqlite3.connect('./Data/imagens_a_f')
    cursor1 = conn1.cursor()
    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS imagens (
        id INTEGER PRIMARY KEY,
        imagem_abertura BLOB,
        imagem_finalizada BLOB,
        mes TEXT,
        FOREIGN KEY (id) REFERENCES ids (ID_UNIC)
        
    )
''')
    conn12 = sqlite3.connect('./Data/Materiais')
    cursor12 = conn12.cursor()

    conn14 = sqlite3.connect('./Data/Meses')
    cursor14 = conn14.cursor()

#cl = st.button("DELETAR TABELAS")
#if cl:
   #cursor.execute("DROP TABLE ELETRICA")
   #cursor.execute("DROP TABLE MECANICA")
   #cursor1.execute("DROP TABLE imagens")
   #cursor.execute("DROP TABLE Ferramentaria")
   #cursor.execute("DROP TABLE PRODUCAO")
   #cursor.execute("DROP TABLE Administrativo")
   #cursor.execute("DROP TABLE Comercial")
   #cursor.execute("DROP TABLE EXPEDICAO")
   #cursor.execute("DROP TABLE TI")
   #cursor.execute("DROP TABLE Serralharia")
   #cursor.execute("DROP TABLE ids")
   #cursor.execute("DROP TABLE checklist")
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

if 'strs' == 'strs':
    solicitante_titulo = 'Insira o solicitante:'
    solicitante_titulo_atl = 'Atualize o solicitante:'
    ocorrencia_titulo = 'Ensira detalhes da ocorrência:'
    ocorrencia_titulo_atl = 'Atualize á ocorrência:'
    setor_titulo = 'Setor solicitante:'
    setor_titulo_atl ='Aualize o Setor:'
    nivel_de_ocorrencia_titulo = 'Nivel da ocorrência:'
    nivel_de_ocorrencia_titulo_atl = 'Atualize o nivel da ocorrência:'
    acao_titulo = 'Tipo de ação:'
    acao_titulo_atl = 'Atualize o tipo da ação:'
    parada_titulo = 'Gerou interrupção no funcionamento?:'
    especialidades_titulo = 'Especifique o tipo de ocorrência:'
    especialidades_titulo_atl = 'Atualize o tipo de ocorrência:'
    local_titulo = 'Localidade:'
    manutentor_titulo = 'Tipo de manutenção'

    help_solicitante = 'Nesta caixa de seleção: você precisa selecionar o responsavel por setor que fez a solicitação de O.S '
    help_ocorrência = 'Nesta caixa de seleção: você precisa inserir a ocorrênica que irá realizar '
    help_setor = 'Nesta caixa de seleção: você precisa selecionar o setor do lider que fez a solicitação de 0.S '
    help_nivel_ocorrencia = 'Nesta caixa de seleção: você precida selecionar o grau de necessidade da ocorrência '
    helpe_acao = 'Nesta caixa de seleção: você precisa selecionar o tipo de açaõ da ocorrência solicitada'
    help_parada = 'Nesta caixa de seleção: você precisa informar se ouve uma interrupção no funcionamento do equipamento'
    help_especialidade = 'Nesta caixa de seleção: você precisa selecionar o tipo de atividade que irá ser aplicada com base na ocorrência'
    help_local = 'Nesta caixa de seleção: você preicsa selecionar o equipamento/local que irá realizar a manutenção'
    help_imagem = 'Nesta caixa de seleção: você precisa anexar uma imagem referente a ocorrência'
    help_imagem_fnlzd = 'Nesta caixa de seleção: você precisa anexar uma imagem após finalizar a ocorrencia'
    help_manutentor = 'Nesta caixa de seleção: você precisa selecionar o tipo de manutenção referente a sua ocorrência'
    help_numero_os = 'Nesta caixa de seleção: você precisa selecionar o numero da O.S que deseja ABRIR ou FINALIZAR'
    help_finalizar_os = 'Nesta caixa de seleção: você precisa selecionar entre SIM ou Não,SIM,para O.S finalizada,Não,para O.S aberta'
    solicitante_list = ['Bruno Kappaun','Cesar Filho','Jameson Sales','Maurilio Sales/Alex Santos','Adriely Lemos','Gilson Freitas','Willian Oliveira','Cesar Augusto','Filipe leite']
    setor_list = ['Tecnologia da Informação','Comercial','Expedição','Administrativo','Ferramentaria','Serralharia','Utilidades','Produção']
    ocorrencia_list = ['Emergência','Muito urgênte','Pouco urgênte','Urgênte']
    acao_list = ['Corretiva','Preventiva','Preditiva','Confecção','Montagem']
    especialidade_list = ['Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem','Limpeza']
    
    extrusão_list = ['Prensa - P8','Puller - 01','Puller - 02','Quench','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Forno de Ferramentas','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts']
    extrusão_list_â = ['Âmbito de extrusão','Prensa - P8','Puller - 01','Puller - 02','Quench','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Forno de Ferramentas','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts']

    estampo_list = ['Prensa Excêntrica - 01','Prensa Excêntrica - 02','Prensa Hidráulica = 03']
    estampo_list_â = ['Âmbito de estampo','Prensa Excêntrica - 01','Prensa Excêntrica - 02','Prensa Hidráulica = 03']
    
    corte = ['Serra Automatica','Serra Manual','Serra fita - FRANHO']
    corte_â = ['Âmbito de corte','Serra Automatica','Serra Manual','Serra fita - FRANHO']
    
    rosca_e_furo = ['Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02']
    rosca_e_furo_â = ['Âmbito de rosca e furo','Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02']
    
    embalagem = ['Embaladora Automatica','Seladora manual - KT001','Seladora manual - KT002']
    embalagem_â = ['Âmbito de embalagem','Embaladora Automatica','Seladora manual - KT001','Seladora manual - KT002']

    ti = ['Manutenção Predial','Suporte']
    ti_â = ['Âmbito da Tecnlogia da Informação','Manutenção Predial','Suporte']

    utilidades_list = ['Manutenção Predial','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone','Esgôto','Caixas pluviais']
    utilidades_list_â = ['Âmbito da Casa de Bombas','Âmbito da Caixa D.Agua','Âmbito da Subestação - 01','Âmbito da Subestação - 02','Âmbito do Portão de automoveis','Âmbito do Portão de pedestres','Âmbito do Interfone']
    
    comercial = ['Manutenção Predial']
    comercial_â = ['Âmbito do Comercial']

    administrativo = ['Manutenção Predial','Casa de Bombas','Caixa D.Agua','Portão de automoveis','Portão de pedestres','Interfone','Esgôto','Caixas pluviais']
    administrativo_â = ['Âmbito da Casa de Bombas','Âmbito da Caixa D.Agua','Âmbito do Portão de automoveis','Âmbito do Portão de pedestres','Âmbito do Interfone']

    ferramentaria_list = ['Manutenção Predial','Maquina de jatear','Talha Elétrica','Recuperação de ferramentas']
    ferramentaria_list_â = ['Âmbito da Ferramentaria','Âmbito da Maquina de jatear','Âmbito da Talha Elétrica']
        
    expedição = ['Manutenção Predial']
    expedição_â = ['Âmbito da Expedição']
    geral_list = ['Prensa - P8 - Puller - 1 - Puller - 2 - Esticadeira - HEAD - Esticadeira - TAIL - Forno de Tarugo - Serra Fria - Forno de Envelhecimento - Prensa Excentrica - 1 - Prensa Excentrica - 2 - Serra Automatica - Serra Manual - Serra fita - FRANHO - Rosqueadeira - MACHO 01 - Rosqueadeira - COSSINETE 01 - Rosqueadeira - COSSINETE 2 - Maquina de jatear - Talha Elétrica - Embaladora Automatica - Manutenção Predial - Artífice - Recuperação de ferramentas - Casa de Bombas - Caixa D.Agua - Subestação - 1 - Subestação - 2 -  Seladora manual - KT001 - Seladora manual - KT002 - Portão de automoveis - Portão de pedestres - Interfone']
    
    tabs_list = ["📝 Cadastro de O.S", " 🔚 Finalizar O.S","📖 O.S Em aberto","✅ O.S Finalizadas","☑ CheckList","👁 Geral"]
    tabs_list_sol = ["📝 Cadastro de O.S","📖 O.S Em aberto ","✅ O.S Finalizadas","👁 Geral"]
    tltle_list  = 'Status e informações de :blue[O.S]'
    header_list = '📝 Cadastro de :blue[O.S]'
    aviso_list = '👁 :blue[Geral]'
    abertas_list = '📖 O.S em aberto'
    finalizadas_list = "✅ O.S Finalizadas"

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

caminho_imagem = './Midia/empty.jpeg'
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
                st.title(tltle_list)
            tab6, tab7,tab8,tab9,tab10,tab11= st.tabs(tabs_list)
            with tab6:
                st.header(header_list,divider='blue')
                colibrim,neymar= st.columns([5,5])  
                with colibrim:
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln1 == 0:
                           numros = 0
                           numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln1,value=allln1,placeholder="Selecione!")
                            numros1 = numros-1
                            consulta1 = "SELECT * FROM ELETRICA"
                        ros_oc = pd.read_sql_query(consulta1, conn)

                        if not ros_oc.empty:
                            preenchimento = ros_oc.loc[numros1]
                            preenchimento = preenchimento.tolist()
                        else:
                            [None,None,None,None,None,None,None,None,None,None,None,None,None,None]
            
                    container = st.container(border=True)
                    if not atd1:
                        Rsolicitante = container.selectbox(solicitante_titulo, (solicitante_list),index=None,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, (solicitante_list),index=None,placeholder='Atualize!',help=help_solicitante)
                        
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, (setor_list),index=None,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                        
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl, (setor_list),index=None,placeholder='Atualize!',help=help_setor)
                        Rsetor = ''

                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, (ocorrencia_list),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,(ocorrencia_list),index=None, placeholder='Atualize!',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, (acao_list),index=None,placeholder='Selecione!',help=helpe_acao)
                        RUacao = ' '
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, (acao_list),index=None,placeholder='Atualize!',help=helpe_acao)
                        Racao = ' '

                    if Rsetor == 'Produção' or RUsetor == 'Produção':
                        if not atd1:
                            segmento = container.selectbox('Defina o segmento de produção:', ('Extrusão','Estampo','Corte','Rosca e Furo','Embalagem'),index=None,placeholder='Selecione!',help=help_setor)
                        if atd1:
                            segmento = container.selectbox('Atualize o segmento de produção:', ('Extrusão','Estampo','Corte','Rosca e Furo','Embalagem'),index=None,placeholder='Atualize!',help=help_setor)
                        if not segmento == None:
                            comb = (f'{Rsetor} {segmento} {Racao}')
                    else:
                        comb = (f'{Rsetor} {Racao}')
                    
                    if not atd1:
                        parada = container.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                    if atd1:
                        parada = container.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                    
                    if not atd1: 
                        especialidades = container.selectbox(especialidades_titulo, (especialidade_list),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl, (especialidade_list),index=None,placeholder='Atualize!',help=help_especialidade)
                    
                    if Rsetor == 'Produção' or RUsetor == 'Produção':
                        if not segmento == None:
                            if comb == 'Produção Extrusão Corretiva' or comb == 'Produção Extrusão Preventiva' or comb == 'Produção Extrusão Preditiva':
                                Local = container.selectbox(local_titulo,(extrusão_list),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Extrusão Confecção' or comb == 'Produção Extrusão Montagem':
                                Local = container.selectbox(local_titulo,(extrusão_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Estampo Corretiva' or comb == 'Produção Estampo Preventiva' or comb == 'Produção Estampo Preditiva':
                                Local = container.selectbox(local_titulo,(estampo_list),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Estampo Confecção' or comb == 'Produção Estampo Montagem':
                                Local = container.selectbox(local_titulo,(estampo_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Embalagem Corretiva' or comb == 'Produção Embalagem Preventiva' or comb == 'Produção Embalagem Preditiva':
                                Local = container.selectbox(local_titulo,(embalagem),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Embalagem Confecção' or comb == 'Produção Embalagem Montagem':
                                Local = container.selectbox(local_titulo,(embalagem_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Rosca e Furo Corretiva' or comb == 'Produção Rosca e Furo Preventiva' or comb == 'Produção Rosca e Furo Preditiva':
                                Local = container.selectbox(local_titulo,(rosca_e_furo),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Rosca e Furo Confecção' or comb == 'Produção Rosca e Furo Montagem':
                                Local = container.selectbox(local_titulo,(rosca_e_furo_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Corte Corretiva' or comb == 'Produção Corte Preventiva' or comb == 'Produção Corte Preditiva':
                                Local = container.selectbox(local_titulo,(corte),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Corte Confecção' or comb == 'Produção Corte Montagem':
                                Local = container.selectbox(local_titulo,(corte_â),index=None,placeholder= 'Selecione!',help=help_local) 
                        else:
                            Local = ''
                    else:
                        segmento = 'sem segmento'
                        if comb == 'Tecnologia da Informação Corretiva' or comb == 'Tecnologia da Informação Preventiva' or comb == 'Tecnologia da Informação Preditiva':
                            Local = container.selectbox(local_titulo,(ti),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Tecnologia da Informação Confecção' or comb == 'Tecnologia da Informação Montagem':
                            Local = container.selectbox(local_titulo,(ti_â),index=None,placeholder= 'Selecione!',help=help_local)
                        else:
                            Local = ' '

                        if comb == 'Administrativo Corretiva' or comb == 'Administrativo Preventiva' or comb == 'Administrativo Preditiva':
                            Local = container.selectbox(local_titulo,(administrativo),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Administrativo Confecção' or comb == 'Administrativo Montagem':
                            Local = container.selectbox(local_titulo,(administrativo_â),index=None,placeholder= 'Selecione!',help=help_local)
                        
                        if comb == 'Comercial Corretiva' or comb == 'Comercial Preventiva' or comb == 'Comercial Preditiva':
                            Local = container.selectbox(local_titulo,(comercial),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Comercial Confecção' or comb == 'Comercial Montagem':
                            Local = container.selectbox(local_titulo,(comercial_â),index=None,placeholder= 'Selecione!',help=help_local)
                        
                        if comb == 'Expedição Corretiva' or comb == 'Expedição Preventiva' or comb == 'Expedição Preditiva':
                            Local = container.selectbox(local_titulo,(expedição),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Expedição Confecção' or comb == 'Expedição Montagem':
                            Local = container.selectbox(local_titulo,(expedição_â),index=None,placeholder= 'Selecione!',help=help_local)

                        if comb == 'Ferramentaria Corretiva' or comb == 'Ferramentaria Preventiva' or comb == 'Ferramentaria Preditiva':
                            Local = container.selectbox(local_titulo,(ferramentaria_list),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Ferramentaria Confecção' or comb == 'Ferramentaria Montagem':
                            Local = container.selectbox(local_titulo,(ferramentaria_list_â),index=None,placeholder= 'Selecione!',help=help_local)

                        if comb == 'Utilidades Corretiva' or comb == 'Utilidades Preventiva' or comb == 'Utilidades Preditiva':
                            Local = container.selectbox(local_titulo,(utilidades_list),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Utilidades Confecção' or comb == 'Utilidades Montagem':
                            Local = container.selectbox(local_titulo,(utilidades_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                       
                    if atd1:
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        agree = container.checkbox('Selecione á caixa para enviar a imagem em outro momento:')
                        if agree:
                            uploaded_files = bytes_imagem
                            bytes_data = bytes_imagem
                        else:
                             uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=int(preenchimento[0]),value=int(preenchimento[0]),placeholder="Selecione!")
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
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem = ? WHERE id = ?",(bytes_data,numros))
                                    conn1.commit()
                                                                          
                            else:
                                omaga = [Rsolicitante,Rstatus,Rsetor,Rniveldaocorrencia,Racao,especialidades,Local,uploaded_files,parada]
                                bools = []
                                for busca in omaga:
                                    if not busca:
                                        bools.append(False)
                                    else:
                                        bools.append(True)

                                if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True and bools[6] == True and bools[7] == True and bools[8] == True:
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_elétrica = ids_shape + 1
                                        st.balloons()
                                        st.toast('Enviando O.S!')
                                        st.toast(f'O.S [{ids_shape_elétrica}] Enviada!')
                                        time.sleep(0.5)
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_elétrica,str(timenow),datenow,monthnow,Local))
                                        cursor.execute("INSERT INTO ELETRICA (OS,SOLICITANTE,SETOR,SEGMENTO,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,ESPECIALIDADE,LOCAL,MÊS,PARADA) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_elétrica , Rsolicitante, Rsetor,segmento,Rstatus,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,especialidades,Local,monthnow,parada))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_elétrica,bytes_data,monthnow))
                                        conn1.commit()
                                        st.rerun()
            #FINALIZAR                                 
            with tab7:
                st.header('🔚 Finalizar O.S ✔',divider='blue')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    containerx = st.container(border=True)
                    setorescolhido = containerx.selectbox('Setor', ('PCM','Tecnologia da Informação','Comercial','Administrativo','Expedição','Produção','Ferramentaria','Serralharia','Elétrica'),index=None,placeholder='Selecione!',help=help_solicitante)
                    fnlz2 = containerx.number_input("Selecione o numero da O.S que deseja Finalizar",min_value=1,max_value=1000,value=1,placeholder="Selecione!",help=help_numero_os)
                    fnlz3 = fnlz2-1
                    finalizar = containerx.selectbox('O.S finalizada?', ('Sim','Não'),index=None,placeholder='Selecione!',help=help_finalizar_os)
                    imagem_finalzida = containerx.file_uploader("Envie uma imagem da ocorrência finalizada:", accept_multiple_files=True)
                    for uploaded_file in imagem_finalzida:
                        imagem_finalzida_bytes = uploaded_file.read()
                    #datainput = containerx.date_input("Data", value=None)
                    #containerx.write(datainput)
                    #timeinput = containerx.time_input('HORA', value=None)
                    #containerx.write(timeinput)
    
                if fLIDERES == 'Equipe de ELÉTRICA':
                    if fSETOR == 'Elétrica':
                        if imagem_finalzida:
                            if setorescolhido == 'Ferramentaria':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Ferramentaria SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 

                            if setorescolhido == 'Elétrica':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE ELETRICA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 
                                    

                            if setorescolhido == 'Produção':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 
                            
                            if setorescolhido == 'Administrativo':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Administrativo SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 
                            
                            if setorescolhido == 'Comercial':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Comercial SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 

                            if setorescolhido == 'Expedição':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 

                            if setorescolhido == 'Serralharia':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Serralharia SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 

                            if setorescolhido == 'Tecnologia da Informação':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE TI SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 

                            if setorescolhido == 'PCM':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor14.execute("UPDATE PCM SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(imagem_finalzida_bytes,fnlz2))
                                    conn1.commit() 
            #ABERTAS
            with tab8:
                st.header('📝 O.S em Aberto', divider='blue')
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    with st.expander("Filtros"):
                        genre = st.radio(
                          "Selecione!",
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
                            numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione!")
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
                            numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=whrlinhas2,value=whrlinhas2,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da k OS",min_value=1,max_value=pcm_id,value=pcm_id,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=rd28,value=rd28,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero   da   OS",min_value=1,max_value=rd34,value=rd34,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione   o  numero   da   OS",min_value=1,max_value=rd42,value=rd42,placeholder="Selecione!")
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
                            numros4 = st.number_input(" Selecione   o  numero   da   OS",min_value=1,max_value=rd50,value=rd50,placeholder="Selecione!")
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
                            numros4 = st.number_input("  Selecione   o  numero   da   OS",min_value=1,max_value=rd58,value=rd58,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da O.S                                ",min_value=1,max_value=rd66,value=rd66,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS          ",min_value=1,max_value=rd79,value=rd79,placeholder="Selecione!")
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
                st.header('✅ O.S Finalizadas', divider='blue')
                jam,jam1 = st.columns([0.2,1])
                with jam:
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
                            numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=whrlinhas4,value=whrlinhas4,placeholder="Selecione!")
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
                            numros2 = st.number_input("Selecione o numero da            OS",min_value=1,max_value=whrlinhas4,value=whrlinhas4,placeholder="Selecione!")
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
                            numros4 = st.number_input(" Selecione  o numero da    OS",min_value=1,max_value=pcm_id1,value=pcm_id1,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione  o  numero  da  OS ",min_value=1,max_value=rd32,value=rd32,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS  ",min_value=1,max_value=rd38,value=rd38,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS    ",min_value=1,max_value=rd46,value=rd46,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS     ",min_value=1,max_value=rd54,value=rd54,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS        ",min_value=1,max_value=rd62,value=rd62,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS         ",min_value=1,max_value=rd70,value=rd70,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS            ",min_value=1,max_value=rd75,value=rd75,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value=rd75)
                            numros5 = numros4-1
                            osespec = rd74.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width28")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width28)
            #CHECKLIST
            with tab10:
                col,col1,col2 = st.columns([0.5,1,0.5])
                with col:
                    with st.expander("",expanded=1):
                        st_ = st.container(border=True)
                        st.header(':blue[Localidade 🚩] ',divider='blue')
                        quadro =st.radio(
                        "Selecione",
                        ['Quadro A01-A04 (PRENSA P8)','Quadro DA1-DA6 (PULLER E ESTICADEIRA)','Quadro AA1-AA3 (FORNO DE TARUGO)','Quadro EA1-EA4 (SERRA E INCESTADOR)','Quadro FA1-FA3 (FORNO DE ENVELHECIMENTO)'],
                        index=0,
                        ) 
                        
                    with st.expander("",expanded=1):
                        st_3 = st.container(border=True)
                        st.header(':blue[Situação 🔎] ',divider='blue')
                        estado =st.radio(
                        "Selecione",
                        ['Equipamento em bom estado e em funcionamento!','Substituição de componente necessaria!','Equipamento danificado mas em funcionamento!'],
                        index=0,
                        )
                    
                    with st.expander("",expanded=1):
                        if estado == 'Substituição de componente necessaria!':
                            mat = pd.read_sql_query("SELECT * FROM Materiais", conn12)
                            mat_shape = mat.shape[0]
                            
                            def example_one():
                                filtered_df = dataframe_explorer(mat, case=False)
                                st.dataframe(filtered_df, use_container_width=True)
                            example_one()               
               
                with col2:
                    with st.expander("",expanded=1):
                        st_1 = st.container(border=True)
                        st.header(':blue[Equipamento ⚙]',divider='blue')
                        equipamento = st.radio(
                        "Selecione",
                        ['Motores','Sensores','Contatores','Botões','Relerés','Disjuntores','Controladores','Fontes','Transformadores','Inversores de frequência','Porta fusiveis','Cilindros hidraulicos','Cilindros pneumaticos','Valvulas hidraulicas','Valvulas pneumaticas'],
                        index=0,
                        )
                    with st.expander("",expanded=1):
                        mat = pd.read_sql_query(f"SELECT * FROM checkList WHERE Equipamento = '{equipamento}' AND Local = '{quadro}'", conn)
                        mat_shape = mat.shape[0]
                        def example_one():
                            filtered_df = dataframe_explorer(mat, case=False)
                            st.dataframe(filtered_df, use_container_width=True)
                        example_one()
                    
                    if 'strs' == 'strs':
                        if equipamento == 'Motores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Limpeza:'
                            tltle_3 = 'Inspeção das Condições Ambientais:'
                            tltle_4 = 'Lubrificação:'
                            tltle_5 = 'Teste de Isolamento:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_8 = 'Teste de Funcionamento:'
                            tltle_9 = 'Calibração (se aplicável):'
                
                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de danos externos, como rachaduras, amassados ou corrosão no invólucro do :blue[motor] Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'
                            errorfull_2 = '° Limpar qualquer sujeira, poeira ou detritos acumulados no :blue[motor] que possam interferir em seu funcionamento.Utilizar produtos de limpeza adequados que não danifiquem o :blue[motor]'
                            errorfull_3 = '° Verificar se o :blue[motor] está instalado em um ambiente adequado em termos de temperatura, umidade e exposição a elementos corrosivos.'
                            errorfull_4 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_5 = '° Realizar testes de resistência de isolamento para garantir que não haja curtos-circuitos ou falhas nos enrolamentos do :blue[motor].'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar a tensão e a corrente de operação do :blue[motor] para garantir que estejam dentro dos limites especificados pelo fabricante.'
                            errorfull_8 = '° Ligar brevemente o :blue[motor] para garantir que ele inicie suavemente e funcione sem ruídos ou vibrações anormais.Verificar se todos os sistemas de proteção (como :blue[disjuntor]es e relés térmicos) estão funcionando corretamente.'
                            errorfull_9 = '° Verificar se os dispositivos de controle e medição associados ao equipamento estão devidamente calibrados e funcionando corretamente.'
                        elif equipamento == 'Sensores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Limpeza:'
                            tltle_3 = 'Inspeção das Condições Ambientais:'
                            tltle_4 = 'Verificação da Precisão e Sensibilidade:'
                            tltle_5 = 'Verificação da Conexão e Comunicação:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_8 = 'Teste de Funcionamento:'
                            tltle_9 = 'Calibração (se aplicável):'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de danos externos, como rachaduras, amassados ou corrosão no invólucro do :blue[Sensor] Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'
                            errorfull_2 = '° Limpar qualquer sujeira, poeira ou detritos acumulados no :blue[Sensor] que possam interferir em seu funcionamento.Utilizar produtos de limpeza adequados que não danifiquem o :blue[Sensor]'
                            errorfull_3 = '° Verificar se o :blue[Sensor] está instalado em um ambiente adequado em termos de temperatura, umidade e exposição a elementos corrosivos.'
                            errorfull_4 = '° Testar a precisão e sensibilidade do :blue[Sensor] em detectar variações ou mudanças nas condições medidas.Comparar as leituras do :blue[Sensor] com padrões conhecidos ou outras :blue[fontes confiáveis de] dados, quando disponíveis.'
                            errorfull_5 = '° Testar a conexão física do :blue[Sensor] com o sistema de monitoramento ou controle.Verificar se a comunicação entre o :blue[Sensor] e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar se o :blue[Sensor] está recebendo a alimentação adequada de acordo com as especificações do fabricante.Testar a integridade do circuito de alimentação e identificar e corrigir quaisquer problemas de fornecimento de energia.'
                            errorfull_8 = '° Realizar testes funcionais para verificar se o :blue[Sensor] está respondendo corretamente aos estímulos ou condições que ele é projetado para detectar.Verificar se os sinais de saída do :blue[Sensor] estão dentro dos limites esperados e se correspondem às condições reais.'
                            errorfull_9 = '° Verificar se o :blue[Sensor] está calibrado corretamente de acordo com as especificações do fabricante.Realizar calibrações periódicas conforme recomendado pelo fabricante ou conforme necessário com base nos resultados das medições.'
                        elif equipamento == 'Contatores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Verificação dos Contatos'
                            tltle_3 = 'Verificação dos Mecanismos de Acionamento'
                            tltle_4 = 'Verificação das Bobinas:'
                            tltle_5 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação dos Dispositivos de Proteção:'
                            tltle_8 = 'Verificação da Conexão e Comunicação:'
                            tltle_9 = 'Aperto dos Terminais e Conexões:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Contator].Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'

                            errorfull_2 = '° Inspecionar os contatos do :blue[Contator] quanto a sinais de desgaste, queimaduras, corrosão ou pontos de solda.Limpar os contatos, se necessário, para remover quaisquer depósitos ou acumulações que possam interferir no funcionamento.'
                            errorfull_3 = '° Testar o mecanismo de acionamento do :blue[Contator] para garantir que esteja operando suavemente e sem obstruções.Verificar se não há pontos de travamento ou desalinhamento no mecanismo.'
                            errorfull_4 = '° Verificar a integridade e a resistência das bobinas do :blue[Contator].Testar a operação das bobinas para garantir que estejam funcionando corretamente e respondendo aos comandos de acionamento.'
                            errorfull_5 = '° Verificar se a tensão e a corrente de operação do :blue[Contator] estão dentro dos limites especificados pelo fabricante.Testar o :blue[Contator] em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar se os dispositivos de proteção, como :blue[disjuntor]es ou fusíveis, estão instalados e funcionando corretamente para proteger o :blue[Contator] e o circuito contra sobrecargas ou curtos-circuitos.'
                            errorfull_8 = '° Testar a conexão física do :blue[Contator] com o sistema de controle ou circuito.Verificar se a comunicação entre o :blue[Contator] e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_9 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'                          
                        elif equipamento == 'Botões':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação do Funcionamento:'
                            tltle_3 = 'Verificação das Conexões:'
                            tltle_4 = 'Verificação da Iluminação:'
                            tltle_5 = 'Verificação da Vedação:'
                            tltle_6 = 'Verificação da Durabilidade:'
                            tltle_7 = 'Ajuste da Sensibilidade:'
                            tltle_8 = 'Verificação da Fixação:'
                            tltle_9 = 'Teste de Funcionamento Geral:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no botão. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no botão, evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar o funcionamento do botão, garantindo que pressioná-lo acione o comando desejado de forma consistente.'
                            errorfull_3 = '° Verificar todas as conexões do botão quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_4 = '° Verificar a iluminação do botão, se aplicável, garantindo que esteja funcionando corretamente.'
                            errorfull_5 = '° Verificar a vedação do botão, garantindo que esteja intacta para proteger contra poeira e umidade.'
                            errorfull_6 = '° Verificar a durabilidade do botão, avaliando sua resistência ao uso repetido ao longo do tempo.'
                            errorfull_7 = '° Ajustar a sensibilidade do botão, se aplicável, para garantir que o acionamento ocorra com a pressão adequada.'
                            errorfull_8 = '° Verificar a fixação do botão, garantindo que esteja firmemente instalado e sem folgas.'
                            errorfull_9 = '° Realizar um teste de funcionamento geral do botão, garantindo que ele opere corretamente em todas as condições de uso.'
                        elif equipamento == 'Relerés':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Verificação dos Contatos'
                            tltle_3 = 'Verificação dos Mecanismos de Acionamento'
                            tltle_4 = 'Verificação das Bobinas:'
                            tltle_5 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação dos Dispositivos de Proteção:'
                            tltle_8 = 'Verificação da Conexão e Comunicação:'
                            tltle_9 = 'Aperto dos Terminais e Conexões:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Relé].Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'
                            errorfull_2 = '° Inspecionar os contatos do :blue[Relé] quanto a sinais de desgaste, queimaduras, corrosão ou pontos de solda.Limpar os contatos, se necessário, para remover quaisquer depósitos ou acumulações que possam interferir no funcionamento.'
                            errorfull_3 = '° Testar o mecanismo de acionamento do :blue[Relé] para garantir que esteja operando suavemente e sem obstruções.Verificar se não há pontos de travamento ou desalinhamento no mecanismo.'
                            errorfull_4 = '° Verificar a integridade e a resistência das bobinas do :blue[Relé].Testar a operação das bobinas para garantir que estejam funcionando corretamente e respondendo aos comandos de acionamento.'
                            errorfull_5 = '° Verificar se a tensão e a corrente de operação do :blue[Relé] estão dentro dos limites especificados pelo fabricante.Testar o :blue[Relé] em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar se os dispositivos de proteção, como :blue[disjuntor]es ou fusíveis, estão instalados e funcionando corretamente para proteger o :blue[Relé] e o circuito contra sobrecargas ou curtos-circuitos.'
                            errorfull_8 = '° Testar a conexão física do :blue[Relé] com o sistema de controle ou circuito.Verificar se a comunicação entre o :blue[Relé] e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_9 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'
                        elif equipamento == 'Disjuntores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação da Tensão Nominal:'
                            tltle_4 = 'Teste de Funcionamento:'
                            tltle_5 = 'Verificação do Disparador:'
                            tltle_6 = 'Verificação do Mecanismo de Atuação:'
                            tltle_7 = 'Teste de Proteção contra Sobrecarga:'
                            tltle_8 = 'Teste de Proteção contra Curto-Circuito:'
                            tltle_9 = 'Teste de Proteção contra Falta à Terra:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[disjuntor]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[disjuntor], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões do :blue[disjuntor] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar se a tensão nominal do :blue[disjuntor] está de acordo com as especificações do equipamento. Substituir o :blue[disjuntor] se a tensão estiver fora dos limites especificados.'
                            errorfull_4 = '° Realizar um teste de funcionamento completo no :blue[disjuntor], incluindo abertura e fechamento sob carga. Verificar se o :blue[disjuntor] opera corretamente em todas as condições.'
                            errorfull_5 = '° Verificar o funcionamento do disparador do :blue[disjuntor], garantindo que ele atue adequadamente em caso de sobrecarga ou curto-circuito.'
                            errorfull_6 = '° Verificar o mecanismo de atuação do :blue[disjuntor], assegurando que ele opere suavemente e sem travamentos.'
                            errorfull_7 = '° Realizar um teste de proteção contra sobrecarga, aplicando uma corrente ligeiramente acima da corrente nominal para verificar se o :blue[disjuntor] interrompe a corrente conforme esperado.'
                            errorfull_8 = '° Realizar um teste de proteção contra curto-circuito, aplicando uma corrente muito alta para verificar se o :blue[disjuntor] interrompe a corrente rapidamente e de forma segura.'
                            errorfull_9 = '° Realizar um teste de proteção contra falta à terra, simulando uma falta à terra para verificar se o :blue[disjuntor] atua corretamente e interrompe a corrente.'
                        elif equipamento == 'Controladores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação dos Cartões de E/S:'
                            tltle_4 = 'Verificação da Alimentação:'
                            tltle_5 = 'Verificação dos Programas:'
                            tltle_6 = 'Backup dos Programas:'
                            tltle_7 = 'Teste de Comunicação:'
                            tltle_8 = 'Teste de Entradas e Saídas:'
                            tltle_9 = 'Teste de Funcionamento Geral:'

                            sucessfull = f'Concluído a {tltle}'
                            sucessfull_1 = f'Concluído a {tltle_1}'
                            sucessfull_2 = f'Concluído a {tltle_2}'
                            sucessfull_3 = f'Concluído a {tltle_3}'
                            sucessfull_4 = f'Concluído a {tltle_4}'
                            sucessfull_5 = f'Concluído a {tltle_5}'
                            sucessfull_6 = f'Concluído o {tltle_6}'
                            sucessfull_7 = f'Concluído o {tltle_7}'
                            sucessfull_8 = f'Concluído o {tltle_8}'
                            sucessfull_9 = f'Concluído o {tltle_9}'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no controlador lógico programável (:blue[CLP]). Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[CLP], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões do :blue[CLP] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar os cartões de entrada e saída (E/S) do :blue[CLP], garantindo que estejam corretamente instalados e sem sinais de danos.'
                            errorfull_4 = '° Verificar a alimentação do :blue[CLP], garantindo que a tensão de entrada esteja dentro dos limites especificados e que não haja flutuações de tensão.'
                            errorfull_5 = '° Verificar os programas armazenados no :blue[CLP], assegurando que estejam corretamente carregados e sem erros de programação.'
                            errorfull_6 = '° Realizar um backup dos programas armazenados no :blue[CLP], garantindo que haja uma cópia de segurança em caso de perda de dados.'
                            errorfull_7 = '° Realizar um teste de comunicação com o :blue[CLP], garantindo que seja possível estabelecer comunicação e fazer upload/download de programas.'
                            errorfull_8 = '° Realizar um teste de entradas e saídas do :blue[CLP], garantindo que todas as entradas e saídas estejam operando corretamente conforme especificado no programa.'
                            errorfull_9 = '° Realizar um teste de funcionamento geral do :blue[CLP], incluindo a execução do programa e verificação do comportamento do sistema controlado.'
                        elif equipamento == 'Fontes':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação da Tensão de Saída:'
                            tltle_4 = 'Verificação da Corrente de Saída:'
                            tltle_5 = 'Verificação da Estabilidade:'
                            tltle_6 = 'Verificação da Proteção contra Surtos:'
                            tltle_7 = 'Teste de Proteção:'
                            tltle_8 = 'Teste de Sobrecarga:'
                            tltle_9 = 'Teste de Funcionamento Geral:'

                            sucessfull = f'Concluído a {tltle}'
                            sucessfull_1 = f'Concluído a {tltle_1}'
                            sucessfull_2 = f'Concluído a {tltle_2}'
                            sucessfull_3 = f'Concluído a {tltle_3}'
                            sucessfull_4 = f'Concluído a {tltle_4}'
                            sucessfull_5 = f'Concluído a {tltle_5}'
                            sucessfull_6 = f'Concluído a {tltle_6}'
                            sucessfull_7 = f'Concluído o {tltle_7}'
                            sucessfull_8 = f'Concluído o {tltle_8}'
                            sucessfull_9 = f'Concluído o {tltle_9}'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos na :blue[fonte de alimentação]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular na :blue[fonte de alimentação], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões da :blue[fonte de alimentação] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar a tensão de saída da :blue[fonte de alimentação], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_4 = '° Verificar a corrente de saída da :blue[fonte de alimentação], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_5 = '° Verificar a estabilidade da :blue[fonte de alimentação], garantindo que não haja flutuações significativas na tensão ou corrente de saída.'
                            errorfull_6 = '° Verificar a proteção contra surtos da :blue[fonte de alimentação], garantindo que esteja funcionando corretamente para proteger o equipamento conectado contra picos de tensão.'
                            errorfull_7 = '° Realizar um teste de proteção da :blue[fonte de alimentação], garantindo que ela atue corretamente em caso de sobretensão, subtensão ou curto-circuito.'
                            errorfull_8 = '° Realizar um teste de sobrecarga na :blue[fonte de alimentação], aplicando uma carga maior que a nominal para verificar se ela continua operando dentro dos limites especificados.'
                            errorfull_9 = '° Realizar um teste de funcionamento geral da :blue[fonte de alimentação], garantindo que ela opere corretamente em todas as condições de carga e temperatura.'
                        elif equipamento == 'Transformadores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação da Tensão Primária:'
                            tltle_4 = 'Verificação da Tensão Secundária:'
                            tltle_5 = 'Verificação dos Enrolamentos:'
                            tltle_6 = 'Teste de Isolação:'
                            tltle_7 = 'Teste de Resistência de Isolamento:'
                            tltle_8 = 'Verificação do Resfriamento:'
                            tltle_9 = 'Teste de Funcionamento:'

                            sucessfull = f'Concluído a {tltle}'
                            sucessfull_1 = f'Concluído a {tltle_1}'
                            sucessfull_2 = f'Concluído a {tltle_2}'
                            sucessfull_3 = f'Concluído a {tltle_3}'
                            sucessfull_4 = f'Concluído a {tltle_4}'
                            sucessfull_5 = f'Concluído a {tltle_5}'
                            sucessfull_6 = f'Concluído o {tltle_6}'
                            sucessfull_7 = f'Concluído o {tltle_7}'
                            sucessfull_8 = f'Concluído a {tltle_8}'
                            sucessfull_9 = f'Concluído o {tltle_9}'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[transformador]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[transformador], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões do :blue[transformador] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar a tensão primária do :blue[transformador], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_4 = '° Verificar a tensão secundária do :blue[transformador], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_5 = '° Verificar os enrolamentos do :blue[transformador] quanto a sinais de danos, superaquecimento ou desgaste excessivo.'
                            errorfull_6 = '° Realizar um teste de isolação no :blue[transformador] para verificar se há algum curto-circuito ou falha no isolamento.'
                            errorfull_7 = '° Realizar um teste de resistência de isolamento para verificar a resistência entre os enrolamentos e o chassi do :blue[transformador].'
                            errorfull_8 = '° Verificar o sistema de resfriamento do :blue[transformador], garantindo que os radiadores ou ventiladores estejam funcionando corretamente.'
                            errorfull_9 = '° Realizar um teste de funcionamento completo do :blue[transformador], garantindo que ele opere corretamente em todas as condições de carga e temperatura.'
                        elif equipamento == 'Inversores de frequência':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação dos Parâmetros:'
                            tltle_3 = 'Verificação dos Cabos e Conexões:'
                            tltle_4 = 'Verificação da Ventilação:'
                            tltle_5 = 'Verificação dos Enrolamentos do :blue[Motor]:'
                            tltle_6 = 'Verificação da Tensão e Corrente de Saída:'
                            tltle_7 = 'Verificação dos Dispositivos de Proteção:'
                            tltle_8 = 'Verificação da Conexão e Comunicação:'
                            tltle_9 = 'Aperto dos Terminais e Conexões:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Inversor].Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Remova qualquer sujeira, poeira ou detritos que possam acumular no :blue[Inversor] e interferir em seu funcionamento.Use ar comprimido ou um pano limpo e seco para limpar o :blue[Inversor] , evitando o uso de produtos químicos que possam danificar os componentes.'
                            errorfull_2 = '° Verifique os parâmetros de operação do :blue[Inversor]  para garantir que estejam configurados conforme as especificações do fabricante e os requisitos de aplicação.Faça ajustes nos parâmetros, se necessário, para otimizar o desempenho do inversor ou corrigir problemas de operação.'
                            errorfull_3 = '° Inspecione os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou problemas de conexão.Aperte quaisquer terminais soltos ou conexões frouxas para garantir uma conexão elétrica segura.'
                            errorfull_4 = '° Verifique se os ventiladores ou sistemas de resfriamento do :blue[Inversor]  estão funcionando corretamente.Limpe os filtros de ar ou ventiladores obstruídos para garantir uma boa circulação de ar e evitar o superaquecimento.'
                            errorfull_5 = '° Verifique os enrolamentos do :blue[motor] conectado ao :blue[Inversor]  quanto a sinais de superaquecimento, danos ou desgaste excessivo.Meça a temperatura dos enrolamentos durante a operação para identificar problemas de sobreaquecimento.'
                            errorfull_6 = '° Meça a tensão e a corrente de saída do :blue[Inversor] para garantir que estejam dentro dos limites especificados pelo fabricante.Teste o :blue[Inversor]  em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_7 = '° Verificar se os dispositivos de proteção, como :blue[disjuntor]es ou fusíveis, estão instalados e funcionando corretamente para proteger o :blue[Inversor]  e o circuito contra sobrecargas ou curtos-circuitos.'
                            errorfull_8 = '° Testar a conexão física do :blue[Inversor]  com o sistema de controle ou circuito.Verificar se a comunicação entre o :blue[Inversor]  e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_9 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'
                        elif equipamento == 'Porta fusiveis':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação da Continuidade:'
                            tltle_3 = 'Verificação da Tensão e Corrente de Saída:'
                            tltle_4 = 'Verificação dos Terminais:'
                            tltle_5 = 'Aperto dos Terminais e Conexões:'
                            tltle_6 = 'Teste de Funcionamento:'
                            tltle_7 = 'Verificação da Compatibilidade dos Fusíveis:'
                            tltle_8 = 'Verificação da Conexão à Terra:'
                            tltle_9 = 'Verificação da Proteção contra Surtos:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Porta fusiveis]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Remova qualquer sujeira, poeira ou detritos que possam acumular no :blue[Porta fusiveis] e interferir em seu funcionamento. Use ar comprimido ou um pano limpo e seco para limpar o :blue[Porta fusiveis], evitando o uso de produtos químicos que possam danificar os componentes.'
                            errorfull_2 = '° Verifique a continuidade dos contatos do :blue[Porta fusiveis] para garantir que estejam em boas condições de funcionamento. Substitua os fusíveis quebrados ou danificados conforme necessário.'
                            errorfull_3 = '° Meça a tensão e a corrente de saída do :blue[Porta fusiveis] para garantir que estejam dentro dos limites especificados pelo fabricante.Teste o :blue[Porta fusiveis] em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_4 = '° Verifique os terminais do :blue[Porta fusiveis] quanto a sinais de desgaste, corrosão ou folga. Aperte quaisquer terminais soltos para garantir uma conexão elétrica segura.'
                            errorfull_5 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'
                            errorfull_6 = '° Realizar testes de funcionamento no :blue[Porta fusiveis] para garantir sua operação adequada.'
                            errorfull_7 = '° Verifique se os fusíveis utilizados são compatíveis com as especificações do equipamento protegido.'
                            errorfull_8 = '° Verificar se a conexão à terra do :blue[Porta fusiveis] está correta e em boas condições.'
                            errorfull_9 = '° Verificar se o :blue[Porta fusiveis] possui proteção contra surtos adequada para proteger os equipamentos conectados contra picos de tensão.'
                        elif equipamento == 'Cilindros hidraulicos':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Cilindro hidraulico]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Cilindro hidraulico], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Cilindro hidraulico] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Cilindro hidraulico] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Cilindro hidraulico] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Cilindro hidraulico] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Cilindro hidraulico] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Cilindro hidraulico] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                        elif equipamento == 'Cilindros pneumaticos':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Cilindro pneumatico]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Cilindro pneumatico], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Cilindro pneumatico] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Cilindro pneumatico] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Cilindro pneumatico] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Cilindro pneumatico] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Cilindro pneumatico] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Cilindro pneumatico] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                        elif equipamento == 'Valvulas hidraulicas':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Valvulas hidraulicas]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Valvulas hidraulicas], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Valvulas hidraulicas] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Valvulas hidraulicas] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Valvulas hidraulicas] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Valvulas hidraulicas] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Valvulas hidraulicas] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Valvulas hidraulicas] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                        elif equipamento == 'Valvulas pneumaticas':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Valvulas pneumaticas]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Valvulas pneumaticas], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Valvulas pneumaticas] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Valvulas pneumaticas] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Valvulas pneumaticas] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Valvulas pneumaticas] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Valvulas pneumaticas] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Valvulas pneumaticas] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                    
                with col1:
                    with st.expander("",expanded=1):
                        st.header(':blue[CheckList 📋]',divider='blue')
                        check_9 =st.text_input('T.A.G de referência do equipamento:')
                        componente = (f'{check_9} pertence a {equipamento}')
                        check = st.checkbox(tltle)
                        if check:
                            st.success(sucessfull)
                        else:
                            st.error(errorfull)
                    
                        check_1 =st.checkbox(tltle_1)
                        if check_1:
                            st.success(sucessfull_1)
                        else:
                            st.error(errorfull_1)
                        
                        check_1_2 =st.checkbox(tltle_2)
                        if check_1_2:
                            st.success(sucessfull_2)
                        else:
                            st.error(errorfull_2)
                        
                        check_2 =st.checkbox(tltle_3)
                        if check_2:
                            st.success(sucessfull_3)
                            if equipamento == 'Disjuntores' or equipamento == 'Fontes' or equipamento == 'Transformadores':
                                col,col1,col2 = st.columns([1,1,3])
                                with col:
                                    st.number_input('Especifique a tensão (V): ',value=0.0,step=0.1)
                            if equipamento == 'Porta fusiveis':
                                col,col1,col2 = st.columns([1,1,5])
                                with col:
                                    st.number_input('Especifique a corrente (A):',value=0.0,step=0.1)
                                with col1:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                            if  equipamento == 'Cilindros hidraulicos' or equipamento == 'Cilindros pneumaticos'or equipamento =='Valvulas hidraulicas'or equipamento =='Valvulas pneumaticas':
                                col,col1,col2 = st.columns([1,1,3])
                                with col:
                                    st.number_input('Especifique a pressão (BAR/PSI):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_3)
                        check_3 =st.checkbox(tltle_4)
                        if check_3:
                            st.success(sucessfull_4)
                            if equipamento == 'Controladores' or equipamento == 'Transformadores':
                                col,col1,col2 = st.columns([1,1,3])
                                with col:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_4)
                        check_4 =st.checkbox(tltle_5)
                        if check_4:
                            st.success(sucessfull_5)
                            if equipamento == 'Contatores' or equipamento == 'Relerés':
                                col,col1,col2 = st.columns([1,1,5])
                                with col:
                                    st.number_input('Especifique a corrente (A):',value=0.0,step=0.1)
                                with col1:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_5)
                            
                        if not equipamento == 'Contatores' and not equipamento == 'Relerés'and not equipamento == 'Inversores de frequência' and not equipamento == 'Porta fusiveis' and not equipamento == 'Sensores':
                            check_5 =st.checkbox(tltle_6)
                            if check_5:
                                st.success(sucessfull_6)
                            else:
                                st.error(errorfull_6 )
                        
                        check_6 =st.checkbox(tltle_7)
                        if check_6:
                            st.success(sucessfull_7)
                            if equipamento == 'Motores' or equipamento == 'Sensores':
                                col,col1,col2 = st.columns([1,1,5])
                                with col:
                                    st.number_input('Especifique a corrente (A):',value=0.0,step=0.1)
                                with col1:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_7)
                        
                        check_7 =st.checkbox(tltle_8)
                        if check_7:
                            st.success(sucessfull_8)
                        else:
                            st.error(errorfull_8)

                        check_8 =st.checkbox('Calibração (se aplicável):')
                        if check_8:
                            st.success(sucessfull_9)
                        else:
                            st.error(errorfull_9)
                        check_10 =st.text_area('Registro de Manutenção:')
                        
                        if not equipamento == 'Contatores' and not equipamento == 'Relerés'and not equipamento == 'Inversores de frequência' and not equipamento == 'Porta fusiveis' and not equipamento == 'Sensores':
                            checkslists = [check_1,check_1_2,check_2,check_3,check_4,check_5,check_6,check_7,check_8,check_9,check_10]
                            tst = all(checkslists)
                            
                        else:
                            checkslists = [check_1,check_1_2,check_2,check_3,check_4,check_6,check_7,check_8,check_9,check_10]
                            tst = all(checkslists)
                        
                        if tst:
                            envio = st.button('(⌐■_■)')
                            if envio:
                                cursor.execute("INSERT INTO checklist (Tag,Local,Equipamento,Situação,Check_1,Check_2,Check_3,Check_4,Check_5,Check_6,Check_7,Check_8,Check_9,Relatorio,Hora,Data,Mês) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)", (check_9,quadro,equipamento,estado,(f'{tltle} Concluido'),(f'{tltle_1} Concluido'),(f'{tltle_2} Concluido'),(f'{tltle_3} Concluido'),(f'{tltle_4} Concluido'),(f'{tltle_5} Concluido'),(f'{tltle_6} Concluido'),(f'{tltle_7} Concluido'),(f'{tltle_8} Concluido'),(f'{tltle_9} Concluido'),timenow,datenow,monthnow))
                                conn.commit()                 
            #GERAL                          
            with tab11:
                st.header (aviso_list,divider='blue')
                omaga = st.multiselect('Selecione:',acao_list,max_selections=1)
                if not omaga == []:
                    corretivas = pd.read_sql_query(f"SELECT * FROM ELETRICA WHERE AÇÃO = '{omaga[0]}'", conn)
                    corretivas_shape = corretivas.shape[0]
                if omaga == []:
                    st.success('Escolha um tipo de ação')
                else:
                    if corretivas_shape == 0:
                        st.success('Não há pendências')
                    else:
                        corretivas = pd.read_sql_query(f"SELECT * FROM MECANICA WHERE AÇÃO = '{omaga[0]}'", conn)
                        corretivas_shape = corretivas.shape[0]
                        st.metric(label="O.S Existentes", value=corretivas_shape)
                        numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=corretivas_shape,value=corretivas_shape,placeholder="Selecione!")
                        numros3 = numros2-1
                        serie_pdf = corretivas.loc[numros3]
                        def load_data():
                            return pd.DataFrame(serie_pdf)
                        st.checkbox("Estender", value=True, key="use_container_width17")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width17)
                        dt = corretivas.loc[numros3]
                        dt = dt.tolist()
        
                        with open(f"./Data/geral_Elétrica.pdf", 'rb') as file:
                            pdf_reader = PyPDF2.PdfReader(file)
                            bttn = st.download_button(
                            label="Exportar O.S 🖨",
                            key= "download_button",
                            data= file,
                            file_name=f"O.S {dt[0]}.pdf",
                            mime='application/octet-stream'
                        )
                        usuario = 'Elétrica'
                        cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                        if cursor1.fetchall():
                            cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                            imagens = cursor1.fetchall()
                            imagens
                            oe = imagens[0][1]
                            imagem = Image.open(BytesIO(oe))

                        localx = corretivas.loc[numros3]
                        pmg = localx.tolist()
                        Solicitante = solicitante_titulo
                        Data = 'Data:'
                        Hora = 'Horario:'
                        Setor = 'Setor:'
                        Os = 'O.S:'
                        maqx = local_titulo
                        dados = [Solicitante,Data,Hora,Setor,Os,maqx,'']
                        img = Image.open('./Midia/ssmm.jpg')
                        img1 = Image.open('./Midia/sales.jpeg')

                        def hello(c,pmg):
                            o = 0
                            b = []
                            for s in str(pmg[1]):
                                if s.isalpha():
                                    o += 1
                                    tmh = 4 * o + 58 
                                    b.append(tmh)

                            ct = []
                            for s in str(pmg[2]):
                                if not pmg[2] =='Produção':
                                    if s.isalpha():
                                        o += 1
                                        tmh = 4 * o + 268
                                        ct.append(tmh)
                                    else:
                                        ''
                            idx = 0             
                            for james in dados:
                                idx = idx + 1
                                largura_da_linha = 0.1
                                width, height = 580, 50
                                raio = 10
                                if idx == 1:
                                #SOLICITANTE
                                    t1,t2 = 15,730
                                    t3,t4 = 58,730
                                    t5,t6 = 20,662
                                    t7,t8 = 380,662
                                    t9,t10 = 500,210
                                    t11,t12 = 90,642

                                    texto = f'{pmg[1]}'
                                    text = f'{pmg[5]}'
                                    textox = 'Grau de ocorrência :'
                                    textoxx = 'Especialidade :'
                                    textos = ''
                                    x1, y1 = b[9], 728
                                    x2, y2 = 58, 728
                                    widt, heigh = 200, 30
                                    r,r1 = 18,630
                                    r2,r3 = 380,630
                                    k1,k2,k3,k4 = 250,680,250,420
                                if idx == 2:
                                #DAT
                                    t1,t2 = 15,705
                                    t3,t4 = 38,705
                                    t5,t6 = 18,583
                                    t7,t8 = 380,583
                                    t9,t10 = 500,210
                                    t11,t12 = 90,563

                                    texto = f'{pmg[6]}'
                                    text = f'{pmg[8]}'
                                    textox = 'Ação :'
                                    textoxx = 'Data de finalização :'
                                    textos = ''
                                    x1, y1 = 75, 703
                                    x2, y2 = 37, 703
                                    r,r1 = 18,550
                                    r2,r3 = 380,550
                                    k1,k2,k3,k4 = 350,680,350,420
                                if idx == 3:
                                    #HORA
                                    t1,t2 = 250,730
                                    t3,t4 = 283,730
                                    t5,t6 = 18,513
                                    t7,t8 = 380,513
                                    t9,t10 = 500,210
                                    t11,t12 = 90,493

                                    texto = f'{pmg[7]}'
                                    text = f'{pmg[9]}'
                                    textox = 'Finalizada? :'
                                    textoxx = 'Horario de finalização :'
                                    textos = ''

                                    x1, y1 = 283, 728
                                    x2, y2 = 310, 728
                                    r,r1 = 18,480
                                    r2,r3 = 380,480
                                    k1,k2,k3,k4 = 500,10,580,10
                                if idx == 4:
                                #SETOR
                                    t1,t2 = 250,705
                                    t3,t4 = 275,705
                                    t5,t6 = 18,422
                                    t9,t10 = 510,15
                                    t11,t12 = 430,642

                                    texto = f'{pmg[2]}'
                                    text = f'{pmg[12]}'
                                    textox = 'Ocorrência :'
                                    textos = 'Bruno Kappaun'
        
                                    x1, y1 = 275, 703
                                    x2, y2 = ct[0], 703
                                    widt, heigh = 560, 60
                                    r,r1 = 18,360
                                if idx == 5:
                                    #OS
                                    t1,t2 = 430,730
                                    t3,t4 = 448,730
                                    t5,t6 = 25,345
                                    t11,t12 = 430,563

                                    texto = f'N° 00{pmg[0]}'
                                    text = f'{pmg[10]}'
                                    textox = 'Visualização do problema:'
                                    x1, y1 = 448, 728
                                    x2, y2 = 475, 728
                                if idx == 6:
                                #maquina
                                    t1,t2 = 430,705
                                    t3,t4 = 455,705
                                    t5,t6 = 30,170
                                    t11,t12 = 430,493
                                    texto =f'{pmg[13]}'
                                    textox = 'Visualização pós problema:'
                                    text = f'{pmg[11]}'
                                    x1, y1 = 455, 703
                                    x2, y2 = 510, 703
                                if idx == 7:
                                    t11,t12 = 25,410
                                    text = f'{pmg[3]}'
                
                                pdfmetrics.registerFont(TTFont('font', './Fontes/ASENINE_.ttf'))
                                cor_do_texto = (0,0,0)
                                font_name = 'font' 

                                pdfmetrics.registerFont(TTFont('ASS', './Fontes/ASSINATURA.ttf'))
                                cor_do_texto = (0,0,0)
                                font_namex = 'ASS' 
            
                                textobject = c.beginText(t1, t2)
                                textobject.setFont(font_name , 13)
                                textobject.setTextOrigin(t1, t2)
                                textobject.textLine(f"{james}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobject)
                                c.setLineWidth(largura_da_linha)
                                c.line(x1,y1,x2,y2)
        
                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t3, t4)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t3, t4)
                                textobjectx.textLine(f"{texto}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t5, t6)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t5, t6)
                                textobjectx.textLine(f"{textox}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t7, t8)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t7, t8)
                                textobjectx.textLine(f"{textoxx}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t9, t10)
                                textobjectx.setFont(font_namex, 10)
                                textobjectx.setTextOrigin(t9, t10)
                                textobjectx.textLine(f"{textos}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t11, t12)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t11, t12)
                                textobjectx.textLine(f"{text}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                raio = 5
                                c.roundRect(r, r1, widt, heigh, raio, stroke=1, fill=0)

                                width, height = 200, 30
                                raio = 5
                                c.roundRect(r2, r3, width, height, raio, stroke=1, fill=0)
                                c.line(k1,k2,k3,k4)
                            width, height = 700, 50
                            raio = 10
                            r,r1 = 8,800
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                            width, height = 580, 680
                            raio = 10
                            r,r1 = 8,0
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)
    
                            x, y = 0,750
                            c.drawInlineImage(img, x,y, width=600,height=100)
                            x, y = 10,180
                            x1,y1 = 10, 20
                            if not corretivas.empty:
                                cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                if cursor1.fetchall():
                                    cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                    imagens = cursor1.fetchall()
                                    oe = imagens[0][1]
                                    oie = imagens[0][2]
                                    imagem = Image.open(BytesIO(oe))
                                    imagem2 = Image.open(BytesIO(oie))
                                    c.drawInlineImage(imagem2, x1,y1, width=400,height=145)
                                    c.drawInlineImage(imagem, x,y, width=400,height=145)   
                        
                        c = canvas.Canvas(f"./Data/geral_{usuario}.pdf")
                        hh = hello(c,pmg)
                        c.save()
            
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
                st.title(tltle_list)
           
            tab6, tab7,tab8,tab9,tab10,tab11= st.tabs(tabs_list)
            with tab6:
                st.header(header_list,divider='blue')
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln1 == 0:
                           numros = 0
                           numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln1,value=allln1,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, (solicitante_list),index=None,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, (solicitante_list),index=None,placeholder='Atualize!',help=help_solicitante)
                        
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, (setor_list),index=None,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                        
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl, (setor_list),index=None,placeholder='Atualize!',help=help_setor)
                        Rsetor = ''

                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, (ocorrencia_list),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,(ocorrencia_list),index=None, placeholder='Atualize!',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, (acao_list),index=None,placeholder='Selecione!',help=helpe_acao)
                        RUacao = ' '
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, (acao_list),index=None,placeholder='Atualize!',help=helpe_acao)
                        Racao = ' '

                    if Rsetor == 'Produção' or RUsetor == 'Produção':
                        if not atd1:
                            segmento = container.selectbox('Defina o segmento de produção:', ('Extrusão','Estampo','Corte','Rosca e Furo','Embalagem'),index=None,placeholder='Selecione!',help=help_setor)
                        if atd1:
                            segmento = container.selectbox('Atualize o segmento de produção:', ('Extrusão','Estampo','Corte','Rosca e Furo','Embalagem'),index=None,placeholder='Atualize!',help=help_setor)
                        if not segmento == None:
                            comb = (f'{Rsetor} {segmento} {Racao}')
                    else:
                        comb = (f'{Rsetor} {Racao}')
                        
                    
                    if not atd1:
                        parada = container.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                    if atd1:
                        parada = container.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                    
                    if not atd1: 
                        especialidades = container.selectbox(especialidades_titulo, (especialidade_list),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl, (especialidade_list),index=None,placeholder='Atualize!',help=help_especialidade)
                    
                    if Rsetor == 'Produção' or RUsetor == 'Produção':
                        if not segmento == None:
                            if comb == 'Produção Extrusão Corretiva' or comb == 'Produção Extrusão Preventiva' or comb == 'Produção Extrusão Preditiva':
                                Local = container.selectbox(local_titulo,(extrusão_list),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Extrusão Confecção' or comb == 'Produção Extrusão Montagem':
                                Local = container.selectbox(local_titulo,(extrusão_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Estampo Corretiva' or comb == 'Produção Estampo Preventiva' or comb == 'Produção Estampo Preditiva':
                                Local = container.selectbox(local_titulo,(estampo_list),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Estampo Confecção' or comb == 'Produção Estampo Montagem':
                                Local = container.selectbox(local_titulo,(estampo_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Embalagem Corretiva' or comb == 'Produção Embalagem Preventiva' or comb == 'Produção Embalagem Preditiva':
                                Local = container.selectbox(local_titulo,(embalagem),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Embalagem Confecção' or comb == 'Produção Embalagem Montagem':
                                Local = container.selectbox(local_titulo,(embalagem_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Rosca e Furo Corretiva' or comb == 'Produção Rosca e Furo Preventiva' or comb == 'Produção Rosca e Furo Preditiva':
                                Local = container.selectbox(local_titulo,(rosca_e_furo),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Rosca e Furo Confecção' or comb == 'Produção Rosca e Furo Montagem':
                                Local = container.selectbox(local_titulo,(rosca_e_furo_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Corte Corretiva' or comb == 'Produção Corte Preventiva' or comb == 'Produção Corte Preditiva':
                                Local = container.selectbox(local_titulo,(corte),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Corte Confecção' or comb == 'Produção Corte Montagem':
                                Local = container.selectbox(local_titulo,(corte_â),index=None,placeholder= 'Selecione!',help=help_local) 
                        else:
                            Local = ''
                            
                
                    else:
                       
                        if comb == 'Tecnologia da Informação Corretiva' or comb == 'Tecnologia da Informação Preventiva' or comb == 'Tecnologia da Informação Preditiva':
                            Local = container.selectbox(local_titulo,(ti),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Tecnologia da Informação Confecção' or comb == 'Tecnologia da Informação Montagem':
                            Local = container.selectbox(local_titulo,(ti_â),index=None,placeholder= 'Selecione!',help=help_local)
                        else:
                            Local = ' '
                           

                        if comb == 'Administrativo Corretiva' or comb == 'Administrativo Preventiva' or comb == 'Administrativo Preditiva':
                            Local = container.selectbox(local_titulo,(administrativo),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Administrativo Confecção' or comb == 'Administrativo Montagem':
                            Local = container.selectbox(local_titulo,(administrativo_â),index=None,placeholder= 'Selecione!',help=help_local)
                        
                        if comb == 'Comercial Corretiva' or comb == 'Comercial Preventiva' or comb == 'Comercial Preditiva':
                            Local = container.selectbox(local_titulo,(comercial),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Comercial Confecção' or comb == 'Comercial Montagem':
                            Local = container.selectbox(local_titulo,(comercial_â),index=None,placeholder= 'Selecione!',help=help_local)
                        
                        if comb == 'Expedição Corretiva' or comb == 'Expedição Preventiva' or comb == 'Expedição Preditiva':
                            Local = container.selectbox(local_titulo,(expedição),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Expedição Confecção' or comb == 'Expedição Montagem':
                            Local = container.selectbox(local_titulo,(expedição_â),index=None,placeholder= 'Selecione!',help=help_local)

                        if comb == 'Ferramentaria Corretiva' or comb == 'Ferramentaria Preventiva' or comb == 'Ferramentaria Preditiva':
                            Local = container.selectbox(local_titulo,(ferramentaria_list),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Ferramentaria Confecção' or comb == 'Ferramentaria Montagem':
                            Local = container.selectbox(local_titulo,(ferramentaria_list_â),index=None,placeholder= 'Selecione!',help=help_local)

                        if comb == 'Utilidades Corretiva' or comb == 'Utilidades Preventiva' or comb == 'Utilidades Preditiva':
                            Local = container.selectbox(local_titulo,(utilidades_list),index=None,placeholder= 'Selecione!',help=help_local)
                        elif comb == 'Utilidades Confecção' or comb == 'Utilidades Montagem':
                            Local = container.selectbox(local_titulo,(utilidades_list_â),index=None,placeholder= 'Selecione!',help=help_local)

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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=int(preenchimento[0]),value=int(preenchimento[0]),placeholder="Selecione!")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM MECANICA WHERE OS = {numero_da_os};')
                                conn.commit()
                                cursor1.execute("UPDATE imagens SET imagem = ? WHERE id = ?",(bytes_data,numros))
                                conn1.commit()
                
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
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_mecanica = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_mecanica}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_mecanica,str(timenow),datenow,monthnow,Local))
                                        cursor.execute("INSERT INTO MECANICA OS,SOLICITANTE,SETOR,SEGMENTO,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,ESPECIALIDADE,LOCAL,MÊS,PARADA) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_mecanica, Rsolicitante, Rsetor,segmento,Rstatus,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,especialidades,Local,monthnow,parada))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn1.commit()

            with tab7:
                st.header('🔚 Finalizar O.S',divider='blue')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    containerx = st.container(border=True)
                    setorescolhido = containerx.selectbox('Setor', ('PCM','Tecnologia da Informação','Comercial','Administrativo','Expedição','Produção','Ferramentaria','Serralharia','Mecânica'),index=None,placeholder='Selecione!',help=help_setor)
                    fnlz2 = containerx.number_input("Selecione o numero da O.S que deseja Finalizar",min_value=1,max_value=1000,value=1,placeholder="Selecione!",help=help_numero_os)
                    fnlz3 = fnlz2-1
                    finalizar = containerx.selectbox('O.S finalizada?', ('Sim','Não'),index=None,placeholder='Selecione!',help=help_finalizar_os)
                    uploaded_filess = containerx.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem_fnlzd)
                    for uploaded_filee in uploaded_filess:
                        bytess_data = uploaded_filee.read()

                    #datainput = containerx.date_input("Data", value=None)
                    #containerx.write(datainput)
                    #timeinput = containerx.time_input('HORA', value=None)
                    #containerx.write(timeinput)

                if fLIDERES == 'Equipe de MECÂNICA':
                    if fSETOR == 'Mecânica':
                        if uploaded_filess:
                            if setorescolhido == 'Ferramentaria':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Ferramentaria SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit() 

                            if setorescolhido == 'Produção':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()  
                            
                            if setorescolhido == 'Administrativo':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Administrativo SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit() 
                                    
                            
                            if setorescolhido == 'Comercial':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Comercial SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()   

                            if setorescolhido == 'Expedição':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()  

                            if setorescolhido == 'Serralharia':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE Serralharia SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()  

                            if setorescolhido == 'Tecnologia da Informação':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE TI SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()  

                            if setorescolhido == 'PCM':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor14.execute("UPDATE PCM SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn14.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()   

                            if setorescolhido == 'Mecânica':    
                                fnl=st.button("Finalizar O.S ✔")
                                if fnl:
                                    st.toast('Finalizando O.S!')
                                    time.sleep(0.5)
                                    st.toast(f'O.S [{fnlz2}] Finalizada!')
                                    cursor.execute("UPDATE MECANICA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datenow,str(timenow),fnlz2))
                                    conn.commit()
                                    cursor1.execute("UPDATE imagens SET imagem_finalizada = ? WHERE id = ?",(bytess_data,fnlz2))
                                    conn1.commit()    

            with tab8:
                st.header(abertas_list, divider='blue')
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    with st.expander("Filtros"):
                        genre = st.radio(
                          "Selecione!",
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
                            numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione!")
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
                            numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=MECANICAvalores,value=MECANICAvalores,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da k OS",min_value=1,max_value=pcm_id2,value=pcm_id2,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS ",min_value=1,max_value=rd30,value=rd30,placeholder="Selecione!")
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
                                numros4 = st.number_input(" Selecione  o  numero  da   OS",min_value=1,max_value=rd36,value=rd36,placeholder="Selecione!")
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
                                numros4 = st.number_input("Selecione  o numero  da    OS",min_value=1,max_value=rd44,value=rd44,placeholder="Selecione!")
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
                                numros4 = st.number_input("Selecione  o  numero   da    OS",min_value=1,max_value=rd52,value=rd52,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione  o  numero   da     OS",min_value=1,max_value=rd60,value=rd60,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione  o    numero   da    OS",min_value=1,max_value=rd68,value=rd68,placeholder="Selecione!")
                            oi = st.metric(label="O.S Existentes", value=rd68)
                            numros5 = numros4-1
                            osespec = rd67.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width13")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width13)
                
            with tab9:
                st.header(finalizadas_list, divider='blue')
                jam,jam1 = st.columns([0.2,1])
                with jam:
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
                            numros2 = st.number_input(" Selecione   o  numero da  OS ",min_value=1,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione!")
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
                        numros2 = st.number_input("Selecione   o   numero  da      OS      ",min_value=1,max_value=1000,value=1,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da O.S    ",min_value=1,max_value=100,value=1,placeholder="Selecione!")
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
                            numros4 = st.number_input(" Selecione  o  numero  da  OS ",min_value=1,max_value=rd30,value=rd30,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS   ",min_value=1,max_value=rd40,value=rd40,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS     ",min_value=1,max_value=rd48,value=rd48,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS       ",min_value=1,max_value=rd56,value=rd56,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS        ",min_value=1,max_value=rd64,value=rd64,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS          ",min_value=1,max_value=rd72,value=rd72,placeholder="Selecione!")
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
                            numros4 = st.number_input("Selecione o numero da  OS           ",min_value=1,max_value=rd77,value=rd77,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value=rd77)
                            numros5 = numros4-1
                            osespec = rd76.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width29")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width29)

            with tab10:
                col,col1,col2 = st.columns([0.5,1,0.5])
                with col:
                    with st.expander("",expanded=1):
                        st_ = st.container(border=True)
                        st.header(':blue[Localidade 🚩] ',divider='blue')
                        quadro =st.radio(
                        "Selecione",
                        ['Quadro A01-A04 (PRENSA P8)','Quadro DA1-DA6 (PULLER E ESTICADEIRA)','Quadro AA1-AA3 (FORNO DE TARUGO)','Quadro EA1-EA4 (SERRA E INCESTADOR)','Quadro FA1-FA3 (FORNO DE ENVELHECIMENTO)'],
                        index=0,
                        ) 
                        
                    with st.expander("",expanded=1):
                        st_3 = st.container(border=True)
                        st.header(':blue[Situação 🔎] ',divider='blue')
                        estado =st.radio(
                        "Selecione",
                        ['Equipamento em bom estado e em funcionamento!','Substituição de componente necessaria!','Equipamento danificado mas em funcionamento!'],
                        index=0,
                        )
                    
                    with st.expander("",expanded=1):
                        if estado == 'Substituição de componente necessaria!':
                            mat = pd.read_sql_query("SELECT * FROM Materiais", conn12)
                            mat_shape = mat.shape[0]
                            def example_one():
                                filtered_df = dataframe_explorer(mat, case=False)
                                st.dataframe(filtered_df, use_container_width=True)
                            example_one()               
               
                with col2:
                    with st.expander("",expanded=1):
                        st_1 = st.container(border=True)
                        st.header(':blue[Equipamento ⚙]',divider='blue')
                        equipamento = st.radio(
                        "Selecione",
                        ['Motores','Sensores','Contatores','Botões','Relerés','Disjuntores','Controladores','Fontes','Transformadores','Inversores de frequência','Porta fusiveis','Cilindros hidraulicos','Cilindros pneumaticos','Valvulas hidraulicas','Valvulas pneumaticas'],
                        index=0,
                        )
                    
                    if 'strs' == 'strs':
                        if equipamento == 'Motores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Limpeza:'
                            tltle_3 = 'Inspeção das Condições Ambientais:'
                            tltle_4 = 'Lubrificação:'
                            tltle_5 = 'Teste de Isolamento:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_8 = 'Teste de Funcionamento:'
                            tltle_9 = 'Calibração (se aplicável):'
                
                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de danos externos, como rachaduras, amassados ou corrosão no invólucro do :blue[motor] Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'
                            errorfull_2 = '° Limpar qualquer sujeira, poeira ou detritos acumulados no :blue[motor] que possam interferir em seu funcionamento.Utilizar produtos de limpeza adequados que não danifiquem o :blue[motor]'
                            errorfull_3 = '° Verificar se o :blue[motor] está instalado em um ambiente adequado em termos de temperatura, umidade e exposição a elementos corrosivos.'
                            errorfull_4 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_5 = '° Realizar testes de resistência de isolamento para garantir que não haja curtos-circuitos ou falhas nos enrolamentos do :blue[motor].'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar a tensão e a corrente de operação do :blue[motor] para garantir que estejam dentro dos limites especificados pelo fabricante.'
                            errorfull_8 = '° Ligar brevemente o :blue[motor] para garantir que ele inicie suavemente e funcione sem ruídos ou vibrações anormais.Verificar se todos os sistemas de proteção (como :blue[disjuntor]es e relés térmicos) estão funcionando corretamente.'
                            errorfull_9 = '° Verificar se os dispositivos de controle e medição associados ao equipamento estão devidamente calibrados e funcionando corretamente.'
                        elif equipamento == 'Sensores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Limpeza:'
                            tltle_3 = 'Inspeção das Condições Ambientais:'
                            tltle_4 = 'Verificação da Precisão e Sensibilidade:'
                            tltle_5 = 'Verificação da Conexão e Comunicação:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_8 = 'Teste de Funcionamento:'
                            tltle_9 = 'Calibração (se aplicável):'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de danos externos, como rachaduras, amassados ou corrosão no invólucro do :blue[Sensor] Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'
                            errorfull_2 = '° Limpar qualquer sujeira, poeira ou detritos acumulados no :blue[Sensor] que possam interferir em seu funcionamento.Utilizar produtos de limpeza adequados que não danifiquem o :blue[Sensor]'
                            errorfull_3 = '° Verificar se o :blue[Sensor] está instalado em um ambiente adequado em termos de temperatura, umidade e exposição a elementos corrosivos.'
                            errorfull_4 = '° Testar a precisão e sensibilidade do :blue[Sensor] em detectar variações ou mudanças nas condições medidas.Comparar as leituras do :blue[Sensor] com padrões conhecidos ou outras :blue[fontes confiáveis de] dados, quando disponíveis.'
                            errorfull_5 = '° Testar a conexão física do :blue[Sensor] com o sistema de monitoramento ou controle.Verificar se a comunicação entre o :blue[Sensor] e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar se o :blue[Sensor] está recebendo a alimentação adequada de acordo com as especificações do fabricante.Testar a integridade do circuito de alimentação e identificar e corrigir quaisquer problemas de fornecimento de energia.'
                            errorfull_8 = '° Realizar testes funcionais para verificar se o :blue[Sensor] está respondendo corretamente aos estímulos ou condições que ele é projetado para detectar.Verificar se os sinais de saída do :blue[Sensor] estão dentro dos limites esperados e se correspondem às condições reais.'
                            errorfull_9 = '° Verificar se o :blue[Sensor] está calibrado corretamente de acordo com as especificações do fabricante.Realizar calibrações periódicas conforme recomendado pelo fabricante ou conforme necessário com base nos resultados das medições.'
                        elif equipamento == 'Contatores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Verificação dos Contatos'
                            tltle_3 = 'Verificação dos Mecanismos de Acionamento'
                            tltle_4 = 'Verificação das Bobinas:'
                            tltle_5 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação dos Dispositivos de Proteção:'
                            tltle_8 = 'Verificação da Conexão e Comunicação:'
                            tltle_9 = 'Aperto dos Terminais e Conexões:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Contator].Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'

                            errorfull_2 = '° Inspecionar os contatos do :blue[Contator] quanto a sinais de desgaste, queimaduras, corrosão ou pontos de solda.Limpar os contatos, se necessário, para remover quaisquer depósitos ou acumulações que possam interferir no funcionamento.'
                            errorfull_3 = '° Testar o mecanismo de acionamento do :blue[Contator] para garantir que esteja operando suavemente e sem obstruções.Verificar se não há pontos de travamento ou desalinhamento no mecanismo.'
                            errorfull_4 = '° Verificar a integridade e a resistência das bobinas do :blue[Contator].Testar a operação das bobinas para garantir que estejam funcionando corretamente e respondendo aos comandos de acionamento.'
                            errorfull_5 = '° Verificar se a tensão e a corrente de operação do :blue[Contator] estão dentro dos limites especificados pelo fabricante.Testar o :blue[Contator] em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar se os dispositivos de proteção, como :blue[disjuntor]es ou fusíveis, estão instalados e funcionando corretamente para proteger o :blue[Contator] e o circuito contra sobrecargas ou curtos-circuitos.'
                            errorfull_8 = '° Testar a conexão física do :blue[Contator] com o sistema de controle ou circuito.Verificar se a comunicação entre o :blue[Contator] e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_9 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'                          
                        elif equipamento == 'Botões':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação do Funcionamento:'
                            tltle_3 = 'Verificação das Conexões:'
                            tltle_4 = 'Verificação da Iluminação:'
                            tltle_5 = 'Verificação da Vedação:'
                            tltle_6 = 'Verificação da Durabilidade:'
                            tltle_7 = 'Ajuste da Sensibilidade:'
                            tltle_8 = 'Verificação da Fixação:'
                            tltle_9 = 'Teste de Funcionamento Geral:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no botão. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no botão, evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar o funcionamento do botão, garantindo que pressioná-lo acione o comando desejado de forma consistente.'
                            errorfull_3 = '° Verificar todas as conexões do botão quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_4 = '° Verificar a iluminação do botão, se aplicável, garantindo que esteja funcionando corretamente.'
                            errorfull_5 = '° Verificar a vedação do botão, garantindo que esteja intacta para proteger contra poeira e umidade.'
                            errorfull_6 = '° Verificar a durabilidade do botão, avaliando sua resistência ao uso repetido ao longo do tempo.'
                            errorfull_7 = '° Ajustar a sensibilidade do botão, se aplicável, para garantir que o acionamento ocorra com a pressão adequada.'
                            errorfull_8 = '° Verificar a fixação do botão, garantindo que esteja firmemente instalado e sem folgas.'
                            errorfull_9 = '° Realizar um teste de funcionamento geral do botão, garantindo que ele opere corretamente em todas as condições de uso.'
                        elif equipamento == 'Relerés':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Verificação dos Cabos e Conexões:'
                            tltle_2 = 'Verificação dos Contatos'
                            tltle_3 = 'Verificação dos Mecanismos de Acionamento'
                            tltle_4 = 'Verificação das Bobinas:'
                            tltle_5 = 'Verificação da Tensão e Corrente de Operação:'
                            tltle_6 = 'Alinhamento e Balanceamento (se aplicável):'
                            tltle_7 = 'Verificação dos Dispositivos de Proteção:'
                            tltle_8 = 'Verificação da Conexão e Comunicação:'
                            tltle_9 = 'Aperto dos Terminais e Conexões:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Relé].Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Inspeccionar os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou aquecimento excessivo.Apertar quaisquer terminais soltos ou conexões frouxas.'
                            errorfull_2 = '° Inspecionar os contatos do :blue[Relé] quanto a sinais de desgaste, queimaduras, corrosão ou pontos de solda.Limpar os contatos, se necessário, para remover quaisquer depósitos ou acumulações que possam interferir no funcionamento.'
                            errorfull_3 = '° Testar o mecanismo de acionamento do :blue[Relé] para garantir que esteja operando suavemente e sem obstruções.Verificar se não há pontos de travamento ou desalinhamento no mecanismo.'
                            errorfull_4 = '° Verificar a integridade e a resistência das bobinas do :blue[Relé].Testar a operação das bobinas para garantir que estejam funcionando corretamente e respondendo aos comandos de acionamento.'
                            errorfull_5 = '° Verificar se a tensão e a corrente de operação do :blue[Relé] estão dentro dos limites especificados pelo fabricante.Testar o :blue[Relé] em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_6 = '° Verificar o alinhamento do :blue[motor] com o acoplamento ou a carga e realizar ajustes conforme necessário.Verificar se há desequilíbrios no rotor e equilibrar, se necessário.'
                            errorfull_7 = '° Verificar se os dispositivos de proteção, como :blue[disjuntor]es ou fusíveis, estão instalados e funcionando corretamente para proteger o :blue[Relé] e o circuito contra sobrecargas ou curtos-circuitos.'
                            errorfull_8 = '° Testar a conexão física do :blue[Relé] com o sistema de controle ou circuito.Verificar se a comunicação entre o :blue[Relé] e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_9 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'
                        elif equipamento == 'Disjuntores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação da Tensão Nominal:'
                            tltle_4 = 'Teste de Funcionamento:'
                            tltle_5 = 'Verificação do Disparador:'
                            tltle_6 = 'Verificação do Mecanismo de Atuação:'
                            tltle_7 = 'Teste de Proteção contra Sobrecarga:'
                            tltle_8 = 'Teste de Proteção contra Curto-Circuito:'
                            tltle_9 = 'Teste de Proteção contra Falta à Terra:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[disjuntor]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[disjuntor], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões do :blue[disjuntor] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar se a tensão nominal do :blue[disjuntor] está de acordo com as especificações do equipamento. Substituir o :blue[disjuntor] se a tensão estiver fora dos limites especificados.'
                            errorfull_4 = '° Realizar um teste de funcionamento completo no :blue[disjuntor], incluindo abertura e fechamento sob carga. Verificar se o :blue[disjuntor] opera corretamente em todas as condições.'
                            errorfull_5 = '° Verificar o funcionamento do disparador do :blue[disjuntor], garantindo que ele atue adequadamente em caso de sobrecarga ou curto-circuito.'
                            errorfull_6 = '° Verificar o mecanismo de atuação do :blue[disjuntor], assegurando que ele opere suavemente e sem travamentos.'
                            errorfull_7 = '° Realizar um teste de proteção contra sobrecarga, aplicando uma corrente ligeiramente acima da corrente nominal para verificar se o :blue[disjuntor] interrompe a corrente conforme esperado.'
                            errorfull_8 = '° Realizar um teste de proteção contra curto-circuito, aplicando uma corrente muito alta para verificar se o :blue[disjuntor] interrompe a corrente rapidamente e de forma segura.'
                            errorfull_9 = '° Realizar um teste de proteção contra falta à terra, simulando uma falta à terra para verificar se o :blue[disjuntor] atua corretamente e interrompe a corrente.'
                        elif equipamento == 'Controladores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação dos Cartões de E/S:'
                            tltle_4 = 'Verificação da Alimentação:'
                            tltle_5 = 'Verificação dos Programas:'
                            tltle_6 = 'Backup dos Programas:'
                            tltle_7 = 'Teste de Comunicação:'
                            tltle_8 = 'Teste de Entradas e Saídas:'
                            tltle_9 = 'Teste de Funcionamento Geral:'

                            sucessfull = f'Concluído a {tltle}'
                            sucessfull_1 = f'Concluído a {tltle_1}'
                            sucessfull_2 = f'Concluído a {tltle_2}'
                            sucessfull_3 = f'Concluído a {tltle_3}'
                            sucessfull_4 = f'Concluído a {tltle_4}'
                            sucessfull_5 = f'Concluído a {tltle_5}'
                            sucessfull_6 = f'Concluído o {tltle_6}'
                            sucessfull_7 = f'Concluído o {tltle_7}'
                            sucessfull_8 = f'Concluído o {tltle_8}'
                            sucessfull_9 = f'Concluído o {tltle_9}'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no controlador lógico programável (:blue[CLP]). Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[CLP], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões do :blue[CLP] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar os cartões de entrada e saída (E/S) do :blue[CLP], garantindo que estejam corretamente instalados e sem sinais de danos.'
                            errorfull_4 = '° Verificar a alimentação do :blue[CLP], garantindo que a tensão de entrada esteja dentro dos limites especificados e que não haja flutuações de tensão.'
                            errorfull_5 = '° Verificar os programas armazenados no :blue[CLP], assegurando que estejam corretamente carregados e sem erros de programação.'
                            errorfull_6 = '° Realizar um backup dos programas armazenados no :blue[CLP], garantindo que haja uma cópia de segurança em caso de perda de dados.'
                            errorfull_7 = '° Realizar um teste de comunicação com o :blue[CLP], garantindo que seja possível estabelecer comunicação e fazer upload/download de programas.'
                            errorfull_8 = '° Realizar um teste de entradas e saídas do :blue[CLP], garantindo que todas as entradas e saídas estejam operando corretamente conforme especificado no programa.'
                            errorfull_9 = '° Realizar um teste de funcionamento geral do :blue[CLP], incluindo a execução do programa e verificação do comportamento do sistema controlado.'
                        elif equipamento == 'Fontes':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação da Tensão de Saída:'
                            tltle_4 = 'Verificação da Corrente de Saída:'
                            tltle_5 = 'Verificação da Estabilidade:'
                            tltle_6 = 'Verificação da Proteção contra Surtos:'
                            tltle_7 = 'Teste de Proteção:'
                            tltle_8 = 'Teste de Sobrecarga:'
                            tltle_9 = 'Teste de Funcionamento Geral:'

                            sucessfull = f'Concluído a {tltle}'
                            sucessfull_1 = f'Concluído a {tltle_1}'
                            sucessfull_2 = f'Concluído a {tltle_2}'
                            sucessfull_3 = f'Concluído a {tltle_3}'
                            sucessfull_4 = f'Concluído a {tltle_4}'
                            sucessfull_5 = f'Concluído a {tltle_5}'
                            sucessfull_6 = f'Concluído a {tltle_6}'
                            sucessfull_7 = f'Concluído o {tltle_7}'
                            sucessfull_8 = f'Concluído o {tltle_8}'
                            sucessfull_9 = f'Concluído o {tltle_9}'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos na :blue[fonte de alimentação]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular na :blue[fonte de alimentação], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões da :blue[fonte de alimentação] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar a tensão de saída da :blue[fonte de alimentação], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_4 = '° Verificar a corrente de saída da :blue[fonte de alimentação], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_5 = '° Verificar a estabilidade da :blue[fonte de alimentação], garantindo que não haja flutuações significativas na tensão ou corrente de saída.'
                            errorfull_6 = '° Verificar a proteção contra surtos da :blue[fonte de alimentação], garantindo que esteja funcionando corretamente para proteger o equipamento conectado contra picos de tensão.'
                            errorfull_7 = '° Realizar um teste de proteção da :blue[fonte de alimentação], garantindo que ela atue corretamente em caso de sobretensão, subtensão ou curto-circuito.'
                            errorfull_8 = '° Realizar um teste de sobrecarga na :blue[fonte de alimentação], aplicando uma carga maior que a nominal para verificar se ela continua operando dentro dos limites especificados.'
                            errorfull_9 = '° Realizar um teste de funcionamento geral da :blue[fonte de alimentação], garantindo que ela opere corretamente em todas as condições de carga e temperatura.'
                        elif equipamento == 'Transformadores':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Conexões:'
                            tltle_3 = 'Verificação da Tensão Primária:'
                            tltle_4 = 'Verificação da Tensão Secundária:'
                            tltle_5 = 'Verificação dos Enrolamentos:'
                            tltle_6 = 'Teste de Isolação:'
                            tltle_7 = 'Teste de Resistência de Isolamento:'
                            tltle_8 = 'Verificação do Resfriamento:'
                            tltle_9 = 'Teste de Funcionamento:'

                            sucessfull = f'Concluído a {tltle}'
                            sucessfull_1 = f'Concluído a {tltle_1}'
                            sucessfull_2 = f'Concluído a {tltle_2}'
                            sucessfull_3 = f'Concluído a {tltle_3}'
                            sucessfull_4 = f'Concluído a {tltle_4}'
                            sucessfull_5 = f'Concluído a {tltle_5}'
                            sucessfull_6 = f'Concluído o {tltle_6}'
                            sucessfull_7 = f'Concluído o {tltle_7}'
                            sucessfull_8 = f'Concluído a {tltle_8}'
                            sucessfull_9 = f'Concluído o {tltle_9}'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[transformador]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[transformador], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar todas as conexões do :blue[transformador] quanto a sinais de frouxidão ou corrosão. Apertar quaisquer conexões soltas e limpar as conexões corroídas.'
                            errorfull_3 = '° Verificar a tensão primária do :blue[transformador], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_4 = '° Verificar a tensão secundária do :blue[transformador], garantindo que esteja dentro dos limites especificados pelo fabricante.'
                            errorfull_5 = '° Verificar os enrolamentos do :blue[transformador] quanto a sinais de danos, superaquecimento ou desgaste excessivo.'
                            errorfull_6 = '° Realizar um teste de isolação no :blue[transformador] para verificar se há algum curto-circuito ou falha no isolamento.'
                            errorfull_7 = '° Realizar um teste de resistência de isolamento para verificar a resistência entre os enrolamentos e o chassi do :blue[transformador].'
                            errorfull_8 = '° Verificar o sistema de resfriamento do :blue[transformador], garantindo que os radiadores ou ventiladores estejam funcionando corretamente.'
                            errorfull_9 = '° Realizar um teste de funcionamento completo do :blue[transformador], garantindo que ele opere corretamente em todas as condições de carga e temperatura.'
                        elif equipamento == 'Inversores de frequência':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação dos Parâmetros:'
                            tltle_3 = 'Verificação dos Cabos e Conexões:'
                            tltle_4 = 'Verificação da Ventilação:'
                            tltle_5 = 'Verificação dos Enrolamentos do :blue[Motor]:'
                            tltle_6 = 'Verificação da Tensão e Corrente de Saída:'
                            tltle_7 = 'Verificação dos Dispositivos de Proteção:'
                            tltle_8 = 'Verificação da Conexão e Comunicação:'
                            tltle_9 = 'Aperto dos Terminais e Conexões:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Inversor].Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Remova qualquer sujeira, poeira ou detritos que possam acumular no :blue[Inversor] e interferir em seu funcionamento.Use ar comprimido ou um pano limpo e seco para limpar o :blue[Inversor] , evitando o uso de produtos químicos que possam danificar os componentes.'
                            errorfull_2 = '° Verifique os parâmetros de operação do :blue[Inversor]  para garantir que estejam configurados conforme as especificações do fabricante e os requisitos de aplicação.Faça ajustes nos parâmetros, se necessário, para otimizar o desempenho do inversor ou corrigir problemas de operação.'
                            errorfull_3 = '° Inspecione os cabos de alimentação e conexões elétricas quanto a sinais de desgaste, danos ou problemas de conexão.Aperte quaisquer terminais soltos ou conexões frouxas para garantir uma conexão elétrica segura.'
                            errorfull_4 = '° Verifique se os ventiladores ou sistemas de resfriamento do :blue[Inversor]  estão funcionando corretamente.Limpe os filtros de ar ou ventiladores obstruídos para garantir uma boa circulação de ar e evitar o superaquecimento.'
                            errorfull_5 = '° Verifique os enrolamentos do :blue[motor] conectado ao :blue[Inversor]  quanto a sinais de superaquecimento, danos ou desgaste excessivo.Meça a temperatura dos enrolamentos durante a operação para identificar problemas de sobreaquecimento.'
                            errorfull_6 = '° Meça a tensão e a corrente de saída do :blue[Inversor] para garantir que estejam dentro dos limites especificados pelo fabricante.Teste o :blue[Inversor]  em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_7 = '° Verificar se os dispositivos de proteção, como :blue[disjuntor]es ou fusíveis, estão instalados e funcionando corretamente para proteger o :blue[Inversor]  e o circuito contra sobrecargas ou curtos-circuitos.'
                            errorfull_8 = '° Testar a conexão física do :blue[Inversor]  com o sistema de controle ou circuito.Verificar se a comunicação entre o :blue[Inversor]  e outros dispositivos ou sistemas está funcionando corretamente.'
                            errorfull_9 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'
                        elif equipamento == 'Porta fusiveis':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação da Continuidade:'
                            tltle_3 = 'Verificação da Tensão e Corrente de Saída:'
                            tltle_4 = 'Verificação dos Terminais:'
                            tltle_5 = 'Aperto dos Terminais e Conexões:'
                            tltle_6 = 'Teste de Funcionamento:'
                            tltle_7 = 'Verificação da Compatibilidade dos Fusíveis:'
                            tltle_8 = 'Verificação da Conexão à Terra:'
                            tltle_9 = 'Verificação da Proteção contra Surtos:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão, sujeira ou danos externos no invólucro do :blue[Porta fusiveis]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Remova qualquer sujeira, poeira ou detritos que possam acumular no :blue[Porta fusiveis] e interferir em seu funcionamento. Use ar comprimido ou um pano limpo e seco para limpar o :blue[Porta fusiveis], evitando o uso de produtos químicos que possam danificar os componentes.'
                            errorfull_2 = '° Verifique a continuidade dos contatos do :blue[Porta fusiveis] para garantir que estejam em boas condições de funcionamento. Substitua os fusíveis quebrados ou danificados conforme necessário.'
                            errorfull_3 = '° Meça a tensão e a corrente de saída do :blue[Porta fusiveis] para garantir que estejam dentro dos limites especificados pelo fabricante.Teste o :blue[Porta fusiveis] em carga para garantir que esteja operando conforme o esperado.'
                            errorfull_4 = '° Verifique os terminais do :blue[Porta fusiveis] quanto a sinais de desgaste, corrosão ou folga. Aperte quaisquer terminais soltos para garantir uma conexão elétrica segura.'
                            errorfull_5 = '° Verificar se todos os terminais e conexões estão firmemente apertados para garantir uma conexão elétrica segura e confiável.'
                            errorfull_6 = '° Realizar testes de funcionamento no :blue[Porta fusiveis] para garantir sua operação adequada.'
                            errorfull_7 = '° Verifique se os fusíveis utilizados são compatíveis com as especificações do equipamento protegido.'
                            errorfull_8 = '° Verificar se a conexão à terra do :blue[Porta fusiveis] está correta e em boas condições.'
                            errorfull_9 = '° Verificar se o :blue[Porta fusiveis] possui proteção contra surtos adequada para proteger os equipamentos conectados contra picos de tensão.'
                        elif equipamento == 'Cilindros hidraulicos':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Cilindro hidraulico]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Cilindro hidraulico], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Cilindro hidraulico] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Cilindro hidraulico] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Cilindro hidraulico] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Cilindro hidraulico] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Cilindro hidraulico] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Cilindro hidraulico] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                        elif equipamento == 'Cilindros pneumaticos':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Cilindro pneumatico]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Cilindro pneumatico], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Cilindro pneumatico] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Cilindro pneumatico] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Cilindro pneumatico] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Cilindro pneumatico] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Cilindro pneumatico] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Cilindro pneumatico] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                        elif equipamento == 'Valvulas hidraulicas':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Valvulas hidraulicas]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Valvulas hidraulicas], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Valvulas hidraulicas] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Valvulas hidraulicas] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Valvulas hidraulicas] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Valvulas hidraulicas] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Valvulas hidraulicas] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Valvulas hidraulicas] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                        elif equipamento == 'Valvulas pneumaticas':
                            tltle = 'Inspeção Visual Externa:'
                            tltle_1 = 'Limpeza:'
                            tltle_2 = 'Verificação das Vedações:'
                            tltle_3 = 'Verificação da Pressão de Operação:'
                            tltle_4 = 'Verificação dos Conexões e Mangueiras:'
                            tltle_5 = 'Verificação do Funcionamento:'
                            tltle_6 = 'Lubrificação:'
                            tltle_7 = 'Teste de Vazamento:'
                            tltle_8 = 'Verificação dos Anéis de Vedação:'
                            tltle_9 = 'Verificação dos Amortecedores:'

                            sucessfull = f'Concluido a :blue[{tltle}]'
                            sucessfull_1 = f'Concluido a :blue[{tltle_1}]'
                            sucessfull_2 = f'Concluido a :blue[{tltle_2}]'
                            sucessfull_3 = f'Concluido a :blue[{tltle_3}]'
                            sucessfull_4 = f'Concluido a :blue[{tltle_4}]'
                            sucessfull_5 = f'Concluido a :blue[{tltle_5}]'
                            sucessfull_6 = f'Concluido o :blue[{tltle_6}]'
                            sucessfull_7 = f'Concluido a :blue[{tltle_7}]'
                            sucessfull_8 = f'Concluido a :blue[{tltle_8}]'
                            sucessfull_9 = f'Concluido o :blue[{tltle_9}]'

                            errorfull = '° Verificar sinais de desgaste, corrosão ou danos externos no :blue[Valvulas pneumaticas]. Assegurar que todas as conexões e fixações estejam seguras e em bom estado.'
                            errorfull_1 = '° Limpar qualquer sujeira, poeira ou detritos que possam acumular no :blue[Valvulas pneumaticas], evitando interferências no seu funcionamento.'
                            errorfull_2 = '° Verificar as vedações do :blue[Valvulas pneumaticas] quanto a sinais de desgaste ou danos. Substituir as vedações danificadas conforme necessário.'
                            errorfull_3 = '° Verificar se a pressão de operação do :blue[Valvulas pneumaticas] está dentro dos limites especificados. Ajustar a pressão conforme necessário.'
                            errorfull_4 = '° Verificar todas as conexões e mangueiras quanto a sinais de vazamento ou danos. Apertar quaisquer conexões frouxas e substituir mangueiras danificadas.'
                            errorfull_5 = '° Verificar o funcionamento do :blue[Valvulas pneumaticas] em todas as suas posições. Testar todas as funções para garantir seu correto funcionamento.'
                            errorfull_6 = '° Verificar o nível de óleo ou graxa nos rolamentos e, se necessário, lubrificar de acordo com as especificações do fabricante.'
                            errorfull_7 = '° Realizar um teste de vazamento no :blue[Valvulas pneumaticas] para garantir que não haja vazamentos após a manutenção.'
                            errorfull_8 = '° Verificar os anéis de vedação do :blue[Valvulas pneumaticas] quanto a sinais de desgaste ou danos. Substituir os anéis danificados conforme necessário.'
                            errorfull_9 = '° Verificar os amortecedores do :blue[Valvulas pneumaticas] quanto a sinais de desgaste ou danos. Substituir os amortecedores danificados conforme necessário.'
                    
                with col1:
                    with st.expander("",expanded=1):
                        st.header(':blue[CheckList 📋]',divider='blue')
                        check_9 =st.text_input('T.A.G de referência do equipamento:')
                        componente = (f'{check_9} pertence a {equipamento}')
                        check = st.checkbox(tltle)
                        if check:
                            st.success(sucessfull)
                        else:
                            st.error(errorfull)
                    
                        check_1 =st.checkbox(tltle_1)
                        if check_1:
                            st.success(sucessfull_1)
                        else:
                            st.error(errorfull_1)
                        
                        check_1_2 =st.checkbox(tltle_2)
                        if check_1_2:
                            st.success(sucessfull_2)
                        else:
                            st.error(errorfull_2)
                        
                        check_2 =st.checkbox(tltle_3)
                        if check_2:
                            st.success(sucessfull_3)
                            if equipamento == 'Disjuntores' or equipamento == 'Fontes' or equipamento == 'Transformadores':
                                col,col1,col2 = st.columns([1,1,3])
                                with col:
                                    st.number_input('Especifique a tensão (V): ',value=0.0,step=0.1)
                            if equipamento == 'Porta fusiveis':
                                col,col1,col2 = st.columns([1,1,5])
                                with col:
                                    st.number_input('Especifique a corrente (A):',value=0.0,step=0.1)
                                with col1:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                            if  equipamento == 'Cilindros hidraulicos' or equipamento == 'Cilindros pneumaticos'or equipamento =='Valvulas hidraulicas'or equipamento =='Valvulas pneumaticas':
                                col,col1,col2 = st.columns([1,1,3])
                                with col:
                                    st.number_input('Especifique a pressão (BAR/PSI):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_3)
                        check_3 =st.checkbox(tltle_4)
                        if check_3:
                            st.success(sucessfull_4)
                            if equipamento == 'Controladores' or equipamento == 'Transformadores':
                                col,col1,col2 = st.columns([1,1,3])
                                with col:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_4)
                        check_4 =st.checkbox(tltle_5)
                        if check_4:
                            st.success(sucessfull_5)
                            if equipamento == 'Contatores' or equipamento == 'Relerés':
                                col,col1,col2 = st.columns([1,1,5])
                                with col:
                                    st.number_input('Especifique a corrente (A):',value=0.0,step=0.1)
                                with col1:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_5)
                            
                        if not equipamento == 'Contatores' and not equipamento == 'Relerés'and not equipamento == 'Inversores de frequência' and not equipamento == 'Porta fusiveis' and not equipamento == 'Sensores':
                            check_5 =st.checkbox(tltle_6)
                            if check_5:
                                st.success(sucessfull_6)
                            else:
                                st.error(errorfull_6 )
                        
                        check_6 =st.checkbox(tltle_7)
                        if check_6:
                            st.success(sucessfull_7)
                            if equipamento == 'Motores' or equipamento == 'Sensores':
                                col,col1,col2 = st.columns([1,1,5])
                                with col:
                                    st.number_input('Especifique a corrente (A):',value=0.0,step=0.1)
                                with col1:
                                    st.number_input('Especifique a tensão (V):',value=0.0,step=0.1)
                        else:
                            st.error(errorfull_7)
                        
                        check_7 =st.checkbox(tltle_8)
                        if check_7:
                            st.success(sucessfull_8)
                        else:
                            st.error(errorfull_8)

                        check_8 =st.checkbox('Calibração (se aplicável):')
                        if check_8:
                            st.success(sucessfull_9)
                        else:
                            st.error(errorfull_9)
                        check_10 =st.text_area('Registro de Manutenção:')
                        
                        if not equipamento == 'Contatores' and not equipamento == 'Relerés'and not equipamento == 'Inversores de frequência' and not equipamento == 'Porta fusiveis' and not equipamento == 'Sensores':
                            checkslists = [check_1,check_1_2,check_2,check_3,check_4,check_5,check_6,check_7,check_8,check_9,check_10]
                            tst = all(checkslists)
                            
                        else:
                            checkslists = [check_1,check_1_2,check_2,check_3,check_4,check_6,check_7,check_8,check_9,check_10]
                            tst = all(checkslists)
                        
                        if tst:
                            envio = st.button('(⌐■_■)')
                            if envio:
                                cursor.execute("INSERT INTO checklistM (Tag,Local,Equipamento,Situação,Check_1,Check_2,Check_3,Check_4,Check_5,Check_6,Check_7,Check_8,Check_9,Relatorio,Hora,Data,Mês) VALUES (?,?,?,?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)", (check_9,quadro,equipamento,estado,(f'{tltle} Concluido'),(f'{tltle_1} Concluido'),(f'{tltle_2} Concluido'),(f'{tltle_3} Concluido'),(f'{tltle_4} Concluido'),(f'{tltle_5} Concluido'),(f'{tltle_6} Concluido'),(f'{tltle_7} Concluido'),(f'{tltle_8} Concluido'),(f'{tltle_9} Concluido'),timenow,datenow,monthnow))
                                conn.commit()
                    
            with tab11:
                st.header (aviso_list,divider='blue')
                omaga = st.multiselect('Selecione:',acao_list,max_selections=1)
                if not omaga == []:
                    corretivas = pd.read_sql_query(f"SELECT * FROM MECANICA WHERE AÇÃO = '{omaga[0]}'", conn)
                    corretivas_shape = corretivas.shape[0]
                if omaga == []:
                    st.success('Escolha um tipo de ação')
                else:
                    if corretivas_shape == 0:
                        st.success('Não há pendências')
                    else:
                        corretivas = pd.read_sql_query(f"SELECT * FROM MECANICA WHERE AÇÃO = '{omaga[0]}'", conn)
                        corretivas_shape = corretivas.shape[0]
                        st.metric(label="O.S Existentes", value=corretivas_shape)
                        numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=corretivas_shape,value=corretivas_shape,placeholder="Selecione!")
                        numros3 = numros2-1
                        serie_pdf = corretivas.loc[numros3]
                        def load_data():
                            return pd.DataFrame(serie_pdf)
                        st.checkbox("Estender", value=True, key="use_container_width17")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width17)
                        dt = corretivas.loc[numros3]
                        dt = dt.tolist()
                        with open(f"./Data/geral_Mecânica.pdf", 'rb') as file:
                            pdf_reader = PyPDF2.PdfReader(file)
                            bttn = st.download_button(
                            label="Exportar O.S 🖨",
                            key= "download_button",
                            data= file,
                            file_name=f"O.S {dt[0]}.pdf",
                            mime='application/octet-stream',
                            help='Por favor atualize antes de fazer a exportação do arquivo!'
                        )
                    
                        usuario = 'Mecânica'
                        cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                        if cursor1.fetchall():
                            cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                            imagens = cursor1.fetchall()
                            oe = imagens[0][1]
                            imagem = Image.open(BytesIO(oe))

                        localx = corretivas.loc[numros3]
                        pmg = localx.tolist()
                        Solicitante = solicitante_titulo
                        Data = 'Data:'
                        Hora = 'Horario:'
                        Setor = 'Setor:'
                        Os = 'O.S:'
                        maqx = local_titulo
                        dados = [Solicitante,Data,Hora,Setor,Os,maqx,'']
                        img = Image.open('./Midia/ssmm.jpg')
                        img1 = Image.open('./Midia/sales.jpeg')

                        def hello(c,pmg):
                            o = 0
                            b = []
                            for s in str(pmg[1]):
                                if s.isalpha():
                                    o += 1
                                    tmh = 4 * o + 58 
                                    b.append(tmh)

                            ct = []
                            for s in str(pmg[2]):
                                if not pmg[2] =='Produção':
                                    if s.isalpha():
                                        o += 1
                                        tmh = 4 * o + 268
                                        ct.append(tmh)
                                    else:
                                        ''
                                        
                            idx = 0             
                            for james in dados:
                                idx = idx + 1
                                largura_da_linha = 0.1
                                width, height = 580, 50
                                raio = 10
                                if idx == 1:
                                #SOLICITANTE
                                    t1,t2 = 15,730
                                    t3,t4 = 58,730
                                    t5,t6 = 20,662
                                    t7,t8 = 380,662
                                    t9,t10 = 500,210
                                    t11,t12 = 90,642

                                    texto = f'{pmg[1]}'
                                    text = f'{pmg[5]}'
                                    textox = 'Grau de ocorrência :'
                                    textoxx = 'Especialidade :'
                                    textos = ''
                                    x1, y1 = b[9], 728
                                    x2, y2 = 58, 728
                                    widt, heigh = 200, 30
                                    r,r1 = 18,630
                                    r2,r3 = 380,630
                                    k1,k2,k3,k4 = 250,680,250,420
                                if idx == 2:
                                #DAT
                                    t1,t2 = 15,705
                                    t3,t4 = 38,705
                                    t5,t6 = 18,583
                                    t7,t8 = 380,583
                                    t9,t10 = 500,210
                                    t11,t12 = 90,563

                                    texto = f'{pmg[6]}'
                                    text = f'{pmg[8]}'
                                    textox = 'Ação :'
                                    textoxx = 'Data de finalização :'
                                    textos = ''
                                    x1, y1 = 75, 703
                                    x2, y2 = 37, 703
                                    r,r1 = 18,550
                                    r2,r3 = 380,550
                                    k1,k2,k3,k4 = 350,680,350,420
                                if idx == 3:
                                    #HORA
                                    t1,t2 = 250,730
                                    t3,t4 = 283,730
                                    t5,t6 = 18,513
                                    t7,t8 = 380,513
                                    t9,t10 = 500,210
                                    t11,t12 = 90,493

                                    texto = f'{pmg[7]}'
                                    text = f'{pmg[9]}'
                                    textox = 'Finalizada? :'
                                    textoxx = 'Horario de finalização :'
                                    textos = ''

                                    x1, y1 = 283, 728
                                    x2, y2 = 310, 728
                                    r,r1 = 18,480
                                    r2,r3 = 380,480
                                    k1,k2,k3,k4 = 500,10,580,10
                                if idx == 4:
                                #SETOR
                                    t1,t2 = 250,705
                                    t3,t4 = 275,705
                                    t5,t6 = 18,422
                                    t9,t10 = 510,15
                                    t11,t12 = 430,642

                                    texto = f'{pmg[2]}'
                                    text = f'{pmg[12]}'
                                    textox = 'Ocorrência :'
                                    textos = 'Bruno Kappaun'
        
                                    x1, y1 = 275, 703
                                    x2, y2 = ct[0], 703
                                    widt, heigh = 560, 60
                                    r,r1 = 18,360
                                if idx == 5:
                                    #OS
                                    t1,t2 = 430,730
                                    t3,t4 = 448,730
                                    t5,t6 = 25,345
                                    t11,t12 = 430,563

                                    texto = f'N° 00{pmg[0]}'
                                    text = f'{pmg[10]}'
                                    textox = 'Visualização do problema:'
                                    x1, y1 = 448, 728
                                    x2, y2 = 475, 728
                                if idx == 6:
                                #maquina
                                    t1,t2 = 430,705
                                    t3,t4 = 455,705
                                    t5,t6 = 30,170
                                    t11,t12 = 430,493
                                    texto =f'{pmg[13]}'
                                    textox = 'Visualização pós problema:'
                                    text = f'{pmg[11]}'
                                    x1, y1 = 455, 703
                                    x2, y2 = 510, 703
                                if idx == 7:
                                    t11,t12 = 25,410
                                    text = f'{pmg[3]}'
                
                                pdfmetrics.registerFont(TTFont('font', './Fontes/ASENINE_.ttf'))
                                cor_do_texto = (0,0,0)
                                font_name = 'font' 

                                pdfmetrics.registerFont(TTFont('ASS', './Fontes/ASSINATURA.ttf'))
                                cor_do_texto = (0,0,0)
                                font_namex = 'ASS' 
            
                                textobject = c.beginText(t1, t2)
                                textobject.setFont(font_name , 13)
                                textobject.setTextOrigin(t1, t2)
                                textobject.textLine(f"{james}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobject)
                                c.setLineWidth(largura_da_linha)
                                c.line(x1,y1,x2,y2)
        
                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t3, t4)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t3, t4)
                                textobjectx.textLine(f"{texto}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t5, t6)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t5, t6)
                                textobjectx.textLine(f"{textox}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t7, t8)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t7, t8)
                                textobjectx.textLine(f"{textoxx}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t9, t10)
                                textobjectx.setFont(font_namex, 10)
                                textobjectx.setTextOrigin(t9, t10)
                                textobjectx.textLine(f"{textos}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t11, t12)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t11, t12)
                                textobjectx.textLine(f"{text}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                raio = 5
                                c.roundRect(r, r1, widt, heigh, raio, stroke=1, fill=0)

                                width, height = 200, 30
                                raio = 5
                                c.roundRect(r2, r3, width, height, raio, stroke=1, fill=0)
                                c.line(k1,k2,k3,k4)
                            width, height = 700, 50
                            raio = 10
                            r,r1 = 8,800
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                            width, height = 580, 680
                            raio = 10
                            r,r1 = 8,0
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)
    
                            x, y = 0,750
                            c.drawInlineImage(img, x,y, width=600,height=100)
                            x, y = 10,180
                            x1,y1 = 10, 20
                            if not corretivas.empty:
                                cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                if cursor1.fetchall():
                                    cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                    imagens = cursor1.fetchall()
                                    imagens
                                    if imagens[0][1]:
                                        oe = imagens[0][1]
                                        imagem = Image.open(BytesIO(oe))
                                        c.drawInlineImage(imagem, x,y, width=400,height=145)  
                                    if imagens[0][2]:
                                        oie = imagens[0][2]
                                        imagem2 = Image.open(BytesIO(oie))
                                        c.drawInlineImage(imagem2, x1,y1, width=400,height=145)
                                    
                        c = canvas.Canvas(f"./Data/geral_{usuario}.pdf")
                        hh = hello(c,pmg)
                        c.save()
            
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
                st.title(tltle_list)

            st.markdown("---")
            tab26,tab27,tab28,tab29= st.tabs(tabs_list_sol)
            with tab26:
                st.header(header_list, divider='blue')
                col9,col10= st.columns([5,5])  
                with col9:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas13 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln14,value=allln14,placeholder="Selecione!",)
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Ivson Paulino',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, ('Ivson Paulino',),index=0,placeholder='Atualize',help=help_solicitante)
                        
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                        
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Ferramentaria',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl, ('Ferramentaria',),index=0,placeholder='Atualize',help=help_setor)
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione!',help=helpe_acao)
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize',help=helpe_acao)

                    if not atd1:
                        especialidades = container.selectbox(especialidades_titulo, ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                                                
                    if Rsetor != 'Extrusão' and Rsetor != 'Produção' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Produção' and RUsetor != 'Utilidades':
                        Local = container.selectbox(local_titulo,('Manutenção Predial','Maquina de jatear','Talha Elétrica','Recuperação de ferramentas'),index=None,placeholder= 'Selecione!',help=help_local)
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione!")
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
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_Ferramentaria = ids_shape + 1
                                    if insdds:
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Ferramentaria}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_Ferramentaria,str(timenow),datenow,monthnow,Local))    
                                        cursor.execute("INSERT INTO Ferramentaria (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?,?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_Ferramentaria , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_Ferramentaria,bytes_data,monthnow))
                                        conn1.commit()
                                        
            with tab27:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button(' Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas13 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas13,value=whrlinhas13,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas13)
                            numros23 = numros22-1
                            osespec5 = whrlinhas12.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec5)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab28:
                st.header(finalizadas_list, divider='blue')
                st.button(' Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd1 == 0:
                        st.success('Não há pendências')
                    else:
                        numros16 = st.number_input("Selecione o numero da   O.S",min_value=1,max_value=rd1,value=rd1,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd1)
                        numros17 = numros16-1
                        osespec6 = rd.loc[numros17]
                        def load_data():
                            return pd.DataFrame(osespec6)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab29:
                st.header (aviso_list,divider='blue')
                omaga = st.multiselect('Selecione:',acao_list,max_selections=1)
                if not omaga == []:
                    corretivas = pd.read_sql_query(f"SELECT * FROM Ferramentaria WHERE AÇÃO = '{omaga[0]}'", conn)
                    corretivas_shape = corretivas.shape[0]
                if omaga == []:
                    st.success('Escolha um tipo de ação')
                else:
                    if corretivas_shape == 0:
                        st.success('Não há pendências')
                    else:
                        st.metric(label="O.S Existentes", value=corretivas_shape)
                        numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=corretivas_shape,value=corretivas_shape,placeholder="Selecione!")
                        numros3 = numros2-1
                        serie_pdf = corretivas.loc[numros3]
                        def load_data():
                            return pd.DataFrame(serie_pdf)
                        st.checkbox("Estender", value=True, key="use_container_width17")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width17)
                        dt = corretivas.loc[numros3]
                        dt = dt.tolist()
        
                        with open(f"./Data/geral_Ferramentaria.pdf",'rb') as file:
                            pdf_reader = PyPDF2.PdfReader(file)
                            bttn = st.download_button(
                            label="Exportar O.S 🖨",
                            key= "download_button",
                            data= file,
                            file_name=f"O.S {dt[0]}.pdf",
                            mime='application/octet-stream'
                        )
                        
                        usuario = 'Ferramentaria'
                        cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                        if cursor1.fetchall():
                            cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                            imagens = cursor1.fetchall()
                            oe = imagens[0][1]
                            imagem = Image.open(BytesIO(oe))

                        localx = corretivas.loc[numros3]
                        pmg = localx.tolist()
                        Solicitante = solicitante_titulo
                        Data = 'Data:'
                        Hora = 'Horario:'
                        Setor = 'Setor:'
                        Os = 'O.S:'
                        maqx = local_titulo
                        dados = [Solicitante,Data,Hora,Setor,Os,maqx,'']
                        img = Image.open('./Midia/ssmm.jpg')
                        img1 = Image.open('./Midia/sales.jpeg')

                        def hello(c,pmg):
                            o = 0
                            b = []
                            for s in str(pmg[1]):
                                if s.isalpha():
                                    o += 1
                                    tmh = 4 * o + 58 
                                    b.append(tmh)

                            ct = []
                            for s in str(pmg[2]):
                                if not pmg[2] =='Produção':
                                    if s.isalpha():
                                        o += 1
                                        tmh = 4 * o + 268
                                        ct.append(tmh)
                                    else:
                                        ''
                            idx = 0             
                            for james in dados:
                                idx = idx + 1
                                largura_da_linha = 0.1
                                width, height = 580, 50
                                raio = 10
                                if idx == 1:
                                #SOLICITANTE
                                    t1,t2 = 15,730
                                    t3,t4 = 58,730
                                    t5,t6 = 20,662
                                    t7,t8 = 380,662
                                    t9,t10 = 500,210
                                    t11,t12 = 90,642

                                    texto = f'{pmg[1]}'
                                    text = f'{pmg[5]}'
                                    textox = 'Grau de ocorrência :'
                                    textoxx = 'Especialidade :'
                                    textos = ''
                                    x1, y1 = b[9], 728
                                    x2, y2 = 58, 728
                                    widt, heigh = 200, 30
                                    r,r1 = 18,630
                                    r2,r3 = 380,630
                                    k1,k2,k3,k4 = 250,680,250,420
                                if idx == 2:
                                #DAT
                                    t1,t2 = 15,705
                                    t3,t4 = 38,705
                                    t5,t6 = 18,583
                                    t7,t8 = 380,583
                                    t9,t10 = 500,210
                                    t11,t12 = 90,563

                                    texto = f'{pmg[6]}'
                                    text = f'{pmg[8]}'
                                    textox = 'Ação :'
                                    textoxx = 'Data de finalização :'
                                    textos = ''
                                    x1, y1 = 75, 703
                                    x2, y2 = 37, 703
                                    r,r1 = 18,550
                                    r2,r3 = 380,550
                                    k1,k2,k3,k4 = 350,680,350,420
                                if idx == 3:
                                    #HORA
                                    t1,t2 = 250,730
                                    t3,t4 = 283,730
                                    t5,t6 = 18,513
                                    t7,t8 = 380,513
                                    t9,t10 = 500,210
                                    t11,t12 = 90,493

                                    texto = f'{pmg[7]}'
                                    text = f'{pmg[9]}'
                                    textox = 'Finalizada? :'
                                    textoxx = 'Horario de finalização :'
                                    textos = ''

                                    x1, y1 = 283, 728
                                    x2, y2 = 310, 728
                                    r,r1 = 18,480
                                    r2,r3 = 380,480
                                    k1,k2,k3,k4 = 500,10,580,10
                                if idx == 4:
                                #SETOR
                                    t1,t2 = 250,705
                                    t3,t4 = 275,705
                                    t5,t6 = 18,422
                                    t9,t10 = 510,15
                                    t11,t12 = 430,642

                                    texto = f'{pmg[2]}'
                                    text = f'{pmg[12]}'
                                    textox = 'Ocorrência :'
                                    textos = 'Bruno Kappaun'
        
                                    x1, y1 = 275, 703
                                    x2, y2 = ct[0], 703
                                    widt, heigh = 560, 60
                                    r,r1 = 18,360
                                if idx == 5:
                                    #OS
                                    t1,t2 = 430,730
                                    t3,t4 = 448,730
                                    t5,t6 = 25,345
                                    t11,t12 = 430,563

                                    texto = f'N° 00{pmg[0]}'
                                    text = f'{pmg[10]}'
                                    textox = 'Visualização do problema:'
                                    x1, y1 = 448, 728
                                    x2, y2 = 475, 728
                                if idx == 6:
                                #maquina
                                    t1,t2 = 430,705
                                    t3,t4 = 455,705
                                    t5,t6 = 30,170
                                    t11,t12 = 430,493
                                    texto =f'{pmg[13]}'
                                    textox = 'Visualização pós problema:'
                                    text = f'{pmg[11]}'
                                    x1, y1 = 455, 703
                                    x2, y2 = 510, 703
                                if idx == 7:
                                    t11,t12 = 25,410
                                    text = f'{pmg[3]}'
                
                                pdfmetrics.registerFont(TTFont('font', './Fontes/ASENINE_.ttf'))
                                cor_do_texto = (0,0,0)
                                font_name = 'font' 

                                pdfmetrics.registerFont(TTFont('ASS', './Fontes/ASSINATURA.ttf'))
                                cor_do_texto = (0,0,0)
                                font_namex = 'ASS' 
            
                                textobject = c.beginText(t1, t2)
                                textobject.setFont(font_name , 13)
                                textobject.setTextOrigin(t1, t2)
                                textobject.textLine(f"{james}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobject)
                                c.setLineWidth(largura_da_linha)
                                c.line(x1,y1,x2,y2)
        
                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t3, t4)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t3, t4)
                                textobjectx.textLine(f"{texto}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t5, t6)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t5, t6)
                                textobjectx.textLine(f"{textox}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t7, t8)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t7, t8)
                                textobjectx.textLine(f"{textoxx}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t9, t10)
                                textobjectx.setFont(font_namex, 10)
                                textobjectx.setTextOrigin(t9, t10)
                                textobjectx.textLine(f"{textos}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t11, t12)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t11, t12)
                                textobjectx.textLine(f"{text}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                raio = 5
                                c.roundRect(r, r1, widt, heigh, raio, stroke=1, fill=0)

                                width, height = 200, 30
                                raio = 5
                                c.roundRect(r2, r3, width, height, raio, stroke=1, fill=0)
                                c.line(k1,k2,k3,k4)
                            width, height = 700, 50
                            raio = 10
                            r,r1 = 8,800
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                            width, height = 580, 680
                            raio = 10
                            r,r1 = 8,0
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)
    
                            x, y = 0,750
                            c.drawInlineImage(img, x,y, width=600,height=100)
                            x, y = 10,180
                            x1,y1 = 10, 20
                            if not corretivas.empty:
                                cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                if cursor1.fetchall():
                                    cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                    imagens = cursor1.fetchall()
                                    imagens
                                    if imagens[0][1]:
                                        oe = imagens[0][1]
                                        imagem = Image.open(BytesIO(oe))
                                        c.drawInlineImage(imagem, x,y, width=400,height=145)  
                                    if imagens[0][2]:
                                        oie = imagens[0][2]
                                        imagem2 = Image.open(BytesIO(oie))
                                        c.drawInlineImage(imagem2, x1,y1, width=400,height=145)
                    
                        c = canvas.Canvas(f"./Data/geral_{usuario}.pdf")
                        hh = hello(c,pmg)
                        c.save()

if fLIDERES == 'Maurilio Sales/Alex Santos':
    if fSETOR == 'Produção':
        if senha == '1405':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl6 = st.button("DELETAR TABELA")
            #if cl6:
                #cursor.execute("DROP TABLE PRODUCAO")
                #conn.commit()
            with ps6:
                st.title(tltle_list)
            st.markdown("---")
            tab30,tab31,tab32,tab33= st.tabs(tabs_list_sol)
            with tab30:
                st.header(header_list, divider='blue')
                col11,col12= st.columns([5,5])  
                with col11:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln16 == 0:
                           numros = 0
                           numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln16,value=allln16,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Maurilio Sales/Alex Santos',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, ('Maurilio Sales/Alex Santos',),index=0,placeholder='Atualize!',help=help_solicitante)
                        
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Produção',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                        
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl, ('Produção',),index=0,placeholder='Atualize!',help=help_setor)
                        Rsetor = ''

                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, (ocorrencia_list),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,(ocorrencia_list),index=None, placeholder='Atualize!',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, (acao_list),index=None,placeholder='Selecione!',help=helpe_acao)
                        RUacao = ' '
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, (acao_list),index=None,placeholder='Atualize!',help=helpe_acao)
                        Racao = ' '

                    if Rsetor == 'Produção' or RUsetor == 'Produção':
                        if not atd1:
                            segmento = container.selectbox('Defina o segmento de produção:', ('Extrusão','Estampo','Corte','Rosca e Furo','Embalagem'),index=None,placeholder='Selecione!',help=help_setor)
                        if atd1:
                            segmento = container.selectbox('Atualize o segmento de produção:', ('Extrusão','Estampo','Corte','Rosca e Furo','Embalagem'),index=None,placeholder='Atualize!',help=help_setor)
                        if not segmento == None:
                            comb = (f'{Rsetor} {segmento} {Racao}')
                    else:
                        comb = (f'{Rsetor} {Racao}')
                    
                    if not atd1:
                        parada = container.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                    if atd1:
                        parada = container.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                    
                    if not atd1: 
                        especialidades = container.selectbox(especialidades_titulo, (especialidade_list),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl, (especialidade_list),index=None,placeholder='Atualize!',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                            
                    if Rsetor == 'Produção' or RUsetor == 'Produção':
                        if not segmento == None:
                            if comb == 'Produção Extrusão Corretiva' or comb == 'Produção Extrusão Preventiva' or comb == 'Produção Extrusão Preditiva':
                                Local = container.selectbox(local_titulo,(extrusão_list),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Extrusão Confecção' or comb == 'Produção Extrusão Montagem':
                                Local = container.selectbox(local_titulo,(extrusão_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Estampo Corretiva' or comb == 'Produção Estampo Preventiva' or comb == 'Produção Estampo Preditiva':
                                Local = container.selectbox(local_titulo,(estampo_list),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Estampo Confecção' or comb == 'Produção Estampo Montagem':
                                Local = container.selectbox(local_titulo,(estampo_list_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Embalagem Corretiva' or comb == 'Produção Embalagem Preventiva' or comb == 'Produção Embalagem Preditiva':
                                Local = container.selectbox(local_titulo,(embalagem),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Embalagem Confecção' or comb == 'Produção Embalagem Montagem':
                                Local = container.selectbox(local_titulo,(embalagem_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Rosca e Furo Corretiva' or comb == 'Produção Rosca e Furo Preventiva' or comb == 'Produção Rosca e Furo Preditiva':
                                Local = container.selectbox(local_titulo,(rosca_e_furo),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Rosca e Furo Confecção' or comb == 'Produção Rosca e Furo Montagem':
                                Local = container.selectbox(local_titulo,(rosca_e_furo_â),index=None,placeholder= 'Selecione!',help=help_local)
                            
                            if comb == 'Produção Corte Corretiva' or comb == 'Produção Corte Preventiva' or comb == 'Produção Corte Preditiva':
                                Local = container.selectbox(local_titulo,(corte),index=None,placeholder= 'Selecione!',help=help_local)
                            elif comb == 'Produção Corte Confecção' or comb == 'Produção Corte Montagem':
                                Local = container.selectbox(local_titulo,(corte_â),index=None,placeholder= 'Selecione!',help=help_local) 
                        else:
                            Local =  ' '

                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=int(preenchimento[0]),max_value=int(preenchimento[0]),value=int(preenchimento[0]),placeholder="Selecione!")
                            dell = st.button('Excluir 🗑')
                            if dell:
                                st.toast(f'Deletando O.S!')
                                time.sleep(0.5)
                                st.toast(f'O.S [{numero_da_os}] Deletada!')
                                cursor.execute(f'DELETE FROM PRODUCAO WHERE OS = {numero_da_os};')
                                conn.commit()

                if fLIDERES == 'Maurilio Sales/Alex Santos':
                    if fSETOR == 'Produção':
                        if senha == '1405':
                            if atd1:
                                atl1 = st.button('Atualize ↻')
                                if atl1:
                                    st.balloons()
                                    st.toast('Atualizando O.S!')
                                    time.sleep(0.5)
                                    cursor.execute("UPDATE PRODUCAO SET  OCORRENCIA = ?,GRAU = ?, AÇÃO = ?, MANUTENTOR = ?,SEGMENTO = ? WHERE OS = ?",(RUstatus,RUniveldaocorrencia,RUacao,manutentor,segmento,int(preenchimento[0])))
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
                    
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_producao = ids_shape + 1
                                    if insdds:
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_producao}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_producao,str(timenow),datenow,monthnow,Local))                      
                                        cursor.execute("INSERT INTO PRODUCAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA,SEGMENTO) VALUES (?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)", (ids_shape_producao , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,parada,segmento))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_producao,bytes_data,monthnow))
                                        conn1.commit()
            with tab31:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button(' Atualize  ↻ ')
                    with st.expander("Abertas"):
                        if whrlinhas19 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas19,value=whrlinhas19,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas19)
                            numros23 = numros22-1
                            osespec9 = whrlinhas18.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec9)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab32:
                st.header(finalizadas_list, divider='blue')
                st.button(' Atualize   ↻ ')
                with st.expander("Finalizadas"):
                    if rd5 == 0:
                        st.success('Não há pendências')
                    else:
                        numros18 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd5,value=rd5,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd5)
                        numros19 = numros18-1
                        osespec10 = rd4.loc[numros19]
                        def load_data():
                            return pd.DataFrame(osespec10)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab33:
                st.header (aviso_list,divider='blue')
                omaga = st.multiselect('Selecione:',acao_list,max_selections=1)
                if not omaga == []:
                    corretivas = pd.read_sql_query(f"SELECT * FROM PRODUCAO WHERE AÇÃO = '{omaga[0]}'", conn)
                    corretivas_shape = corretivas.shape[0]
                if omaga == []:
                    st.success('Escolha um tipo de ação')
                else:
                    if corretivas_shape == 0:
                        st.success('Não há pendências')
                    else:
                        st.metric(label="O.S Existentes", value=corretivas_shape)
                        numros2 = st.number_input("Selecione o numero da O.S",min_value=1,max_value=corretivas_shape,value=corretivas_shape,placeholder="Selecione!")
                        numros3 = numros2-1
                        serie_pdf = corretivas.loc[numros3]
                        def load_data():
                            return pd.DataFrame(serie_pdf)
                        st.checkbox("Estender", value=True, key="use_container_width17")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width17)
                        dt = corretivas.loc[numros3]
                        dt = dt.tolist()
    
                        with open(f"./Data/geral_Produção.pdf", 'rb') as file:
                            pdf_reader = PyPDF2.PdfReader(file)
                            bttn = st.download_button(
                            label="Exportar O.S 🖨",
                            key= "download_button",
                            data= file,
                            file_name=f"O.S {dt[0]}.pdf",
                            mime='application/octet-stream'
                        )
                        usuario = 'Produção'
                        cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                        if cursor1.fetchall():
                            cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                            imagens = cursor1.fetchall()
                            oe = imagens[0][1]
                            imagem = Image.open(BytesIO(oe))
                        localx = corretivas.loc[numros3]
                        pmg = localx.tolist()
                        Solicitante = solicitante_titulo
                        Data = 'Data:'
                        Hora = 'Horario:'
                        Setor = 'Setor:'
                        Os = 'O.S:'
                        maqx = local_titulo
                        dados = [Solicitante,Data,Hora,Setor,Os,maqx,'']
                        img = Image.open('./Midia/ssmm.jpg')
                        img1 = Image.open('./Midia/sales.jpeg')

                        def hello(c,pmg):
                            o = 0
                            b = []
                            for s in str(pmg[1]):
                                if s.isalpha():
                                    o += 1
                                    tmh = 4 * o + 58 
                                    b.append(tmh)

                            ct = []
                            for s in str(pmg[2]):
                                if not pmg[2] =='Produção':
                                    if s.isalpha():
                                        o += 1
                                        tmh = 4 * o + 268
                                        ct.append(tmh)
                                    else:
                                        ''
                            idx = 0             
                            for james in dados:
                                idx = idx + 1
                                largura_da_linha = 0.1
                                width, height = 580, 50
                                raio = 10
                                if idx == 1:
                                #SOLICITANTE
                                    t1,t2 = 15,730
                                    t3,t4 = 58,730
                                    t5,t6 = 20,662
                                    t7,t8 = 380,662
                                    t9,t10 = 500,210
                                    t11,t12 = 90,642

                                    texto = f'{pmg[1]}'
                                    text = f'{pmg[5]}'
                                    textox = 'Grau de ocorrência :'
                                    textoxx = 'Especialidade :'
                                    textos = ''
                                    x1, y1 = b[9], 728
                                    x2, y2 = 58, 728
                                    widt, heigh = 200, 30
                                    r,r1 = 18,630
                                    r2,r3 = 380,630
                                    k1,k2,k3,k4 = 250,680,250,420
                                if idx == 2:
                                #DAT
                                    t1,t2 = 15,705
                                    t3,t4 = 38,705
                                    t5,t6 = 18,583
                                    t7,t8 = 380,583
                                    t9,t10 = 500,210
                                    t11,t12 = 90,563

                                    texto = f'{pmg[6]}'
                                    text = f'{pmg[8]}'
                                    textox = 'Ação :'
                                    textoxx = 'Data de finalização :'
                                    textos = ''
                                    x1, y1 = 75, 703
                                    x2, y2 = 37, 703
                                    r,r1 = 18,550
                                    r2,r3 = 380,550
                                    k1,k2,k3,k4 = 350,680,350,420
                                if idx == 3:
                                    #HORA
                                    t1,t2 = 250,730
                                    t3,t4 = 283,730
                                    t5,t6 = 18,513
                                    t7,t8 = 380,513
                                    t9,t10 = 500,210
                                    t11,t12 = 90,493

                                    texto = f'{pmg[7]}'
                                    text = f'{pmg[9]}'
                                    textox = 'Finalizada? :'
                                    textoxx = 'Horario de finalização :'
                                    textos = ''

                                    x1, y1 = 283, 728
                                    x2, y2 = 310, 728
                                    r,r1 = 18,480
                                    r2,r3 = 380,480
                                    k1,k2,k3,k4 = 500,10,580,10
                                if idx == 4:
                                #SETOR
                                    t1,t2 = 250,705
                                    t3,t4 = 275,705
                                    t5,t6 = 18,422
                                    t9,t10 = 510,15
                                    t11,t12 = 430,642

                                    texto = f'{pmg[2]}'
                                    text = f'{pmg[12]}'
                                    textox = 'Ocorrência :'
                                    textos = 'Bruno Kappaun'
        
                                    x1, y1 = 275, 703
                                    x2, y2 = ct[0], 703
                                    widt, heigh = 560, 60
                                    r,r1 = 18,360
                                if idx == 5:
                                    #OS
                                    t1,t2 = 430,730
                                    t3,t4 = 448,730
                                    t5,t6 = 25,345
                                    t11,t12 = 430,563

                                    texto = f'N° 00{pmg[0]}'
                                    text = f'{pmg[10]}'
                                    textox = 'Visualização do problema:'
                                    x1, y1 = 448, 728
                                    x2, y2 = 475, 728
                                if idx == 6:
                                #maquina
                                    t1,t2 = 430,705
                                    t3,t4 = 455,705
                                    t5,t6 = 30,170
                                    t11,t12 = 430,493
                                    texto =f'{pmg[13]}'
                                    textox = 'Visualização pós problema:'
                                    text = f'{pmg[11]}'
                                    x1, y1 = 455, 703
                                    x2, y2 = 510, 703
                                if idx == 7:
                                    t11,t12 = 25,410
                                    text = f'{pmg[3]}'
                
                                pdfmetrics.registerFont(TTFont('font', './Fontes/ASENINE_.ttf'))
                                cor_do_texto = (0,0,0)
                                font_name = 'font' 

                                pdfmetrics.registerFont(TTFont('ASS', './Fontes/ASSINATURA.ttf'))
                                cor_do_texto = (0,0,0)
                                font_namex = 'ASS' 
            
                                textobject = c.beginText(t1, t2)
                                textobject.setFont(font_name , 13)
                                textobject.setTextOrigin(t1, t2)
                                textobject.textLine(f"{james}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobject)
                                c.setLineWidth(largura_da_linha)
                                c.line(x1,y1,x2,y2)
        
                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t3, t4)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t3, t4)
                                textobjectx.textLine(f"{texto}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t5, t6)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t5, t6)
                                textobjectx.textLine(f"{textox}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t7, t8)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t7, t8)
                                textobjectx.textLine(f"{textoxx}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,0)
                                textobjectx = c.beginText(t9, t10)
                                textobjectx.setFont(font_namex, 10)
                                textobjectx.setTextOrigin(t9, t10)
                                textobjectx.textLine(f"{textos}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                cor_do_texto = (0,0,1)
                                textobjectx = c.beginText(t11, t12)
                                textobjectx.setFont(font_name, 10)
                                textobjectx.setTextOrigin(t11, t12)
                                textobjectx.textLine(f"{text}")
                                c.setFillColor(cor_do_texto)
                                c.drawText(textobjectx)

                                raio = 5
                                c.roundRect(r, r1, widt, heigh, raio, stroke=1, fill=0)

                                width, height = 200, 30
                                raio = 5
                                c.roundRect(r2, r3, width, height, raio, stroke=1, fill=0)
                                c.line(k1,k2,k3,k4)
                            width, height = 700, 50
                            raio = 10
                            r,r1 = 8,800
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                            width, height = 580, 680
                            raio = 10
                            r,r1 = 8,0
                            c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                            x, y = 0,750
                            c.drawInlineImage(img, x,y, width=600,height=100)
                            x, y = 10,180
                            x1,y1 = 10, 20
                            if not corretivas.empty:
                                cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                if cursor1.fetchall():
                                    cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                                    imagens = cursor1.fetchall()
                                    imagens
                                    if imagens[0][1]:
                                        oe = imagens[0][1]
                                        imagem = Image.open(BytesIO(oe))
                                        c.drawInlineImage(imagem, x,y, width=400,height=145)  
                                    if imagens[0][2]:
                                        oie = imagens[0][2]
                                        imagem2 = Image.open(BytesIO(oie))
                                        c.drawInlineImage(imagem2, x1,y1, width=400,height=145)   
                    
                        c = canvas.Canvas(f"./Data/geral_{usuario}.pdf")
                        hh = hello(c,pmg)
                        c.save()

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
                st.title(tltle_list)

            st.markdown("---")
            tab34,tab35,tab36,tab37= st.tabs(tabs_list_sol)
            with tab34:
                st.header(header_list, divider='blue')
                col13,col14= st.columns([5,5])  
                with col13:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if allln18 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln18 ,value=allln18 ,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Gilson Freitas',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(setor_titulo_atl ('Gilson Freitas',),index=0,placeholder='Atualize',help=help_solicitante)
                    
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Administrativo',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl,('Administrativo',),index=0,placeholder='Atualize',help=help_setor)
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione!',help=helpe_acao)
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize',help=helpe_acao)

                    if not atd1:
                        especialidades = container.selectbox(especialidades_titulo, ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                                        
                    if Rsetor != 'Extrusão' and Rsetor != 'Produção' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Produção' and RUsetor != 'Utilidades':
                        Local = container.selectbox(local_titulo,('Manutenção Predial','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone'),index=None,placeholder= 'Selecione!',help=help_local)
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione!")
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
                    
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_Administrativo = ids_shape + 1
                                    if insdds:
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Administrativo}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_Administrativo,str(timenow),datenow,monthnow,Local))
                                        cursor.execute("INSERT INTO Administrativo (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?, ?,  ?,?, ?, ?,?,?,?,?,?,?)", (ids_shape_Administrativo , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn1.commit()
                                        
            with tab35:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button(' Atualize ↻  ')
                    with st.expander("Abertas"):
                        if whrlinhas24 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  O.S",min_value=1,max_value=whrlinhas24,value=whrlinhas24,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas24)
                            numros23 = numros22-1
                            osespec13 = whrlinhas23.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec13)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab36:
                st.header(finalizadas_list, divider='blue')
                st.button('Atualize ↻        ')
                with st.expander("Finalizadas"):
                    if rd9 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        numros20 = st.number_input("Selecione o numero da   O.S",min_value=1,max_value=rd9,value=rd9,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd9)
                        numros21 = numros20-1
                        osespec14 = rd8.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec14)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab37:
                st.header(aviso_list, divider='blue')
                st.button('Atualize ↻   ')
                with st.expander("Geral"):
                    if allln18 == 0:
                        st.success('Não há pendências')
                    else:
                        numros20 = st.number_input("Selecione o numero da    O.S",min_value=1,max_value=allln18,value=allln18,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= allln18)
                        numros21 = numros20-1
                        osespec15 = allln17.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec15)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

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
                st.title(tltle_list)
            st.markdown("---")
            tab38,tab39,tab40,tab41= st.tabs(tabs_list_sol)
            with tab38:
                st.header(header_list, divider='blue')
                col15,col16= st.columns([5,5])  
                with col15:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas29 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=whrlinhas29 ,value=whrlinhas29 ,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Adriely Lemos',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, ('Adriely Lemos',),index=0,placeholder='Atualize',help=help_solicitante)
                    
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atlvalue=preenchimento[3],placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Comercial',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl,('Comercial',),index=0,placeholder='Atualize',help=help_setor)
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione!',help=helpe_acao)
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize',help=helpe_acao)

                    if not atd1:
                        especialidades = container.selectbox(especialidades_titulo, ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                                        
                            
                    if Rsetor != 'Extrusão' and Rsetor != 'Produção' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Produção' and RUsetor != 'Utilidades':
                        Local = container.selectbox(local_titulo,('Manutenção Predial'),index=None,placeholder= 'Selecione!',help=help_local)
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione!")
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
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_Comercial = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Comercial}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_Comercial,str(timenow),datenow,monthnow,Local))
                                        cursor.execute("INSERT INTO Comercial (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?, ?,?,?,? ,?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_Comercial , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn1.commit()
                                             
            with tab39:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button('  Atualize ↻ ')
                    with st.expander("Abertas"):
                        if whrlinhas29 == 0:
                            st.success('Não há pendências')
                        else:
                            numros22 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas29,value=whrlinhas29,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas29)
                            numros23 = numros22-1
                            osespec17 = whrlinhas28.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec17)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab40:
                st.header(finalizadas_list, divider='blue')
                st.button(' Atualize ↻  ' )
                with st.expander("Finalizadas"):
                    if rd13 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        numros22 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd13,value=rd13,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd13)
                        numros23 = numros22-1
                        osespec18 = rd12.loc[numros23]
                        def load_data():
                            return pd.DataFrame(osespec18)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab41:
                st.header(aviso_list, divider='blue')
                st.button(' Atualize ↻ ')
                with st.expander("Geral"):
                    if allln20 == 0:
                        st.success('Não há pendências')
                    else:
                        numros22 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln20,value=allln20,placeholder="Selecione!")
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
                st.title(tltle_list)

            st.markdown("---")
            tab42,tab43,tab44,tab45= st.tabs(tabs_list_sol)
            with tab42:
                st.header(header_list, divider='blue')
                col17,col18= st.columns([5,5])  
                with col17:
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas34 == 0:
                            numros1 = 0
                            numros = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln22,value=allln22,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Willian Oliveira',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, ('Willian Oliveira',),index=0,placeholder='Atualize',help=help_solicitante)
                    
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Expedição',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl,('Expedição',),index=0,placeholder='Atualize',help=help_setor)
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione!',help=helpe_acao)
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize',help=helpe_acao)

                    if not atd1:
                        especialidades = container.selectbox(especialidades_titulo, ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                   
                    if Rsetor != 'Extrusão' and Rsetor != 'Produção' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Produção' and RUsetor != 'Utilidades':
                        Local = container.selectbox(local_titulo,('Manutenção Predial'),index=None,placeholder= 'Selecione!',help=help_local)
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione!")
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
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_expedicao = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_expedicao}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_expedicao,str(timenow),datenow,monthnow,Local))
                                        cursor.execute("INSERT INTO EXPEDICAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?, ?,?, ?, ?, ?,?,?,?,?,?,?)", (ids_shape_expedicao, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn1.commit()
                                    
            with tab43:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas34 == 0:
                            st.success('Não há pendências')
                        else:
                            numros24 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas34,value=whrlinhas34,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas34)
                            numros25 = numros24-1
                            osespec21 = whrlinhas33.loc[numros25]
                            def load_data():
                                return pd.DataFrame(osespec21)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab44:
                st.header(finalizadas_list, divider='blue')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd17 == 0:
                        st.success('Não há pendências')
                    else:
                        numros24 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd17,value=rd17,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd17)
                        numros25 = numros24-1
                        osespec22 = rd16.loc[numros25]
                        def load_data():
                            return pd.DataFrame(osespec22)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab45:
                st.header(aviso_list, divider='blue')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    if allln22 == 0:
                        st.success('Não há pendências')
                    else:
                        numros24 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln22,value=allln22,placeholder="Selecione!")
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
                st.title(tltle_list)

            st.markdown("---")
            tab46,tab47,tab48,tab49= st.tabs(tabs_list_sol)
            with tab46:
                st.header(header_list, divider='blue')
                col19,col20= st.columns([5,5])  
                with col19:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas39 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln24 ,value=allln24 ,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Cesar Augusto',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, ('Cesar Augusto',),index=0,placeholder='Atualize',help=help_solicitante)
                    
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Serralharia',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl,('Serralharia',),index=0,placeholder='Atualize',help=help_setor)
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione!',help=helpe_acao)
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize',help=helpe_acao)

                    if not atd1:
                        especialidades = container.selectbox(especialidades_titulo, ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                                          
                    if Rsetor != 'Extrusão' and Rsetor != 'Produção' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Produção' and RUsetor != 'Utilidades':
                        Local = container.selectbox(local_titulo,('Manutenção Predial','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Serra fita - FRANHO'),index=None,placeholder= 'Selecione!',help=help_local)
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=preenchimento[0],placeholder="Selecione!")
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
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_Serralharia = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_Serralharia}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_Serralharia,str(timenow),datenow,monthnow,Local))
                                        cursor.execute("INSERT INTO Serralharia (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?, ?, ?, ?, ?,?,?,?,?,?,?,?)", (ids_shape_Serralharia, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn1.commit()
                                                    
            with tab47:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas39 == 0:
                            st.success('Não há pendências')
                        else:
                            numros26 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas39,value=whrlinhas39,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas39)
                            numros27 = numros26-1
                            osespec25 = whrlinhas38.loc[numros27]
                            def load_data():
                                return pd.DataFrame(osespec25)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab48:
                st.header(finalizadas_list, divider='blue')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd21 == 0:
                        st.success('Não há pendências')
                    else:
                        numros26 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd21,value=rd21,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd21)
                        numros27 = numros26-1
                        osespec26 = rd20.loc[numros27]
                        def load_data():
                            return pd.DataFrame(osespec26)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab49:
                st.header(aviso_list, divider='blue')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    if allln24 == 0:
                        st.success('Não há pendências')
                    else:
                        numros26 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln24,value=allln24,placeholder="Selecione!")
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
                st.title(tltle_list)

            st.markdown("---")
            tab50,tab51,tab52,tab53= st.tabs(tabs_list_sol)
            with tab50:
                st.header(header_list, divider='blue')
                col21,col22= st.columns([5,5])  
                with col21:                  
                    atd1 = st.toggle('Atualizar os dados')
                    if atd1:
                        if whrlinhas44 == 0:
                            numros = 0
                            numros1 = 0
                        else:
                            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=1,max_value=allln26 ,value=allln26 ,placeholder="Selecione!")
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
                        Rsolicitante = container.selectbox(solicitante_titulo, ('Filipe Leite',),index=0,placeholder='Selecione!',help=help_solicitante)
                    if atd1:
                        RUsolicitante = container.selectbox(solicitante_titulo_atl, ('Filipe Leite',),index=0,placeholder='Atualize',help=help_solicitante)
                    
                    if not atd1:
                        Rstatus = container.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    if atd1:
                        RUstatus = container.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia',help=help_ocorrência)
                    
                    if not atd1:
                        Rsetor = container.selectbox(setor_titulo, ('Tecnologia da Informação',),index=0,placeholder='Selecione!',help=help_setor)
                        RUsetor = ''
                    if atd1:
                        RUsetor = container.selectbox(setor_titulo_atl,('Tecnologia da Informação',),index=0,placeholder='Atualize',help=help_setor)
                        Rsetor = ''
                    
                    if not atd1:
                        Rniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo, ('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                    if atd1:
                        RUniveldaocorrencia = container.selectbox(nivel_de_ocorrencia_titulo_atl,('Emergência','Muito urgênte','Pouco urgênte','Urgênte'),index=None, placeholder='Atualize',help=help_nivel_ocorrencia)

                    if not atd1:
                        Racao = container.selectbox(acao_titulo, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione!',help=helpe_acao)
                    if atd1:
                        RUacao = container.selectbox(acao_titulo_atl, ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Atualize',help=helpe_acao)

                    if not atd1:
                        especialidades = container.selectbox(especialidades_titulo, ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione!',help=help_especialidade)
                    if atd1:
                        especialidades = container.selectbox(especialidades_titulo_atl ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize',help=help_especialidade)
                    
                    if not atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                    if atd1:
                        manutentor = container.selectbox(manutentor_titulo, ('Elétrica','Mecânica'),index=None,placeholder='Selecione!',help=help_manutentor)
                                        
                    if Rsetor != 'Extrusão' and Rsetor != 'Produção' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Produção' and RUsetor != 'Utilidades':
                        Local = container.selectbox(local_titulo,('Manutenção Predial'),index=None,placeholder= 'Selecione!',help=help_local)
                    
                    if atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
                        for uploaded_file in uploaded_files:

                            bytes_data = uploaded_file.read()
                    if not atd1:   
                        uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True,help=help_imagem)
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
                            numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=1,max_value=1000,value=int(preenchimento[0]),placeholder="Selecione!")
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
                                    insdds = st.button("Enviar O.S 📤")
                                    if insdds:
                                        ids_shape_ti = ids_shape + 1
                                        st.balloons()                     
                                        st.toast('Enviando O.S!')
                                        time.sleep(0.5)
                                        st.toast(f'O.S [{ids_shape_ti}] Enviada!')
                                        cursor.execute('PRAGMA foreign_keys = ON;')
                                        cursor.execute("INSERT INTO ids (ID_UNIC,HORA,DATA,Mês,MAQUINA) VALUES (?,?,?,?,?)", (ids_shape_ti,str(timenow),datenow,monthnow,Local))                                     
                                        cursor.execute("INSERT INTO TI (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,Local,MÊS,PARADA) VALUES (?,?,?,?,?,?, ?, ?, ?, ?,?,?,?,?,?,?)", (ids_shape_ti, str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,Local,monthnow,'Sim'))
                                        conn.commit()
                                        cursor1.execute("INSERT INTO imagens (id,imagem_abertura,mes) VALUES (?,?,?)", (ids_shape_mecanica,bytes_data,monthnow))
                                        conn1.commit()
                                        conn.close()

            with tab51:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header(abertas_list, divider='blue')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        if whrlinhas44 == 0:
                            st.success('Não há pendências')
                        else:
                            numros28 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=whrlinhas44,value=whrlinhas44,placeholder="Selecione!")
                            st.metric(label="O.S Existentes", value= whrlinhas44)
                            numros29 = numros28-1
                            osespec29 = whrlinhas43.loc[numros29]
                            def load_data():
                                return pd.DataFrame(osespec29)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab52:
                st.header(finalizadas_list, divider='blue')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    if rd73 == 0:
                        st.success('Não há pendências')
                    else:
                        numros28 = st.number_input("Selecione o numero da   OS",min_value=1,max_value=rd73,value=rd73,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= rd73)
                        numros29 = numros28-1
                        osespec30 = rd72.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec30)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)
            
            with tab53:
                st.header(aviso_list, divider='blue')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):  
                    if allln26 == 0:
                        st.success('Não há pendências')
                    else:
                        numros28 = st.number_input("Selecione o numero da    OS",min_value=1,max_value=allln26,value=allln26,placeholder="Selecione!")
                        st.metric(label="O.S Existentes", value= allln26)
                        numros29 = numros28-1
                        osespec31 = allln25.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec31)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)
