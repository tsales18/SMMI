import pandas as pd
import streamlit as st
from PIL import Image
import time as time
import datetime as datetime
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, event
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, MetaData, Column, Integer, String, FLOAT, VARCHAR, Date, Time
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import Sequence
import webbrowser
import sqlite3
import openpyxl
import altair as alt


# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title=('MANUTENÇÃO SSM SOLAR DO BRASIL'),
    page_icon='SMMI',
    layout='wide',
    
    initial_sidebar_state='expanded',
    menu_items={""
        'Get Help': 'http://www.meusite.com.br',
        'Report a bug': "http://www.meuoutrosite.com.br",
        'About': "Na duvida,duvide!"
    }
)


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
                time.sleep(2)
                st.success("Pronto!")
    st.write("Bem Vindo")

    with st.expander('#$#$'):
        st.success('Nada além de um homem comum,com pensamentos comuns')
     
#cl = st.button("DELETAR TABELAS")
#if cl:
   #cursor.execute("DROP TABLE ABERTURA")
   #conn.commit()

if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if 'BANCOS' == 'BANCOS':
    conn1 = sqlite3.connect('ROSIVALDO')
    cursor1 = conn1.cursor()
    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS ROSIVALDO (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF
        )
'''   )
    conn4 = sqlite3.connect('FERRAMENTARIA')
    cursor4 = conn4.cursor()
    cursor4.execute('''
    CREATE TABLE IF NOT EXISTS FERRAMENTARIA (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
       
                   
    )
''')



    conn5 = sqlite3.connect('PRODUCAO')
    cursor5 = conn5.cursor()
    cursor5.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCAO (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
                   
    )
''')

    conn6 = sqlite3.connect('ADMINISTRATIVO')
    cursor6 = conn6.cursor()
    cursor6.execute('''
    CREATE TABLE IF NOT EXISTS ADMINISTRATIVO (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
                
       
                   
    )
''')

    conn7 = sqlite3.connect('COMERCIAL')
    cursor7 = conn7.cursor()
    cursor7.execute('''
    CREATE TABLE IF NOT EXISTS COMERCIAL (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
        
       
                   
    )
''')

    conn8 = sqlite3.connect('EXPEDICAO')
    cursor8 = conn8.cursor()
    cursor8.execute('''
    CREATE TABLE IF NOT EXISTS EXPEDICAO (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
       
                   
    )
''')

    conn9 = sqlite3.connect('SERRALHARIA')
    cursor9 = conn9.cursor()
    cursor9.execute('''
    CREATE TABLE IF NOT EXISTS SERRALHARIA (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
       
                   
    )
''')

    conn10 = sqlite3.connect('CESAR')
    cursor10 = conn10.cursor()
    cursor10.execute('''
    CREATE TABLE IF NOT EXISTS CESAR (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF
       
                   
    )
''')

    conn11 = sqlite3.connect('TI')
    cursor11 = conn11.cursor()
    cursor11.execute('''
    CREATE TABLE IF NOT EXISTS TI (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF,
        HORAF,
        MANUTENTOR
   
    )
''')                                                     

#leitura do banco rosivaldo
allln = pd.read_sql_query("SELECT * FROM ROSIVALDO", conn1)
allln1 = allln.shape[0]
consulta1 = "SELECT * FROM ROSIVALDO"
allinhas = pd.read_sql_query(consulta1, conn1)

#OS ABERTAS  NÃO FINALIZADAS
consulta2 = "SELECT * FROM ROSIVALDO WHERE FINALIZADA = 'Não'"
whrlinhas1 = pd.read_sql_query(consulta2, conn1)
whrlinhas2 = whrlinhas1.shape[0] 

#OS FINALIZADAS
consulta3 = "SELECT * FROM ROSIVALDO WHERE FINALIZADA = 'Sim'"
whrlinhas3 = pd.read_sql_query(consulta3, conn1)
whrlinhas4 = whrlinhas3.shape[0]

if 'FERRAMENTARIA' == 'FERRAMENTARIA':
    #feedback ferramentaria
    allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
    allln14 = allln13.shape[0]

    query = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Não'"
    rd2 = pd.read_sql_query(query, conn4)
    rd3 = rd2.shape[0]

    query1 = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Sim'"
    rd = pd.read_sql_query(query1, conn4)
    rd1 = rd.shape[0]

    query = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
    rd25 = pd.read_sql_query(query, conn4)
    rd26 = rd25.shape[0]

    query1 = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
    rd27 = pd.read_sql_query(query1, conn4)
    rd28 = rd27.shape[0]

    query = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
    rd29 = pd.read_sql_query(query, conn4)
    rd30 = rd29.shape[0]

    query1 = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
    rd31 = pd.read_sql_query(query1, conn4)
    rd32 = rd31.shape[0]

if 'PRODUÇÃO'=='PRODUÇÃO':
    #FEEDBACK PRODUÇÃO
    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não'"
    rd6 = pd.read_sql_query(query, conn5)
    rd7 = rd6.shape[0]

    query1 = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim'"
    rd4 = pd.read_sql_query(query1, conn5)
    rd5 = rd4.shape[0]

    allln15 = pd.read_sql_query("SELECT * FROM PRODUCAO", conn5)
    allln16 = allln15.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
    rd33 = pd.read_sql_query(query, conn5)
    rd34 = rd33.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
    rd35 = pd.read_sql_query(query, conn5)
    rd36 = rd35.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
    rd37 = pd.read_sql_query(query, conn5)
    rd38 = rd37.shape[0]

    query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
    rd39 = pd.read_sql_query(query, conn5)
    rd40 = rd39.shape[0]

    allln15 = pd.read_sql_query("SELECT * FROM PRODUCAO", conn5)
    allln16 = allln15.shape[0]
    consulta9 = "SELECT * FROM PRODUCAO"
    allinhas16 = pd.read_sql_query(consulta9, conn5)

    #OS ABERTAS  NÃO FINALIZADAS
    consulta10 = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não'"
    whrlinhas18 = pd.read_sql_query(consulta10, conn5)
    whrlinhas19 = whrlinhas18.shape[0]

    #OS FINALIZADAS
    cursor5.execute("SELECT * FROM PRODUCAO WHERE FINALIZADA = ?;", ('Sim',))
    whrlinhas20 = cursor5.fetchall()
    whrlinhas21 = pd.DataFrame(whrlinhas20)
    whrlinhas22 = whrlinhas21.shape[0]

if 'administrativo' == 'administrativo':
    #FEEDBACK ADMINISTRATIVO
    query = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Não'"
    rd10 = pd.read_sql_query(query, conn6)
    rd11 = rd10.shape[0]

    query1 = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Sim'"
    rd8 = pd.read_sql_query(query1, conn6)
    rd9 = rd8.shape[0]

    allln17 = pd.read_sql_query("SELECT * FROM ADMINISTRATIVO", conn6)
    allln18 = allln17.shape[0]

    query = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
    rd41 = pd.read_sql_query(query, conn6)
    rd42 = rd41.shape[0]

    query = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
    rd43 = pd.read_sql_query(query, conn6)
    rd44 = rd43.shape[0]

    query = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
    rd45 = pd.read_sql_query(query, conn6)
    rd46 = rd45.shape[0]

    query = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
    rd47 = pd.read_sql_query(query, conn6)
    rd48 = rd47.shape[0]

