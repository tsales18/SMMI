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
        HORAF
       
                   
    )
''')
#feedback
query = "SELECT * FROM ROSIVALDO WHERE SETOR = 'FERRAMENTARIA' AND FINALIZADA = 'Não'"
rd2 = pd.read_sql_query(query, conn1)
rd3 = rd2.shape[0]
ddd = rd2.loc[0]

query = "SELECT * FROM ROSIVALDO WHERE SETOR = 'FERRAMENTARIA' AND FINALIZADA = 'Sim'"
rd = pd.read_sql_query(query, conn1)
rd1 = rd.shape[0]
rdd = rd.loc


allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
allln14 = allln13.shape[0]
consulta2 = "SELECT * FROM FERRAMENTARIA"
allinhas15 = pd.read_sql_query(consulta2, conn4)

#OS ABERTAS  NÃO FINALIZADAS 
cursor4.execute("SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = ?;", ('Não',))
whrlinhas12 = cursor4.fetchall()
whrlinhas13 = pd.DataFrame(whrlinhas12)
whrlinhas14 = whrlinhas13.shape[0]  

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
            cl5 = st.button("DELETAR TABELA")
            if cl5:
                cursor4.execute("DROP TABLE FERRAMENTARIA")
                conn4.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab26,tab27,tab28,tab29= st.tabs(["Cadastro","OS Abertas","OS Finalizadas","Geral"])
            with tab26:
                st.header("Cadastro de ocorrência")
                col9,col10= st.columns(2)  
                with col9:                  
                    atd4 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Fs = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        if atd4:
                            FUs = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Fst = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd4:
                            FUst = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Fstr = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd4:
                            Fustr = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Fndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd4:
                            FUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Fac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd4:
                            Fuac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd4:
                            Urelatorio = st.text_input('Atualize o Relatorio')
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
                        numros12 = st.number_input("Selecion6numros16 o numero da OS que deseja atualizar",min_value=1,max_value=allln14,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln14)
                        numros17 = numros12-1
                        osespec4 = allinhas15.loc[numros17]
                        def load_dataa():
                            return pd.DataFrame(osespec4)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        conn4.close()
                        
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'IVSON PAULINO':
                    if fSETOR == 'FERRAMENTARIA':
                        if senha == '70':
                            attt = st.button("INSERIR DADOS")
                            if attt:
                                if attt:
                                    allln12 = allln14 + 1

                                if attt:
                                    cursor4.execute("INSERT INTO FERRAMENTARIA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln9 , str(Fs), str(Fstr), str(Fst),str(Fndo),Fdata,str(Ftemp),Fac,'Não',None,None))
                                    conn4.commit()
                                    conn4.close()
                                        
            with tab27:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    numros18 = st.number_input("Selecione o numero da OS",min_value=1,max_value=rd3,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd3)
                    numros19 = numros18-1
                    osespec4 = rd2.loc[numros19]
                    def load_data():
                        return pd.DataFrame(osespec4)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)
                with sats:
                    numros18 = st.number_input("Selecione o numero da OS",min_value=1,max_value=whrlinhas14,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= whrlinhas14)
                    numros19 = numros18-1
                    osespec5 = whrlinhas13.loc[numros19]
                    def load_data():
                        return pd.DataFrame(osespec5)
                    st.checkbox("Estender", value=True, key="use_container_widthh")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab28:
                numros16 = st.number_input("Selecione o numero da  OS",min_value=1,max_value=rd1,value=1,placeholder="Selecione")
                st.metric(label="OS Existentes", value= rd1)
                numros17 = numros16-1
                osespec6 = rd.loc[numros17]
                def load_data():
                    return pd.DataFrame(osespec6)
                st.checkbox("Estender", value=True, key= "use_containner_width")
                df = load_data()
                st.dataframe(df, use_container_width=st.session_state.use_container_width)


conn4
cursor4
allln13
allln14
allinhas15
whrlinhas12
whrlinhas13
whrlinhas14
whrlinhas15
whrlinhas16
whrlinhas17
cl5
col9
col10
tab26
tab27
tab28
tab29
atd4
Fs
FUs
Fst
FUst
Fstr
Fustr
Fndo
FUndo
Fac
Fuac
Ftemp
FUtemp
Fdata
FUdata
numros16
numros17
numros18
numros19
osespec4
osespec5
osespec6
osespec7
atl3
insdds3
fnlz8
fnlz9
datainput5
timeinput6
fnl2
'FERRAMENTARIA FABIO'
'1406'
'MECÂNICA'






