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


conn10 = sqlite3.connect('CESAR')
cursor10 = conn10.cursor()
cursor10.execute('''
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


#leitura do banco CESAR
allln = pd.read_sql_query("SELECT * FROM CESAR", conn10)
allln1 = allln.shape[0]
consulta1 = "SELECT * FROM CESAR"
allinhas = pd.read_sql_query(consulta1, conn10)

#OS ABERTAS  NÃO FINALIZADAS
consulta4 = "SELECT * FROM CESAR WHERE FINALIZADA = 'Não'"
whrlinhas1 = pd.read_sql_query(consulta4, conn10)
whrlinhas2 = whrlinhas1.shape[0] 

#OS FINALIZADAS
consulta5 = "SELECT * FROM CESAR WHERE FINALIZADA = 'Sim'"
whrlinhas3 = pd.read_sql_query(consulta5, conn10)
whrlinhas4 = whrlinhas3.shape[0]



#leitura do banco FERRAMENTARIA
if fLIDERES == 'CESAR FILHO':
    if fSETOR == 'MECÂNICA':
        if senha == '1400':
            cl1 = st.button("DELETAR TABELA")
            if cl1:
                cursor10.execute("DROP TABLE CESAR")
                conn10.commit()
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
                        numros = st.number_input("Selecione o numero da OS que deseja atualizar",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
                        st.metric(label="OS Existentes", value= allln1)
                        numros1 = numros-1
                        if allln1 == 0:
                            st.success('Não há pendências')
                        else:
                            osespec = allinhas.loc[numros1]
                            def load_dataa():

                                return pd.DataFrame(osespec)
                            st.checkbox("Estender", value=True, key="use_container_widthh")
                            df = load_dataa()
                            st.dataframe(df, use_container_width=st.session_state.use_container_width)
                      


                if fLIDERES == 'CESAR FILHO':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1400':
                            if Rniveldaocorrencia != "Selecione":
                                if Rsolicitante != "Selecione":
                                    if Rsetor != "Selecione":
                                            if atd1: 
                                                st.caption('É necessario finalizar esta OS antes de inciar outra.')
                                                atl = st.button('atualize')
                                                if atl:
                                                    st.balloons()
                                                    cursor10.execute("UPDATE CESAR SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, DATA = ?, HORA = ?, AÇÃO = ? WHERE OS = ?",(RUsolicitante, RUsetor, RUstatus,RUniveldaocorrencia,RUdata,str(RUtempoi),RUacao,numros))
                                                    conn10.commit()
                                                    conn10.close()
                                                                                           
                                            else:
                                                insdds = st.button("INSERIR DADOS")

                                                if insdds:
                                                    allln3 = allln1 + 1
                                                if insdds:
                                                    st.balloons()
                                                    cursor10.execute("INSERT INTO CESAR (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?)", (allln3 , str(Rsolicitante), str(Rsetor), str(Rstatus),str(Rniveldaocorrencia),Rdata,str(Rtempoi),Racao,'Não',None,None))
                                                    conn10.commit()
                                                    conn10.close()
                           
            with tab7:
                st.header('Finalizar OS')
                jefferson,lourdes=st.columns(2)
                with jefferson:
                    setorescolhido = st.selectbox('Setor', ('TECNOLOGIA DA INFORMAÇÃO','COMERCIAL','ADMINISTRATIVO','EXPEDIÇÃO','PRODUÇÃO','FERRAMENTARIA','SERRALHARIA','MECÂNICA'),index=None,placeholder='Selecione')
                    fnlz2 = st.number_input("Selecione o numero da OS que deseja Finalizar",min_value=0,max_value=1000,value=0,placeholder="Selecione")
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

                if fLIDERES == 'CESAR':
                    if fSETOR == 'MECÂNICA':
                        if senha == '1400':
                            if setorescolhido == 'FERRAMENTARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor4.execute("UPDATE FERRAMENTARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn4.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')
                            if setorescolhido == 'MECÂNICA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor10.execute("UPDATE CESAR SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn10.commit()
                                    conn10.close()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

                            if setorescolhido == 'PRODUÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor5.execute("UPDATE PRODUCAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn5.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')
                            
                            if setorescolhido == 'ADMINISTRATIVO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor6.execute("UPDATE ADMINISTRATIVO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn6.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 
                            
                            if setorescolhido == 'COMERCIAL':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor7.execute("UPDATE COMERCIAL SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn7.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

                            if setorescolhido == 'EXPEDIÇÃO':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor8.execute("UPDATE EXPEDICAO SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn8.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.')  

                            if setorescolhido == 'SERRALHARIA':    
                                fnl=st.button("FINALIZAR")
                                if fnl:
                                    cursor9.execute("UPDATE SERRALHARIA SET FINALIZADA = ?, DATAF = ?, HORAF = ? WHERE OS = ?",(finalizar,datainput,str(timeinput),fnlz2))
                                    conn9.commit()
                                    st.caption('Dia muito lindo é mais que o infinito é puro e belo inocente como uma flor.') 

            with tab8:
                st.header('Manutenção', divider='rainbow')
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
                
                st.markdown('--------')
                with st.expander("Produção"):
                    numros4 = st.number_input("Selecione o numero da      OS",min_value=0,max_value=rd7,value=rd7,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd7)
                    numros5 = numros4-1
                    if rd7 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd6.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)

                st.markdown('--------')
                with st.expander("Administrativo"):
                    numros4 = st.number_input("Selecione o numero  da      OS",min_value=0,max_value=rd11,value=rd11,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd11)
                    numros5 = numros4-1
                    if rd11 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd10.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)

                st.markdown('--------')
                with st.expander("Comercial"):
                    numros4 = st.number_input("Selecione o numero  da      OS",min_value=0,max_value=rd15,value=rd15,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd15)
                    numros5 = numros4-1
                    if rd15 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd14.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)
                
                st.markdown('--------')
                with st.expander("Expedição"):
                    numros4 = st.number_input("Selecione o numero  da       OS",min_value=0,max_value=rd19,value=rd19,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd19)
                    numros5 = numros4-1
                    if rd19 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd18.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width          ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)
                
                st.markdown('--------')
                with st.expander("Serralharia"):
                    numros4 = st.number_input("Selecione  o numero  da       OS",min_value=0,max_value=rd23,value=rd23,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd23)
                    numros5 = numros4-1
                    if rd23 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd22.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width                                                     ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)
                
                
            with tab9:
                st.header('Manutenção', divider='rainbow')
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
                        st.checkbox("Estender", value=True, key="use_container_width  ")
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
                
                st.markdown('--------')
                with st.expander("Produção"):
                    numros4 = st.number_input("Selecione o  numero da      OS",min_value=0,max_value=rd5,value=rd5,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd5)
                    numros5 = numros4-1
                    if rd5 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd4.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width    ")
                        lddtt = load_data()
                        st.dataframe(lddtt, use_container_width=st.session_state.use_container_width)
                
                st.markdown('--------')
                with st.expander("Administrativo"):
                    numros4 = st.number_input("Selecione o numero da               OS",min_value=0,max_value=rd9,value=rd9,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd9)
                    numros5 = numros4-1
                    if rd9 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd8.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width     ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)

                st.markdown('--------')
                with st.expander("Comercial"):
                    numros4 = st.number_input(" Selecione  o numero  da       OS",min_value=0,max_value=rd13,value=rd13,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd13)
                    numros5 = numros4-1
                    if rd13 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd12.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width      ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)
                
                st.markdown('--------')
                with st.expander("Expedição"):
                    numros4 = st.number_input("Selecione  o  numero  da         OS",min_value=0,max_value=rd17,value=rd17,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd17)
                    numros5 = numros4-1
                    if rd17 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd16.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        st.checkbox("Estender", value=True, key="use_container_width               ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)
                
                st.markdown('--------')
                with st.expander("Serralharia"):
                    numros4 = st.number_input("Selecione o numero   da       OS",min_value=0,max_value=rd21,value=rd21,placeholder="Selecione")
                    st.metric(label="OS Existentes", value=rd21)
                    numros5 = numros4-1
                    if rd21 == 0:
                        st.success('Não há pendências')
                    else:
                        osespec = rd20.loc[numros5]
                        def load_data():
                            return pd.DataFrame(osespec)
                        
                        st.checkbox("Estender", value=True, key=" use_container_width                                                        ")
                        lddt = load_data()
                        st.dataframe(lddt, use_container_width=st.session_state.use_container_width)

            with tab10:
                st.header('Manutenção', divider='rainbow')
                statuses,sats,statuses1=st.columns([90,8,20])
                with statuses:
                    with st.expander("See explanation"):
                        numros10 = st.number_input("Selecione o numero da    OS",min_value=0,max_value=allln1,value=allln1,placeholder="Selecione")
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