if 'comercial' == 'comercial':
    #FEEDBACK COMERCIAL
    query = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Não'"
    rd14 = pd.read_sql_query(query, conn7)
    rd15 = rd14.shape[0]

    query1 = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Sim'"
    rd12 = pd.read_sql_query(query1, conn7)
    rd13 = rd12.shape[0]

    allln19 = pd.read_sql_query("SELECT * FROM COMERCIAL", conn7)
    allln20 = allln19.shape[0]

    query = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
    rd49 = pd.read_sql_query(query, conn7)
    rd50 = rd49.shape[0]

    query = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
    rd51 = pd.read_sql_query(query, conn7)
    rd52 = rd51.shape[0]

    query = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
    rd53 = pd.read_sql_query(query, conn7)
    rd54 = rd53.shape[0]

    query = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
    rd55 = pd.read_sql_query(query, conn7)
    rd56 = rd55.shape[0]

if 'EXPEDIÇÃO' == 'EXPEDIÇÃO':
    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não'"
    rd18 = pd.read_sql_query(query, conn8)
    rd19 = rd18.shape[0]

    query1 = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim'"
    rd16 = pd.read_sql_query(query1, conn8)
    rd17 = rd16.shape[0]

    allln21 = pd.read_sql_query("SELECT * FROM EXPEDICAO", conn8)
    allln22 = allln21.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
    rd57 = pd.read_sql_query(query, conn8)
    rd58 = rd57.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
    rd59 = pd.read_sql_query(query, conn8)
    rd60 = rd59.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
    rd61 = pd.read_sql_query(query, conn8)
    rd62 = rd61.shape[0]

    query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
    rd63 = pd.read_sql_query(query, conn8)
    rd64 = rd63.shape[0]

if 'SERRALHARIA' == 'SERRALHARIA':
    #FEEDBACK SERRALHARIA
    query = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Não'"
    rd22 = pd.read_sql_query(query, conn9)
    rd23 = rd22.shape[0]

    query1 = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Sim'"
    rd20 = pd.read_sql_query(query1, conn9)
    rd21 = rd20.shape[0]

    allln23 = pd.read_sql_query("SELECT * FROM SERRALHARIA", conn9)
    allln24 = allln23.shape[0]

    query = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
    rd65 = pd.read_sql_query(query, conn9)
    rd66 = rd65.shape[0]

    query = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
    rd67 = pd.read_sql_query(query, conn9)
    rd68 = rd67.shape[0]

    query = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
    rd69 = pd.read_sql_query(query, conn9)
    rd70 = rd69.shape[0]

    query = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
    rd71 = pd.read_sql_query(query, conn9)
    rd72 = rd71.shape[0]

if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

query = "SELECT * FROM TI WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'ELÉTRICA'"
rd74 = pd.read_sql_query(query, conn11)
rd75 = rd74.shape[0]

query = "SELECT * FROM TI WHERE FINALIZADA = 'Sim' AND MANUTENTOR = 'MECÂNICA'"
rd76 = pd.read_sql_query(query, conn11)
rd77 = rd76.shape[0]

query = "SELECT * FROM TI WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'ELÉTRICA'"
rd78= pd.read_sql_query(query, conn11)
rd79 = rd78.shape[0]

query = "SELECT * FROM TI WHERE FINALIZADA = 'Não' AND MANUTENTOR = 'MECÂNICA'"
rd80 = pd.read_sql_query(query, conn11)
rd81 = rd80.shape[0]

