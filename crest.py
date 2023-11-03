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

conn2 = sqlite3.connect('IVANILDO')
cursor2 = conn2.cursor()
cursor2.execute('''
    CREATE TABLE IF NOT EXISTS IVANILDO (
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



#leitura do banco rosivaldo
allln4 = pd.read_sql_query("SELECT * FROM ROSIVALDO", conn2)
allln5 = allln4.shape[0]
consulta2 = "SELECT * FROM ROSIVALDO"
allinhas1 = pd.read_sql_query(consulta2, conn2)

#OS ABERTAS  NÃO FINALIZADAS 
cursor2.execute("SELECT * FROM ROSIVALDO WHERE FINALIZADA = ?;", ('Não',))
whlinhas6 = cursor2.fetchall()
whrlinhas7 = pd.DataFrame(whlinhas6)
whrlinhas8 = whrlinhas7.shape[0]  

#OS FINALIZADAS
cursor2.execute("SELECT * FROM ROSIVALDO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas9 = cursor2.fetchall()
whrlinhas10 = pd.DataFrame(whrlinhas9)
whrlinhas11 = whrlinhas10.shape[0]



if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'IVANILDO':
    if fSETOR == 'ELÉTRICA':
        if senha == '1408':
            cl2 = st.button("DELETAR TABELA")
            if cl2:
                cursor2.execute("DROP TABLE ROSIVALDO")
                conn2.commit()
            image = Image.open('./Midia/ssmm.jpg')
            col3,col4 = st.columns([1,1])
            with col3:
                st.title('Status e informações de OS')
           
            tab11, tab12,tab13,tab14,tab15= st.tabs(["Cadastro", "Finalizar","OS Em aberto","OS Finalizadas","Geral"])
            with tab11:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd2 = st.toggle('Atualizar os dados')
                    with st.form('my form3'):
                        st.markdown("---")
                        Isolicitante = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        if atd2:
                            IUsolicitante = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Istatus = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd2:
                            IUstatus = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Isetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd2:
                            IUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Iniveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd2:
                            IUniveldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Iacao = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd2:
                            IUacao = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd2:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

                        Itempoi = st.time_input('Horario', value=None)
                        if atd2:
                            IUtempoi = st.time_input('Atualize o Horario', value=None)
                            st.write(Itempoi)

                        Idata = st.date_input("Data", value=None)
                        if atd2:
                            IUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with neymar:
                    if atd2:
                        numros4 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln5,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln5)
                        numros5 = numros4-1
                        osespec1 = allinhas1.loc[numros5]
                        def load_dataa():
                            return pd.DataFrame(osespec1)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        conn2.close()


                if fLIDERES == 'IVANILDO':
                    if fSETOR == 'ELÉTRICA':
                        if senha == '1408':
                            if Iniveldaocorrencia != "Selecione":
                                if Isolicitante != "Selecione":
                                    if Isetor != "Selecione":
                                            if atd2: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl1 = st.button('atualize')
                                                if atl1:
                                                   st.balloons()
                                                   cursor2.execute("UPDATE ROSIVALDO SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(IUsolicitante, IUsetor, IUstatus,IUniveldaocorrencia,IUdata,str(IUtempoi),IUacao,numros4))
                                                   conn2.commit()
                                                   conn2.close()
                                                
                                            else:
                                                insdds1 = st.button("INSERIR DADOS")

                                                if insdds1:
                                                   allln3 = allln5 + 1
                                                if insdds1:
                                                   st.balloons()
                                                   cursor2.execute("INSERT INTO ROSIVALDO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln3 , str(Isolicitante), str(Isetor), str(Istatus),str(Iniveldaocorrencia),Idata,str(Itempoi),Iacao,'Não',None,None))
                                                   conn2.commit()
                                                   conn2.close()
                                                    
            with tab12:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    fnlz4 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=allln5,value=0,placeholder="Selecione")
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        fnlz5 = fnlz4-1
                        datainput2 = st.date_input("Data", value=None)
                        st.write(datainput2)
                        st.markdown("---")
                        timeinput2 = st.time_input('HORA', value=None)
                        st.write(timeinput2)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'IVANILDO':
                    if fSETOR == 'ELÉTRICA':
                        if senha == '1408':                                                                                                                     
                            fnl=st.button("FINALIZAR")
                            if fnl:
                                cursor2.execute("UPDATE ROSIVALDO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput2,str(timeinput2),fnlz4))
                                conn2.commit()
                                conn2.close()
                                st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente com uma flor.')
                                
                            
            with tab13:
                st.metric(label="OS em aberto", value= whrlinhas8)
                whrlinhas7 = pd.DataFrame(whlinhas6)
                st.dataframe(whrlinhas7)
                st.write(whrlinhas8)
                

            with tab14:
                st.metric(label="OS Finalizadas",value=whrlinhas11)
                whrlinhas10 = pd.DataFrame(whrlinhas9)
                st.dataframe(whrlinhas10)
                st.write(whrlinhas11)

            with tab15:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                    numros6 = st.number_input("Selecione o numero da OS",min_value=1,max_value=allln5,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln5)
                    numros7 = numros6-1
                    osespec1 = allinhas1.loc[numros7]
                    def load_data():
                        return pd.DataFrame(osespec1)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)




cl2
col3
col4
tab11
tab12
tab13
tab14
tab15
atd2
Isolicitante
IUsolicitante
Istatus
IUstatus
Isetor
IUsetor
Iniveldaocorrencia
IUniveldaocorrencia
Iacao
IUacao
Itempoi
Idata
IUdata
numros4
numros5
numros6
numros7
osespec1
atl1
insdds1
fnlz4
fnlz5
datainput2
timeinput2
fnl
'IVANILDO'
'1408'