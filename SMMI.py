import pandas as pd
import streamlit as st
import altair as alt
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
    nrows=8
    
)

conn.commit()
# -- Criar o sidebar
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
    (df['LIDERES'] == fLIDERES)
    
]

conn = st.connection('SMMI', type='sql')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ABERTURA (
        OS INTEGER PRIMARY KEY,
        SOLCITANTE TEXT,
        SETOR TEXT,
        TIPO_DE_OCORRENCIA TEXT,
        NIVEL_DA_OCORRENCIA TEXT,
        DATA DATE,
        HORA TIME
        
    )
''')
      
if fLIDERES == 'FELIPE LEITE':
    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps1,ps2,ps3,ps4,ps5 = st.columns(5)
            with ps1:
                st.image(image,width=1700)
                st.title('Status e informações de OS')
           
            
            tab1, tab2, tab3= st.tabs(["Cadastro", "Finalizar","OS Abertas"])
            with tab1:
                st.header("Cadastro de ocorrência")
                colibrim,neymar,lula,sales,poura= st.columns([0.5,0.1,0.1,0.1,0.1])  
                with colibrim:
                    with st.form('my form2'):
                        st.markdown("---")
                        solicitante = st.selectbox('Solicitante', ('Selecione','FILIPE',),index=0)
                        status = st.selectbox('Tipo de Ocorrência', ('Selecione','ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES'),index=0,)   
                        st.markdown("---")
                        setor = st.selectbox('Setor', ('Selecione','TECNOLOGIA DA INFORMAÇÃO',), index=0)
                        niveldaocorrencia = st.selectbox('Nivel da ocorrência', ('Selecione','EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE', 'URGÊNTE'), index=0)
                        st.markdown("---")
                        relatorio = st.text_input('Relatorio')
                        tempoi = st.time_input('HORA DE INICIO', value=None)
                        st.write(tempoi)
                        st.form_submit_button('↻')
                            
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if niveldaocorrencia != "Selecione":
                                if solicitante != "Selecione":
                                    if setor != "Selecione":
                                        if num > num1:
                                            st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                        else:
                                            att = st.button("INSERIR DADOS")
                                            if att:
                                                cursor.execute("INSERT INTO ABERTURA (OS,SOLCITANTE,SETOR,TIPO_DE_OCORRENCIA,NIVEL_DA_OCORRENCIA,DATA,HORA) VALUES (?, ?, ?, ?, ?, ?, ?)", (OSF, SOLICITANTEF, SETORF, TIPO_DE_OCORRENCIAF,NIVEL_DE_OCORRENCIAF,DATAF,HORAF))
                                                conn.commit()
                                            if att:
                                                st.balloons()
                                                st.session_state.OS += 1
                                                st.experimental_rerun()
                        
            with tab2:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    with st.form('my form'):
                        df3 = st.date_input("Data", value=None)
                        st.write(df3)
                        st.markdown("---")
                        t = st.time_input('HORA', value=None)
                        st.write(t)
                        st.form_submit_button('↻')
                                  
                  
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if num <= num1:
                                st.caption('É necessario ABRIR outra OS para finalizar.') 
                                st.write(num)
                                st.write(num1)
                            else:
                                st.caption('É necessario finalizar esta OS antes de inciar outra.')                                                                                                                         
                                FIn=st.button("FINALIZAR")
                                if FIn:
                                    ins2 = DADOS1.insert()
                                    conn.execute(ins2,DATA =df3, HORA_FINAL=t)
                                if FIn:
                                    st.session_state.FIN += 1
                                    st.balloons()
                                   
                                   
                                       
                                
            with tab3:
                statuses,sats,statuses1=st.columns([55,8,20])
                with statuses:
                    df1 = pd.DataFrame(DATA)
                    st.table(df1)
                with sats:
                    df2 = pd.DataFrame(DATA1)
                    st.dataframe((df2))               
                with statuses1:
                    df6= pd.DataFrame(DATA2)
                    st.dataframe(df6)
                    
                    


                                                                          
if senha != '69':
    video_file = open('./Midia/SSMMOV.mp4', 'rb')
    video_bytes = video_file.read() 
    st.video(video_bytes)
    
if fLIDERES == 'IVSON PAULINO':
    if fSETOR == 'FERRAMENTARIA':
        if senha == '70':
            image = Image.open('./Midia/ssmm.jpg')
            ps6,ps7= st.columns(2)
            with ps6:
                st.image(image,width=1700)
                st.title('Status e informações de OS')

            st.markdown("---")
            tab4,tab5= st.tabs(["Cadastro","OS Abertas"])
            with tab4:
                st.header("Cadastro de ocorrência")
                col1,col2= st.columns(2)  
                with col1:
                    with st.form('my form2'):
                        st.markdown("---")
                        solicitanteF = st.selectbox('Solicitante', ('Selecione','FILIPE',),index=0)
                        statusF = st.selectbox('Tipo de Ocorrência', ('Selecione','ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES'),index=0,)   
                        st.markdown("---")
                        setorF = st.selectbox('Setor', ('Selecione','TECNOLOGIA DA INFORMAÇÃO',), index=0)
                        niveldaocorrenciaF = st.selectbox('Nivel da ocorrência', ('Selecione','EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE', 'URGÊNTE'), index=0)
                        st.markdown("---")
                        relatorioF = st.text_input('Relatorio')
                        tempoiF = st.time_input('HORA DE INICIO', value=None)
                        st.write(tempoiF)
                        st.markdown("---")
                        data = st.date_input("Data", value=None)
                        st.form_submit_button('↻')
                        
                
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'IVSON PAULINO':
                    if fSETOR == 'FERRAMENTARIA':
                        if senha == '70':
                            if niveldaocorrenciaF != "Selecione":
                                if solicitanteF != "Selecione":
                                    if setorF != "Selecione":
                                        attt = st.button("INSERIR DADOS")
                                        if attt:
                                            ABR1 =(
                                                   insert(ABERTURAF).
                                                   values(SOLICITANTE=solicitanteF, SETOR=setorF,
                                                           TIPO_DE_OCORRENCIA=statusF, NIVEL_DA_OCÔRRENCIA=niveldaocorrenciaF,
                                                           DATA=data,MOMENTO=tempoiF) 
                                                   ) 
                                            with engine.connect() as conn:
                                                  conn.execute(ABR1)
                                        if attt:
                                            st.session_state.OS += 1
                                          
            with tab5:
                statuses,sats,statuses1=st.columns([80,8,20])
                with statuses:
                    st.dataframe(tempoi)
    
                with statuses1:
                    st.dataframe(tempoiF)
                               
                                    
                                 
                                    
                       






                                   
                              

    


            
                                        
               
                


                

                            
            
            

                 
                 
                 

    





                