#ELÉTRICA
if fLIDERES == 'EQUIPE DE ELÉTRICA':
    if fSETOR == 'ELÉTRICA':
        if senha == '1409':
            #cl1 = st.button("DELETAR TABELA")
            #if cl1:
                #cursor1.execute("DROP TABLE ROSIVALDO")
                #conn1.commit()
            image = Image.open('./Midia/ssmm.jpg')
            col1,col2 = st.columns([1,1])
            with col1:
                st.title('Status e informações de O.S')
            tab6, tab7,tab8,tab9,tab10= st.tabs(["|Cadastro|", "|Finalizar|","|OS Em aberto|","|OS Finalizadas|","|Geral|"])
            with tab6:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd1 = st.toggle('Atualizar os dados')
                    with st.form('my form3'):
                        st.markdown("---")
                        Rsolicitante = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        if atd1:
                            RUsolicitante = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Rstatus = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd1:
                            RUstatus = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Rsetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','UTILIDADES'),index=None,placeholder='Selecione')
                        if atd1:
                            RUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','UTILIDADES'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Rniveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd1:
                            RUniveldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Racao = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva','Instalação'),index=None,placeholder='Selecione')
                        if atd1:
                            RUacao = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva','Instalação'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd1:
                           #Urelatorio = st.text_input('Atualize o Relatorio')
                           #st.markdown("---")

                        Rtempoi = st.time_input('Horario', value=None)
                        if atd1:
                            RUtempoi = st.time_input('Atualize o Horario', value=None)
                            st.write(Rtempoi)

                        Rdata = st.date_input("Data", value=None)
                        if atd1:
                            RUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with neymar:
                    if atd1:
                        numros = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros1 = numros-1
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros1]
                            def load_dataa():

                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)
                            numero_da_os = st.number_input("Selecione o numero da OS que deseja DELETAR",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                            dell = st.button('⨉ DELETAR ⨉')
                            if dell:
                                cursor1.execute(f'DELETE FROM ROSIVALDO WHERE OS = {numero_da_os};')
                                conn1.commit()
                      
                if fLIDERES == 'EQUIPE DE ELÉTRICA':
                    if fSETOR == 'ELÉTRICA':
                        if senha == '1409':
                            if Rniveldaocorrencia != "Selecione":
                                if Rsolicitante != "Selecione":
                                    if Rsetor != "Selecione":
                                            if atd1: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl = st.button('Atualize')
                                                if atl:
                                                    st.balloons()
                                                    cursor1.execute("UPDATE ROSIVALDO SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(RUsolicitante, RUsetor, RUstatus,RUniveldaocorrencia,RUdata,str(RUtempoi),RUacao,numros))
                                                    conn1.commit()
                                            
                                                                                           
                                            else:
                                                insdds = st.button("INSERIR DADOS")
                                                if insdds:
                                                    allln3 = allln1 + 1
                                                if insdds:
                                                    st.balloons()
                                                    cursor1.execute("INSERT INTO ROSIVALDO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln3 , Rsolicitante, Rsetor,Rstatus,Rniveldaocorrencia,Rdata,str(Rtempoi),Racao,'Não',None,None))
                                                    conn1.commit()
                                                    conn1.close()
                           
            with tab7:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    with st.form('my form'):
                        setorescolhido = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','ELÉTRICA'),index=None,placeholder='Selecione')
                        fnlz2 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=1000,value=0,placeholder="Selecione")
                        fnlz3 = fnlz2-1
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        datainput = st.date_input("Data", value=None)
                        st.write(datainput)
                        timeinput = st.time_input('HORA', value=None)
                        st.write(timeinput)
                        st.form_submit_button('↻')

                if fLIDERES == 'EQUIPE DE ELÉTRICA':
                    if fSETOR == 'ELÉTRICA':
                        if senha == '1409':
                            if setorescolhido == 'FERRAMENTARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor4.execute("UPDATE FERRAMENTARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn4.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')

                            if setorescolhido == 'ELÉTRICA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor1.execute("UPDATE ROSIVALDO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn1.commit()
                                    conn1.close()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

                            if setorescolhido == 'PRODUÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor5.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn5.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')
                            
                            if setorescolhido == 'ADMINISTRATIVO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor6.execute("UPDATE ADMINISTRATIVO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn6.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 
                            
                            if setorescolhido == 'COMERCIAL':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor7.execute("UPDATE COMERCIAL SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn7.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

                            if setorescolhido == 'EXPEDIÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor8.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn8.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')  

                            if setorescolhido == 'SERRALHARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor9.execute("UPDATE SERRALHARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn9.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')

                            if setorescolhido == 'TECNOLOGIA DA INFORMAÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor11.execute("UPDATE TI SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn11.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')         

            with tab8:
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    st.header('Manutenção', divider='rainbow')
                    with st.expander("Filtros"):
                        genre = st.radio(
                          "Selecione",
                        ["ELÉTRICA","POR DATA"],
                        index=0,
                        )
          
                with st.expander(f"Minhas OS ({whrlinhas2})"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'POR DATA':
                        with diferent1:
                            cls = st.date_input('Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM ROSIVALDO WHERE FINALIZADA = 'Não' AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn1)
                            whrlinhas91 = whrlinhas90.shape[0]
                            numros2 = st.number_input("Selecione o numero da OS",min_value=whrlinhas91,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="OS Existentes", value= whrlinhas2)
                            numros3 = numros2-1
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width2")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width2)
                        with diferent2:
                            st.button('↻')
                    
                    else:
                        numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=whrlinhas2,value=whrlinhas2,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas2)
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

                #FERRAMENTARIA   
                st.markdown('----------')
                with st.expander("Ferramentaria"):
                    
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=rd28,value=rd28,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd28)
                        numros5 = numros4-1
                        if rd28 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd27.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width4")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width4)
                    
                    
                #PRODUÇÃO
                with st.expander("Produção"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero   da   OS",min_value=0,max_value=rd34,value=rd34,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd34)
                        numros5 = numros4-1
                        if rd34 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = rd33.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width5")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width5)
            
                  
                #ADMINISTRATIVO
                with st.expander("Administrativo"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione   o  numero   da   OS",min_value=0,max_value=rd42,value=rd42,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd42)
                        numros5 = numros4-1
                        if rd42 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = rd41.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width7")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width7)
            
                with st.expander("Comercial"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input(" Selecione   o  numero   da   OS",min_value=0,max_value=rd50,value=rd50,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd50)
                        numros5 = numros4-1
                        if rd50 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = rd49.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width9")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width9)

                #EXPEDIÇÃO
                with st.expander("Expedição"):
                  if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("  Selecione   o  numero   da   OS",min_value=0,max_value=rd58,value=rd58,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd58)
                        numros5 = numros4-1
                        if rd58 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = rd57.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width11")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width11)
            
                #SERRALHARIA
                with st.expander("Serralharia"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da OS                                ",min_value=0,max_value=rd66,value=rd66,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd66)
                        numros5 = numros4-1
                        if rd66 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = rd65.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width13")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width13)
                
                #TECNOLOGIA DA INFORMAÇÃO
                with st.expander("Tecnologia da informação"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS          ",min_value=0,max_value=rd79,value=rd79,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd79)
                        numros5 = numros4-1
                        if rd79 == 0:
                            st.success('Não há pendências')
                        else:
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
                        genre = st.radio("Selecione ",["ELÉTRICA", "MECÂNICA"],index=0)

                with st.expander(f"Minhas OS {whrlinhas2}"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'POR DATA':
                        with diferent1:
                            cls = st.date_input('Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM ROSIVALDO WHERE FINALIZADA = 'Sim AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn1)
                            whrlinhas91 = whrlinhas90.shape[0]
                            numros2 = st.number_input("Selecione o numero da OS",min_value=whrlinhas91,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="OS Existentes", value= whrlinhas91)
                            numros3 = numros2-1
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width17")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width17)
                        with diferent2:
                            st.button('↻')
                    
                    else:
                        numros2 = st.number_input("Selecione o numero da            OS",min_value=1,max_value=whrlinhas2,value=whrlinhas2,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas2)
                        numros3 = numros2-1
                        if whrlinhas2 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = whrlinhas1.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width19")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width19)
                
                #FERRAMENTARIA
                st.markdown('------')
                with st.expander("Ferramentaria"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione  o  numero  da  OS ",min_value=0,max_value=rd32,value=rd32,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd32)
                        numros5 = numros4-1
                        if rd32 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd31.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width21")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width21)
                
                with st.expander("Produção"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS  ",min_value=0,max_value=rd38,value=rd38,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd38)
                        numros5 = numros4-1
                        if rd38 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd37.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width23")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width23)

                with st.expander("Administrativo"):
                    if genre == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS    ",min_value=0,max_value=rd46,value=rd46,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd46)
                        numros5 = numros4-1
                        if rd46 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd45.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width24")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width24)

                with st.expander("Comercial"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS     ",min_value=0,max_value=rd54,value=rd54,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd54)
                        numros5 = numros4-1
                        if rd54 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd53.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width25")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width25)
                    
                with st.expander("Expedição"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS        ",min_value=0,max_value=rd62,value=rd62,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd62)
                        numros5 = numros4-1
                        if rd62 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd61.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width26")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width26)
                
                with st.expander("Serralharia"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("Selecione o numero da  OS         ",min_value=0,max_value=rd70,value=rd70,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd70)
                        numros5 = numros4-1
                        if rd70 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd69.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key ="use_container_width27")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width27)
                
                with st.expander("Tecnologia da informação"):
                    if 'ELÉTRICA' == 'ELÉTRICA':
                        numros4 = st.number_input("  Selecione o numero da  OS          ",min_value=0,max_value=rd75,value=rd75,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd75)
                        numros5 = numros4-1
                        if rd75 == 0:
                            st.success('Não há pendências')
                        else:
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
                    with st.expander("See explanation"):
                        numros10 = st.number_input(" Selecione o  numero da     OS",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros11 = numros10-1
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros11]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width29")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width29)

#MECÂNICA
allln = pd.read_sql_query("SELECT * FROM CESAR", conn10)
allln1 = allln.shape[0]
consulta4 = "SELECT * FROM CESAR"
allinhas = pd.read_sql_query(consulta4, conn10)

#OS ABERTAS  NÃO FINALIZADAS
consulta5 = "SELECT * FROM CESAR WHERE FINALIZADA = 'Não'"
cesardados = pd.read_sql_query(consulta5, conn10)
cesarvalores = cesardados.shape[0] 

#OS FINALIZADAS
consulta6 = "SELECT * FROM CESAR WHERE FINALIZADA = 'Sim'"
cesardados1 = pd.read_sql_query(consulta6, conn10)
cesarvalores1= cesardados1.shape[0]

if fLIDERES == 'EQUIPE DE MECÂNICA':
    if fSETOR == 'MECÂNICA':
        if senha == '1400':
            #cl1 = st.button("DELETAR TABELA")
            #if cl1:
                #cursor10.execute("DROP TABLE CESAR")
                #conn10.commit()
            image = Image.open('./Midia/ssmm.jpg')
            col1,col2 = st.columns([1,1])
            with col1:
                st.title('Status e informações de O.S')
           
            tab6, tab7,tab8,tab9,tab10= st.tabs(["| Cadastro |", "| Finalizar |","| OS Em aberto |","| OS Finalizadas |","| Geral |"])
            with tab6:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd1 = st.toggle('Atualizar os dados')
                    with st.form('my form3'):
                        st.markdown("---")
                        Rsolicitante = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO','CESAR FILHO'),index=None,placeholder='Selecione')
                        if atd1:
                            RUsolicitante = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO','CESAR FILHO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Rstatus = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd1:
                            RUstatus = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Rsetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','UTILIDADES'),index=None,placeholder='Selecione')
                        if atd1:
                            RUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','UTILIDADES'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Rniveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd1:
                            RUniveldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Racao = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva','INSTALAÇÃO'),index=None,placeholder='Selecione')
                        if atd1:
                            RUacao = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd1:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Rtempoi = st.time_input('Horario', value=None)
                        if atd1:
                            RUtempoi = st.time_input('Atualize o Horario', value=None)
                            st.write(Rtempoi)

                        Rdata = st.date_input("Data", value=None)
                        if atd1:
                            RUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with neymar:
                    if atd1:
                        numros = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros1 = numros-1
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros1]
                            def load_dataa():

                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                            numero_da_os = st.number_input("Selecione o numero da OS que deseja DELETAR",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                            dell = st.button('⨉ DELETAR ⨉')
                            if dell:
                                cursor10.execute(f'DELETE FROM CESAR WHERE OS = {numero_da_os};')
                                conn10.commit()
                      
                if fLIDERES == 'EQUIPE DE MECÂNICA':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1400':
                            if Rniveldaocorrencia != "Selecione":
                                if Rsolicitante != "Selecione":
                                    if Rsetor != "Selecione":
                                            if atd1: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl = st.button('atualize')
                                                if atl:
                                                    st.balloons()
                                                    cursor10.execute("UPDATE CESAR SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(RUsolicitante, RUsetor, RUstatus,RUniveldaocorrencia,RUdata,str(RUtempoi),RUacao,numros))
                                                    conn10.commit()
                                                    conn10.close()
                                                                                           
                                            else:
                                                insdds = st.button("INSERIR DADOS")

                                                if insdds:
                                                    allln3 = allln1 + 1
                                                if insdds:
                                                    st.balloons()
                                                    cursor10.execute("INSERT INTO CESAR (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln3 , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),Rdata,str(Rtempoi),Racao,'Não',None,None))
                                                    conn10.commit()
                                                    conn10.close()
                           
            with tab7:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    with st.form('my form'):
                        setorescolhido = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','MECÂNICA'),index=None,placeholder='Selecione')
                        fnlz2 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=1000,value=0,placeholder="Selecione")
                        fnlz3 = fnlz2-1
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        datainput = st.date_input("Data", value=None)
                        st.write(datainput)
                        st.markdown("---")
                        timeinput = st.time_input('HORA', value=None)
                        st.write(timeinput)
                        st.form_submit_button('↻')

                if fLIDERES == 'EQUIPE DE MECÂNICA':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1400':
                            if setorescolhido == 'FERRAMENTARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor4.execute("UPDATE FERRAMENTARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn4.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')

                            if setorescolhido == 'MECÂNICA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor10.execute("UPDATE CESAR SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn10.commit()
                                    conn10.close()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

                            if setorescolhido == 'PRODUÇÃO':    
                                fnl1=st.button("FINALIZAR")
                                if fnl1:
                                    cursor5.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn5.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')
                            
                            if setorescolhido == 'ADMINISTRATIVO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor6.execute("UPDATE ADMINISTRATIVO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn6.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 
                            
                            if setorescolhido == 'COMERCIAL':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor7.execute("UPDATE COMERCIAL SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn7.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

                            if setorescolhido == 'EXPEDIÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor8.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn8.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')  

                            if setorescolhido == 'SERRALHARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor9.execute("UPDATE SERRALHARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn9.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')

                            if setorescolhido == 'TECNOLOGIA DA INFORMAÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor11.execute("UPDATE TI SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn11.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')

            with tab8:
                jam,jam1 = st.columns([0.2,1])
                with jam:
                    st.header('Manutenção', divider='rainbow')
                    with st.expander("Filtros"):
                        genre = st.radio(
                          "Selecione",
                        ["MECÂNICA","POR DATA"],
                        index=0,
                        )
                with st.expander(f"Minhas OS {cesarvalores}"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'POR DATA':
                        with diferent1:
                            cls = st.date_input('Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM CESAR WHERE FINALIZADA = 'Não' AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn10)
                            whrlinhas91 = whrlinhas90.shape[0]
                            numros2 = st.number_input("Selecione o numero da OS",min_value=whrlinhas91,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="OS Existentes", value= cesarvalores)
                            numros3 = numros2-1
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width2")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width2)
                        with diferent2:
                            st.button('↻')
                    else:
                        numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=cesarvalores,value=cesarvalores,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= cesarvalores)
                        numros3 = numros2-1
                        if cesarvalores == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = cesardados.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width2")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width2)

                #FERRAMENTARIA   
                st.markdown('------')
                with st.expander("Ferramentaria"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS ",min_value=0,max_value=rd30,value=rd30,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd30)
                        numros5 = numros4-1
                        if rd30 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd29.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width17")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width17)
                    
                #PRODUÇÃO
                with st.expander("Produção"):
                    if 'MECÂNICA' == 'MECÂNICA':
                            numros4 = st.number_input(" Selecione  o  numero  da   OS",min_value=0,max_value=rd36,value=rd36,placeholder="Selecione")
                            st.metric(label="OS Existentes", value=rd36)
                            numros5 = numros4-1
                            if rd36 == 0:
                               st.success('Não há pendências')
                            else:
                                osespec = rd35.loc[numros5]
                                def load_data():
                                    return pd.DataFrame(osespec)
                                st.checkbox("Estender", value=True, key="use_container_width5")
                                lddt = load_data()
                                st.dataframe(lddt, use_container_width=st.session_state.use_container_width5)
                #ADMINISTRATIVO
                with st.expander("Administrativo"):
                    if 'MECÂNICA' == 'MECÂNICA':
                            numros4 = st.number_input("Selecione  o numero  da    OS",min_value=0,max_value=rd44,value=rd44,placeholder="Selecione")
                            st.metric(label="OS Existentes", value=rd44)
                            numros5 = numros4-1
                            if rd44 == 0:
                               st.success('Não há pendências')
                            else:
                                osespec = rd43.loc[numros5]
                                def load_data():
                                    return pd.DataFrame(osespec)
                                st.checkbox("Estender", value=True, key="use_container_width7")
                                lddt = load_data()
                                st.dataframe(lddt, use_container_width=st.session_state.use_container_width7)
                #COMERCIAL
                with st.expander("Comercial"):
                    if 'MECÂNICA' == 'MECÂNICA':
                            numros4 = st.number_input("Selecione  o  numero   da    OS",min_value=0,max_value=rd52,value=rd52,placeholder="Selecione")
                            st.metric(label="OS Existentes", value=rd52)
                            numros5 = numros4-1
                            if rd52 == 0:
                               st.success('Não há pendências')
                            else:
                                osespec = rd51.loc[numros5]
                                def load_data():
                                    return pd.DataFrame(osespec)
                                st.checkbox("Estender", value=True, key="use_container_width9")
                                lddt = load_data()
                                st.dataframe(lddt, use_container_width=st.session_state.use_container_width9)

                #EXPEDIÇÃO
                with st.expander("Expedição"):
                  if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione  o  numero   da    OS",min_value=0,max_value=rd60,value=rd60,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd60)
                        numros5 = numros4-1
                        if rd60 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd59.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width11")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width11)
                
                #SERRALHARIA
                with st.expander("Serralharia"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione  o    numero   da    OS",min_value=0,max_value=rd68,value=rd68,placeholder="Selecione")
                        oi = st.metric(label="OS Existentes", value=rd68)
                        numros5 = numros4-1
                        if rd68 == 0:
                            st.success('Não há pendências')
                        else:
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
                        genre = st.radio("Selecione ",["MECÂNICA","POR DATA"],index=0)
                    
                with st.expander(f"Minhas OS {cesarvalores1}"):
                    diferent1,diferent2 = st.columns([0.2,0.00000000000001])
                    if genre == 'POR DATA':
                        with diferent1:
                            cls = st.date_input(' Escolha á data')
                            status = str(cls)
                            consulta3 = f"SELECT * FROM CESAR WHERE FINALIZADA = 'Sim' AND DATA = '{status}'"
                            whrlinhas90 = pd.read_sql_query(consulta3, conn10)
                            whrlinhas91 = whrlinhas90.shape[0]
                            numros2 = st.number_input(" Selecione   o  numero da  OS ",min_value=whrlinhas91,max_value=whrlinhas91,value=whrlinhas91,placeholder="Selecione")
                            st.metric(label="OS Existentes", value= whrlinhas91)
                            numros3 = numros2-1
                        if whrlinhas91 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = whrlinhas90.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width14")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width14)
                        with diferent2:
                            st.button('↻    ')
                    else:
                        numros2 = st.number_input("Selecione   o   numero  da     OS     ",min_value=1,max_value=cesarvalores1,value=cesarvalores1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= cesarvalores1)
                        numros3 = numros2-1
                        if cesarvalores1 == 0:
                           st.success('Não há pendências')
                        else:
                            osespec = cesardados1.loc[numros3]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width15")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width15)

                
                #FERRAMENTARIA
                st.markdown('------')
                with st.expander("Ferramentaria"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input(" Selecione  o  numero  da  OS ",min_value=0,max_value=rd30,value=rd30,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd30)
                        numros5 = numros4-1
                        if rd30 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd29.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width18")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width18)
                
                with st.expander("Produção"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS   ",min_value=0,max_value=rd40,value=rd40,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd40)
                        numros5 = numros4-1
                        if rd40 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd39.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width19")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width19)
                            
                with st.expander("Administrativo"):
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS     ",min_value=0,max_value=rd48,value=rd48,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd48)
                        numros5 = numros4-1
                        if rd48 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd47.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width21")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width21)

                with st.expander("Comercial"):            
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS       ",min_value=0,max_value=rd56,value=rd56,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd56)
                        numros5 = numros4-1
                        if rd56 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd55.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width23")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width23)

                with st.expander("Expedição"):            
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS        ",min_value=0,max_value=rd64,value=rd64,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd64)
                        numros5 = numros4-1
                        if rd64 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd63.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width25")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width25)
                
                with st.expander("Serralharia"):                
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS          ",min_value=0,max_value=rd72,value=rd72,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd72)
                        numros5 = numros4-1
                        if rd72 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = rd71.loc[numros5]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width27")
                            lddt = load_data()
                            st.dataframe(lddt, use_container_width=st.session_state.use_container_width27)
                
                with st.expander("Tecnologia da informação"):    
                    if 'MECÂNICA' == 'MECÂNICA':
                        numros4 = st.number_input("Selecione o numero da  OS           ",min_value=0,max_value=rd77,value=rd77,placeholder="Selecione")
                        st.metric(label="OS Existentes", value=rd77)
                        numros5 = numros4-1
                        if rd77 == 0:
                            st.success('Não há pendências')
                        else:
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
                        numros10 = st.number_input("Selecione o numero da     OS",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros11 = numros10-1
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros11]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_width30")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width30) 
#FERRAMENTARIA


allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
allln14 = allln13.shape[0]

allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
allln14 = allln13.shape[0]
consulta7 = "SELECT * FROM FERRAMENTARIA"
allinhas15 = pd.read_sql_query(consulta7, conn4)

#OS ABERTAS  NÃO FINALIZADAS
consulta8 = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Não'"
whrlinhas12 = pd.read_sql_query(consulta8, conn4)
whrlinhas13 = whrlinhas12.shape[0]

#OS FINALIZADAS
cursor4.execute("SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas15 = cursor4.fetchall()
whrlinhas16 = pd.DataFrame(whrlinhas15)
whrlinhas17 = whrlinhas16.shape[0]

if fLIDERES == 'IVSON PAULINO':
    if fSETOR == 'FERRAMENTARIA':
        if senha == '70':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl5 = st.button("DELETAR TABELA")
            #if cl5:
                #cursor4.execute("DROP TABLE FERRAMENTARIA")
                #conn4.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab26,tab27,tab28,tab29= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral |"])
            with tab26:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col9,col10= st.columns(2)  
                with col9:                  
                    atd4 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Fs = st.selectbox('Solicitante', ('IVSON PAULINO',),index=0,placeholder='Selecione')
                        
                        Fstr = st.selectbox('Setor', ('FERRAMENTARIA',),index=0,placeholder='Selecione')
                        st.markdown('---------')

                        Fst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd4:
                            FUst = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")
                    
                        Fndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd4:
                            FUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                            
                        Fac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd4:
                            Fuac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Fmnt = st.selectbox('Tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd4:
                            Fmnt = st.selectbox('Atualize o tipe de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        Ftemp = st.time_input('Horario', value=None)
                        if atd4:
                            FUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Ftemp)

                        Fdata = st.date_input("Data", value=None)
                        if atd4:
                            FUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')
                
                with col10:
                    if atd4:
                        numros12 = st.number_input("Selecion6numros16 o numero da OS que deseja atualizar",min_value=0,max_value=allln14,value=allln14,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln14)
                        numros17 = numros12-1
                        if allln14 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec4 = allinhas15.loc[numros17]
                            def load_dataa():
                                return pd.DataFrame(osespec4)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'IVSON PAULINO':
                    if fSETOR == 'FERRAMENTARIA':
                        if senha == '70':
                            if atd4: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor4.execute("UPDATE FERRAMENTARIA SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(FUst,FUndo,FUdata,str(FUtemp),Fuac,numros12))
                                    conn4.commit()
                                    conn4.close()
                                                                                           
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln14 + 1
                                if insdds:
                                    st.balloons()
                                    cursor4.execute("INSERT INTO FERRAMENTARIA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(Fs), str(Fstr), str(Fst),str(Fndo),Fdata,str(Ftemp),Fac,'Não',None,None,Fmnt))
                                    conn4.commit()
                                    conn4.close()
                                        
            with tab27:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Ferramentaria', divider='rainbow')
                    st.button(' Atualize ↻')
                    with st.expander("Abertas"):
                        numros22 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas13,value=whrlinhas13,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas13)
                        numros23 = numros22-1
                        if whrlinhas13 == 0:
                            st.success('Não há pendências')
                        else:
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
                    numros16 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd1,value=rd1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd1)
                    numros17 = numros16-1
                    if rd1 == 0:
                        st.success('Não há pendências')
                        
                    else:
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
                    numros20 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln14,value=allln14,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln14)
                    numros21 = numros20-1
                    if allln14 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec7 = allln13.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec7)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)
#PRODUCAO
if fLIDERES == 'MAURILIO SALES':
    if fSETOR == 'PRODUÇÃO':
        if senha == '1405':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl6 = st.button("DELETAR TABELA")
            #if cl6:
                #cursor5.execute("DROP TABLE PRODUCAO")
                #conn5.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab30,tab31,tab32,tab33= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral |"])
            with tab30:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col11,col12= st.columns(2)  
                with col11:                  
                    atd5 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Ps = st.selectbox('Solicitante', ('MAURILIO SALES',),index=0,placeholder='Selecione')

                        Pstr = st.selectbox('Setor', ('PRODUÇÃO',),index=0,placeholder='Selecione')
                    
                        Pst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd5:
                            PUst = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")
                        
                        Pndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd5:
                            PUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Pac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd5:
                            PUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Pmnt = st.selectbox('Tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd5:
                            PUmnt = st.selectbox('Atualize o tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd5:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Ptemp = st.time_input('Horario', value=None)
                        if atd5:
                            PUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Ptemp)

                        Pdata = st.date_input("Data", value=None)
                        if atd5:
                            PUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Insira um foto", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col12:
                    if atd5:
                        numros12 = st.number_input("Selecion6numros18 o numero da OS que deseja atualizar",min_value=0,max_value=allln16,value=allln16,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln16)
                        numros19 = numros12-1
                        if allln16 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec8 = allinhas16.loc[numros19]
                            def load_dataa():
                                return pd.DataFrame(osespec8)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'MAURILIO SALES':
                    if fSETOR == 'PRODUÇÃO':
                        if senha == '1405':
                            if atd5:
                                atl1 = st.button('atualize')
                                st.balloons()
                                cursor5.execute("UPDATE PRODUCAO SET   OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ?, MANUTENTOR = ? WHERE OS = ?",(PUst,PUndo,PUdata,str(PUtemp),PUac,PUmnt,numros12))
                                conn5.commit()
                                conn5.close()
                                                                                           
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln16 + 1
                                if insdds:
                                    st.balloons()
                                    cursor5.execute("INSERT INTO PRODUCAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (allln12 , str(Ps), str(Pstr), str(Pst),str(Pndo),Pdata,str(Ptemp),Pac,'Não',None,None,Pmnt))
                                    conn5.commit()
                                    conn5.close()
                                        
            with tab31:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('PRODUÇÃO', divider='rainbow')
                    st.button(' Atualize ↻  ')
                    with st.expander("Abertas"):
                        numros22 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas19,value=whrlinhas19,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas19)
                        numros23 = numros22-1
                        if whrlinhas19 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec9 = whrlinhas18.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec9)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)


            with tab32:
                st.header('PRODUÇÃO', divider='rainbow')
                st.button(' Atualize ↻   ')
                with st.expander("Finalizadas"):
                    numros18 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd5,value=rd5,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd5)
                    numros19 = numros18-1
                    if rd5 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec10 = rd4.loc[numros19]
                        def load_data():
                            return pd.DataFrame(osespec10)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab33:
                st.header('PRODUÇÃO', divider='rainbow')
                st.button('Atualize ↻    ')
                with st.expander("Geral"):
                    numros20 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln16,value=allln16,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln16)
                    numros21 = numros20-1
                    if allln16 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec11 = allln15.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec11)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)
#ADMINISTRATIVO
#GERAL ADMINISTRATIVO
allln17 = pd.read_sql_query("SELECT * FROM ADMINISTRATIVO", conn6)
allln18 = allln17.shape[0]
consulta2 = "SELECT * FROM ADMINISTRATIVO"
allinhas17 = pd.read_sql_query(consulta2, conn6)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Não'"
whrlinhas23 = pd.read_sql_query(consulta3, conn6)
whrlinhas24 = whrlinhas23.shape[0]

#OS FINALIZADAS
cursor6.execute("SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas25 = cursor6.fetchall()
whrlinhas26 = pd.DataFrame(whrlinhas25)
whrlinhas27 = whrlinhas26.shape[0]

if fLIDERES == 'GILSON FREITAS':
    if fSETOR == 'ADMINISTRATIVO':
        if senha == '1404':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl7 = st.button("DELETAR TABELA")
            #if cl7:
                #cursor6.execute("DROP TABLE ADMINISTRATIVO")
                #conn6.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab34,tab35,tab36,tab37= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral |"])
            with tab34:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col13,col14= st.columns(2)  
                with col13:                  
                    atd6 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        As = st.selectbox('Solicitante', ('GILSON FREITAS',),index=0,placeholder='Selecione')
                        
                        Astr = st.selectbox('Setor', ('ADMINISTRATIVO',),index=0,placeholder='Selecione')
                        st.markdown("---")

                        Ast = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd6:
                            AUst = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")
                        
                        Ando = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd6:
                            AUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Aac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd6:
                            AUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Amnt = st.selectbox('Tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd6:
                            Amnt = st.selectbox('Atualize o tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd6:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Atemp = st.time_input('Horario', value=None)
                        if atd6:
                            AUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Atemp)

                        Adata = st.date_input("Data", value=None)
                        if atd6:
                            AUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col14:
                    if atd6:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln18,value=allln18,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln18)
                        numros21 = numros12-1
                        if allln18 ==0:
                            st.success('Não há pendências')
                        else:
                            osespec12 = allinhas17.loc[numros21]
                            def load_dataa():
                                return pd.DataFrame(osespec12)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'GILSON FREITAS':
                    if fSETOR == 'ADMINISTRATIVO':
                        if senha == '1404':
                            if atd6: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor6.execute("UPDATE ADMINISTRATIVO SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(AUst,AUndo,AUdata,str(AUtemp),AUac,numros12))
                                    conn6.commit()
                                    conn6.close()
                                                                    
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln18 + 1
                                if insdds:
                                    st.balloons()
                                    cursor6.execute("INSERT INTO ADMINISTRATIVO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(As), str(Astr), str(Ast),str(Ando),Adata,str(Atemp),Aac,'Não',None,None,Amnt))
                                    conn6.commit()
                                    conn6.close()
                                        
            with tab35:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('ADMINISTRATIVO', divider='rainbow')
                    st.button(' Atualize ↻  ')
                    with st.expander("Abertas"):
                        numros22 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas24,value=whrlinhas24,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas24)
                        numros23 = numros22-1
                        if whrlinhas24 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec13 = whrlinhas23.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec13)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab36:
                st.header('ADMINISTRATIVO', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Finalizadas"):
                    numros20 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd9,value=rd9,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd9)
                    numros21 = numros20-1
                    if rd9 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        osespec14 = rd8.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec14)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab37:
                st.header('ADMINISTRATIVO', divider='rainbow')
                st.button('Atualize ↻   ')
                with st.expander("Geral"):
                    numros20 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln18,value=allln18,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln18)
                    numros21 = numros20-1
                    if allln18 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec15 = allln17.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec15)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

#COMERCIAL
#GERAL COMERCIAL
allln19 = pd.read_sql_query("SELECT * FROM COMERCIAL", conn7)
allln20 = allln19.shape[0]
consulta2 = "SELECT * FROM COMERCIAL"
allinhas18 = pd.read_sql_query(consulta2, conn7)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Não'"
whrlinhas28 = pd.read_sql_query(consulta3, conn7)
whrlinhas29 = whrlinhas28.shape[0]

#OS FINALIZADAS
cursor7.execute("SELECT * FROM COMERCIAL WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas30 = cursor7.fetchall()
whrlinhas31 = pd.DataFrame(whrlinhas30)
whrlinhas32 = whrlinhas31.shape[0]

if fLIDERES == 'ADRIELY LEMOS':
    if fSETOR == 'COMERCIAL':
        if senha == '1403':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl8 = st.button("DELETAR TABELA")
            #if cl8:
                #cursor7.execute("DROP TABLE COMERCIAL")
                #conn7.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab38,tab39,tab40,tab41= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral |"])
            with tab38:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col15,col16= st.columns(2)  
                with col15:                  
                    atd7 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Cs = st.selectbox('Solicitante', ('ADRIELY LEMOS',),index=0,placeholder='Selecione')
                        Castr = st.selectbox('Setor', ('COMERCIAL',),index=0,placeholder='Selecione')
                        
                        Cast = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd7:
                            Cust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Cando = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd7:
                            Cundo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Cac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd7:
                            CUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Cmnt = st.selectbox('Tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd7:
                            Cmnt = st.selectbox('Atualize o tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")
                                                
                        #relatorio = st.text_input('Relatorio')
                        #if atd7:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Ctemp = st.time_input('Horario', value=None)
                        if atd7:
                            CUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Ctemp)

                        Cdata = st.date_input("Data", value=None)
                        if atd7:
                            CUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col16:
                    if atd7:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln120,value=allln120,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln120)
                        numros23 = numros12-1
                        if allln120 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec16 = allinhas18.loc[numros23]
                            def load_dataa():
                                return pd.DataFrame(osespec16)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'ADRIELY LEMOS':
                    if fSETOR == 'COMERCIAL':
                        if senha == '1403':
                           if atd7: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor7.execute("UPDATE COMERCIAL SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(Cust,Cundo,CUdata,str(CUtemp),CUac,numros12))
                                    conn7.commit()
                                    conn7.close()
                                                                    
                           else:
                            insdds = st.button("INSERIR DADOS")
                            if insdds:
                                allln12 = allln20 + 1
                            if insdds:
                                st.balloons()
                                cursor7.execute("INSERT INTO COMERCIAL (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(Cs), str(Castr), str(Cast),str(Cando),Cdata,str(Ctemp),Cac,'Não',None,None,Cmnt))
                                conn7.commit()
                                conn7.close()
                                        
            with tab39:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('COMERCIAL', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        numros22 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas29,value=whrlinhas29,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas29)
                        numros23 = numros22-1
                        if whrlinhas29 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec17 = whrlinhas28.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec17)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab40:
                st.header('COMERCIAL', divider='rainbow')
                st.button(' Atualize ↻  ' )
                with st.expander("Finalizadas"):
                    numros22 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd13,value=rd13,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd13)
                    numros23 = numros22-1
                    if rd13 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        osespec18 = rd12.loc[numros23]
                        def load_data():
                            return pd.DataFrame(osespec18)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab41:
                st.header('COMERCIAL', divider='rainbow')
                st.button(' Atualize ↻ ')
                with st.expander("Geral"):
                    numros22 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln120,value=allln120,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln120)
                    numros23 = numros22-1
                    if allln120 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec19 = allln19.loc[numros23]
                        def load_data():
                            return pd.DataFrame(osespec19)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

#EXPEDICAO
#GERAL EXPEDICAO
allln21 = pd.read_sql_query("SELECT * FROM EXPEDICAO", conn8)
allln22 = allln21.shape[0]
consulta2 = "SELECT * FROM EXPEDICAO"
allinhas19 = pd.read_sql_query(consulta2, conn8)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não'"
whrlinhas33 = pd.read_sql_query(consulta3, conn8)
whrlinhas34 = whrlinhas33.shape[0]

#OS FINALIZADAS
cursor8.execute("SELECT * FROM EXPEDICAO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas35 = cursor8.fetchall()
whrlinhas36 = pd.DataFrame(whrlinhas35)
whrlinhas37 = whrlinhas36.shape[0]

if fLIDERES == 'ALEX SANTOS':
    if fSETOR == 'EXPEDIÇÃO':
        if senha == '1402':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl9 = st.button("DELETAR TABELA")
            #if cl9:
                #cursor8.execute("DROP TABLE EXPEDICAO")
                #conn8.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab42,tab43,tab44,tab45= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral| "])
            with tab42:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col17,col18= st.columns(2)  
                with col17:                  
                    atd8 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Ec = st.selectbox('Solicitante', ('ALEX SANTOS',),index=0,placeholder='Selecione')

                        Eastr = st.selectbox('Setor', ('EXPEDICAO',),index=0,placeholder='Selecione')
                      
                        East = st.text_input('Tipo de Ocorrência',value=0,placeholder='Insira sua ocôrrencia')
                        if atd8:
                            Eust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Endo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd8:
                            EUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Eac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd8:
                            EUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Emnt = st.selectbox('Eletrica ou Mecânica', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd8:
                            Emnt = st.selectbox('Eletrica ou Mecânica', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd8:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Etemp = st.time_input('Horario', value=None)
                        if atd8:
                            EUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Etemp)

                        Edata = st.date_input("Data", value=None)
                        if atd8:
                            EUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a EcV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col18:
                    if atd8:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln22,value=allln22,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln22)
                        numros25 = numros12-1
                        if allln22 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec20 = allinhas19.loc[numros25]
                            def load_dataa():
                                return pd.DataFrame(osespec20)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'ALEX SANTOS':
                    if fSETOR == 'EXPEDIÇÃO':
                        if senha == '1402':  
                            if atd8: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor8.execute("UPDATE EXPEDICAO SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(Eust,EUndo,EUdata,str(EUtemp),EUac,numros12))
                                    conn8.commit()
                                    conn8.close()
                                                                    
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln22 + 1
                                if insdds:
                                    st.balloons()
                                    cursor8.execute("INSERT INTO EXPEDICAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(Ec), str(Eastr), str(East),str(Endo),Edata,str(Etemp),Eac,'Não',None,None,Emnt))
                                    conn8.commit()
                                    conn8.close()
                                        
            with tab43:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('EXPEDIÇÃO', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        numros24 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas34,value=whrlinhas34,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas34)
                        numros25 = numros24-1
                        if whrlinhas34 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec21 = whrlinhas33.loc[numros25]
                            def load_data():
                                return pd.DataFrame(osespec21)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab44:
                st.header('EXPEDIÇÃO', divider='rainbow')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    numros24 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd17,value=rd17,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd17)
                    numros25 = numros24-1
                    if rd17 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        osespec22 = rd16.loc[numros25]
                        def load_data():
                            return pd.DataFrame(osespec22)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab45:
                st.header('EXPEDIÇÃO', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    numros24 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln22,value=allln22,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln22)
                    numros25 = numros24-1
                    if allln22 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec23 = allln21.loc[numros25]
                        def load_data():
                            return pd.DataFrame(osespec23)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

#SERRALHARIA
#GERAL SERRALHARIA
allln23 = pd.read_sql_query("SELECT * FROM SERRALHARIA", conn9)
allln24 = allln23.shape[0]
consulta2 = "SELECT * FROM SERRALHARIA"
allinhas20 = pd.read_sql_query(consulta2, conn9)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Não'"
whrlinhas38 = pd.read_sql_query(consulta3, conn9)
whrlinhas39 = whrlinhas38.shape[0]

#OS FINALIZADAS
cursor9.execute("SELECT * FROM SERRALHARIA WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas40 = cursor9.fetchall()
whrlinhas41 = pd.DataFrame(whrlinhas40)
whrlinhas42 = whrlinhas41.shape[0]

if fLIDERES == 'CESAR AUGUSTO':
    if fSETOR == 'SERRALHARIA':
        if senha == '1401':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl10 = st.button("DELETAR TABELA")
            #if cl10:
                #cursor9.execute("DROP TABLE SERRALHARIA")
                #conn9.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab46,tab47,tab48,tab49= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral |"])
            with tab46:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col19,col20= st.columns(2)  
                with col19:                  
                    atd9 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Sc = st.selectbox('Solicitante', ('CESAR AUGUSTO',),index=0,placeholder='Selecione')

                        Sstr = st.selectbox('Setor', ('SERRALHARIA',),index=0,placeholder='Selecione')
                       
                        Sst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd9:
                            Sust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Sndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd9:
                            SUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Sac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd9:
                            SUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Smnt = st.selectbox('Eletrica ou Mecânica', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd9:
                            Smnt = st.selectbox('Eletrica ou Mecânica', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd9:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Stemp = st.time_input('Horario', value=None)
                        if atd9:
                            SUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Stemp)

                        Sdata = st.date_input("Data", value=None)
                        if atd9:
                            SUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a EcV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col20:
                    if atd9:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln24,value=allln24,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln24)
                        numros27 = numros12-1
                        if allln24 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec24 = allinhas20.loc[numros27]
                            def load_dataa():
                                return pd.DataFrame(osespec24)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'CESAR AUGUSTO':
                    if fSETOR == 'SERRALHARIA':
                        if senha == '1401':
                            if atd9: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor9.execute("UPDATE SERRALHARIA SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(Sust,SUndo,SUdata,str(SUtemp),SUac,numros12))
                                    conn9.commit()
                                    conn9.close()
                                                                    
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln24 + 1
                                if insdds:
                                    st.balloons()
                                    cursor9.execute("INSERT INTO SERRALHARIA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(Sc), str(Sstr), str(Sst),str(Sndo),Sdata,str(Stemp),Sac,'Não',None,None,Smnt))
                                    conn9.commit()
                                    conn9.close()
                                        
            with tab47:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('SERRALHARIA', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        numros26 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas39,value=whrlinhas39,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas39)
                        numros27 = numros26-1
                        if whrlinhas39 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec25 = whrlinhas38.loc[numros27]
                            def load_data():
                                return pd.DataFrame(osespec25)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab48:
                st.header('SERRALHARIA', divider='rainbow')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    numros26 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd21,value=rd21,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd21)
                    numros27 = numros26-1
                    if rd21 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        osespec26 = rd20.loc[numros27]
                        def load_data():
                            return pd.DataFrame(osespec26)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)

            with tab49:
                st.header('SERRALHARIA', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    numros26 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln24,value=allln24,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln24)
                    numros27 = numros26-1
                    if allln24 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec27 = allln23.loc[numros27]
                        def load_data():
                            return pd.DataFrame(osespec27)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)

query = "SELECT * FROM TI WHERE FINALIZADA = 'Não'"
rd70 = pd.read_sql_query(query, conn11)
rd71 = rd70.shape[0]

query1 = "SELECT * FROM TI WHERE FINALIZADA = 'Sim'"
rd72 = pd.read_sql_query(query1, conn11)
rd73 = rd72.shape[0]

allln25 = pd.read_sql_query("SELECT * FROM TI", conn11)
allln26 = allln25.shape[0]

allln25 = pd.read_sql_query("SELECT * FROM TI", conn11)
allln26 = allln25.shape[0]
consulta2 = "SELECT * FROM TI"
allinhas21 = pd.read_sql_query(consulta2, conn11)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM TI WHERE FINALIZADA = 'Não'"
whrlinhas43 = pd.read_sql_query(consulta3, conn11)
whrlinhas44 = whrlinhas43.shape[0]

#OS FINALIZADAS
cursor11.execute("SELECT * FROM TI WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas45 = cursor11.fetchall()
whrlinhas46 = pd.DataFrame(whrlinhas45)
whrlinhas47 = whrlinhas46.shape[0]

if fLIDERES == 'FILIPE LEITE':
    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            #cl11 = st.button("DELETAR TABELA")
            #if cl11:
                #cursor11.execute("DROP TABLE TI")
                #conn11.commit()
            with ps6:
                st.title('Status e informações de O.S')

            st.markdown("---")
            tab50,tab51,tab52,tab53= st.tabs(["| Cadastro |","| OS Abertas |","| OS Finalizadas |","| Geral |"])
            with tab50:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col21,col22= st.columns(2)  
                with col21:                  
                    atd10 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Tc = st.selectbox('Solicitante', ('FILIPE LEITE',),index=0,placeholder='Selecione')

                        Tstr = st.selectbox('Setor', ('TI',),index=0,placeholder='Selecione')
                       
                        Tst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd10:
                            Tust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Tndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd10:
                            TUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Tac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd10:
                            TUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Tmnt = st.selectbox('Tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd10:
                            Tmnt = st.selectbox('Atualize o tipo de manutenção', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        #relatorio = st.text_input('Relatorio')
                        #if atd10:
                            #Urelatorio = st.text_input('Atualize o Relatorio')
                            #st.markdown("---")

                        Ttemp = st.time_input('Horario', value=None)
                        if atd10:
                            TUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Ttemp)

                        Tdata = st.date_input("Data", value=None)
                        if atd10:
                            TUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a EcV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col22:
                    if atd10:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln26,value=allln26,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln26)
                        numros29 = numros12-1
                        if allln26 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec28 = allinhas21.loc[numros29]
                            def load_dataa():
                                return pd.DataFrame(osespec28)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'FILIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if atd10: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor11.execute("UPDATE TI SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(Tust,TUndo,TUdata,str(TUtemp),TUac,numros12))
                                    conn11.commit()
                                    conn11.close()
                                                                    
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln26 + 1
                                if insdds:
                                    st.balloons()
                                    cursor11.execute("INSERT INTO TI (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(Tc), str(Tstr), str(Tst),str(Tndo),Tdata,str(Ttemp),Tac,'Não',None,None,Tmnt))
                                    conn11.commit()
                                    conn11.close()
                                        
            with tab51:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('TI', divider='rainbow')
                    st.button('Atualize ↻')
                    with st.expander("Abertas"):
                        numros28 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas44,value=whrlinhas44,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas44)
                        numros29 = numros28-1
                        if whrlinhas44 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec29 = whrlinhas43.loc[numros29]
                            def load_data():
                                return pd.DataFrame(osespec29)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab52:
                st.header('TI', divider='rainbow')
                st.button('Atualize ↻ ')
                with st.expander("Finalizadas"):
                    numros28 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd73,value=rd73,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd73)
                    numros29 = numros28-1
                    if rd73 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        osespec30 = rd72.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec30)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)
            
            with tab53:
                st.header('TI', divider='rainbow')
                st.button('Atualize ↻  ')
                with st.expander("Geral"):
                    numros28 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln26,value=allln26,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln26)
                    numros29 = numros28-1
                    if allln26 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec31 = allln25.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec31)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)









