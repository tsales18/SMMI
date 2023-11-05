import pandas as pd
import streamlit as st
from PIL import Image
import time as time
import datetime as datetime
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, event
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, MetCdata, Column, Integer, String, FLOAT, VARCHAR, Date, Time
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
    
    with st.spinner("CarregCando..."):
                time.sleep(2)
                st.success("Pronto!")
    st.write("Bem Vindo")
    
    st.write('✅')
    tab1_qtde_produto = df.loc[(
    df['SETOR'] == fSETOR) &
    (df['LIDERES'] == fLIDERES)]

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
        HORAF
       
                   
    )
''')

#MANUTENÇÃO 
query = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Não'"
rd14 = pd.read_sql_query(query, conn7)
rd15 = rd14.shape[0]

query1 = "SELECT * FROM COMERCIAL WHERE FINALIZADA = 'Sim'"
rd12 = pd.read_sql_query(query1, conn7)
rd13 = rd12.shape[0]

allln19 = pd.read_sql_query("SELECT * FROM COMERCIAL", conn7)
allln120 = allln19.shape[0]


#COMERCIAL
#GERAL COMERCIAL
allln19 = pd.read_sql_query("SELECT * FROM COMERCIAL", conn7)
allln120 = allln19.shape[0]
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
    if fSETOR == 'PRODUÇÃO':
        if senha == '1403':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            cl8 = st.button("DELETAR TABELA")
            if cl8:
                cursor7.execute("DROP TABLE COMERCIAL")
                conn7.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab38,tab39,tab40,tab41= st.tabs(["CadCastro","OS Abertas","OS Finalizadas","Geral"])
            with tab38:
                st.header('CadCastro de ocorrências', divider='rainbow')
                col15,col16= st.columns(2)  
                with col15:                  
                    atd7 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Cs = st.selectbox('Solicitante', ('ADRIELY LEMOS',),index=None,placeholder='Selecione')
                        if atd7:
                            Cus = st.selectbox('Atualize o Solicitante', ('ADRIELY LEMOS'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Cast = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd7:
                            Cust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Castr = st.selectbox('Setor', ('COMERCIAL',),index=None,placeholder='Selecione')
                        if atd7:
                            Custr = st.selectbox('Aualize o Setor', ('COMERCIAL'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Cando = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd7:
                            Cundo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Cac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd7:
                            CUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd7:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

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
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln120,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln120)
                        numros23 = numros12-1
                        osespec16 = allinhas18.loc[numros23]
                        def load_dataa():
                            return pd.DataFrame(osespec16)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                        
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'ADRIELY LEMOS':
                    if fSETOR == 'PRODUÇÃO':
                        if senha == '1403':
                            Inserts2 = st.button("INSERIR DADOS")
                            if Inserts2:
                                allln12 = allln120 + 1

                            if Inserts2:
                                st.balloons()
                                cursor7.execute("INSERT INTO COMERCIAL (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(Cs), str(Castr), str(Cast),str(Cando),Cdata,str(Ctemp),Cac,'Não',None,None))
                                conn7.commit()
                                conn7.close()
                                        
            with tab39:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('COMERCIAL', divider='rainbow')
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
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab40:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key="use_container_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab41:
                st.header('PRODUÇÃO', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key= "uuse_containner_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)















rd12
rd13
rd14
rd15
conn7
cursor7
allln19
allln120
allinhas18
whrlinhas28
whrlinhas29
whrlinhas30
whrlinhas31
whrlinhas32
cl8
col15
col16
tab38
tab39
tab40
tab41
atd7
Cs
Cus
Cast
Cust
Castr
Custr
Cando
Cundo
Cac
CUac
Ctemp
CUtemp
Cdata
CUdata
numros22
numros23
osespec16
osespec17
osespec18
osespec19
Inserts2
insdds3
fnlz8
fnlz9
datainput5
timeinput6
fnl2
'COMERCIAL'
'COMERCIAL'
'1403'
'ADRIELY LEMOS'







