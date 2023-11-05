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

conn = sqlite3.connect('SMMI')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ABERTURA (
        OS INTEGER PRIMARY KEY,
        SOLICITANTE TEXT,
        SETOR TEXT,
        OCORRENCIA TEXT,
        GRAU TEXT,
        DATA DATE,
        HORA TIME,
        AÇÃO TEXT,
        FINALIZADA TEXT,
        DATAF DATE,
        HORAF TIME
                 
    )
''')

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



#leitura do banco smmi
cnt = pd.read_sql_query("SELECT * FROM ABERTURA", conn)
cnt1 = cnt.shape[0]
consulta = "SELECT * FROM ABERTURA"
ln = pd.read_sql_query(consulta, conn)

#OS ABERTAS  NÃO FINALIZADAS 
cursor.execute("SELECT * FROM ABERTURA WHERE FINALIZADA = ?;", ('Não',))
filas = cursor.fetchall()
fl = pd.DataFrame(filas)
fl1 = fl.shape[0] 

#OS FINALIZADAS
cursor.execute("SELECT * FROM ABERTURA WHERE FINALIZADA = ?;", ('Sim',))
filas1 = cursor.fetchall()
fl2 = pd.DataFrame(filas1)
fl3 = fl2.shape[0]


cl = st.button("DELETAR TABELAS")
if cl:
   cursor.execute("DROP TABLE ABERTURA")
   conn.commit()

if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'FELIPE LEITE':
    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
        if senha == '69':
            image = Image.open('./Midia/ssmm.jpg')
            ps1,ps2 = st.columns([1,1])
            with ps1:
                st.title('Status e informações de OS')
           
            tab1, tab2, tab3,tab4,tab5= st.tabs(["Cadastro", "Finalizar","OS Em aberto","OS Finalizadas","Geral"])
            with tab1:
                st.header("Cadastro de ocorrência")
                colibrim,neymar= st.columns([2,3])  
                with colibrim:
                    atd = st.toggle('Atualizar os dados')
                    with st.form('my form2'):
                        st.markdown("---")
                        solicitante = st.selectbox('Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Selecione')
                        if atd:
                            Usolicitante = st.selectbox('Atualize o Solicitante', ('FILIPE','JAMESON','MAURILIO SALES','BRUNO KAPPAUN','EDUARDO BICUDO','ADRIELY LEMOS','GILSON FREITAS','ALEX SANTOS','CESAR AUGUSTO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        status = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd:
                            Ustatus = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        setor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd:
                            Usetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','ELETRICA'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        niveldaocorrencia = st.selectbox('Nivel da ocorrência', ('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None,placeholder='Selecione')
                        if atd:
                            Univeldaocorrencia = st.selectbox('Atualize o Nivel da ocorrência',('EMERGÊNCIA','MUITO URGÊNTE','POUCO URGÊNTE','URGÊNTE'),index=None, placeholder='Atualize')
                            st.markdown("---")
                        acao = st.selectbox('Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                        if atd:
                            Uacao = st.selectbox('Atualize o Tipo da ação', ('Corretiva','Preventiva','Preditiva'),index=None,placeholder='Selecione')
                            st.markdown("---")

                        relatorio = st.text_input('Relatorio')
                        if atd:
                            Urelatorio = st.text_input('Atualize o Relatorio')
                            st.markdown("---")

                        tempoi = st.time_input('Horario', value=None)
                        if atd:
                            Utempoi = st.time_input('Atualize o Horario', value=None)
                            st.write(tempoi)

                        data = st.date_input("Data", value=None)
                        if atd:
                            Udata = st.date_input("Atualize a Data", value=None)
                        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                        st.form_submit_button('↻')

                with neymar:
                    if atd:
                        sos = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=cnt1,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= cnt1)
                        sos1 = sos-1
                        ln1 = ln.loc[sos1]
                        def load_dataa():
                            return pd.DataFrame(ln1)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        


                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':
                            if niveldaocorrencia != "Selecione":
                                if solicitante != "Selecione":
                                    if setor != "Selecione":
                                            if atd: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl = st.button('atualize')
                                                if atl:
                                                   st.balloons()
                                                   cursor.execute("UPDATE ABERTURA SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(Usolicitante, Usetor, Ustatus,Univeldaocorrencia,Udata,str(Utempoi),Uacao,sos))
                                                   conn.commit()
                                                   conn.close()
                                                
                                            else:
                                                att = st.button("INSERIR DADOS")

                                                if att:
                                                   cnt3 = cnt1 + 1
                                                if att:
                                                   st.balloons()
                                                   cursor.execute("INSERT INTO ABERTURA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (cnt3 , str(solicitante), str(setor), str(status),str(niveldaocorrencia),data,str(tempoi),acao,'Não',None,None))
                                                   conn.commit()
                                                   conn.close()
                                               
                     
            with tab2:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    fnlz = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=1,max_value=cnt1,value=1,placeholder="Selecione")
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        fnlz1 = fnlz-1
                        dateinput1 = st.date_input("Data", value=None)
                        st.write(dateinput1)
                        st.markdown("---")
                        timeinput1 = st.time_input('HORA', value=None)
                        st.write(timeinput1)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'FELIPE LEITE':
                    if fSETOR == 'TECNOLOGIA DA INFORMAÇÃO':
                        if senha == '69':                                                                                                                     
                            FIn=st.button("FINALIZAR")
                            if FIn:
                                cursor.execute("UPDATE ABERTURA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,dateinput1,str(timeinput1),fnlz))
                                conn.commit()
                                conn.close()
                                st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente com uma flor.')
                                
                            
            with tab3:
                st.metric(label="OS em aberto", value= fl1)
                fl = pd.DataFrame(filas)
                st.dataframe(fl)
                st.write(fl1)
                

            with tab4:
                st.metric(label="OS Finalizadas", value= fl3)
                fl2 = pd.DataFrame(filas1)
                st.dataframe(fl2)
                st.write(fl3)

            with tab5:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                    numros2 = st.number_input("Selecione o numero da OS",min_value=1,max_value=cnt1,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= cnt1)
                    numros3 = numros2-1
                    ln1 = ln.loc[numros3]
                    def load_data():
                        return pd.DataFrame(ln1)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)
                    conn.close()
                                                            
if senha != '69':

    video_file = open('./Midia/SSMMOV.mp4', 'rb')
    video_bytes = video_file.read() 
    st.video(video_bytes)



conn1 = sqlite3.connect('ROSIVALDO')
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
        FINALIZADA TEXT,
        DATAF,
        HORAF
       
                   
    )
''')


