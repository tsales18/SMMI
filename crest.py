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

conn1 = sqlite3.connect('SMMI')
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
        FINALIZADA TEXT   
                   
    )
''')



#leitura do banco smmi
allln = pd.read_sql_query("SELECT * FROM ROSIVALDO", conn1)
allln1 = allln.shape[0]
consulta1 = "SELECT * FROM ROSIVALDO"
allinhas = pd.read_sql_query(consulta1, conn1)

#OS ABERTAS  NÃO FINALIZADAS 
cursor1.execute("SELECT * FROM ROSIVALDO WHERE FINALIZADA = ?;", ('Não',))
whlinhas = cursor1.fetchall()
whrlinhas1 = pd.DataFrame(whlinhas)
whrlinhas2 = whrlinhas1.shape[0]  

#OS FINALIZADAS
cursor1.execute("SELECT * FROM ROSIVALDO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas3 = cursor1.fetchall()
whrlinhas4 = pd.DataFrame(whrlinhas3)
whrlinhas5 = whrlinhas4.shape[0]



if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'ROSIVALDO':
    if fSETOR == 'ELÉTRICA':
        if senha == '1409':
            image = Image.open('./Midia/ssmm.jpg')
            col1,col2 = st.columns([1,1])
            with col1:
                st.title('Status e informações de OS')
           
            tab6, tab7,tab8,tab9,tab10= st.tabs(["Cadastro", "Finalizar","OS Em aberto","OS Finalizadas","Geral"])
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

                        Rstatus = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd1:
                            RUstatus = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Rsetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd1:
                            RUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Rniveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd1:
                            RUniveldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Racao = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd1:
                            RUacao = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd1:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

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
                        numros = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln1,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros1 = numros-1
                        osespec = allinhas.loc[numros1]
                        def load_dataa():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        conn1.close()


                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '1409':
                            if Rniveldaocorrencia != "Selecione":
                                if Rsolicitante != "Selecione":
                                    if Rsetor != "Selecione":
                                            if atd1: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl = st.button('atualize')
                                                if atl:
                                                   st.balloons()
                                                   cursor1.execute("UPDATE ROSIVALDO SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(RUsolicitante, RUsetor, RUstatus,RUniveldaocorrencia,RUdata,str(RUtempoi),RUacao,numros))
                                                   conn1.commit()
                                                   conn1.close()
                                                
                                            else:
                                                att = st.button("INSERIR DADOS")

                                                if att:
                                                   allln3 = allln1 + 1
                                                if att:
                                                   st.balloons()
                                                   cursor1.execute("INSERT INTO ROSIVALDO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA) VALUES (?, ?, ?, ?, ?, ?,?,?,?)", (allln3 , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),Rdata,str(Rtempoi),Racao,'Não'))
                                                   conn1.commit()
                                                   conn1.close()
                                               
                     
            with tab7:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    fnlz2 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=1,max_value=allln1,value=1,placeholder="Selecione")
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        fnlz3 = fnlz2-1
                        datainput = st.date_input("Data", value=None)
                        st.write(datainput)
                        st.markdown("---")
                        timeinput = st.time_input('HORA', value=None)
                        st.write(timeinput)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '1409':                                                                                                                     
                            fnl=st.button("FINALIZAR")
                            if fnl:
                                cursor1.execute("UPDATE ROSIVALDO SET FINALIZADA = ? WHERE OS = ?",(finalizar,fnlz2))
                                conn1.commit()
                                conn1.close()
                                st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente com uma flor.')
                                
                            
            with tab8:
                st.metric(label="OS em aberto", value= whrlinhas2)
                whrlinhas1 = pd.DataFrame(whlinhas)
                st.dataframe(whrlinhas1)
                st.write(whrlinhas2)
                

            with tab9:
                st.metric(label="OS Finalizadas", value= whrlinhas5)
                whrlinhas4 = pd.DataFrame(whrlinhas3)
                st.dataframe(whrlinhas4)
                st.write(whrlinhas5)

            with tab10:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                    Nmr = st.number_input("Selecione o numero da OS",min_value=1,max_value=allln1,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln1)
                    Nmr1 = Nmr-1
                    osespec = allinhas.loc[Nmr1]
                    def load_data():
                        return pd.DataFrame(osespec)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)
                    