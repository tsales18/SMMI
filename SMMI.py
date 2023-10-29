import pandas as pd
import streamlit as st
import altair as alt
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
import requests

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title=('MANUTENÇÃO SSM SOLAR DO BRASIL'),
    page_icon='SMMI',
    layout='wide',
    
    initial_sidebar_state='expanded',
    menu_items={
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
    nrows=8
    
)

# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Midia/sales.jpeg')
    st.image(logo_teste, width=300)
    st.subheader('MANUTENÇÃO SSM SOLAR DO BRASIL')
    fLIDERES = st.selectbox(
        "LIDER:",
        options=df['LIDERES'].unique()
    )
    fSETOR = st.selectbox(
        "SETOR:",
        options=df['SETOR'].unique()
    )
    senha = st.text_input('Ensira sua senha')
    
    with st.spinner("Carregando..."):
                time.sleep(2)
                st.success("Pronto!")
    st.write("Bem Vindo")
    
    st.write('✅')
    
    connection_url = URL.create(
    "mssql+pyodbc",
    username="DESKTOP-62QBI08\james",
    password="47297913",
    host="DESKTOP-62QBI08\WINCCPLUSMIG2014",
    port=51304,
    database="SSMM",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
        "authentication": "ActiveDirectoryIntegrated",
    },
)
engine = create_engine(connection_url).execution_options(
    isolation_level="AUTOCOMMIT"
)
conn = engine.connect()

if st.button('🔄'):
    M = MetaData()
    ABERTURA = Table('ABERTURA', M,
                Column('OS', Integer, primary_key=True),
                Column('SOLICITANTE', String(1000)),
                Column("SETOR", String(1000)),
                Column('TIPO_DE_OCORRENCIA', String(1000)),
                Column('NIVEL_DA_OCÔRRENCIA', String(50)))
                
    M.create_all(engine)
    M = MetaData()
    ABERTURAF = Table('ABERTURAF', M,
                Column('OS', Integer, primary_key=True),
                Column('SOLICITANTE', String(1000)),
                Column("SETOR", String(1000)),
                Column('TIPO_DE_OCORRENCIA', String(1000)),
                Column('NIVEL_DA_OCÔRRENCIA', String(50)),
                Column('DATA', (Date)),
                Column('MOMENTO', (Time)))
    M.create_all(engine) 

    M = MetaData()
    DADOS = Table('DADOS', M,
             Column('HORA_INICIADA', (Time(0)), nullable=False))
    M.create_all(engine)  
    
    M = MetaData()
    DADOS1 = Table('DADOS1', M,
              Column('DATA', (Date), nullable=False),
              Column('HORA_FINAL', (Time(0)), nullable=False))
    M.create_all(engine)
    
    
    M = MetaData()
    DADOSF = Table('DADOSF', M,
                Column('HORA_INICIADA', (Time(0)), nullable=False))
    M.create_all(engine)


          

DATA = pd.read_sql_table("ABERTURA", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
"driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
"&authentication=ActiveDirectoryIntegrated")

DATA1 = pd.read_sql_table("DADOS", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
"driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
"&authentication=ActiveDirectoryIntegrated")

DATA2 = pd.read_sql_table("DADOS1", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
"driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
"&authentication=ActiveDirectoryIntegrated")

dt = pd.DataFrame(DATA)
num =dt.shape[0]
dt1 = pd.DataFrame(DATA2)
num1 = dt1.shape[0]

tab1_qtde_produto = df.loc[(
    df['SETOR'] == fSETOR) &
    (df['LIDERES'] == fLIDERES)
]
      
