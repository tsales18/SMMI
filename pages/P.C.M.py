import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import sqlite3
import time
import calendar
from PIL import Image
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import PyPDF2
from io import BytesIO
import plotly.graph_objects as go
from datetime import datetime, timedelta
from streamlit_extras.metric_cards import style_metric_cards
style_metric_cards()

df = pd.read_excel(
    io = './Datasets/system_extraction.xlsx',
    engine='openpyxl',
    sheet_name='salesreport',
    usecols='A:D',
    nrows=12
)

if 'bancos'=='bancos':
    conn14 = sqlite3.connect('./Data/Meses')
    cursor14 = conn14.cursor()
    cursor14.execute('''
    CREATE TABLE IF NOT EXISTS Janeiro (
        ID TEXT,
        OCORRÊNCIA TEXT
    
    )
''')
    
    conn = sqlite3.connect('./Data/Setores')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PCM (
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
        MANUTENTOR,
        ESPECIALIDADE,
        LMC, 
        Local,
        MÊS,
        PARADA
                            
    )
''')
    
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MTTR (
        DATA DATE,
        HORA INTEGER,
        MÊS,
        MAQUINA TEXT    
                              
    )
''')
    
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MTBF (
        DATA DATE,
        HORA INTEGER,
        MÊS,
        MAQUINA TEXT
                              
    )
''')
    


    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DSP (
        DATA DATE,
        HORA INTEGER,
        MÊS,
        MAQUINA TEXT
                              
    )
''')
    
timenow = datetime.now().replace(microsecond=0).time()
datenow = datetime.now().date()
monthnow = datetime.now().strftime('%B')
monthnumbernow = datetime.now().month

senha = ()
with st.sidebar:
    logo_teste = Image.open('./Midia/sales.jpeg')
    st.image(logo_teste, width=300)
    st.subheader('Pcm')
    img = Image.open('./Midia/user.png')
    with st.form('Logon'):
        st.image(img,width=100)
        if senha == '47297913':
           st.write('OK')
        else:
            senha = st.text_input('Ensira sua senha',type="password")
        st.form_submit_button('Entrar')
        
    with st.spinner("Carregando..."):
            st.success("Pronto!")
            if senha == '47297913':
                logon = True
                st.write("Bem Vindo Jameson!")
            else:
                logon = False
                