#leitura do banco rosivaldo
allln = pd.read_sql_query("SELECT * FROM ROSIVALDO", conn1)
allln1 = allln.shape[0]
consulta1 = "SELECT * FROM ROSIVALDO"
allinhas = pd.read_sql_query(consulta1, conn1)

#OS ABERTAS  NÃO FINALIZADAS
consulta4 = "SELECT * FROM ROSIVALDO WHERE FINALIZADA = 'Não'"
whrlinhas1 = pd.read_sql_query(consulta4, conn1)
whrlinhas2 = whrlinhas1.shape[0] 

#OS FINALIZADAS
consulta5 = "SELECT * FROM ROSIVALDO WHERE FINALIZADA = 'Sim'"
whrlinhas3 = pd.read_sql_query(consulta5, conn1)
whrlinhas4 = whrlinhas3.shape[0]

#feedback ferramentaria
query = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Não'"
rd2 = pd.read_sql_query(query, conn4)
rd3 = rd2.shape[0]

query1 = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Sim'"
rd = pd.read_sql_query(query1, conn4)
rd1 = rd.shape[0]

allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
allln14 = allln13.shape[0]



if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'ROSIVALDO':
    if fSETOR == 'ELÉTRICA':
        if senha == '1409':
            cl1 = st.button("DELETAR TABELA")
            if cl1:
                cursor1.execute("DROP TABLE ROSIVALDO")
                conn1.commit()
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

                        Rstatus = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd1:
                            RUstatus = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Rsetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd1:
                            RUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Atualize')
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
                      


                if fLIDERES == 'ROSIVALDO':
                    if fSETOR == 'ELÉTRICA':
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
                                                insdds = st.button("INSERIR DADOS")

                                                if insdds:
                                                    allln3 = allln1 + 1
                                                if insdds:
                                                    st.balloons()
                                                    cursor1.execute("INSERT INTO ROSIVALDO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln3 , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),Rdata,str(Rtempoi),Racao,'Não',None,None))
                                                    conn1.commit()
                                                    conn1.close()
                           
            with tab7:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    setorescolhido = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','ELÉTRICA'),index=None,placeholder='Selecione')
                    fnlz2 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=allln1,value=0,placeholder="Selecione")
                    fnlz3 = fnlz2-1
                    st.write(fnlz2)
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        datainput = st.date_input("Data", value=None)
                        st.write(datainput)
                        st.markdown("---")
                        timeinput = st.time_input('HORA', value=None)
                        st.write(timeinput)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'ROSIVALDO':
                    if fSETOR == 'ELÉTRICA':
                        if senha == '1409':
                            if setorescolhido == 'FERRAMENTARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor4.execute("UPDATE FERRAMENTARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn4.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')
                            if setorescolhido == 'ELÉTRICA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor1.execute("UPDATE ROSIVALDO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn1.commit()
                                    conn1.close()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')    

                          
                            
                                
                            
            with tab8:
                with st.expander("Minhas OS"):
                    numros2 = st.number_input("Selecione o numero da OS",min_value=whrlinhas2,max_value=whrlinhas2,value=whrlinhas2,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= whrlinhas2)
                    numros3 = numros2-1
                    if whrlinhas2 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = whrlinhas1.loc[numros3]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

                st.markdown('--------')
                with st.expander("Ferramentaria"):
                    numros4 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=rd3,value=rd3,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd3)
                    numros5 = numros4-1
                    if rd3 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd2.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)
                
            with tab9:
                with st.expander("Minhas OS"):
                    numros6 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas4,value=whrlinhas4,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= whrlinhas4)
                    numros7 = numros6-1
                    if whrlinhas4 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = whrlinhas3.loc[numros7]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
                st.markdown('--------')
                with st.expander("Ferramentaria"):
                    numros8 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=rd1,value=rd1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd1)
                    numros9 = numros8-1
                    if rd1 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd.loc[numros9]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_contaainer_widtth")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                
            with tab10:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:
                    with st.expander("See explanation"):
                        numros10 = st.number_input("Selecione o numero da OS",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros11 = numros10-1
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros11]
                            def load_data():
                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="usee_container_width")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

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