if fLIDERES == 'FELIPE LEITE':
    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps1,ps2,ps3,ps4,ps5 = st.columns(5)
            with ps1:
                st.image(image,width=1700)
                st.title('Status e informações de OS')
            b0,b1 = st.columns([1,26])
            with b0:
                if st.button('↻'):
                    DATA = pd.read_sql_table("ABERTURA", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
                    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
                    "&authentication=ActiveDirectoryIntegrated")
                    DATA1 = pd.read_sql_table("DADOS", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
                    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
                    "&authentication=ActiveDirectoryIntegrated")
                    DATA2 = pd.read_sql_table("DADOS1", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
                    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
                    "&authentication=ActiveDirectoryIntegrated")
            st.markdown("---")
            
            
            tab1, tab2, tab3= st.tabs(["Cadastro", "Finalizar","OS Abertas"])

            with tab1:
                st.header("Cadastro de ocorrência")
                colibrim,neymar,lula,sales,poura= st.columns([0.5,0.1,0.1,0.1,0.1])  
                with colibrim:
                    with st.form('my form2'):
                        st.markdown("---")
                        solicitante = st.selectbox('Solicitante', ('Selecione','FILIPE',),index=0)
                        status = st.selectbox('Tipo de Ocorrência', ('Selecione','ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES'),index=0,)   
                        st.markdown("---")
                        setor = st.selectbox('Setor', ('Selecione','TECNOLOGIA DA INFORMAÇÃO',), index=0)
                        niveldaocorrencia = st.selectbox('Nivel da ocorrência', ('Selecione','EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE', 'URGÊNTE'), index=0)
                        st.markdown("---")
                        relatorio = st.text_input('Relatorio')
                        tempoi = st.time_input('HORA DE INICIO', value=None)
                        st.write(tempoi)
                        st.form_submit_button('↻')
                            
                M = MetaData()
                ABERTURA = Table('ABERTURA', M,
                        Column('OS', Integer, primary_key=True),
                        Column('SOLICITANTE', String(1000)),
                        Column("SETOR", String(1000)),
                        Column('TIPO_DE_OCORRENCIA', String(1000)),
                        Column('NIVEL_DA_OCÔRRENCIA', String(50)),
                        Column('Hora de inicio', (Time)))
                M.create_all(engine) 
                
                
                M = MetaData()
                DADOS = Table('DADOS', M,
                          Column('HORA_INICIADA', (Time(0)), nullable=False))
                M.create_all(engine)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if niveldaocorrencia != "Selecione":
                                if solicitante != "Selecione":
                                    if setor != "Selecione":
                                        if num > num1:
                                            st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                        else:
                                            att = st.button("INSERIR DADOS")
                                            if att:
                                                ins = ABERTURA.insert()
                                                conn.execute(ins,SOLICITANTE = solicitante, SETOR = setor, TIPO_DE_OCORRENCIA =                                                                                                                                             status,NIVEL_DA_OCÔRRENCIA=niveldaocorrencia)                                     
                                                ins1 = DADOS.insert()
                                                conn.execute(ins1, HORA_INICIADA=tempoi)
                      
                                            if att:
                                                st.balloons()
                                                st.session_state.OS += 1
                                                st.experimental_rerun()
                        
            with tab2:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    with st.form('my form'):
                        df3 = st.date_input("Data", value=None)
                        st.write(df3)
                        st.markdown("---")
                        t = st.time_input('HORA', value=None)
                        st.write(t)
                        st.form_submit_button('↻')
                        
                M = MetaData()
                DADOS1 = Table('DADOS1', M,
                          Column('DATA', (Date), nullable=False),
                          Column('HORA_FINAL', (Time(0)), nullable=False))
                M.create_all(engine)                
                  
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if num <= num1:
                                st.caption('É necessario ABRIR outra OS para finalizar.') 
                                st.write(num)
                                st.write(num1)
                            else:
                                st.caption('É necessario finalizar esta OS antes de inciar outra.')                                                                                                                         
                                FIn=st.button("FINALIZAR")
                                if FIn:
                                    ins2 = DADOS1.insert()
                                    conn.execute(ins2,DATA =df3, HORA_FINAL=t)
                                if FIn:
                                    st.session_state.FIN += 1
                                    st.balloons()
                                   
                                   
                                       
                                
            with tab3:
                statuses,sats,statuses1=st.columns([55,8,20])
                with statuses:
                    df1 = pd.DataFrame(DATA)
                    st.table(df1)
                with sats:
                    df2 = pd.DataFrame(DATA1)
                    st.dataframe((df2))               
                with statuses1:
                    df6= pd.DataFrame(DATA2)
                    st.dataframe(df6)
                    
                    
DATA3 = pd.read_sql_table("ABERTURAF", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
"driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
"&authentication=ActiveDirectoryIntegrated")