st.header('MANUTENÇÃO')
senha = ()
lider = df.drop(columns=['SETOR','FILIAL','STATUS'])
setor = df.drop(columns=['LIDERES','FILIAL','STATUS'])
tab,tab1,tab2 = st.tabs(["| INput |","| Geral |",'Calendario de manutenção'])
with tab:
    col,col1 = st.columns([1,1])
    ano_atualx = 2024
    with col:
        mesx = st.selectbox('Escolha o mês:',('Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'))
        if mesx == 'Janeiro':
            mes = 1
        elif mesx == 'Fevereiro':
            mes = 2
        elif mesx == 'Marco':
            mes = 3
        elif mesx == 'Abril':
            mes = 4
        elif mesx == 'Maio':
            mes = 5
        elif mesx == 'Junho':
            mes = 6
        elif mesx == 'Julho':
            mes = 7
        elif mesx == 'Agosto':
            mes = 8
        elif mesx == 'Setembro':
            mes = 9
        elif mesx == 'Outubro':
            mes = 10
        elif mesx == 'Novembro':
            mes = 11
        elif mesx == 'Dezembro':
            mes = 12
        dias_do_mes = calendar.monthcalendar(2024, mes)
        if mesx == 'Setembro':
            dias = st.selectbox('Escolha o Dia: ',(f'{dias_do_mes[0][0]}',f'{dias_do_mes[0][1]}',f'{dias_do_mes[0][2]}',f'{dias_do_mes[0][3]}',f'{dias_do_mes[0][4]}',f'{dias_do_mes[0][5]}',f'{dias_do_mes[0][6]}',f'{dias_do_mes[1][0]}',f'{dias_do_mes[1][1]}',
                                        f'{dias_do_mes[1][2]}',f'{dias_do_mes[1][3]}',f'{dias_do_mes[1][4]}',f'{dias_do_mes[1][5]}',f'{dias_do_mes[1][6]}',f'{dias_do_mes[2][0]}',f'{dias_do_mes[2][1]}',f'{dias_do_mes[2][2]}',f'{dias_do_mes[2][3]}',
                                        f'{dias_do_mes[2][4]}',f'{dias_do_mes[2][5]}',f'{dias_do_mes[2][6]}',f'{dias_do_mes[3][0]}',f'{dias_do_mes[3][1]}',f'{dias_do_mes[3][2]}',f'{dias_do_mes[3][3]}',f'{dias_do_mes[3][4]}',f'{dias_do_mes[3][5]}',
                                        f'{dias_do_mes[3][6]}',f'{dias_do_mes[4][0]}',f'{dias_do_mes[4][1]}',f'{dias_do_mes[4][2]}',f'{dias_do_mes[4][3]}',f'{dias_do_mes[4][4]}',f'{dias_do_mes[4][5]}',f'{dias_do_mes[4][6]}',f'{dias_do_mes[5][0]}',
                                        f'{dias_do_mes[5][1]}'
                                        ))
        elif mesx == 'Dezembro':
            dias = st.selectbox('Escolha o Dia:  ',(f'{dias_do_mes[0][0]}',f'{dias_do_mes[0][1]}',f'{dias_do_mes[0][2]}',f'{dias_do_mes[0][3]}',f'{dias_do_mes[0][4]}',f'{dias_do_mes[0][5]}',f'{dias_do_mes[0][6]}',f'{dias_do_mes[1][0]}',f'{dias_do_mes[1][1]}',
                                        f'{dias_do_mes[1][2]}',f'{dias_do_mes[1][3]}',f'{dias_do_mes[1][4]}',f'{dias_do_mes[1][5]}',f'{dias_do_mes[1][6]}',f'{dias_do_mes[2][0]}',f'{dias_do_mes[2][1]}',f'{dias_do_mes[2][2]}',f'{dias_do_mes[2][3]}',
                                        f'{dias_do_mes[2][4]}',f'{dias_do_mes[2][5]}',f'{dias_do_mes[2][6]}',f'{dias_do_mes[3][0]}',f'{dias_do_mes[3][1]}',f'{dias_do_mes[3][2]}',f'{dias_do_mes[3][3]}',f'{dias_do_mes[3][4]}',f'{dias_do_mes[3][5]}',
                                        f'{dias_do_mes[3][6]}',f'{dias_do_mes[4][0]}',f'{dias_do_mes[4][1]}',f'{dias_do_mes[4][2]}',f'{dias_do_mes[4][3]}',f'{dias_do_mes[4][4]}',f'{dias_do_mes[4][5]}',f'{dias_do_mes[4][6]}',f'{dias_do_mes[5][0]}',
                                        f'{dias_do_mes[5][1]}'
                                        ))
        elif not mesx == 'Dezembro' or 'Setembro':
            dias = st.selectbox('Escolha o Dia:   ',(f'{dias_do_mes[0][0]}',f'{dias_do_mes[0][1]}',f'{dias_do_mes[0][2]}',f'{dias_do_mes[0][3]}',f'{dias_do_mes[0][4]}',f'{dias_do_mes[0][5]}',f'{dias_do_mes[0][6]}',f'{dias_do_mes[1][0]}',f'{dias_do_mes[1][1]}',
                                    f'{dias_do_mes[1][2]}',f'{dias_do_mes[1][3]}',f'{dias_do_mes[1][4]}',f'{dias_do_mes[1][5]}',f'{dias_do_mes[1][6]}',f'{dias_do_mes[2][0]}',f'{dias_do_mes[2][1]}',f'{dias_do_mes[2][2]}',f'{dias_do_mes[2][3]}',
                                    f'{dias_do_mes[2][4]}',f'{dias_do_mes[2][5]}',f'{dias_do_mes[2][6]}',f'{dias_do_mes[3][0]}',f'{dias_do_mes[3][1]}',f'{dias_do_mes[3][2]}',f'{dias_do_mes[3][3]}',f'{dias_do_mes[3][4]}',f'{dias_do_mes[3][5]}',
                                    f'{dias_do_mes[3][6]}',f'{dias_do_mes[4][0]}',f'{dias_do_mes[4][1]}',f'{dias_do_mes[4][2]}',f'{dias_do_mes[4][3]}',f'{dias_do_mes[4][4]}',f'{dias_do_mes[4][5]}',f'{dias_do_mes[4][6]}'
                                    ))
    data = f'{dias} de {mesx} de {ano_atualx}'
    st.write(data)
    xcol,xcol1= st.columns([3,3]) 
    with xcol:
        atd1 = st.toggle('Atualizar os dados')
        if atd1:
            consulta1 = "SELECT * FROM PCM"
            ros_oc = pd.read_sql_query(consulta1, conn)
            numero2 = ros_oc.shape[0] 
            numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=0,max_value=1000,value=1,placeholder="Selecione")
            numros1 = numros-1
            if not ros_oc.empty:
                preenchimento = ros_oc.loc[numros1]
                preenchimento = preenchimento.tolist()
            else:
                preenchimento = 'NONE'
    
        container = st.container(border=True)
        if not atd1:
            situação = container.selectbox('Situação:', ('LEVES','MODERADAS','CRITICAS'),index=None,placeholder='Selecione')
        if atd1:
            situação = container.selectbox('Atualize a Situação:', ('LEVES','MODERADAS','CRITICAS'),index=None,placeholder='Atualize')
           
        if not atd1:
            Rsolicitante = container.selectbox('Solicitante:', ('Jameson Sales','Cesar Filho'),index=None,placeholder='Selecione')
        if atd1:
            RUsolicitante = container.selectbox('Atualize o Solicitante:', ('Jameson Sales','Cesar Filho'),index=None,placeholder='Atualize')
                        
        if not atd1:
            textx = container.text_area('Tipo de Ocorrência:',value=None,placeholder='Insira sua ocôrrencia')
        if atd1:
            textx = container.text_area('Atualize o tipo de Ocorrência:',value=preenchimento[3],placeholder='Insira sua ocôrrencia')
                        
        if not atd1:
            Rsetor = container.selectbox('Setor:', ('Tecnolofia da informação:','Comercial','Administrativo','Expedição','Produção','Ferramentaria','Serralharia','Utilidades','Estampo corte e furo','Extrusão'),index=None,placeholder='Selecione')
            RUsetor = ''
        if atd1:
            RUsetor = container.selectbox('Aualize o Setor:', ('Tecnolofia da informação:','Comercial','Administrativo','Expedição','Produção','Ferramentaria','Serralharia','Utilidades','Estampo corte e furo','Extrusão'),index=None,placeholder='Atualize')
            Rsetor = ''
                    
        if not atd1:
            Rniveldaocorrencia = container.selectbox('Nivel da ocorrência:', ('Emergência','Muito urgênte','Pouco urgÊnte','Urgênte'),index=None,placeholder='Selecione')
        if atd1:
            RUniveldaocorrencia = container.selectbox('Atualize o Nivel da ocorrência:',('Emergência','Muito urgênte','Pouco urgÊnte','Urgênte'),index=None, placeholder='Atualize')
            Rniveldaocorrencia = ''

        if not atd1:
            Racao = container.selectbox('Tipo da ação:', ('Corretiva','Preventiva','Preditiva','Instalação'),index=None,placeholder='Selecione')
        if atd1:
            RUacao = container.selectbox('Atualize o Tipo da ação:', ('Corretiva','Preventiva','Preditiva','Instalação'),index=None,placeholder='Atualize')
            Racao = ''

        if not atd1:
            especialidades = container.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Selecione')
        if atd1:
            especialidades = container.selectbox('Atualize á Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=None,placeholder='Atualize')

        if not atd1:
            manutentor = container.selectbox('Tipo de mautenção:',('Elétrica','Mecânica'),index=None,placeholder='Defina')
        if atd1:
            manutentor = container.selectbox('Atualize o tipo de manutenção:',('Elétrica','Mecânica'),index=None,placeholder='Defina')    
        
        if Rsetor == 'Extrusão' or RUsetor == 'Extrusão':
            Local = container.selectbox('Local:',('Prensa P8','Puller - 1','Puller - 2','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Serra Fria','Forno de Envelhecimento'),index=None,placeholder= 'Selecione')
                        
        if Rsetor == 'Estampo, corte e furo' or RUsetor == 'Estampo corte e furo':
            Local = container.selectbox('Local:',('Prensa Excentrica - 1','Prensa Excentrica - 2','Serra Automatica','Serra Manual','Embaladora Automatica','Seladora manual - KT001','Seladora manual - KT002'),index=None,placeholder= 'Selecione')
                        
        if Rsetor == 'Utilidades' or RUsetor == 'Utilidades':
            Local = container.selectbox('Local:',('Casa de Bombas','Caixa D.Agua','Subestação - 1','Subestação - 2'),index=None,placeholder= 'Selecione')
                            
        if Rsetor != 'Extrusão' and Rsetor != 'Estampo corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo corte e furo' and RUsetor != 'Utilidades':
            Local = container.selectbox('Local:',('Elétrica Predial','Artífice'),index=None,placeholder= 'Selecione')
        
        if atd1:   
            uploaded_files = container.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
        if not atd1:   
            uploaded_files = container.file_uploader("Envie imagem foto da ocorrência:", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()

    with xcol1:
        if atd1:
            st.metric(label="O.S Existentes", value= numero2)
            if numero2 == 0:
                st.success('Não há pendências')
            else:
                osespec = ros_oc.loc[numros1]
                def load_dataa():
                    return pd.DataFrame(osespec)
                st.checkbox("Estender", value=True, key="use_container_width1")
                df = load_dataa()
                st.dataframe(df, use_container_width=st.session_state.use_container_width1)
                numero_da_os = st.number_input("Selecione o numero da O.S que deseja DELETAR",min_value=0,max_value=1000,value=1,placeholder="Selecione")
                dell = st.button('Excluir 🗑')
                if dell:
                    st.toast(f'Deletando O.S!')
                    time.sleep(0.5)
                    cursor.execute(f'DELETE FROM PCM WHERE OS = {numero_da_os};')
                    conn.commit()

    omaga = [Rniveldaocorrencia,Racao,especialidades,Local,manutentor,textx]
    bools = []
    if logon:
        consulta3 = f"SELECT * FROM PCM"
        pmes_leve = pd.read_sql_query(consulta3, conn)
        numero2 = pmes_leve.shape[0]
        for busca in omaga:
            if not busca:
                bools.append(True)
            else:
                bools.append(False)
    
        if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False:
            if situação == 'LEVES':
                insertx = st.button('Enviar Ocorrência')
                if insertx: 
                    cursor14.execute(f"UPDATE {mesx} SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data))
                    conn14.commit()
                    pcm_id = numero2 + 1

                    cursor.execute("INSERT INTO PCM (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,LMC,LOCAL,MÊS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pcm_id, 'JAMESON SALES', 'PCM',textx,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,situação,Local,monthnow))
                    conn.commit()
             
                consulta3 = f"SELECT * FROM {mesx}"
                mes_leve = pd.read_sql_query(consulta3, conn14)
                numero2 = mes_leve.shape[0]
            
                consulta3 = f"SELECT * FROM PCM"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                numero2 = pmes_leve.shape[0]

        if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False: 
            if situação == 'MODERADAS':
                insertx = st.button('Enviar Ocorrência ')
                if insertx: 
                    cursor14.execute(f"UPDATE {mesx}_WARNING SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data))
                    conn14.commit()
                    pcm_id = numero2 + 1

                    cursor.execute("INSERT INTO PCM (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,LMC,LOCAL,MÊS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pcm_id, 'JAMESON SALES', 'PCM',textx,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,situação,Local,monthnow))
                    conn.commit()

                consulta3 = f"SELECT * FROM {mesx}_WARNING"
                mes_warning = pd.read_sql_query(consulta3, conn14)
                numero2 = mes_warning.shape[0]
            
                consulta3 = f"SELECT * FROM PCM"
                pmes_leve = pd.read_sql_query(consulta3, conn14)
                numero2 = pmes_leve.shape[0]

        if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False and bools[5] == False:

            if situação == 'CRITICAS':
                insertx = st.button('Enviar Ocorrência  ')
                if insertx: 
                    cursor14.execute(f"UPDATE {mesx}_ERROR SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data))
                    conn14.commit()
                    pcm_id = numero2 + 1

                    cursor.execute("INSERT INTO PCM (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,LMC,LOCAL,MÊS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pcm_id, 'JAMESON SALES', 'PCM',textx,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,situação,Local,monthnow))
                    conn.commit()
                
                consulta3 = f"SELECT * FROM {mesx}_ERROR"
                mes_error = pd.read_sql_query(consulta3, conn14)
                consulta3 = f"SELECT * FROM PCM"
                pmes_leve = pd.read_sql_query(consulta3, conn14)
                numero2 = pmes_leve.shape[0]
        
        if atd1:
            atl = st.button('Atualize ↻')
            if atl:
                st.balloons()
                st.toast('Atualizando O.S!')
                time.sleep(0.1)
                st.toast(f' Atualizada!')
                cursor14.execute(f"UPDATE {mesx} SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data))
                conn14.commit()
                cursor.execute("UPDATE PCM SET SOLICITANTE = ?, SETOR = ?,OCORRENCIA = ?,GRAU = ?, AÇÃO = ?,LOCAL = ?, ESPECIALIDADE = ?,LMC = ? WHERE OS = ?",(RUsolicitante, RUsetor, textx,RUniveldaocorrencia,RUacao,Local,especialidades,situação,numros))
                cursor.execute("UPDATE imagens SET imagem = ? WHERE id = ?",(bytes_data,numros))
                conn.commit()

with tab1:
    maq = ['Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem']
    tabelas = ['ELETRICA', 'MECANICA','FERRAMENTARIA','PRODUCAO','TI','ADMINISTRATIVO','COMERCIAL','EXPEDICAO','PCM']
    col,col1 = st.columns([1,1])
    with col:
        maquina = st.selectbox('Local:',('Prensa - P8','Puller - 01','Puller - 02','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts','Prensa Excentrica - 01','Prensa Excentrica - 02','Serra Automatica','Serra Manual','Serra fita  - FRANHO','Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Maquina de jatear','Talha Elétrica','Embaladora Automatica','Elétrica Predial','Artífice','Recuperação de ferramentas','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Seladora manual - KT001','Seladora manual - KT002','Portão de automoveis','Portão de pedestres','Interfone'), placeholder='Selecione')
    with col1:
        mes_op = st.selectbox('Escolha  o  mês:',('January','February','March','April','May','June','July','August','September','October','November','December'),index=monthnumbernow-1)
    cnt = 0
    falhas = ['ELETRICA']
    for james in tabelas:
        for james1 in maq:
            consulta3 = f"SELECT * FROM {james} WHERE Local = '{maquina}' AND ESPECIALIDADE = '{james1}' AND MÊS = '{mes_op}'"
            shape1 = pd.read_sql_query(consulta3, conn)
            shape = shape1.shape[0]
            cnt = cnt + 1
            falhas.append(shape)
            if cnt == 22:
                falhas.append(tabelas[1])
            if cnt == 44:
                falhas.append(tabelas[2])
            if cnt == 66:
                falhas.append(tabelas[3])
            if cnt == 88:
                falhas.append(tabelas[4])
            if cnt == 110:
                falhas.append(tabelas[5])
            if cnt == 132:
                falhas.append(tabelas[6])
            if cnt == 154:
                falhas.append(tabelas[7])
            if cnt == 176:
                falhas.append(tabelas[8])

    qntd_falhas = []
    for soma in range(22):
        falhasx = falhas[1 + soma]+falhas[24 + soma]+falhas[47 + soma]+falhas[70 + soma]+falhas[93 + soma]+falhas[116 + soma]+falhas[139 + soma]+falhas[162 + soma]+falhas[185 + soma]
        qntd_falhas.append(falhasx)
    
    col1,col2,col3 = st.columns([4,0.001,4])
    #GRAFICOS
    with col1:
        with st.form('Grafico'):
            st.header('Ocorrências com mais :red[recôrrencias]',divider='red')
            def get_chart_63301528():
                import plotly.graph_objects as go
                labels = ['Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem']     
                values = [qntd_falhas[0],qntd_falhas[1], qntd_falhas[2],qntd_falhas[3], qntd_falhas[4], qntd_falhas[5],qntd_falhas[6],qntd_falhas[7],qntd_falhas[8],qntd_falhas[9],qntd_falhas[10],qntd_falhas[11],qntd_falhas[12],qntd_falhas[13],qntd_falhas[14],qntd_falhas[15],qntd_falhas[16],qntd_falhas[17],qntd_falhas[18],qntd_falhas[19],qntd_falhas[20],qntd_falhas[21]]
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
                oi =  st.plotly_chart(fig, theme="streamlit")
                return oi
            get_chart_63301528()
            st.form_submit_button('🔄')
    
    especialidades_eletricas = ['Falhas Elétricas','Elétrônica','Rede Industrial','Erro de Logica','Falhas na Automação','Problemas de Software','Impactos externos']
    with st.expander('💡'):
        especialidadesx = st.selectbox('Especialidade:', ('Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem'),index=0)        
        Trues = []
        for s in especialidades_eletricas:
            if s in especialidadesx:
                Trues.append(True)
            else:
                Trues.append(False)

        if True in Trues:
            grupo_setores = ['Elétrica','Produção','P.C.M','Ferramentaria','T.I','Comercial','Administrativo','Serralharia','Expedição']
        else:
            grupo_setores = ['Mecânica','Produção','P.C.M','Ferramentaria','T.I','Comercial','Administrativo','Serralharia','Expedição']        

        setor = st.selectbox('Setor:', (grupo_setores),index=0,placeholder='Selecione')
        if setor == 'Elétrica':
            setor = 'ELETRICA'
        if setor == 'Mecânica':
            setor = 'MECANICA'
        if setor == 'Produção':
            setor = 'PRODUCAO'
        if setor == 'T.I':
            setor = 'TI'
        if setor == 'Expedição':
            setor = 'EXPEDICAO'
        if setor == 'P.C.M':
            setor = 'PCM'

        consulta3 = f"SELECT * FROM {setor} WHERE Local = '{maquina}' AND ESPECIALIDADE = '{especialidadesx}' AND MÊS = '{mes_op}'"
        pmes_leve = pd.read_sql_query(consulta3, conn)
        local = pmes_leve
        shape = pmes_leve.shape[0]
        st.metric(label="Ocorrências existentes", value= shape)
        xscol,xscol1 = st.columns([145,5])

        with xscol:
            st.caption('Anterior')
            after = st.button('⬅')
        with xscol1:
            st.caption('Proximo')
            before = st.button('➡')

        if 'FIN' not in st.session_state:
            st.session_state.FIN = 0
        if not st.session_state.FIN  >= shape - 1:
            if before:
                st.session_state.FIN = st.session_state.FIN + 1
        if not  st.session_state.FIN <= 0:     
            if after:
                st.session_state.FIN= st.session_state.FIN - 1
        if not pmes_leve.empty:

            pmes_leve = pmes_leve.loc[st.session_state.FIN]
            def load_dataa():
                return pd.DataFrame(pmes_leve)
            st.checkbox("Estender", value=True, key="use_container_width")
            df = load_dataa()
            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            dt = local.loc[st.session_state.FIN]
            dt = dt.tolist()
    
            with open("./Data/hello.pdf", 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                st.download_button(
                label="Exportar O.S 🖨",
                key= "download_button",
                data= file,
                file_name=f"O.S {dt[0]}.pdf",
                mime='application/octet-stream'
                )
        
            cursor.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
            if cursor.fetchall():
                cursor.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                imagens = cursor.fetchall()
                oe = imagens[0][1]
                imagem = Image.open(BytesIO(oe))

            localx = local.loc[st.session_state.FIN]
            pmg = localx.tolist()
        else:
            pmg = ['NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE']
            st.warning(f'Não a Ordens para: {maquina} - {setor} - {especialidadesx}')
    
    with col3:
        hora_inicias = []
        horas_finais = []
        tabelasx = ['ELETRICA', 'MECANICA','FERRAMENTARIA','PRODUCAO','TI','ADMINISTRATIVO','COMERCIAL','EXPEDICAO','PCM']
        consulta3 = f"SELECT * FROM MTTR"
        mttr  = pd.read_sql_query(consulta3, conn)
        mttr_shape = mttr.shape[0]
        omaga = '00:00:00'
        po = datetime.strptime(omaga, "%H:%M:%S")
        bools = []
        for search in tabelasx:
            consulta3 = f"SELECT HORA,HORAF FROM '{search}' WHERE Local = '{maquina}' AND DATA = '{datenow}'"
            result  = pd.read_sql_query(consulta3, conn)
            resultt = result.shape[0]
            if result.empty:
                bools.append(False)
            else:
                bools.append(True)
            for indice, linha in result.iterrows():
                horasIN = linha.tolist()
                hora_inicias.append(horasIN)
                if not horasIN[0] == None and not horasIN[1] == None:
                    tempo1 = datetime.strptime(horasIN[0], "%H:%M:%S")
                    tempo2 = datetime.strptime(horasIN[1], "%H:%M:%S")
                    diferenca = tempo1 - tempo2
                    if tempo1 < tempo2:
                        diferenca = timedelta(days=0, seconds=(tempo2 - tempo1).seconds)
                    diferenca_formatada = str(diferenca)
                    horas, minutos, segundos = map(int,diferenca_formatada.split(':'))
                    tempo1 = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    tempo2 = timedelta(hours=0, minutes=0, seconds=0)
                    soma_total = tempo1 + tempo2
                    po += soma_total
                    stry = str(soma_total)
                    horas, resto = divmod(soma_total.seconds, 3600)
                    minutos, segundos = divmod(resto, 60)
                    alou  = str(po)
                    data_hora_objeto = datetime.strptime(alou , "%Y-%m-%d %H:%M:%S")
                    horario_formatado = data_hora_objeto.strftime("%H:%M:%S")
        
                    horas, minutos, segundos = map(int,horario_formatado.split(':'))
                    hrs = horas + minutos/60 + segundos/3600
                    dsp = 100-hrs/10.48*100
                    cursor.execute("INSERT INTO DSP (DATA,HORA,MÊS,MAQUINA) VALUES (?,?,?,?)", (datenow,dsp,monthnow,maquina))
                    conn.commit()

        consulta3 = f"SELECT * FROM DSP WHERE MAQUINA = '{maquina}'"
        result  = pd.read_sql_query(consulta3, conn)
        resultt = result.shape[0]
        
        def get_chart_2006546():
            import plotly.express as px
            fig = px.histogram(result, x="DATA", y="HORA", histfunc= "avg", nbins=100, text_auto=True)
            oi = st.plotly_chart(fig, theme="streamlit")
            return oi
        
        with st.form('Grafico2'):
            st.header('Disponibilidade de :red[Maquina]',divider='red')
            get_chart_2006546()
            st.form_submit_button('🔄   ')
        
    col,col1,col2 = st.columns([4,0.001,4])
    with col:
        consulta3 = f"SELECT * FROM MTBF"
        allln = pd.read_sql_query(f"SELECT HORA FROM ids WHERE DATA = '{datenow}'", conn)
        allln1 = allln.shape[0]
        horarios = []
        for indice, linha in allln.iterrows():
            list = linha.tolist()
            horarios.append(list)
        leng = len(horarios)
        soma = tempo1 = datetime.strptime('00:00:00', "%H:%M:%S")
        if allln1 > 1:
            for s in range(leng):
                if not s == leng - 1:
                    tempo1 = datetime.strptime(horarios[s][0], "%H:%M:%S")
                    tempo2 = datetime.strptime(horarios[s + 1][0], "%H:%M:%S")
                    if tempo2 < tempo1:
                        diferenca = timedelta(days=0, seconds=(tempo2 - tempo1).seconds)
                    else:
                        diferenca = tempo2 - tempo1
                    soma += diferenca
                    stry = str(soma)
                    data_hora_objeto = datetime.strptime(str(soma) , "%Y-%m-%d %H:%M:%S")
                    if s == leng - 2:
                        oma = data_hora_objeto.strftime("%H:%M:%S")
                    horario_formatado = data_hora_objeto.strftime("%H:%M:%S")
                    cursor.execute("INSERT INTO MTBF (DATA,HORA,MÊS,MAQUINA) VALUES (?,?,?,?)", (datenow,horario_formatado,monthnow,maquina))
                    conn.commit()
        else:
            oma = 0
        consulta3 = f"SELECT * FROM MTBF WHERE MAQUINA = '{maquina}'"
        mtbf_df  = pd.read_sql_query(consulta3, conn)
        mtbf_shape = mtbf_df.shape[0]        
        def get_chart_81779437():
            fig = go.Figure([go.Scatter(x=mtbf_df['DATA'], y=mtbf_df['HORA'])])
            return fig
        omaga = get_chart_81779437()
        with st.form('Grafico3'):
            st.header(' :red[M.T.B.F]',divider='red')
            st.metric(label= "M.T.B.F", value=horario_formatado,delta=oma)   
            omaga 
            st.form_submit_button('🔄 ')
      
    with col1:
        hora_inicias = []
        horas_finais = []
        tabelasx = ['ELETRICA', 'MECANICA','FERRAMENTARIA','PRODUCAO','TI','ADMINISTRATIVO','COMERCIAL','EXPEDICAO','PCM']
        consulta3 = f"SELECT * FROM MTTR"
        mttr  = pd.read_sql_query(consulta3, conn)
        mttr_shape = mttr.shape[0]
        omaga = '00:00:00'
        po = datetime.strptime(omaga, "%H:%M:%S")
        bools = []
        for search in tabelasx:
            consulta3 = f"SELECT HORA,HORAF FROM '{search}' WHERE Local = '{maquina}' AND DATA = '{datenow}'"
            result  = pd.read_sql_query(consulta3, conn)
            resultt = result.shape[0]
            if result.empty:
                bools.append(False)
            else:
                bools.append(True)
            for indice, linha in result.iterrows():
                horasIN = linha.tolist()
                hora_inicias.append(horasIN)
                if not horasIN[0] == None and not horasIN[1] == None:
                    tempo1 = datetime.strptime(horasIN[0], "%H:%M:%S")
                    tempo2 = datetime.strptime(horasIN[1], "%H:%M:%S")
                    diferenca = tempo1 - tempo2
                    if tempo1 < tempo2:
                        diferenca = timedelta(days=0, seconds=(tempo2 - tempo1).seconds)
                    diferenca_formatada = str(diferenca)
                    horas, minutos, segundos = map(int,diferenca_formatada.split(':'))
                    tempo1 = timedelta(hours=horas, minutes=minutos, seconds=segundos)
                    tempo2 = timedelta(hours=0, minutes=0, seconds=0)
                    soma_total = tempo1 + tempo2
                    po += soma_total
                    stry = str(soma_total)
                    horas, resto = divmod(soma_total.seconds, 3600)
                    minutos, segundos = divmod(resto, 60)
                    alou  = str(po)
                    data_hora_objeto = datetime.strptime(alou , "%Y-%m-%d %H:%M:%S")
                    horario_formatado = data_hora_objeto.strftime("%H:%M:%S")
                    cursor.execute("INSERT INTO MTTR (DATA,HORA,MÊS,MAQUINA) VALUES (?,?,?,?)", (datenow,horario_formatado,monthnow,maquina))
                    conn.commit()

    with col2:
        consulta3 = f"SELECT * FROM MTTR WHERE MAQUINA = '{maquina}'"
        mttr  = pd.read_sql_query(consulta3, conn)
        mttr_shape = mttr.shape[0]

        if mttr.empty:
            horario_formatado = 0
            stry = 0
        
        if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False and bools[5] == False and bools[6] == False and bools[7] == False and bools[8] == False:
            horario_formatado = 0
            stry = 0
        
        def get_chart_81779437():
            # Using graph_objects
            fig = go.Figure([go.Scatter(x=mttr['DATA'], y=mttr['HORA'])])
            return fig
        omaga = get_chart_81779437()
        with st.form('Grafico4'):
            st.header(' :red[M.T.T.R]',divider='red')
            st.metric(label= "M.T.T.R", value=horario_formatado,delta=stry)
            omaga
            st.form_submit_button('🔄 ')

with tab2:
    col,col1 = st.columns([0.4,1])
    with col:
        meses = st.selectbox('Escolha o mês ',('Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'))
        mesx = meses
    col4,col,col1,col2 = st.columns([50,4,4,4])
    with col4:
        st.header(f'Manutenção para :blue[{meses}]',divider='green')
    with st.expander('Legenda'):
        with col:
            color = st.color_picker('Situação L','#00f900')
        with col1:
            color1 = st.color_picker('Situação M','#D6D217')
        with col2:
            color2 = st.color_picker('Situação C','#F90004')
    col,col1,col2,col3,col4,col5,col6= st.columns([1,1,1,1,1,1,1])

    if 'region' == 'region':
        consulta3 = f"SELECT * FROM {meses}"
        jan_leve = pd.read_sql_query(consulta3, conn14)
        consulta3 = f"SELECT * FROM {mesx}_WARNING"
        jan_moderado = pd.read_sql_query(consulta3, conn14)
        consulta3 = f"SELECT * FROM {meses}_ERROR"
        jan_critico = pd.read_sql_query(consulta3, conn14)
        oi = jan_leve.drop(columns= ['ID'])
        oix = jan_moderado.drop(columns= ['ID'])
        oixx = jan_critico.drop(columns= ['ID'])
        lists_prev = [oi[coluna].tolist() for coluna in oi.columns]
        lists_prevx = [oix[coluna].tolist() for coluna in oix.columns]
        lists_prevxx = [oixx[coluna].tolist() for coluna in oixx.columns]
        jan_list_prev = [lists_prev,lists_prevx,lists_prevxx]

    def salesprev(meses):
        ano_atual = 2024
        if meses == 'Janeiro':
            mes = 1
        elif meses == 'Fevereiro':
            mes = 2
        elif meses == 'Marco':
            mes = 3
        elif meses == 'Abril':
            mes = 4
        elif meses == 'Maio':
            mes = 5
        elif meses == 'Junho':
            mes = 6
        elif meses == 'Julho':
            mes = 7
        elif meses == 'Agosto':
            mes = 8
        elif meses == 'Setembro':
            mes = 9
        elif meses == 'Outubro':
            mes = 10
        elif meses == 'Novembro':
            mes = 11
        elif meses == 'Dezembro':
            mes = 12
        ano = ano_atual
        dias_do_mes = calendar.monthcalendar(ano, mes)
        return dias_do_mes
    def salestext(mesx,ano_atualx,lists_prev,lists_prevx,lists_prevxx):
        if mesx == 'Janeiro':
            mes = 1
            prev_jan = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Fevereiro':
            mes = 2
            prev_fev = [lists_prev,lists_prevx,lists_prevxx]
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Marco':
            mes = 3
            prev_mar = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Abril':
            mes = 4
            prev_abr = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Maio':
            mes = 5
            prev_mai = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Junho':
            mes = 6
            prev_jun = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Julho':
            mes = 7
            prev_jul = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Agosto':
            mes = 8
            prev_agst = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Setembro':
            mes = 9
            prev_set = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_out = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Outubro':
            mes = 10
            prev_out = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_nvmb = 0
            prev_dzmb = 0
        elif mesx == 'Novembro':
            mes = 11
            prev_nvmb = [lists_prev,lists_prevx,lists_prevxx]
            prev_out = 0
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_dzmb = 0
        elif mesx == 'Dezembro':
            mes = 12
            prev_dzmb = [lists_prev,lists_prevx,lists_prevxx]
            prev_fev = 0
            prev_jan = 0 
            prev_mar = 0
            prev_abr = 0
            prev_mai = 0
            prev_jun = 0
            prev_jul = 0
            prev_agst = 0
            prev_set = 0
            prev_out = 0
            prev_nvmb = 0
        ano = 2024
        dias_do_mes = calendar.monthcalendar(ano, 1)
        return mes,prev_jan,prev_fev,prev_mar,prev_abr,prev_mai,prev_jun,prev_jul,prev_agst,prev_set,prev_out,prev_nvmb,prev_dzmb
    salesprevx = salesprev(meses) 
    salesprevxx = salestext(mesx,ano_atualx,lists_prev,lists_prevx,lists_prevxx) 
    IDK = salesprevxx[0]
    with col:
        st.write('Segunda')
        container = st.container(border=True)
        container.write(f'{salesprevx[0][0]} de'f' {meses}')
        container.success(f'{salesprevxx[IDK][0][0][0]}') 
        container.warning(f'{salesprevxx[IDK][1][0][0]}')
        container.error(f'{salesprevxx[IDK][2][0][0]}')

        container = st.container(border=True )
        container.write(f'{salesprevx[1][0]} de'f' {meses}')        
        container.success(f"{salesprevxx[IDK][0][0][7]}") 
        container.warning(f'{salesprevxx[IDK][1][0][7]}')
        container.error(f'{salesprevxx[IDK][2][0][7]}')
 
        container = st.container(border=True)
        container.write(f'{salesprevx[2][0]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][14]}") 
        container.warning(f'{salesprevxx[IDK][1][0][14]}')
        container.error(f'{salesprevxx[IDK][2][0][14]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[3][0]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][21]}") 
        container.warning(f'{salesprevxx[IDK][1][0][21]}')
        container.error(f'{salesprevxx[IDK][2][0][21]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[4][0]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][28]}") 
        container.warning(f'{salesprevxx[IDK][1][0][28]}')
        container.error(f'{salesprevxx[IDK][2][0][28]}')
        
        if meses == 'Dezembro':
            container = st.container(border=True)
            container.write(f'{salesprevx[5][0]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][35]}") 
            container.warning(f'{salesprevxx[IDK][1][0][35]}')
            container.error(f'{salesprevxx[IDK][2][0][35]}')

        if meses == 'Setembro':
            container = st.container(border=True)
            container.write(f'{salesprevx[5][0]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][35]}") 
            container.warning(f'{salesprevxx[IDK][1][0][35]}')
            container.error(f'{salesprevxx[IDK][2][0][35]}')
    with col1:
        st.write('Terça')
        container = st.container(border=True)
        container.write(f'{salesprevx[0][1]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][1]}") 
        container.warning(f'{salesprevxx[IDK][1][0][1]}')
        container.error(f'{salesprevxx[IDK][2][0][1]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[1][1]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][8]}") 
        container.warning(f'{salesprevxx[IDK][1][0][8]}')
        container.error(f'{salesprevxx[IDK][2][0][8]}')

    
        container = st.container(border=True)
        container.write(f'{salesprevx[2][1]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][15]}") 
        container.warning(f'{salesprevxx[IDK][1][0][15]}')
        container.error(f'{salesprevxx[IDK][2][0][15]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[3][1]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][22]}") 
        container.warning(f'{salesprevxx[IDK][1][0][22]}')
        container.error(f'{salesprevxx[IDK][2][0][22]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[4][1]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][29]}") 
        container.warning(f'{salesprevxx[IDK][1][0][29]}')
        container.error(f'{salesprevxx[IDK][2][0][29]}')
    
        if meses == 'Dezembro':
            container = st.container(border=True)
            container.write(f'{salesprevx[5][1]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][36]}") 
            container.warning(f'{salesprevxx[IDK][1][0][36]}')
            container.error(f'{salesprevxx[IDK][2][0][36]}')
    with col2:
        st.write('Quarta')   
        
        container = st.container(border=True)
        container.write(f'{salesprevx[0][2]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][2]}") 
        container.warning(f'{salesprevxx[IDK][1][0][2]}')
        container.error(f'{salesprevxx[IDK][2][0][2]}')
        
        
        container = st.container(border=True)
        container.write(f'{salesprevx[1][2]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][9]}") 
        container.warning(f'{salesprevxx[IDK][1][0][9]}')
        container.error(f'{salesprevxx[IDK][2][0][9]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[2][2]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][16]}") 
        container.warning(f'{salesprevxx[IDK][1][0][16]}')
        container.error(f'{salesprevxx[IDK][2][0][16]}')

        container = st.container(border=True)
        container.write(f'{salesprevx[3][2]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][23]}") 
        container.warning(f'{salesprevxx[IDK][1][0][23]}')
        container.error(f'{salesprevxx[IDK][2][0][23]}')

        container = st.container(border=True)
        container.write(f'{salesprevx[4][2]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][30]}") 
        container.warning(f'{salesprevxx[IDK][1][0][30]}')
        container.error(f'{salesprevxx[IDK][2][0][30]}')
    with col3:
        st.write('Quinta')
        container = st.container(border=True)
        container.write(f'{salesprevx[0][3]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][3]}") 
        container.warning(f'{salesprevxx[IDK][1][0][3]}')
        container.error(f'{salesprevxx[IDK][2][0][3]}')

        
        container = st.container(border=True)
        container.write(f'{salesprevx[1][3]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][10]}") 
        container.warning(f'{salesprevxx[IDK][1][0][10]}')
        container.error(f'{salesprevxx[IDK][2][0][10]}')

        container = st.container(border=True)
        container.write(f'{salesprevx[2][3]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][17]}") 
        container.warning(f'{salesprevxx[IDK][1][0][17]}')
        container.error(f'{salesprevxx[IDK][2][0][17]}')

        container = st.container(border=True)
        container.write(f'{salesprevx[3][3]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][24]}") 
        container.warning(f'{salesprevxx[IDK][1][0][24]}')
        container.error(f'{salesprevxx[IDK][2][0][24]}')

        if not salesprevx[4][3] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[4][3]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][24]}") 
            container.warning(f'{salesprevxx[IDK][1][0][24]}')
            container.error(f'{salesprevxx[IDK][2][0][24]}')
    with col4:
        st.write('Sexta') 
        
        container = st.container(border=True)
        container.write(f'{salesprevx[0][4]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][4]}") 
        container.warning(f'{salesprevxx[IDK][1][0][4]}')
        container.error(f'{salesprevxx[IDK][2][0][4]}')
        
        container = st.container(border=True)
        container.write(f'{salesprevx[1][4]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][11]}") 
        container.warning(f'{salesprevxx[IDK][1][0][11]}')
        container.error(f'{salesprevxx[IDK][2][0][11]}')

        container = st.container(border=True)
        container.write(f'{salesprevx[2][4]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][18]}") 
        container.warning(f'{salesprevxx[IDK][1][0][18]}')
        container.error(f'{salesprevxx[IDK][2][0][18]}')

        if not salesprevx[3][4] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[3][4]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][25]}") 
            container.warning(f'{salesprevxx[IDK][1][0][25]}')
            container.error(f'{salesprevxx[IDK][2][0][25]}')

        if meses == 'Feveiro':
            tct = 28
        else:
            if not salesprevx[4][4] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[4][4]} de'f' {meses}')
                container.success(f"{salesprevxx[IDK][0][0][31]}") 
                container.warning(f'{salesprevxx[IDK][1][0][31]}')
                container.error(f'{salesprevxx[IDK][2][0][31]}')
    with col5:
        st.write('Sabado') 
        container = st.container(border=True)
        container.write(f'{salesprevx[0][5]} de'f' {meses}')
        container.success(f"{salesprevxx[IDK][0][0][5]}") 
        container.warning(f'{salesprevxx[IDK][1][0][5]}')
        container.error(f'{salesprevxx[IDK][2][0][5]}')

        if not salesprevx[1][5] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[1][5]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][12]}") 
            container.warning(f'{salesprevxx[IDK][1][0][12]}')
            container.error(f'{salesprevxx[IDK][2][0][12]}')

        if not salesprevx[2][5] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[2][5]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][19]}") 
            container.warning(f'{salesprevxx[IDK][1][0][19]}')
            container.error(f'{salesprevxx[IDK][2][0][19]}')

        if not salesprevx[3][5] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[3][5]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][26]}") 
            container.warning(f'{salesprevxx[IDK][1][0][26]}')
            container.error(f'{salesprevxx[IDK][2][0][26]}')

        if not salesprevx[4][5] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[4][5]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][32]}") 
            container.warning(f'{salesprevxx[IDK][1][0][32]}')
            container.error(f'{salesprevxx[IDK][2][0][32]}')
    with col6:

        st.write('Domingo')
        if not salesprevx[0][6] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[0][6]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][6]}") 
            container.warning(f'{salesprevxx[IDK][1][0][6]}')
            container.error(f'{salesprevxx[IDK][2][0][6]}')
        
        if not salesprevx[1][6] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[1][6]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][13]}") 
            container.warning(f'{salesprevxx[IDK][1][0][13]}')
            container.error(f'{salesprevxx[IDK][2][0][13]}')

        if not salesprevx[2][6] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[2][6]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][20]}") 
            container.warning(f'{salesprevxx[IDK][1][0][20]}')
            container.error(f'{salesprevxx[IDK][2][0][20]}')

        if not salesprevx[3][6] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[3][6]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][27]}") 
            container.warning(f'{salesprevxx[IDK][1][0][27]}')
            container.error(f'{salesprevxx[IDK][2][0][27]}')

        if not salesprevx[4][6] == 0:
            container = st.container(border=True)
            container.write(f'{salesprevx[4][6]} de'f' {meses}')
            container.success(f"{salesprevxx[IDK][0][0][34]}") 
            container.warning(f'{salesprevxx[IDK][1][0][34]}')
            container.error(f'{salesprevxx[IDK][2][0][34]}')

Solicitante = 'Solicitante:'
Data = 'Data:'
Hora = 'Horario:'
Setor = 'Setor:'
Os = 'O.S:'
maqx = 'Maquina:'
dados = [Solicitante,Data,Hora,Setor,Os,maqx,'']
img = Image.open('./Midia/ssmm.jpg')
img1 = Image.open('./Midia/sales.jpeg')

def hello(c,pmg):
    idx = 0
    for james in dados:
        idx = idx + 1
        largura_da_linha = 0.1
        width, height = 580, 50
        raio = 10

        if idx == 1:
            #SOLICITANTE
            t1,t2 = 15,730
            t3,t4 = 58,730
            t5,t6 = 20,662
            t7,t8 = 380,662
            t9,t10 = 500,210
            t11,t12 = 90,642

            texto = f'{pmg[1]}'
            text = f'{pmg[4]}'
            textox = 'Grau de ocorrência :'
            textoxx = 'Especialidade :'
            textos = ''
            x1, y1 = 90, 728
            x2, y2 = 58, 728
            widt, heigh = 200, 30
            r,r1 = 18,630
            r2,r3 = 380,630
            k1,k2,k3,k4 = 250,680,250,420     
        if idx == 2:
            #DATA
            t1,t2 = 15,705
            t3,t4 = 38,705
            t5,t6 = 18,583
            t7,t8 = 380,583
            t9,t10 = 500,210
            t11,t12 = 90,563

            texto = f'{pmg[5]}'
            text = f'{pmg[7]}'
            textox = 'Ação :'
            textoxx = 'Data de finalização :'
            textos = ''
            x1, y1 = 75, 703
            x2, y2 = 37, 703
            r,r1 = 18,550
            r2,r3 = 380,550
            k1,k2,k3,k4 = 350,680,350,420         
        if idx == 3:
            #HORA
            t1,t2 = 250,730
            t3,t4 = 283,730
            t5,t6 = 18,513
            t7,t8 = 380,513
            t9,t10 = 500,210
            t11,t12 = 90,493

            texto = f'{pmg[6]}'
            text = f'{pmg[8]}'
            textox = 'Finalizada? :'
            textoxx = 'Horario de finalização :'
            textos = ''

            x1, y1 = 283, 728
            x2, y2 = 340, 728
            r,r1 = 18,480
            r2,r3 = 380,480
            k1,k2,k3,k4 = 500,200,580,200        
        if idx == 4:
            #SETOR
            t1,t2 = 250,705
            t3,t4 = 275,705
            t5,t6 = 18,422
            t9,t10 = 515,205
            t11,t12 = 430,642

            texto = f'{pmg[2]}'
            text = f'{pmg[11]}'
            textox = 'Ocorrência :'
            textos = 'Bruno Kappaun'
            
            x1, y1 = 275, 703
            x2, y2 = 320, 703
            widt, heigh = 560, 60
            r,r1 = 18,360

            #r2,r3 = 380,410
        if idx == 5:
            #OS
            t1,t2 = 430,730
            t3,t4 = 448,730
            t5,t6 = 25,345
            t11,t12 = 430,563

            texto = f'N° 00{pmg[0]}'
            text = f'{pmg[9]}'
            textox = 'Visualização do problema:'
            x1, y1 = 448, 728
            x2, y2 = 475, 728
            #r,r1 = 18,340
            #r2,r3 = 380,340
        if idx == 6:
            #maquina
            t1,t2 = 430,705
            t3,t4 = 468,705
            t11,t12 = 430,493
            texto =f'{pmg[12]}'
            text = f'{pmg[10]}'
            x1, y1 = 468, 703
            x2, y2 = 510, 703
            #r,r1 = 18,270  
            #r2,r3 = 380,270 
        if idx == 7:
            t11,t12 = 25,410
            text = f'{pmg[3]}'
            
        pdfmetrics.registerFont(TTFont('font', './Fontes/ASENINE_.ttf'))
        cor_do_texto = (0,0,0)
        font_name = 'font' 

        pdfmetrics.registerFont(TTFont('ASS', './Fontes/ASSINATURA.ttf'))
        cor_do_texto = (0,0,0)
        font_namex = 'ASS' 
        
        textobject = c.beginText(t1, t2)
        textobject.setFont(font_name , 13)
        textobject.setTextOrigin(t1, t2)
        textobject.textLine(f"{james}")
        c.setFillColor(cor_do_texto)
        c.drawText(textobject)
        c.setLineWidth(largura_da_linha)
        c.line(x1,y1,x2,y2)
    
        cor_do_texto = (0,0,1)
        textobjectx = c.beginText(t3, t4)
        textobjectx.setFont(font_name, 10)
        textobjectx.setTextOrigin(t3, t4)
        textobjectx.textLine(f"{texto}")
        c.setFillColor(cor_do_texto)
        c.drawText(textobjectx)

        cor_do_texto = (0,0,0)
        textobjectx = c.beginText(t5, t6)
        textobjectx.setFont(font_name, 10)
        textobjectx.setTextOrigin(t5, t6)
        textobjectx.textLine(f"{textox}")
        c.setFillColor(cor_do_texto)
        c.drawText(textobjectx)

        cor_do_texto = (0,0,0)
        textobjectx = c.beginText(t7, t8)
        textobjectx.setFont(font_name, 10)
        textobjectx.setTextOrigin(t7, t8)
        textobjectx.textLine(f"{textoxx}")
        c.setFillColor(cor_do_texto)
        c.drawText(textobjectx)

        cor_do_texto = (0,0,0)
        textobjectx = c.beginText(t9, t10)
        textobjectx.setFont(font_namex, 10)
        textobjectx.setTextOrigin(t9, t10)
        textobjectx.textLine(f"{textos}")
        c.setFillColor(cor_do_texto)
        c.drawText(textobjectx)

        cor_do_texto = (0,0,1)
        textobjectx = c.beginText(t11, t12)
        textobjectx.setFont(font_name, 10)
        textobjectx.setTextOrigin(t11, t12)
        textobjectx.textLine(f"{text}")
        c.setFillColor(cor_do_texto)
        c.drawText(textobjectx)

        raio = 5
        c.roundRect(r, r1, widt, heigh, raio, stroke=1, fill=0)

        width, height = 200, 30
        raio = 5
        c.roundRect(r2, r3, width, height, raio, stroke=1, fill=0)

        c.line(k1,k2,k3,k4)

    #c.setFont('Helvetica', 10)
    #c.drawString(115,730, "Hello World puta que pariu ou")
    #c.grid(xlist, ylist)
    #c.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
    #c.arc(x1, y1, x2, y2, startAng=30, extent=120)
    #c.rect(x, y, width, height, stroke=1, fill=0)
    #c.ellipse(x1,y1, x2,y2, stroke=1, fill=0)
    #c.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0)
    #c.circle(x_cen, y_cen, raio, stroke=1, fill=0)
    width, height = 580, 50
    raio = 10
    r,r1 = 8,695
    c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)
    
    width, height = 580, 500
    raio = 10
    r,r1 = 8,180
    c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)
    
    #c.drawRightString(x, y, texto)
    #c.drawCentredString(x, y, texto)
    x, y = 0,750
    c.drawInlineImage(img, x,y, width=600,height=100)

    x, y = 25,240
    if not pmes_leve.empty:
        cursor.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
        if cursor.fetchall():
            cursor.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
            imagens = cursor.fetchall()
            oe = imagens[0][1]
            imagem = Image.open(BytesIO(oe))
            c.drawInlineImage(imagem, x,y, width=400,height=100)
    #x1,y1 = 50,400
    #c.drawInlineImage(img1, x1,y1, width=500,height=150)
c = canvas.Canvas("./Data/hello.pdf")
hello(c,pmg)
c.save()
