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
        HORAF
       
                   
    )
''')

#MANUTENÇÃO 
query = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não'"
rd6 = pd.read_sql_query(query, conn5)
rd7 = rd6.shape[0]

query1 = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Sim'"
rd4 = pd.read_sql_query(query1, conn5)
rd5 = rd4.shape[0]

allln15 = pd.read_sql_query("SELECT * FROM PRODUCAO", conn5)
allln16 = allln15.shape[0]


#PRODUCAO
#GERAL PRODUCAO
allln15 = pd.read_sql_query("SELECT * FROM PRODUCAO", conn5)
allln16 = allln15.shape[0]
consulta2 = "SELECT * FROM PRODUCAO"
allinhas16 = pd.read_sql_query(consulta2, conn5)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM PRODUCAO WHERE FINALIZADA = 'Não'"
whrlinhas18 = pd.read_sql_query(consulta3, conn5)
whrlinhas19 = whrlinhas18.shape[0]

#OS FINALIZADAS
cursor5.execute("SELECT * FROM PRODUCAO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas20 = cursor5.fetchall()
whrlinhas21 = pd.DataFrame(whrlinhas20)
whrlinhas22 = whrlinhas21.shape[0]



if fLIDERES == 'MAURILIO SALES':
    if fSETOR == 'PRODUÇÃO':
        if senha == '1405':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            cl6 = st.button("DELETAR TABELA")
            if cl6:
                cursor5.execute("DROP TABLE PRODUCAO")
                conn5.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab30,tab31,tab32,tab33= st.tabs(["Cadastro","OS Abertas","OS Finalizadas","Geral"])
            with tab30:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col11,col12= st.columns(2)  
                with col11:                  
                    atd5 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Ps = st.selectbox('Solicitante', ('MAURILIO SALES',),index=None,placeholder='Selecione')
                        if atd5:
                            PUs = st.selectbox('Atualize o Solicitante', ('MAURILIO SALES'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Pst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd5:
                            PUst = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Pstr = st.selectbox('Setor', ('PRODUCAO',),index=None,placeholder='Selecione')
                        if atd5:
                            PUstr = st.selectbox('Aualize o Setor', ('PRODUCAO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Pndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd5:
                            PUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Pac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd5:
                            PUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd5:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

                        Ptemp = st.time_input('Horario', value=None)
                        if atd5:
                            PUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Ptemp)

                        Pdata = st.date_input("Data", value=None)
                        if atd5:
                            PUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col12:
                    if atd5:
                        numros12 = st.number_input("Selecion6numros18 o numero da OS que deseja atualizar",min_value=1,max_value=allln16,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln16)
                        numros19 = numros12-1
                        osespec8 = allinhas16.loc[numros19]
                        def load_dataa():
                            return pd.DataFrame(osespec8)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                        
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'MAURILIO SALES':
                    if fSETOR == 'PRODUÇÃO':
                        if senha == '1405':
                            Inserts = st.button("INSERIR DADOS")
                            if Inserts:
                                allln12 = allln16 + 1

                            if Inserts:
                                st.balloons()
                                cursor5.execute("INSERT INTO PRODUCAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(Ps), str(Pstr), str(Pst),str(Pndo),Pdata,str(Ptemp),Pac,'Não',None,None))
                                conn5.commit()
                                conn5.close()
                                        
            with tab31:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('PRODUCAO', divider='rainbow')
                    with st.expander("Abertas"):
                        numros22 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas19,value=0,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas19)
                        numros23 = numros22-1
                        if whrlinhas19 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec9 = whrlinhas18.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec9)
                            st.checkbox("Estender", value=True, key="usee_containner_widthh")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab32:
                st.header('PRODUCAO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key="use_container_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab33:
                st.header('PRODUCAO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key= "uuse_containner_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)















rd4
rd5
rd6
rd7
conn5
cursor5
allln15
allln16
allinhas16
whrlinhas18
whrlinhas19
whrlinhas20
whrlinhas21
whrlinhas22
cl6
col11
col12
tab30
tab31
tab32
tab33
atd5
Ps
PUs
Pst
PUst
Pstr
PUstr
Pndo
PUndo
Pac
PUac
Ptemp
PUtemp
Pdata
PUdata
numros18
numros19
osespec8
osespec9
osespec10
osespec11
Inserts
insdds3
fnlz8
fnlz9
datainput5
timeinput6
fnl2
'PRODUCAO'
'1405'
'MAURILIO SALES'






