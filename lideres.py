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
import requests
import sqlite3
import openpyxl


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
    nrows=12
    
)

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
        HORAF
       
                   
    )
''')

#MANUTENÇÃO 
query = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Não'"
rd10 = pd.read_sql_query(query, conn6)
rd11 = rd10.shape[0]

query1 = "SELECT * FROM ADMINISTRATIVO WHERE FINALIZADA = 'Sim'"
rd8 = pd.read_sql_query(query1, conn6)
rd9 = rd8.shape[0]

allln17 = pd.read_sql_query("SELECT * FROM ADMINISTRATIVO", conn6)
allln18 = allln17.shape[0]


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
    if fSETOR == 'PRODUÇÃO':
        if senha == '1404':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            cl7 = st.button("DELETAR TABELA")
            if cl7:
                cursor6.execute("DROP TABLE ADMINISTRATIVO")
                conn6.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab34,tab35,tab36,tab37= st.tabs(["Cadastro","OS Abertas","OS Finalizadas","Geral"])
            with tab34:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col13,col14= st.columns(2)  
                with col13:                  
                    atd6 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        As = st.selectbox('Solicitante', ('GILSON FREITAS',),index=None,placeholder='Selecione')
                        if atd6:
                            AUs = st.selectbox('Atualize o Solicitante', ('GILSON FREITAS'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Ast = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd6:
                            AUst = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Astr = st.selectbox('Setor', ('ADMINISTRATIVO',),index=None,placeholder='Selecione')
                        if atd6:
                            AUstr = st.selectbox('Aualize o Setor', ('ADMINISTRATIVO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Ando = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd6:
                            AUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Aac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd6:
                            AUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd6:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

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
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln18,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln18)
                        numros21 = numros12-1
                        osespec12 = allinhas17.loc[numros21]
                        def load_dataa():
                            return pd.DataFrame(osespec12)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                        
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'GILSON FREITAS':
                    if fSETOR == 'PRODUÇÃO':
                        if senha == '1404':
                            Inserts1 = st.button("INSERIR DADOS")
                            if Inserts1:
                                allln12 = allln18 + 1

                            if Inserts1:
                                st.balloons()
                                cursor6.execute("INSERT INTO ADMINISTRATIVO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(As), str(Astr), str(Ast),str(Ando),Adata,str(Atemp),Aac,'Não',None,None))
                                conn6.commit()
                                conn6.close()
                                        
            with tab35:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('ADMINISTRATIVO', divider='rainbow')
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
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab36:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key="use_container_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab37:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key= "uuse_containner_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)















rd8
rd9
rd10
rd11
conn6
cursor6
allln17
allln18
allinhas17
whrlinhas23
whrlinhas24
whrlinhas25
whrlinhas26
whrlinhas27
cl7
col13
col14
tab34
tab35
tab36
tab37
atd6
As
AUs
Ast
AUst
Astr
AUstr
Ando
AUndo
Aac
AUac
Atemp
AUtemp
Adata
AUdata
numros20
numros21
osespec12
osespec13
osespec14
osespec15
Inserts1
insdds3
fnlz8
fnlz9
datainput5
timeinput6
fnl2
'ADMINISTRATIVO'
'ADMINISTRATIVO'
'1404'
'GILSON FREITAS'