DATA4 = pd.read_sql_table("DADOSF", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
"driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
"&authentication=ActiveDirectoryIntegrated")

                                                                          
if senha != '69':
    video_file = open('./Midia/SSMMOV.mp4', 'rb')
    video_bytes = video_file.read() 
    st.video(video_bytes)
    
if fLIDERES == 'IVSON PAULINO':
    if fSETOR == 'FERRAMENTARIA':
        if senha == '70':
            image = Image.open('./Mídia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            with ps6:
                st.image(image,width=1700)
                st.title('Status e informações de OS')
            b3,b4 = st.columns([1,26])
            with b3:
                if st.button('↻'):
                    DATA3 = pd.read_sql_table("ABERTURAF", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
                    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
                    "&authentication=ActiveDirectoryIntegrated")
                    DATA4 = pd.read_sql_table("DADOSF", con = "mssql+pyodbc://DESKTOP-62QBI08\james:47297913@DESKTOP-62QBI08\WINCCPLUSMIG2014:51304/SSMM?"
                    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
                    "&authentication=ActiveDirectoryIntegrated")
            st.markdown("---")
            tab4,tab5= st.tabs(["Cadastro","OS Abertas"])
            with tab4:
                st.header("Cadastro de ocorrência")
                col1,col2= st.columns(2)  
                with col1:
                    with st.form('my form2'):
                        st.markdown("---")
                        solicitanteF = st.selectbox('Solicitante', ('Selecione','FILIPE',),index=0)
                        statusF = st.selectbox('Tipo de Ocorrência', ('Selecione','ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES'),index=0,)   
                        st.markdown("---")
                        setorF = st.selectbox('Setor', ('Selecione','TECNOLOGIA DA INFORMAÇÃO',), index=0)
                        niveldaocorrenciaF = st.selectbox('Nivel da ocorrência', ('Selecione','EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE', 'URGÊNTE'), index=0)
                        st.markdown("---")
                        relatorioF = st.text_input('Relatorio')
                        tempoiF = st.time_input('HORA DE INICIO', value=None)
                        st.write(tempoiF)
                        st.markdown("---")
                        data = st.date_input("Data", value=None)
                        st.form_submit_button('↻')
                        
                            
                M = MetaData()
                ABERTURAF = Table('ABERTURAF', M,
                        Column('OS', Integer, primary_key=True),
                        Column('SOLICITANTE', String(1000)),
                        Column('SETOR', String(1000)),
                        Column('TIPO_DE_OCORRENCIA', String(1000)),
                        Column('NIVEL_DA_OCÔRRENCIA', String(50)),
                        Column('DATA', (Date)),
                        Column('MOMENTO', (Time)))
                M.create_all(engine) 
                
                M = MetaData()
                DADOSF = Table('DADOSF', M,
                          Column('HORA_INICIADA', (Time(0)), nullable=False))
                M.create_all(engine)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'IVSON PAULINO':
                    if fSETOR == 'FERRAMENTARIA':
                        if senha == '70':
                            if niveldaocorrenciaF != "Selecione":
                                if solicitanteF != "Selecione":
                                    if setorF != "Selecione":
                                        attt = st.button("INSERIR DADOS")
                                        if attt:
                                            ins2 = ABERTURAF.insert()
                                            conn.execute(ins2,SOLICITANTE = solicitanteF, SETOR = setorF, TIPO_DE_OCORRENCIA =                                                                                                                                           statusF,NIVEL_DA_OCÔRRENCIA=niveldaocorrenciaF, DATA = data, MOMENTO = tempoiF)                             
                                            ins3 = DADOSF.insert()
                                            conn.execute(ins3, HORA_INICIADA=tempoiF)
                                        if attt:
                                            st.session_state.OS += 1
                                          
            with tab5:
                statuses,sats,statuses1=st.columns([80,8,20])
                with statuses:
                    def load_data():
                        return pd.DataFrame(DATA3)
                    st.checkbox("Estender", value=True, key= "use_container_width")
                    df8 = load_data()
                    st.dataframe(df8, use_container_width=st.session_state.use_container_width)
        
                with statuses1:
                    df7= pd.DataFrame(DATA2)
                    st.dataframe(df7)
                               
                                    
                                 
                                    
                       






                                   
                              

    


            
                                        
               
                


                

                            
            
            

                 
                 
                 

    





                
