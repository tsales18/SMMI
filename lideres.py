import pandas as pd
import streamlit as st
from PIL import Image
import time as time
import datetime as datetime
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, event
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, MetSdata, Column, Integer, String, FLOAT, VARCHAR, Date, Time
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
    
    with st.spinner("CarregSndo..."):
                time.sleep(2)
                st.success("Pronto!")
    st.write("Bem Vindo")
    
    st.write('✅')
    tab1_qtde_produto = df.loc[(
    df['SETOR'] == fSETOR) &
    (df['LIDERES'] == fLIDERES)]

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
        HORAF
       
                   
    )
''')

#MANUTENÇÃO 
query = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Não'"
rd22 = pd.read_sql_query(query, conn9)
rd23 = rd22.shape[0]

query1 = "SELECT * FROM SERRALHARIA WHERE FINALIZADA = 'Sim'"
rd20 = pd.read_sql_query(query1, conn9)
rd21 = rd20.shape[0]

allln23 = pd.read_sql_query("SELECT * FROM SERRALHARIA", conn9)
allln24 = allln23.shape[0]


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
            cl10 = st.button("DELETAR TABELA")
            if cl10:
                cursor9.execute("DROP TABLE SERRALHARIA")
                conn9.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab46,tab47,tab48,tab49= st.tabs(["Cadastro","OS Abertas","OS Finalizadas","Geral"])
            with tab46:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col19,col20= st.columns(2)  
                with col19:                  
                    atd9 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Sc = st.selectbox('Solicitante', ('CESAR AUGUSTO',),index=None,placeholder='Selecione')
                        if atd9:
                            SUs = st.selectbox('Atualize o Solicitante', ('CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Sst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd9:
                            Sust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Sstr = st.selectbox('Setor', ('SERRALHARIA',),index=None,placeholder='Selecione')
                        if atd9:
                            SUstr = st.selectbox('Aualize o Setor', ('SERRALHARIA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Sndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd9:
                            SUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Sac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd9:
                            EUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd9:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

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
                            st.checkbox("Estender", value=True, key="use_container_widthh")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'CESAR AUGUSTO':
                    if fSETOR == 'SERRALHARIA':
                        if senha == '1401':
                            Inserts4 = st.button("INSERIR DADOS")
                            if Inserts4:
                                allln12 = allln24 + 1

                            if Inserts4:
                                st.balloons()
                                cursor9.execute("INSERT INTO SERRALHARIA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(Sc), str(Sstr), str(Sst),str(Sndo),Sdata,str(Stemp),Sac,'Não',None,None))
                                conn9.commit()
                                conn9.close()
                                        
            with tab47:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('SERRALHARIA', divider='rainbow')
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
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab48:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key="use_container_width      ")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab49:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key= "uuse_containner_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)















rd20
rd21
rd22
rd23
conn9
cursor9
allln23
allln24
allinhas20
whrlinhas38
whrlinhas39
whrlinhas40
whrlinhas41
whrlinhas42
cl10
col19
col20
tab46
tab47
tab48
tab49
atd9
Sc
SUs
Sst
Sust
Sstr
SUstr
Sndo
SUndo
Sac
EUac
Stemp
SUtemp
Sdata
SUdata
numros26
numros27
osespec24
osespec25
osespec26
osespec27
Inserts4
'SERRALHARIA'
'SERRALHARIA'
'1401'
'CESAR AUGUSTO'