#leitura do banco ivanildo
allln4 = pd.read_sql_query("SELECT * FROM IVANILDO", conn2)
allln5 = allln4.shape[0]
consulta2 = "SELECT * FROM IVANILDO"
allinhas1 = pd.read_sql_query(consulta2, conn2)

#OS ABERTAS  NÃO FINALIZADAS 
cursor2.execute("SELECT * FROM IVANILDO WHERE FINALIZADA = ?;", ('Não',))
whlinhas6 = cursor2.fetchall()
whrlinhas7 = pd.DataFrame(whlinhas6)
whrlinhas8 = whrlinhas7.shape[0]  

#OS FINALIZADAS
cursor2.execute("SELECT * FROM IVANILDO WHERE FINALIZADA = ?;", ('Sim',))
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
                cursor2.execute("DROP TABLE IVANILDO")
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

                        Istatus = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd2:
                            st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
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
                                                   cursor2.execute("UPDATE IVANILDO SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(IUsolicitante, IUsetor, IUstatus,IUniveldaocorrencia,IUdata,str(IUtempoi),IUacao,numros4))
                                                   conn2.commit()
                                                   conn2.close()
                                                
                                            else:
                                                insdds1 = st.button("INSERIR DADOS")

                                                if insdds1:
                                                   allln3 = allln5 + 1
                                                if insdds1:
                                                   st.balloons()
                                                   cursor2.execute("INSERT INTO IVANILDO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln3 , str(Isolicitante), str(Isetor), str(Istatus),str(Iniveldaocorrencia),Idata,str(Itempoi),Iacao,'Não',None,None))
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
                                cursor2.execute("UPDATE IVANILDO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput2,str(timeinput2),fnlz4))
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

conn2 = sqlite3.connect('CESAR')
cursor2 = conn2.cursor()
cursor2.execute('''
    CREATE TABLE IF NOT EXISTS CESAR (
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
allln7 = pd.read_sql_query("SELECT * FROM CESAR", conn2)
allln8 = allln7.shape[0]
consulta2 = "SELECT * FROM CESAR FILHO"
allinhas1 = pd.read_sql_query(consulta2, conn2)

#OS ABERTAS  NÃO FINALIZADAS 
cursor2.execute("SELECT * FROM CESAR WHERE FINALIZADA = ?;", ('Não',))
whlinhas6 = cursor2.fetchall()
whrlinhas7 = pd.DataFrame(whlinhas6)
whrlinhas8 = whrlinhas7.shape[0]  

#OS FINALIZADAS
cursor2.execute("SELECT * FROM CESAR WHERE FINALIZADA = ?;", ('Sim',))
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
                cursor2.execute("DROP TABLE CESAR")
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

                        Cstatus = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd3:
                            CUstatus = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Csetor = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd3:
                            CUsetor = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Atualize')
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
                                                   cursor2.execute("UPDATE CESAR SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(CUsolicitante, CUsetor, CUstatus,CUniveldaocorrencia,CUdata,str(CUtempoi),CUacao,numros8))
                                                   conn2.commit()
                                                   conn2.close()
                                                
                                            else:
                                                insdds2 = st.button("INSERIR DADOS")

                                                if insdds2:
                                                    allln6 = allln8 + 1
                                                if insdds2:
                                                    st.balloons()
                                                    cursor2.execute("INSERT INTO CESAR (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln6 , str(Csolicitante), str(Csetor), str(Cstatus),str(Cniveldaocorrencia),Cdata,str(Ctempoi),Cacao,'Não',None,None))
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
                                cursor2.execute("UPDATE CESAR SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput3,str(timeinput4),fnlz6))
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

conn3 = sqlite3.connect('MARCIO')
cursor3 = conn3.cursor()
cursor3.execute('''
    CREATE TABLE IF NOT EXISTS MARCIO (
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



#leitura do banco MARCIO
allln10 = pd.read_sql_query("SELECT * FROM MARCIO", conn3)
allln11 = allln10.shape[0]
consulta2 = "SELECT * FROM MARCIO"
allinhas1 = pd.read_sql_query(consulta2, conn3)

#OS ABERTAS  NÃO FINALIZADAS 
cursor3.execute("SELECT * FROM MARCIO WHERE FINALIZADA = ?;", ('Não',))
whlinhas6 = cursor3.fetchall()
whrlinhas7 = pd.DataFrame(whlinhas6)
whrlinhas8 = whrlinhas7.shape[0]  

#OS FINALIZADAS
cursor3.execute("SELECT * FROM MARCIO WHERE FINALIZADA = ?;", ('Sim',))
whrlinhas9 = cursor3.fetchall()
whrlinhas10 = pd.DataFrame(whrlinhas9)
whrlinhas11 = whrlinhas10.shape[0]



if 'OS' not in st.session_state:
    st.session_state.OS = 0
        
if 'FIN' not in st.session_state:
    st.session_state.FIN = 0

if fLIDERES == 'MARCIO FABIO':
    if fSETOR == 'MECÂNICA':
        if senha == '1406':
            cl4 = st.button("DELETAR TABELA")
            if cl4:
                cursor3.execute("DROP TABLE MARCIO")
                conn3.commit()
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

                        Mst = st.text_input('Tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                        if atd4:
                            MUst = st.text_input('Atualize o tipo de Ocorrência',value=None,placeholder='Insira sua ocôrrencia')
                            st.markdown("---")

                        Mstr = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Selecione')
                        if atd4:
                            MUstr = st.selectbox('Aualize o Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA'),index=None,placeholder='Atualize')
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
                        numros12 = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=1,max_value=allln11,value=1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln11)
                        numros13 = numros12-1
                        osespec3 = allinhas1.loc[numros13]
                        def load_dataa():
                            return pd.DataFrame(osespec3)
                        st.checkbox("Estender", value=True, key="use_container_widthh")
                        df = load_dataa()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)
                        conn3.close()


                if fLIDERES == 'MARCIO FABIO':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1406':
                            if Mndo != "Selecione":
                                if Ms != "Selecione":
                                    if Mstr != "Selecione":
                                            if atd4: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl3 = st.button('atualize')
                                                if atl3:
                                                   st.balloons()
                                                   cursor3.execute("UPDATE MARCIO SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(MUs, MUstr, MUst,MUndo,MUdata,str(MUtempoi),MUac,numros12))
                                                   conn3.commit()
                                                   conn3.close()
                                                
                                            else:
                                                insdds3 = st.button("INSERIR DADOS")

                                                if insdds3:
                                                   allln9 = allln11 + 1
                                                if insdds3:
                                                   st.balloons()
                                                   cursor3.execute("INSERT INTO MARCIO (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln9 , str(Ms), str(Mstr), str(Mst),str(Mndo),Mdata,str(Mtemp),Mac,'Não',None,None))
                                                   conn3.commit()
                                                   conn3.close()
                                                    
            with tab22:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    fnlz8 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=allln11,value=0,placeholder="Selecione")
                    with st.form('my form'):
                        finalizar = st.selectbox('OS finalizada?', ('Sim','Não'),index=None,placeholder='Selecione')
                        fnlz9 = fnlz8-1
                        datainput5 = st.date_input("Data", value=None)
                        st.write(datainput5)
                        st.markdown("---")
                        timeinput6 = st.time_input('HORA', value=None)
                        st.write(timeinput6)
                        st.form_submit_button('↻')

                                  
                if fLIDERES == 'MARCIO FABIO':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1406':                                                                                                                     
                            fnl2=st.button("FINALIZAR")
                            if fnl2:
                                cursor3.execute("UPDATE MARCIO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput5,str(timeinput6),fnlz8))
                                conn3.commit()
                                conn3.close()
                                st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente com uma flor.')
                                
                            
            with tab23:
                st.metric(label="OS em aberto", value= whrlinhas8)
                whrlinhas7 = pd.DataFrame(whlinhas6)
                st.dataframe(whrlinhas7)
                st.write(whrlinhas8)
                

            with tab24:
                st.metric(label="OS Finalizadas",value=whrlinhas11)
                whrlinhas10 = pd.DataFrame(whrlinhas9)
                st.dataframe(whrlinhas10)
                st.write(whrlinhas11)

            with tab25:
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:   
                    numros14 = st.number_input("Selecione o numero da OS",min_value=1,max_value=allln11,value=1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln11)
                    numros15 = numros14-1
                    osespec3 = allinhas1.loc[numros15]
                    def load_data():
                        return pd.DataFrame(osespec3)
                    st.checkbox("Estender", value=True, key="use_container_width")
                    df = load_data()
                    st.dataframe(df, use_container_width=st.session_state.use_container_width)


allln13 = pd.read_sql_query("SELECT * FROM FERRAMENTARIA", conn4)
allln14 = allln13.shape[0]
consulta2 = "SELECT * FROM FERRAMENTARIA"
allinhas15 = pd.read_sql_query(consulta2, conn4)

#OS ABERTAS  NÃO FINALIZADAS
consulta3 = "SELECT * FROM FERRAMENTARIA WHERE FINALIZADA = 'Não'"
whrlinhas12 = pd.read_sql_query(consulta3, conn4)
whrlinhas13 = whrlinhas12.shape[0]

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
                st.header('Cadastro de ocorrências', divider='rainbow')
                col9,col10= st.columns(2)  
                with col9:                  
                    atd4 = st.toggle('Atualizar os dados')
                    with st.form('my form4'):
                        st.markdown("---")
                        Fs = st.selectbox('Solicitante', ('IVSON PAULINO',),index=None,placeholder='Selecione')
                        if atd4:
                            FUs = st.selectbox('Atualize o Solicitante', ('IVSON PAULINO'),index=None,placeholder='Atualize')
                            st.markdown("---")

                        Fst = st.selectbox('Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Selecione')
                        if atd4:
                            FUst = st.selectbox('Atualize o Tipo de Ocorrência', ('ELETRICA PREDIAL MANUTENÇÃO EM PAINES TROCA DE COMPONENTES',),index=None, placeholder='Atualize')
                            st.markdown("---")

                        Fstr = st.selectbox('Setor', ('FERRAMENTARIA',),index=None,placeholder='Selecione')
                        if atd4:
                            Fustr = st.selectbox('Aualize o Setor', ('FERRAMENTARIA'),index=None,placeholder='Atualize')
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
                
                        
                if 'OS' not in st.session_state:
                    st.session_state.OS = 0
                    
                if 'FIN' not in st.session_state:
                    st.session_state.FIN = 0
                        
                if fLIDERES == 'IVSON PAULINO':
                    if fSETOR == 'FERRAMENTARIA':
                        if senha == '70':
                            attt = st.button("INSERIR DADOS")
                            if attt:
                                allln12 = allln14 + 1

                            if attt:
                                st.balloons()
                                cursor4.execute("INSERT INTO FERRAMENTARIA (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln12 , str(Fs), str(Fstr), str(Fst),str(Fndo),Fdata,str(Ftemp),Fac,'Não',None,None))
                                conn4.commit()
                                conn4.close()
                                        
            with tab27:
                statuses,sats,statuses1=st.columns([80,0.1,0.1])
                with statuses:
                    st.header('Ferramentaria', divider='rainbow')
                    with st.expander("Abertas"):
                        numros22 = st.number_input("Selecione o numero da  OS",min_value=0,max_value=whrlinhas13,value=0,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= whrlinhas13)
                        numros23 = numros22-1
                        if whrlinhas13 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec5 = whrlinhas12.loc[numros23]
                            def load_data():
                                return pd.DataFrame(osespec5)
                            st.checkbox("Estender", value=True, key="usee_containner_widthh")
                            df = load_data()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab28:
                st.header('Ferramentaria', divider='rainbow')
                with st.expander("Finalizadas"):
                    numros16 = st.number_input("Selecione o numero da   OS",min_value=0,max_value=rd1,value=rd1,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= rd1)
                    numros17 = numros16-1
                    if rd1 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec6 = rd.loc[numros17]
                        def load_data():
                            return pd.DataFrame(osespec6)
                        st.checkbox("Estender", value=True, key="use_container_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)

            with tab29:
                st.header('Ferramentaria', divider='rainbow')
                with st.expander("Geral"):
                    numros20 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln14,value=allln14,placeholder="Selecione")
                    st.metric(label="OS Existentes", value= allln14)
                    numros21 = numros20-1
                    if allln14 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec7 = allln13.loc[numros21]
                        def load_data():
                            return pd.DataFrame(osespec7)
                        st.checkbox("Estender", value=True, key= "uuse_containner_width")
                        df = load_data()
                        st.dataframe(df, use_container_width=st.session_state.use_container_width)






