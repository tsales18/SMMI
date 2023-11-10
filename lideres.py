import pandas as pd
import streamlit as st
from PIL import Image
import time as time
import datetime as datetime
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, event
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, MetTdata, Column, Integer, String, FLOAT, VARCHAR, Date, Time
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
    
    with st.spinner("CarregTndo..."):
                time.sleep(2)
                st.success("Pronto!")
    st.write("Bem Vindo")
    
    st.write('✅')
    tab1_qtde_produto = df.loc[(
    df['SETOR'] == fSETOR) &
    (df['LIDERES'] == fLIDERES)]

conn11 = sqlite3.connect('TI')
cursor11 = conn11.cursor()
cursor11.execute('''
    CREATE TABLE IF NOT EXISTS TI (
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
        HORAF,
        MANUTENTOR
   
    )
''')

#MANUTENÇÃO 
query = "SELECT * FROM TI WHERE FINALIZADA = 'Não'"
rd70 = pd.read_sql_query(query, conn11)
rd71 = rd70.shape[0]

query1 = "SELECT * FROM TI WHERE FINALIZADA = 'Sim'"
rd72 = pd.read_sql_query(query1, conn11)
rd73 = rd72.shape[0]

allln25 = pd.read_sql_query("SELECT * FROM TI", conn11)
allln26 = allln25.shape[0]


allln25 = pd.read_sql_query("SELECT * FROM TI", conn11)
allln26 = allln25.shape[0]
consulta2 = "SELECT * FROM TI"
allinhas21 = pd.read_sql_query(consulta2, conn11)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM TI WHERE FINALIZADA = 'Não'"
whrlinhas43 = pd.read_sql_query(consulta3, conn11)
whrlinhas44 = whrlinhas43.shape[0]

#OS FINALIZADAS
cursor11.execute("SELECT * FROM TI WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas45 = cursor11.fetchall()
whrlinhas46 = pd.DataFrame(whrlinhas45)
whrlinhas47 = whrlinhas46.shape[0]

if fLIDERES == 'FILIPE LEITE':
    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            cl11 = st.button("DELETAR TABELA")
            if cl11:
                cursor11.execute("DROP TABLE TI")
                conn11.commit()
            with ps6:
                st.title('Status e informações de OS')

            st.markdown("---")
            tab50,tab51,tab52,tab53= st.tabs(["Cadastro","OS Abertas","OS Finalizadas","Geral"])
            with tab50:
                st.header('Cadastro de ocorrências', divider='rainbow')
                col21,col22= st.columns(2)  
                with col21:                  
                    atd10 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Tc = st.selectbox('Solicitante', ('FILIPE LEITE',),index=None,placeholder='Selecione')

                        Tstr = st.selectbox('Setor', ('TI',),index=None,placeholder='Selecione')
                       
                        Tst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd10:
                            Tust = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Tndo = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd10:
                            TUndo = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        Tac = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd10:
                            TUac = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")
                        
                        Tmnt = st.selectbox('Eletrica ou Mecânica', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                        if atd10:
                            Tmnt = st.selectbox('Eletrica ou Mecânica', ('ELÉTRICA','MECÂNICA'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd10:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

                        Ttemp = st.time_input('Horario', value=None)
                        if atd10:
                            TUtemp = st.time_input('Atualize o Horario', value=None)
                            st.write(Ttemp)

                        Tdata = st.date_input("Data", value=None)
                        if atd10:
                            TUdata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a EcV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with col22:
                    if atd10:
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln26,value=allln26,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln26)
                        numros29 = numros12-1
                        if allln26 == 0:
                            st.success('Não há pendências')
                        else:    
                            osespec28 = allinhas21.loc[numros29]
                            def load_dataa():
                                return pd.DataFrame(osespec28)
                            st.checkbox("Estender", value=True, key="use_container_width")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'FILIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if atd10: 
                                atl1 = st.button('atualize')
                                if atl1:
                                    st.balloons()
                                    cursor11.execute("UPDATE TI SET OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(Tust,TUndo,TUdata,str(TUtemp),TUac,numros12))
                                    conn11.commit()
                                    conn11.close()
                                                                    
                            else:
                                insdds = st.button("INSERIR DADOS")
                                if insdds:
                                    allln12 = allln26 + 1
                                if insdds:
                                    st.balloons()
                                    cursor11.execute("INSERT INTO TI (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)", (allln12 , str(Tc), str(Tstr), str(Tst),str(Tndo),Tdata,str(Ttemp),Tac,'Não',None,None,Tmnt))
                                    conn11.commit()
                                    conn11.close()
                                        
            with tab51:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('TI', divider='rainbow')
                    with st.expander("Abertas"):
                        numros28 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas44,value=whrlinhas44,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas44)
                        numros29 = numros28-1
                        if whrlinhas44 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec29 = whrlinhas43.loc[numros29]
                            def load_data():
                                return pd.DataFrame(osespec29)
                            st.checkbox("Estender", value=True, key="use_container_width1")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width1)

            with tab52:
                st.header('TI', divider='rainbow')
                with st.expander("Finalizadas"):
                    numros28 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd73,value=rd73,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd73)
                    numros29 = numros28-1
                    if rd73 == 0:
                        st.success('Não há pendências')
                        
                    else:
                        osespec30 = rd72.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec30)
                        st.checkbox("Estender", value=True, key="use_container_width2")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width2)
            
            with tab53:
                st.header('TI', divider='rainbow')
                with st.expander("Geral"):
                    numros28 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln26,value=allln26,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln26)
                    numros29 = numros28-1
                    if allln26 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec31 = allln25.loc[numros29]
                        def load_data():
                            return pd.DataFrame(osespec31)
                        st.checkbox("Estender", value=True, key= "use_container_width3")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width3)















rd72
rd73
rd70
rd71
conn11
cursor11
allln25
allln26
allinhas21
whrlinhas43
whrlinhas44
whrlinhas45
whrlinhas46
whrlinhas47
cl11
col21
col22
tab50
tab51
tab52
tab53
atd10
Tc
Tst
Tust
Tstr
Tndo
TUndo
Tac
TUac
Ttemp
TUtemp
Tdata
TUdata
numros28
numros29
osespec28
osespec29
osespec30
osespec31
Inserts4
'FILIPE LEITE'
'TECNOLOGIA DA INFORMAÇÃO'
'69'
'FILIPE LEITE'







