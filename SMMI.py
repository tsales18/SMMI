import pandas as pd
import streamlit as st
import pyodbc
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
import sqlite3
import MySQLdb



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
    
tab1_qtde_produto = df.loc[(
    df['SETOR'] == fSETOR) &
    (df['LIDERES'] == fLIDERES)]

conn = sqlite3.connect('SMMI')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ABERTURA (
        OS INTEGER PRIMARY KEY,
        SOLCITANTE TEXT,
        SETOR TEXT,
        TIPO_DE_OCORRENCIA TEXT,
        NIVEL_DA_OCORRENCIA TEXT,
        DATA DATE,
        HORA TIME
                   
    )
''')  

#leitura do banco smmi
cnt = pd.read_sql_query("SELECT * FROM ABERTURA", conn)
cnt1 = cnt.shape[0]
ln = pd.read_sql_query("SELECT * FROM ABERTURA", conn)

cl = st.button("close")
if cl:
   cursor.execute("DROP TABLE ABERTURA")
   conn.commit()

if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'FELIPE LEITE':
    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps1,ps2,ps3,ps4,ps5 = st.columns(5)
            with ps1:
                st.image(image,width=1700)
                st.title('Status e informações de OS')
           
            tab1, tab2, tab3= st.tabs(["Cadastro", "Finalizar","OS Abertas"])
            with tab1:
                st.header("Cadastro de ocorrência")
                colibrim,neymar,lula,sales,poura= st.columns([1,1,0.1,0.1,0.1])  
                with colibrim:
                    with st.form('my form2'):
                        st.markdown("---")
                        atd = st.toggle('Atualizar os dados')
                        solicitante = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        st.markdown("---")
                        status = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        st.markdown("---")
                        setor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Selecione')
                        st.markdown("---")
                        niveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        st.markdown("---")
                        relatorio = st.text_input('Relatorio')
                        st.markdown("---")
                        tempoi = st.time_input('Horario', value=None)
                        st.markdown("---")                    
                        data = st.date_input("Data", value=None)
                        st.markdown("---")
                        st.form_submit_button('↻')
                with neymar:
                    with st.form('my form3'):
                        st.markdown("---")
                        atd = st.toggle('Inserir os dados')
                        if atd:
                            Usolicitante = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        if atd:
                            Ustatus = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES'),index=None, placeholder='Selecione')
                            st.markdown("---")
                        if atd:
                            Usetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        if atd:
                            Univeldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Selecione')
                            st.markdown("---")
                        if atd:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")
                        if atd:
                            Utempoi = st.time_input('Atualize o Horario', value=None)
                            st.markdown("---")
                        if atd:
                            Udata = st.date_input("Atualize a Data", value=None)
                            st.markdown("---")
                        st.form_submit_button('bah')
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if niveldaocorrencia != "Selecione":
                                if solicitante != "Selecione":
                                    if setor != "Selecione":   
                                            st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                            att = st.button("INSERIR DADOS")
                                            if att:
                                               cnt3 = cnt1 + 1
                                            if att:
                                               st.balloons()
                                               cursor.execute("INSERT INTO ABERTURA (OS,SOLCITANTE,SETOR,TIPO_DE_OCORRENCIA,NIVEL_DA_OCORRENCIA,DATA,HORA) VALUES (?, ?, ?, ?, ?, ?,?)", (cnt3 , str(solicitante), str(setor), str(status),str(niveldaocorrencia),data,str(tempoi)))
                                               conn.commit()
                                               conn.close()
                                               
                                            
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
                                  
                  
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                                st.caption('É necessario ABRIR outra OS para finalizar.') 
                                
                        else:
                            st.caption('É necessario finalizar esta OS antes de inciar outra.')                                                                                                                         
                            FIn=st.button("FINALIZAR")
                            
                  
            with tab3:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                   Nmr = st.number_input("Selecione o numero da OS",min_value=1,max_value=cnt1,value=1,placeholder="Selecione")
                   st.metric(label="OS Existentes", value= cnt1)
                   Nmr1 = Nmr-1
                   ln1 = ln.loc[Nmr1]
                   st.dataframe(ln1)
                   conn.close()
        
                with sats:
                    st.write('OPA')
                                  
                with statuses1:                
                    st.write('OPA')
                                                                                         
if senha != '69':
    video_file = open('./Midia/SSMMOV.mp4', 'rb')
    video_bytes = video_file.read() 
    st.video(video_bytes) 
    
if fLIDERES == 'IVSON PAULINO':
    if fSETOR == 'FERRAMENTARIA':
        if senha == '70':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            with ps6:
                st.image(image,width=1700)
                st.title('Status e informações de OS')

            st.markdown("---")
            tab4,tab5= st.tabs(["Cadastro","OS Abertas"])
            with tab4:
                st.header("Cadastro de ocorrência")
                col1,col2= st.columns(2)  
                with col1:
                    with st.form('my form2'):
                        st.markdown("---")
                        solicitanteF = st.selectbox('Solicitante', ('FILIPE',),index=0)
                        statusF = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES'),index=0,)   
                        st.markdown("---")
                        setorF = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO',), index=0)
                        niveldaocorrenciaF = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE', 'URGÊNTE'), index=0)
                        st.markdown("---")
                        relatorioF = st.text_input('Relatorio')
                        tempoiF = st.time_input('HORA DE INICIO', value=None)
                        st.write(tempoiF)
                        st.markdown("---")
                        dataF = st.date_input("Data", value=None)
                        st.form_submit_button('↻')
                        
                
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
                                        
                                            
                                        
                                          
            with tab5:
                statuses,sats,statuses1=st.columns([80,8,20])
                with statuses:
                    st.dataframe(tempoi)
    
                with statuses1:
                    st.dataframe(tempoiF)



   