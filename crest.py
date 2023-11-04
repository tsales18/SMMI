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



#leitura do banco FERRAMENTARIA
allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
allln14 = allln13.shape[0]
consulta2 = "SELECT * FROM FERRAMENTARIA"
allinhas1 = pd.read_sql_query(consulta2, conn4)

#OS ABERTAS  NÃO FINALIZADAS 
cursor4.execute("SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = ?;", ('Não',))
whlinhas12 = cursor4.fetchall()
whrlinhas13 = pd.DataFrame(whlinhas12)
whrlinhas14 = whrlinhas13.shape[0]  

#OS FINALIZADAS
cursor4.execute("SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas15 = cursor4.fetchall()
whrlinhas16 = pd.DataFrame(whrlinhas15)
whrlinhas17 = whrlinhas16.shape[0]



if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'FERRAMENTARIA':
    if fSETOR == 'MECÂNICA':
        if senha == '1407':
            cl4 = st.button("DELETAR TABELA")
            if cl4:
                cursor4.execute("DROP TABLE FERRAMENTARIA")
                conn4.commit()
            image = Image.open('./Midia/ssmm.jpg')
            col7,col8 = st.columns([1,1])
            with col7:
                st.title('Status e informações de OS')
           
            tab21, tab22,tab23,tab24,tab25= st.tabs(["Cadastro", "Finalizar","OS Em aberto","OS Finalizadas","Geral"])
            with tab21:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd4 = st.toggle('Atualizar os dados')
                    with st.form('my form3'):
                        st.markdown("---")
                        Ms = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        if atd4:
                            MUs = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Mst = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd4:
                            MUst = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Mstr = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd4:
                            MUstr = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Mndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd4:
                            MUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Mac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd4:
                            MUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd4:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

                        Mtemp = st.time_input('Horario', value=None)
                        if atd4:
                            MUtempoi = st.time_input('Atualize o Horario', value=None)
                            st.write(Mtemp)

                        Mdata = st.date_input("Data", value=None)
                        if atd4:
                            MUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with neymar:
                    if atd4:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln14,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln14)
                        numros13 = numros12-1
                        osespec3 = allinhas1.loc[numros13]
                        def load_dataa():
                            return pd.DataFrame(osespec3)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        conn4.close()


                if fLIDERES == 'FERRAMENTARIA':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1407':
                            if Mndo != "Selecione":
                                if Ms != "Selecione":
                                    if Mstr != "Selecione":
                                            if atd4: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl3 = st.button('atualize')
                                                if atl3:
                                                   st.balloons()
                                                   cursor4.execute("UPDATE FERRAMENTARIA SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(MUs, MUstr, MUst,MUndo,MUdata,str(MUtempoi),MUac,numros12))
                                                   conn4.commit()
                                                   conn4.close()
                                                
                                            else:
                                                insdds3 = st.button("INSERIR DADOS")

                                                if insdds3:
                                                   allln12 = allln14 + 1
                                                if insdds3:
                                                   st.balloons()
                                                   cursor4.execute("INSERT INTO FERRAMENTARIA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(Ms), str(Mstr), str(Mst),str(Mndo),Mdata,str(Mtemp),Mac,'Não',None,None))
                                                   conn4.commit()
                                                   conn4.close()
                                                    
            with tab22:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    fnlz8 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=allln14,value=0,placeholder="Selecione")
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        fnlz9 = fnlz8-1
                        datainput5 = st.date_input("Data", value=None)
                        st.write(datainput5)
                        st.markdown("---")
                        timeinput6 = st.time_input('HORA', value=None)
                        st.write(timeinput6)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'FERRAMENTARIA':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1407':                                                                                                                     
                            fnl2=st.button("FINALIZAR")
                            if fnl2:
                                cursor4.execute("UPDATE FERRAMENTARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput5,str(timeinput6),fnlz8))
                                conn4.commit()
                                conn4.close()
                                st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente com uma flor.')
                                
                            
            with tab23:
                st.metric(label="OS em aberto", value= whrlinhas14)
                whrlinhas13 = pd.DataFrame(whlinhas12)
                st.dataframe(whrlinhas13)
                st.write(whrlinhas14)
                

            with tab24:
                st.metric(label="OS Finalizadas",value=whrlinhas17)
                whrlinhas16 = pd.DataFrame(whrlinhas15)
                st.dataframe(whrlinhas16)
                st.write(whrlinhas17)

            with tab25:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                    numros14 = st.number_input("Selecione o numero da OS",min_value=1,max_value=allln14,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln14)
                    numros15 = numros14-1
                    osespec3 = allinhas1.loc[numros15]
                    def load_data():
                        return pd.DataFrame(osespec3)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)



conn4
cursor4
allln12
allln13
allln14
cl4
col7
col8
tab21
tab22
tab23
tab24
tab25
atd4
Ms
MUs
Mst
MUst
Mstr
MUstr
Mndo
MUndo
Mac
MUac
Mtemp
MUtempoi
Mdata
MUdata
numros12
numros13
numros14
numros15
osespec3
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