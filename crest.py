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

conn2 = sqlite3.connect('CESAR FILHO')
cursor2 = conn2.cursor()
cursor2.execute('''
    CREATE TABLE IF NOT EXISTS CESAR FILHO (
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



#leitura do banco CESAR FILHO
allln7 = pd.read_sql_query("SELECT * FROM CESAR FILHO", conn2)
allln8 = allln7.shape[0]
consulta2 = "SELECT * FROM CESAR FILHO"
allinhas1 = pd.read_sql_query(consulta2, conn2)

#OS ABERTAS  NÃO FINALIZADAS 
cursor2.execute("SELECT * FROM CESAR FILHO WHERE FINALIZADA = ?;", ('Não',))
whlinhas6 = cursor2.fetchall()
whrlinhas7 = pd.DataFrame(whlinhas6)
whrlinhas8 = whrlinhas7.shape[0]  

#OS FINALIZADAS
cursor2.execute("SELECT * FROM CESAR FILHO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas9 = cursor2.fetchall()
whrlinhas10 = pd.DataFrame(whrlinhas9)
whrlinhas11 = whrlinhas10.shape[0]



if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'CESAR FILHO':
    if fSETOR == 'MECÂNICA':
        if senha == '1407':
            cl3 = st.button("DELETAR TABELA")
            if cl3:
                cursor2.execute("DROP TABLE CESAR FILHO")
                conn2.commit()
            image = Image.open('./Midia/ssmm.jpg')
            col5,col6 = st.columns([1,1])
            with col5:
                st.title('Status e informações de OS')
           
            tab16, tab17,tab18,tab19,tab20= st.tabs(["Cadastro", "Finalizar","OS Em aberto","OS Finalizadas","Geral"])
            with tab16:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd3 = st.toggle('Atualizar os dados')
                    with st.form('my form3'):
                        st.markdown("---")
                        Csolicitante = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        if atd3:
                            CUsolicitante = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Cstatus = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd3:
                            CUstatus = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Csetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd3:
                            CUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Cniveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd3:
                            CUniveldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Cacao = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd3:
                            CUacao = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd3:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

                        Ctempoi = st.time_input('Horario', value=None)
                        if atd3:
                            CUtempoi = st.time_input('Atualize o Horario', value=None)
                            st.write(Ctempoi)

                        Cdata = st.date_input("Data", value=None)
                        if atd3:
                            CUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with neymar:
                    if atd3:
                        numros8 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln8,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln8)
                        numros9 = numros8-1
                        osespec2 = allinhas1.loc[numros9]
                        def load_dataa():
                            return pd.DataFrame(osespec2)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        conn2.close()


                if fLIDERES == 'CESAR FILHO':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1407':
                            if Cniveldaocorrencia != "Selecione":
                                if Csolicitante != "Selecione":
                                    if Csetor != "Selecione":
                                            if atd3: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl2 = st.button('atualize')
                                                if atl2:
                                                   st.balloons()
                                                   cursor2.execute("UPDATE CESAR FILHO SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(CUsolicitante, CUsetor, CUstatus,CUniveldaocorrencia,CUdata,str(CUtempoi),CUacao,numros8))
                                                   conn2.commit()
                                                   conn2.close()
                                                
                                            else:
                                                insdds2 = st.button("INSERIR DADOS")

                                                if insdds2:
                                                   allln6 = allln8 + 1
                                                if insdds2:
                                                   st.balloons()
                                                   cursor2.execute("INSERT INTO CESAR FILHO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln6 , str(Csolicitante), str(Csetor), str(Cstatus),str(Cniveldaocorrencia),Cdata,str(Ctempoi),Cacao,'Não',None,None))
                                                   conn2.commit()
                                                   conn2.close()
                                                    
            with tab17:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    fnlz6 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=allln8,value=0,placeholder="Selecione")
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        fnlz7 = fnlz6-1
                        datainput3 = st.date_input("Data", value=None)
                        st.write(datainput3)
                        st.markdown("---")
                        timeinput4 = st.time_input('HORA', value=None)
                        st.write(timeinput4)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'CESAR FILHO':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1407':                                                                                                                     
                            fnl1=st.button("FINALIZAR")
                            if fnl1:
                                cursor2.execute("UPDATE CESAR FILHO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput3,str(timeinput4),fnlz6))
                                conn2.commit()
                                conn2.close()
                                st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente com uma flor.')
                                
                            
            with tab18:
                st.metric(label="OS em aberto", value= whrlinhas8)
                whrlinhas7 = pd.DataFrame(whlinhas6)
                st.dataframe(whrlinhas7)
                st.write(whrlinhas8)
                

            with tab19:
                st.metric(label="OS Finalizadas",value=whrlinhas11)
                whrlinhas10 = pd.DataFrame(whrlinhas9)
                st.dataframe(whrlinhas10)
                st.write(whrlinhas11)

            with tab20:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                    numros10 = st.number_input("Selecione o numero da OS",min_value=1,max_value=allln8,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln8)
                    numros11 = numros10-1
                    osespec2 = allinhas1.loc[numros11]
                    def load_data():
                        return pd.DataFrame(osespec2)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)




allln6
allln7
allln8
cl3
col5
col6
tab16
tab17
tab18
tab19
tab20
atd3
Csolicitante
CUsolicitante
Cstatus
CUstatus
Csetor
CUsetor
Cniveldaocorrencia
CUniveldaocorrencia
Cacao
CUacao
Ctempoi
CUtempoi
Cdata
CUdata
numros8
numros9
numros10
numros11
osespec2
atl2
insdds2
fnlz6
fnlz7
datainput3
timeinput4
fnl1
'CESAR FILHO'
'1407'
'MECÂNICA'