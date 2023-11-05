import pandas as pd
import streamlit as st
from PIL import Image
import time as time
import datetime as datetime
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, event
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, MetEdata, Column, Integer, String, FLOAT, VARCHAR, Date, Time
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
    
    with st.spinner("CarregEndo..."):
                time.sleep(2)
                st.success("Pronto!")
    st.write("Bem Vindo")
    
    st.write('✅')
    tab1_qtde_produto = df.loc[(
    df['SETOR'] == fSETOR) &
    (df['LIDERES'] == fLIDERES)]

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
        HORAF
       
                   
    )
''')

#MANUTENÇÃO 
query = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Não'"
rd18 = pd.read_sql_query(query, conn8)
rd19 = rd18.shape[0]

query1 = "SELECT * FROM EXPEDICAO WHERE FINALIZADA = 'Sim'"
rd16 = pd.read_sql_query(query1, conn8)
rd17 = rd16.shape[0]

allln21 = pd.read_sql_query("SELECT * FROM EXPEDICAO", conn8)
allln22 = allln21.shape[0]


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
            cl9 = st.button("DELETAR TABELA")
            if cl9:
                cursor8.execute("DROP TABLE EXPEDICAO")
                conn8.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab42,tab43,tab44,tab45= st.tabs(["Cadastro","OS Abertas","OS Finalizadas","Geral"])
            with tab42:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col17,col18= st.columns(2)  
                with col17:                  
                    atd8 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Ec = st.selectbox('Solicitante', ('ALEX SANTOS',),index=None,placeholder='Selecione')
                        if atd8:
                            Eus = st.selectbox('Atualize o Solicitante', ('ALEX SANTOS'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        East = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd8:
                            Eust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Eastr = st.selectbox('Setor', ('EXPEDICAO',),index=None,placeholder='Selecione')
                        if atd8:
                            EUstr = st.selectbox('Aualize o Setor', ('EXPEDICAO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Endo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd8:
                            EUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Eac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd8:
                            EUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd8:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

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
                            st.checkbox("Estender", value=True, key="use_container_widthh")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'ALEX SANTOS':
                    if fSETOR == 'EXPEDIÇÃO':
                        if senha == '1402':
                            Inserts3 = st.button("INSERIR DADOS")
                            if Inserts3:
                                allln12 = allln22 + 1

                            if Inserts3:
                                st.balloons()
                                cursor8.execute("INSERT INTO EXPEDICAO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(Ec), str(Eastr), str(East),str(Endo),Edata,str(Etemp),Eac,'Não',None,None))
                                conn8.commit()
                                conn8.close()
                                        
            with tab43:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('EXPEDICAO', divider='rainbow')
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
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab44:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key="use_container_width      ")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab45:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key= "uuse_containner_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)















rd16
rd17
rd18
rd19
conn8
cursor8
allln21
allln22
allinhas19
whrlinhas33
whrlinhas34
whrlinhas35
whrlinhas36
whrlinhas37
cl9
col17
col18
tab42
tab43
tab44
tab45
atd8
Ec
Eus
East
Eust
Eastr
EUstr
Endo
EUndo
Eac
EUac
Etemp
EUtemp
Edata
EUdata
numros24
numros25
osespec20
osespec21
osespec22
osespec23
Inserts3
'EXPEDICAO'
'EXPEDICAO'
'1402'
'ALEX SANTOS'







