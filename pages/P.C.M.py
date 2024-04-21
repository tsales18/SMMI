import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import sqlite3
import time
import calendar
from PIL import Image
from datetime import datetime
import pytz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import PyPDF2
from io import BytesIO
import plotly.graph_objects as go
from datetime import datetime, timedelta
from streamlit_extras.metric_cards import style_metric_cards
import json
import os

style_metric_cards()
novo_fuso_horario = pytz.timezone('America/Sao_Paulo')
hora_atual = datetime.now().replace(microsecond=0)
hora_atual_no_novo_fuso = hora_atual.astimezone(novo_fuso_horario)
data_hora_com_fuso = str(hora_atual_no_novo_fuso)
data_hora_obj = datetime.strptime(data_hora_com_fuso, "%Y-%m-%d %H:%M:%S%z")
horas = data_hora_obj.strftime("%H")
minutos = data_hora_obj.strftime("%M")
segundos = data_hora_obj.strftime("%S")
timenow = (f"{horas}:{minutos}:{segundos}")

#timenow = datetime.now().replace(microsecond=0).time()
datenow = datetime.now().date()
monthnow = datetime.now().strftime('%B')
monthnumbernow = datetime.now().month

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
        PARADA,
        Calendario
                            
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

    conn1 = sqlite3.connect('./Data/imagens_a_f')
    cursor1 = conn1.cursor()

if 'strs' =='strs':
    solicitante_titulo = 'Solicitante:'
    solicitante_titulo_atl = 'Atualize o solicitante:'
    ocorrencia_titulo = 'Ensira detalhes da ocorrência:'
    ocorrencia_titulo_atl = 'Atualize á ocorrência:'
    setor_titulo = 'Setor solicitante:'
    setor_titulo_atl ='Aualize o Setor:'
    nivel_de_ocorrencia_titulo = 'Nivel da ocorrência:'
    nivel_de_ocorrencia_titulo_atl = 'Atualize o nivel da ocorrência:'
    acao_titulo = 'Tipo de ação:'
    acao_titulo_atl = 'Atualize o tipo da ação:'
    parada_titulo = 'Gerou interrupção no funcionamento?:'
    especialidades_titulo = 'Especifique o tipo de ocorrência:'
    especialidades_titulo_atl = 'Atualize o tipo de ocorrência'
    local_titulo = 'Localidade'
    manutentor_titulo = 'Tipo de manutenção'
    
    help_solicitante = 'Nesta caixa de seleção: você precisa selecionar o responsavel por setor que fez a solicitação de O.S '
    help_ocorrência = 'Nesta caixa de seleção: você precisa inserir a ocorrênica que irá realizar '
    help_setor = 'Nesta caixa de seleção: você precisa selecionar o setor do lider que fez a solicitação de 0.S '
    help_nivel_ocorrencia = 'Nesta caixa de seleção: você precida selecionar o grau de necessidade da ocorrência '
    helpe_acao = 'Nesta caixa de seleção: você precisa selecionar o tipo de açaõ da ocorrência solicitada'
    help_parada = 'Nesta caixa de seleção: você precisa informar se ouve uma interrupção no funcionamento do equipamento'
    help_especialidade = 'Nesta caixa de seleção: você precisa selecionar o tipo de atividade que irá ser aplicada com base na ocorrência'
    help_local = 'Nesta caixa de seleção: você preicsa selecionar o equipamento/local que irá realizar a manutenção'
    help_imagem = 'Nesta caixa de seleção: você precisa anexar uma imagem referente a ocorrência'
    help_imagem_fnlzd = 'Nesta caixa de seleção: você precisa anexar uma imagem após finalizar a ocorrencia'
    help_manutentor = 'Nesta caixa de seleção: você precisa selecionar o tipo de manutenção referente a sua ocorrência'
    help_numero_os = 'Nesta caixa de seleção: você precisa selecionar o numero da O.S que deseja ABRIR ou FINALIZAR'
    help_finalizar_os = 'Nesta caixa de seleção: você precisa selecionar entre SIM ou Não,SIM,para O.S finalizada,Não,para O.S aberta'
    solicitante_list = ['Bruno Kappaun','Cesar Filho','Jameson Sales','Maurilio Sales/Alex Santos','Adriely Lemos','Gilson Freitas','Willian Oliveira','Cesar Augusto','Filipe leite']
    setor_list = ['Tecnologia da Informação','Comercial','Administrativo','Ferramentaria','Serralharia','Utilidades','Estampo,embalagem,corte e furo','Extrusão']
    ocorrencia_list = ['Emergência','Muito urgênte','Pouco urgênte','Urgênte']
    acao_list = ['Corretiva','Preventiva','Preditiva','Confecção','Montagem']
    especialidade_list = ['Falhas Elétricas','Elétrônica','Rede Industrial','Desgaste Mecânico','Erro de Logica','Problemas Hidraulicos','Problemas Pneumaticas','Lubrificação','Problemas Térmicos','Falhas na Automação','Problemas de Software','Impactos externos','Aferição','Reinstalação','Instalação','Recuperação','Melhoria','Reabastecimento','Ajuste','Instalação e Ajuste','Reinstalação e Ajuste','Soldagem','Limpeza']
    extrusão_list = ['Prensa - P8','Puller - 01','Puller - 02','Quench','Esticadeira - HEAD','Esticadeira - TAIL','Forno de Tarugo','Serra Fria','Forno de Envelhecimento','T1 - Belts','T2 - Belts','T3 - Belts','T4 - Belts']
    estampo_etc_list = ['Prensa Excentrica - 01','Prensa Excentrica - 02','Serra Automatica','Serra Manual','Serra fita - FRANHO','Rosqueadeira - MACHO 01','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Embaladora Automatica','Seladora manual - KT001','Seladora manual - KT002']
    utilidades_list = ['Elétrica Predial','Casa de Bombas','Caixa D.Agua','Subestação - 01','Subestação - 02','Portão de automoveis','Portão de pedestres','Interfone']
    all = ['Elétrica Predial','Artífice','Casa de Bombas','Caixa D.Agua','Portão de automoveis','Portão de pedestres','Interfone']
    serralharia_list = ['Elétrica Predial','Artífice','Rosqueadeira - COSSINETE 01','Rosqueadeira - COSSINETE 02','Serra fita - FRANHO']
    ferramentaria_list = ['Elétrica Predial','Artífice','Maquina de jatear','Talha Elétrica','Recuperação de ferramentas']
    geral_list = ['Prensa - P8 - Puller - 1 - Puller - 2 - Esticadeira - HEAD - Esticadeira - TAIL - Forno de Tarugo - Serra Fria - Forno de Envelhecimento - Prensa Excentrica - 1 - Prensa Excentrica - 2 - Serra Automatica - Serra Manual - Serra fita - FRANHO - Rosqueadeira - MACHO 01 - Rosqueadeira - COSSINETE 01 - Rosqueadeira - COSSINETE 2 - Maquina de jatear - Talha Elétrica - Embaladora Automatica - Elétrica Predial - Artífice - Recuperação de ferramentas - Casa de Bombas - Caixa D.Agua - Subestação - 1 - Subestação - 2 -  Seladora manual - KT001 - Seladora manual - KT002 - Portão de automoveis - Portão de pedestres - Interfone']
    local_titulo = 'Localidade'

novo_fuso_horario = pytz.timezone('America/Sao_Paulo')
hora_atual = datetime.now().replace(microsecond=0)
hora_atual_no_novo_fuso = hora_atual.astimezone(novo_fuso_horario)
data_hora_com_fuso = str(hora_atual_no_novo_fuso)
data_hora_obj = datetime.strptime(data_hora_com_fuso, "%Y-%m-%d %H:%M:%S%z")
horas = data_hora_obj.strftime("%H")
minutos = data_hora_obj.strftime("%M")
segundos = data_hora_obj.strftime("%S")
timenow = (f"{horas}:{minutos}:{segundos}")

#timenow = datetime.now().replace(microsecond=0).time()
datenow = datetime.now().date()
monthnow = datetime.now().strftime('%B')
monthnumbernow = datetime.now().month
senha = ()       

senha = ()
lider = df.drop(columns=['SETOR','FILIAL','STATUS'])
setor = df.drop(columns=['LIDERES','FILIAL','STATUS'])
tab1,tab3,tab2 = st.tabs(["🔛 Indicadores",'Relatorios 🧾','📅 Calendario de manutenção'])

with tab1:
    st.header('Indicadores de :blue[manutenção], por localidade!')
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
        total = qntd_falhas[0]+qntd_falhas[1]+ qntd_falhas[2]+qntd_falhas[3]+qntd_falhas[4]+qntd_falhas[5]+qntd_falhas[6]+qntd_falhas[7]+qntd_falhas[8]+qntd_falhas[9]+qntd_falhas[10]+qntd_falhas[11]+qntd_falhas[12]+qntd_falhas[13]+qntd_falhas[14]+qntd_falhas[15]+qntd_falhas[16]+qntd_falhas[17]+qntd_falhas[18]+qntd_falhas[19]+qntd_falhas[20]+qntd_falhas[21]
        with st.form('Grafico'):
            st.header('Ocorrências com mais :red[recôrrencias]',divider='red')
            st.metric(label="Total",value=total) 
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
            
            cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
            if cursor1.fetchall():
                cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                imagens = cursor1.fetchall()
                oe = imagens[0][1]
                imagem = Image.open(BytesIO(oe))
            
            usuario = 'PCM'
            localx = local.loc[st.session_state.FIN]
            pmg = localx.tolist()
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
                o = 0
                b = []
                for s in str(pmg[1]):
                    if s.isalpha():
                        o += 1
                        tmh = 4 * o + 58 
                        b.append(tmh)

                ct = []
                for s in str(pmg[2]):
                    if not pmg[2] =='Produção':
                        if s.isalpha():
                            o += 1
                            tmh = 4 * o + 268
                            ct.append(tmh)
                        else:
                            ''
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
                        text = f'{pmg[5]}'
                        textox = 'Grau de ocorrência :'
                        textoxx = 'Especialidade :'
                        textos = ''
                        x1, y1 = b[9], 728
                        x2, y2 = 58, 728
                        widt, heigh = 200, 30
                        r,r1 = 18,630
                        r2,r3 = 380,630
                        k1,k2,k3,k4 = 250,680,250,420
                    if idx == 2:
                    #DAT
                        t1,t2 = 15,705
                        t3,t4 = 38,705
                        t5,t6 = 18,583
                        t7,t8 = 380,583
                        t9,t10 = 500,210
                        t11,t12 = 90,563

                        texto = f'{pmg[6]}'
                        text = f'{pmg[8]}'
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

                        texto = f'{pmg[7]}'
                        text = f'{pmg[9]}'
                        textox = 'Finalizada? :'
                        textoxx = 'Horario de finalização :'
                        textos = ''

                        x1, y1 = 283, 728
                        x2, y2 = 310, 728
                        r,r1 = 18,480
                        r2,r3 = 380,480
                        k1,k2,k3,k4 = 500,10,580,10
                    if idx == 4:
                    #SETOR
                        t1,t2 = 250,705
                        t3,t4 = 275,705
                        t5,t6 = 18,422
                        t9,t10 = 510,15
                        t11,t12 = 430,642

                        texto = f'{pmg[2]}'
                        text = f'{pmg[12]}'
                        textox = 'Ocorrência :'
                        textos = 'Bruno Kappaun'

                        x1, y1 = 275, 703
                        x2, y2 = 275, 703
                        widt, heigh = 560, 60
                        r,r1 = 18,360
                    if idx == 5:
                        #OS
                        t1,t2 = 430,730
                        t3,t4 = 448,730
                        t5,t6 = 25,345
                        t11,t12 = 430,563

                        texto = f'N° 00{pmg[0]}'
                        text = f'{pmg[10]}'
                        textox = 'Visualização do problema:'
                        x1, y1 = 448, 728
                        x2, y2 = 475, 728
                    if idx == 6:
                    #maquina
                        t1,t2 = 430,705
                        t3,t4 = 455,705
                        t5,t6 = 30,170
                        t11,t12 = 430,493
                        texto =f'{pmg[13]}'
                        textox = 'Visualização pós problema:'
                        text = f'{pmg[11]}'
                        x1, y1 = 455, 703
                        x2, y2 = 510, 703
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
                width, height = 700, 50
                raio = 10
                r,r1 = 8,800
                c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                width, height = 580, 680
                raio = 10
                r,r1 = 8,0
                c.roundRect(r, r1, width, height, raio, stroke=1, fill=0)

                x, y = 0,750
                c.drawInlineImage(img, x,y, width=600,height=100)
                x, y = 10,180
                x1,y1 = 10, 20
                if not pmes_leve.empty:
                    cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                    if cursor1.fetchall():
                        cursor1.execute(f'SELECT * FROM imagens WHERE id = {dt[0]}')
                        imagens = cursor1.fetchall()
                        oe = imagens[0][1]
                        oie = imagens[0][2]
                        imagem = Image.open(BytesIO(oe))
                        imagem2 = Image.open(BytesIO(oie))
                        if not pmes_leve.empty:
                            if not oe == None:
                                imagem = Image.open(BytesIO(oe))
                                c.drawInlineImage(imagem, x,y, width=400,height=145)

                            if not oie == None:
                                imagem2 = Image.open(BytesIO(oie))
                                c.drawInlineImage(imagem2, x1,y1, width=400,height=145))   
                    
            c = canvas.Canvas(f"./Data/geral_{usuario}.pdf")
            hh = hello(c,pmg)
            c.save()
        else:
            pmg = ['NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE']
            st.warning(f'Não a Ordens para: {maquina} - {setor} - {especialidadesx}')

    #DISPONIBILIDADE
    with col3:
        hora_inicias = []
        horas_finais = []
        datasIN = []
        values = []
        disponibilidade = []
        tabelasx = ['ELETRICA', 'MECANICA','PRODUCAO','ADMINISTRATIVO','COMERCIAL','EXPEDICAO','PCM']
        consulta3 = f"SELECT * FROM MTTR"
        mttr  = pd.read_sql_query(consulta3, conn)
        mttr_shape = mttr.shape[0]
        omaga = '00:00:00'
        po = datetime.strptime(omaga, "%H:%M:%S")
        bools = []
        for search in tabelasx:
            consulta3 = f"SELECT HORA,HORAF,DATA FROM '{search}' WHERE Local = '{maquina}' AND AÇÃO != 'Preventiva' AND MÊS = '{mes_op}'"
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
                    horas, minutos, segundos = map(int,str(soma_total).split(':'))
                    hrs = horas + minutos/60 + segundos/3600
                    dsp = 100-hrs/10.48*100
                    disponibilidade.append(dsp)
                    datasIN.append(horasIN[2])
                    
        disponibilidade = pd.DataFrame(disponibilidade)
        dsp_shape = disponibilidade.shape[0]
        datasIN = pd.DataFrame(datasIN)
        if disponibilidade.empty or datasIN.empty:
            disponibilidade = [0,0]
            datasIN = [0,0]
            disponibilidade = pd.DataFrame(disponibilidade)
            datasIN = pd.DataFrame(datasIN)
        
        soma_dsp = disponibilidade.sum()
        res = soma_dsp[0]/dsp_shape
        res = round(res,2)
       
        def get_chart_2006546():
            import plotly.express as px
            fig = px.histogram(x=datasIN[0], y=disponibilidade[0], histfunc= "avg", nbins=100, text_auto=True)
            oi = st.plotly_chart(fig, theme="streamlit")
            return oi
        with st.form('Grafico2'):
            st.header('Disponibilidade de :red[Maquina]',divider='red')
            st.metric(label="Media",value=(f'{res}%')) 
            get_chart_2006546()
            st.form_submit_button('🔄   ')
    col,col1,col2 = st.columns([4,0.0001,4])
    #MTBF
    with col:
        allln = pd.read_sql_query(f"SELECT HORA FROM ids WHERE MAQUINA = '{maquina}' AND Mês = '{mes_op}'", conn)
        allln1 = allln.shape[0]
        horarios = []
        values =[]
        for indice, linha in allln.iterrows():
            list = linha.tolist()
            horarios.append(list)
        leng = len(horarios)
        soma = tempo1 = datetime.strptime('00:00:00', "%H:%M:%S")
        valor_adicionado = []
        if allln1 >= 1:
            for s in range(leng-1):
                if not s == leng - 1:
                    tempo1 = datetime.strptime(horarios[s][0], "%H:%M:%S")
                    tempo2 = datetime.strptime(horarios[s + 1][0], "%H:%M:%S")
                    if tempo2 < tempo1:
                        diferenca = timedelta(days=0, seconds=(tempo2 - tempo1).seconds)
                    else:
                        diferenca = tempo2 - tempo1
                    soma += diferenca
                    stry = str(soma)
                    data_hora_objeto = datetime.strptime(str(soma),"%Y-%m-%d %H:%M:%S")
                    if s == leng - 2:
                        oma = data_hora_objeto.strftime("%H:%M:%S")
                    horario_formatado = data_hora_objeto.strftime("%H:%M:%S")
                    values.append(horario_formatado)
                    valor_adicionado.append(str(diferenca))
                    horas = pd.DataFrame(values)
                    leng = len(values)
         
        with st.form('Graficooie3'):
            allln = pd.read_sql_query(f"SELECT * FROM ids WHERE MAQUINA = '{maquina}' AND Mês = '{mes_op}'", conn)
            allln1 = allln.shape[0]
            datas = allln['DATA']
            shape = datas.shape[0]
            if not values == [] and not valor_adicionado == []:
                horas_list = horas[0]
                horas_list = horas_list.tolist()
                datas_list = datas.tolist()
                del datas_list[shape-1]
                datas = pd.DataFrame(datas_list)

            if not values == [] and not valor_adicionado == []:
                horas_list = horas[0]
                horas_list = horas_list.tolist()
            else:
                horas_list = ['0']
                valor_adicionado = ['0']
                datas = [0,0]
                datas = pd.DataFrame(datas)
                horas = [0,0]
                horas = pd.DataFrame(horas)

            st.header(':red[M.T.B.F]',divider='red')
            st.metric(label= "M.T.B.F",value=horas_list[leng-1],delta=valor_adicionado[leng-1]) 
            def get_chart_81779437():
                fig = go.Figure([go.Scatter(x=datas[0], y=horas[0])])
                return fig
            omaga = get_chart_81779437()
            omaga 
            st.form_submit_button('🔄 ')
            leng = len(values)
    #MTTR            
    with col2:
        #MTTR
        hora_inicias = []
        horas_finais = []
        datasIN = []
        values = []
        tabelasx = ['ELETRICA', 'MECANICA','PRODUCAO','ADMINISTRATIVO','COMERCIAL','EXPEDICAO','PCM']
        omaga = '00:00:00'
        po = datetime.strptime(omaga, "%H:%M:%S")
        bools = []
        for search in tabelasx:
            consulta3 = f"SELECT HORA,HORAF,DATA FROM '{search}' WHERE Local = '{maquina}' AND AÇÃO != 'Preventiva' AND MÊS = '{mes_op}'"
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
                    values.append(horario_formatado)
                    datasIN.append(horasIN[2])        
    
        datasIN = pd.DataFrame(datasIN)
        value = pd.DataFrame(values)
        with st.form('grafico4'):
            if value.empty and datasIN.empty:
                datasIN = [0,0]
                values = [0,0]
                datasIN = pd.DataFrame(datasIN)
                value = pd.DataFrame(values)
                horario_formatado = 0
                stry = 0

            def get_chart_81779437():
                # Using graph_objects
                fig = go.Figure([go.Scatter(x=datasIN[0], y=value[0])])
                return fig
            omaga = get_chart_81779437()
            st.header(' :red[M.T.T.R]',divider='red')
            st.metric(label= "M.T.T.R", value=horario_formatado,delta=stry)
            omaga
            st.form_submit_button('🔄 ')
    
with tab2:
    with st.sidebar:
        file_path = "./Datasets/pcm.json"
        if os.path.exists(file_path):
            # Lê os dados do arquivo JSON
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
            senha = data['senha']
        logo_teste = Image.open('./Midia/sales.jpeg')
        st.image(logo_teste, width=300)
        #st.subheader('Pcm')
        img = Image.open('./Midia/user.png')
        if not senha == '47297913':
            with st.form('Logon'):
                st.image(img,width=100)
                if senha == '47297913':
                    st.write('OK')
                    log = True
                else:
                    senha = st.text_input('Ensira sua senha',type="password")

                st.form_submit_button('Entrar')

        if senha == '47297913':
            data = {
                "senha": f"{senha}",
            }
            file_path = "./Datasets/pcm.json"

            # Escreve o dicionário no arquivo JSON
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            log = True
            
        else:
            data = {
                "senha": "",
            }
            file_path = "./Datasets/pcm.json"
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
            log = False
        
        if log:
            col,col1 = st.columns([1,1])
            ano_atualx = 2024
        
            xcol,xcol1= st.columns([3,3]) 
            with xcol:
                atd1 = st.toggle('Atualizar os dados')
                if atd1:
                    consulta1 = "SELECT * FROM PCM"
                    ros_oc = pd.read_sql_query(consulta1, conn)
                    ros_oc
                    numero2 = ros_oc.shape[0] 

                    numros = st.number_input("Navegue por suas O.S para atualizar-las",min_value=0,max_value=1000,value=1,placeholder="Selecione")
                    numros1 = numros-1
                    if not ros_oc.empty:
                        preenchimento = ros_oc.loc[numros1]
                        preenchimento = preenchimento.tolist()
                    else:
                        preenchimento = 'NONE'
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
       
            
            with st.form('sales'):
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
                    
                data_m = f'{dias} de {mesx} de {ano_atualx}'
                st.write(data_m)
                
                if not atd1:
                    situação = st.selectbox('Grau de necessidade:', ('Leves','Moderadas','Urgêntes'),index=None,placeholder='Selecione')
                if atd1:
                    situação = st.selectbox('Atualize a Situação:', ('Leves','Moderadas','Urgêntes'),index=None,placeholder='Atualize')
                
                if not atd1:
                    Rsolicitante = st.selectbox(solicitante_titulo, (solicitante_list),index=None,placeholder='Selecione!',help=help_solicitante)
                if atd1:
                    RUsolicitante = st.selectbox(solicitante_titulo_atl, (solicitante_list),index=None,placeholder='Atualize!',help=help_solicitante)
                    
                if not atd1:
                    textx = st.text_area(ocorrencia_titulo,value=None,placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                if atd1:
                    textx = st.text_area(ocorrencia_titulo_atl,value=preenchimento[3],placeholder='Insira sua ocôrrencia!',help=help_ocorrência)
                
                if not atd1:
                    Rsetor = st.selectbox(setor_titulo, (setor_list),index=None,placeholder='Selecione!',help=help_setor)
                    RUsetor = ''
                if atd1:
                    RUsetor = st.selectbox(setor_titulo_atl, (setor_list),index=None,placeholder='Atualize!',help=help_setor)
                    Rsetor = ''
                
                if not atd1:
                    Rniveldaocorrencia = st.selectbox(nivel_de_ocorrencia_titulo, (ocorrencia_list),index=None,placeholder='Selecione!',help=help_nivel_ocorrencia)
                if atd1:
                    RUniveldaocorrencia = st.selectbox(nivel_de_ocorrencia_titulo_atl,(ocorrencia_list),index=None, placeholder='Atualize!',help=help_nivel_ocorrencia)
                    Rniveldaocorrencia = ''
                if not atd1:
                    Racao = st.selectbox(acao_titulo, (acao_list),index=None,placeholder='Selecione!',help=helpe_acao)
                if atd1:
                    RUacao = st.selectbox(acao_titulo_atl, (acao_list),index=None,placeholder='Atualize!',help=helpe_acao)
                    Racao = ''
                if not atd1:
                    parada = st.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                if atd1:
                    parada = st.selectbox(parada_titulo, ('Sim','Não'),index=None,placeholder='Selecione!',help=help_parada)
                
                if not atd1: 
                    especialidades = st.selectbox(especialidades_titulo, (especialidade_list),index=None,placeholder='Selecione!',help=help_especialidade)
                
                if atd1:
                    especialidades = st.selectbox(especialidades_titulo_atl, (especialidade_list),index=None,placeholder='Atualize!',help=help_especialidade)
                
                if not atd1:
                    manutentor = st.selectbox('Tipo de mautenção:',('Elétrica','Mecânica'),index=None,placeholder='Defina')
                if atd1:
                    manutentor = st.selectbox('Atualize o tipo de manutenção:',('Elétrica','Mecânica'),index=None,placeholder='Defina')    
                
                if Rsetor == 'Extrusão' or RUsetor == 'Extrusão':
                    Local = st.selectbox(local_titulo,(extrusão_list),index=None,placeholder= 'Selecione!',help=help_local)
                    
                if Rsetor == 'Estampo,embalagem,corte e furo' or RUsetor == 'Estampo,embalagem,corte e furo':
                    Local = st.selectbox(local_titulo,(estampo_etc_list),index=None,placeholder= 'Selecione!',help=help_local)
                    
                if Rsetor == 'Utilidades' or RUsetor == 'Utilidades':
                    Local = st.selectbox(local_titulo,(utilidades_list),index=None,placeholder= 'Selecione!',help=help_local)
                        
                if Rsetor != 'Extrusão' and Rsetor != 'Estampo,embalagem,corte e furo' and Rsetor != 'Utilidades' and RUsetor != 'Extrusão' and RUsetor != 'Estampo,embalagem,corte e furo' and RUsetor != 'Utilidades' and Rsetor != 'Serralharia' and RUsetor != 'Serralharia' and Rsetor != 'Ferramentaria' and RUsetor != 'Ferramentaria'  and Rsetor != 'Geral' and RUsetor != 'Geral':
                    Local = st.selectbox(local_titulo,(all),index=None,placeholder= 'Selecione!',help=help_local)
                elif Rsetor == 'Serralharia' or RUsetor == 'Serralharia':
                    Local = st.selectbox(local_titulo,(serralharia_list),index=None,placeholder= 'Selecione!',help=help_local)
                elif Rsetor == 'Ferramentaria' or RUsetor == 'Ferramentaria':
                    Local = st.selectbox(local_titulo,(ferramentaria_list),index=None,placeholder= 'Selecione!',help=help_local)
                elif Rsetor == 'Geral' or RUsetor == 'Geral':
                    Local = st.selectbox(local_titulo,(geral_list), placeholder='Selecione!',help=help_local)
    
                if atd1:   
                    uploaded_files = st.file_uploader("Envie uma imagem da ocorrência:", accept_multiple_files=True)
                    for uploaded_file in uploaded_files:
                        bytes_data = uploaded_file.read()
                if not atd1:   
                    uploaded_files = st.file_uploader("Envie imagem foto da ocorrência:", accept_multiple_files=True)
                    for uploaded_file in uploaded_files:
                        bytes_data = uploaded_file.read()
                st.form_submit_button('Inserir')
            
            omaga = [Rniveldaocorrencia,Racao,especialidades,Local,manutentor,textx]
            bools = []
            consulta3 = f"SELECT * FROM PCM"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            numero2 = pmes_leve.shape[0]
            for busca in omaga:
                if not busca:
                    bools.append(True)
                else:
                    bools.append(False)
            if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False:
                if situação == 'Leves':
                    col,col1 = st.columns([1,1])
                    with col:
                        insertx = st.button('Enviar Ocorrência')
                    with col1:
                        logoff = st.button('log-off')
                        if logoff:
                            data = {
                                "senha": "",
                            }
                            file_path = "./Datasets/pcm.json"
                            with open(file_path, "w") as json_file:
                                json.dump(data, json_file, indent=4)
                            log = False
                            st.rerun()

                    if insertx: 
                        cursor14.execute(f"UPDATE {mesx} SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data_m))
                        conn14.commit()
                        pcm_id = numero2 + 1
                        cursor.execute("INSERT INTO PCM (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,LMC,LOCAL,MÊS,Calendario) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pcm_id, 'JAMESON SALES', 'PCM',textx,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,situação,Local,monthnow,data_m))
                        conn.commit()
                
                    consulta3 = f"SELECT * FROM {mesx}"
                    mes_leve = pd.read_sql_query(consulta3, conn14)
                    numero2 = mes_leve.shape[0]
                    consulta3 = f"SELECT * FROM PCM"
                    pmes_leve = pd.read_sql_query(consulta3, conn)
                    numero2 = pmes_leve.shape[0]

            if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False: 
                if situação == 'Moderadas':
                    col,col1 = st.columns([1,1])
                    with col:
                        insertx = st.button('Enviar Ocorrência')
                    with col1:
                        logoff = st.button('log-off')
                        if logoff:
                            data = {
                                "senha": "",
                            }
                            file_path = "./Datasets/pcm.json"
                            with open(file_path, "w") as json_file:
                                json.dump(data, json_file, indent=4)
                            log = False
                            st.rerun()
                    if insertx:
                        cursor14.execute(f"UPDATE {mesx}_WARNING SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data_m))
                        conn14.commit()
                        pcm_id = numero2 + 1
                        cursor.execute("INSERT INTO PCM (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,LMC,LOCAL,MÊS,Calendario) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pcm_id, 'JAMESON SALES', 'PCM',textx,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,situação,Local,monthnow,data_m))
                        conn.commit()

                    consulta3 = f"SELECT * FROM {mesx}_WARNING"
                    mes_warning = pd.read_sql_query(consulta3, conn14)
                    numero2 = mes_warning.shape[0]
                    consulta3 = f"SELECT * FROM PCM"
                    pmes_leve = pd.read_sql_query(consulta3, conn)
                    numero2 = pmes_leve.shape[0]

            if bools[0] == False and bools[1] == False and bools[2] == False and bools[3] == False and bools[4] == False and bools[5] == False:
                if situação == 'Urgêntes':
                    col,col1 = st.columns([1,1])
                    with col:
                        insertx = st.button('Enviar Ocorrência')
                    with col1:
                        logoff = st.button('log-off')
                        if logoff:
                            data = {
                                "senha": "",
                            }
                            file_path = "./Datasets/pcm.json"
                            with open(file_path, "w") as json_file:
                                json.dump(data, json_file, indent=4)
                            log = False
                            st.rerun()

                    if insertx: 
                        cursor14.execute(f"UPDATE {mesx}_ERROR SET OCORRÊNCIA = ? WHERE ID = ?",(textx,data_m))
                        conn14.commit()
                        pcm_id = numero2 + 1
                        cursor.execute("INSERT INTO PCM (OS,SOLICITANTE,SETOR,OCORRENCIA,GRAU,DATA,HORA,AÇÃO,FINALIZADA,DATAF,HORAF,MANUTENTOR,ESPECIALIDADE,LMC,LOCAL,MÊS,Calendario) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pcm_id, 'JAMESON SALES', 'PCM',textx,Rniveldaocorrencia,datenow,str(timenow),Racao,'Não',None,None,manutentor,especialidades,situação,Local,monthnow,data_m))
                        conn.commit()
                    
                    consulta3 = f"SELECT * FROM {mesx}_ERROR"
                    mes_error = pd.read_sql_query(consulta3, conn14)
                    consulta3 = f"SELECT * FROM PCM"
                    pmes_leve = pd.read_sql_query(consulta3, conn)
                    numero2 = pmes_leve.shape[0]
            else:
                logoff = st.button('log-off')
                if logoff:
                    data = {
                        "senha": "",
                    }
                    file_path = "./Datasets/pcm.json"
                    with open(file_path, "w") as json_file:
                        json.dump(data, json_file, indent=4)
                    log = False
                    st.rerun()
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
            color2 = st.color_picker('Situação U','#F90004')
    col,col1,col2,col3,col4,col5,col6= st.columns([1,1,1,1,1,1,1])

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
    
    salesprevx = salesprev(meses) 
    def calendario():
        with col:
            st.write('Segunda')
            container = st.container(border=True)
            container.write(f'{salesprevx[0][0]} de'f' :blue[{meses}]')
           
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            e =  '‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ '
            e1 = '‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ '
            e2 = '‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ '
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')  
                else:
                    st.success(f'')      
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')
            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True )
            container.write(f'{salesprevx[1][0]} de'f' :blue[{meses}]')   
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')      
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')
            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[2][0]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[3][0]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            
            container = st.container(border=True)
            container.write(f'{salesprevx[4][0]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][0]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            
            if meses == 'Dezembro':
                container = st.container(border=True)
                container.write(f'{salesprevx[5][0]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[5][0]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[5][0]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[5][0]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')


            if meses == 'Setembro':
                container = st.container(border=True)
                container.write(f'{salesprevx[5][0]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[5][0]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[5][0]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[5][0]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
        with col1:
            st.write('Terça')
            container = st.container(border=True)
            container.write(f'{salesprevx[0][1]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[1][1]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[2][1]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
            
            container = st.container(border=True)
            container.write(f'{salesprevx[3][1]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
            
            container = st.container(border=True)
            container.write(f'{salesprevx[4][1]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][1]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
        
            if meses == 'Dezembro':
                container = st.container(border=True)
                container.write(f'{salesprevx[5][1]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[5][1]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[5][1]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[5][1]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
        with col2:
            st.write('Quarta')   
            container = st.container(border=True)
            container.write(f'{salesprevx[0][2]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
        
            container = st.container(border=True)
            container.write(f'{salesprevx[1][2]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
            
            container = st.container(border=True)
            container.write(f'{salesprevx[2][2]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[3][2]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
            container = st.container(border=True)
            container.write(f'{salesprevx[4][2]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][2]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
        with col3:
            st.write('Quinta')
            container = st.container(border=True)
            container.write(f'{salesprevx[0][3]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')        
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')
            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[1][3]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[2][3]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[3][3]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][3]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            if not salesprevx[4][3] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[4][3]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][3]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][3]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][3]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
        with col4:
            st.write('Sexta') 
            container = st.container(border=True)
            container.write(f'{salesprevx[0][4]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')
            
            container = st.container(border=True)
            container.write(f'{salesprevx[1][4]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            container = st.container(border=True)
            container.write(f'{salesprevx[2][4]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][4]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            if not salesprevx[3][4] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[3][4]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][4]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][4]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][4]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')

            if meses == 'Feveiro':
                tct = 28
            else:
                if not salesprevx[4][4] == 0:
                    container = st.container(border=True)
                    container.write(f'{salesprevx[4][4]} de'f' :blue[{meses}]')
                    consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][4]} de {meses} de 2024'"
                    pmes_leve = pd.read_sql_query(consulta3, conn)
                    leves_1_shape = pmes_leve.shape[0]
                    leves_1 = pmes_leve['OCORRENCIA']
                    leves_1 = leves_1.tolist()

                    consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][4]} de {meses} de 2024'"
                    pmes_leve = pd.read_sql_query(consulta3, conn)
                    moderadas_1_shape = pmes_leve.shape[0]
                    moderadas_1 = pmes_leve['OCORRENCIA']
                    moderadas_1 = moderadas_1.tolist()

                    consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][4]} de {meses} de 2024'"
                    pmes_leve = pd.read_sql_query(consulta3, conn)
                    urgentes_1_shape = pmes_leve.shape[0]
                    urgentes_1 = pmes_leve['OCORRENCIA']
                    urgentes_1 = urgentes_1.tolist()
                    
                    with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                        if leves_1_shape:
                            for i in range(leves_1_shape):
                                st.success(f'° {leves_1[i]}',icon='✔')
                        else:
                            st.success(f'')
                        
                    with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                        if moderadas_1_shape:
                            for i in range(moderadas_1_shape):
                                st.warning(f'° {moderadas_1[i]}',icon='✔')
                        else:
                            st.warning(f'')

                    with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                        if urgentes_1_shape:
                            for i in range(urgentes_1_shape):
                                st.error(f'° {urgentes_1[i]}',icon='✔')
                        else:
                            st.error(f'')
        with col5:
            st.write('Sabado') 
            container = st.container(border=True)
            container.write(f'{salesprevx[0][5]} de'f' :blue[{meses}]')
            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][5]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            leves_1_shape = pmes_leve.shape[0]
            leves_1 = pmes_leve['OCORRENCIA']
            leves_1 = leves_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][5]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            moderadas_1_shape = pmes_leve.shape[0]
            moderadas_1 = pmes_leve['OCORRENCIA']
            moderadas_1 = moderadas_1.tolist()

            consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][5]} de {meses} de 2024'"
            pmes_leve = pd.read_sql_query(consulta3, conn)
            urgentes_1_shape = pmes_leve.shape[0]
            urgentes_1 = pmes_leve['OCORRENCIA']
            urgentes_1 = urgentes_1.tolist()
            
            with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                if leves_1_shape:
                    for i in range(leves_1_shape):
                        st.success(f'° {leves_1[i]}',icon='✔')
                else:
                    st.success(f'')
                
            with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                if moderadas_1_shape:
                    for i in range(moderadas_1_shape):
                        st.warning(f'° {moderadas_1[i]}',icon='✔')
                else:
                    st.warning(f'')

            with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                if urgentes_1_shape:
                    for i in range(urgentes_1_shape):
                        st.error(f'° {urgentes_1[i]}',icon='✔')
                else:
                    st.error(f'')

            if not salesprevx[1][5] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[1][5]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[2][5] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[2][5]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[3][5] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[3][5]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[4][5] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[4][5]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][5]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
        with col6:
            st.write('Domingo')
            if not salesprevx[0][6] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[0][6]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[0][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[0][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[0][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[1][6] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[1][6]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[1][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[1][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[1][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[2][6] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[2][6]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[2][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[2][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[2][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[3][6] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[3][6]} de 'f' :orange[:blue[{meses}]]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[3][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[3][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[3][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
            if not salesprevx[4][6] == 0:
                container = st.container(border=True)
                container.write(f'{salesprevx[4][6]} de'f' :blue[{meses}]')
                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Leves' AND Calendario = '{salesprevx[4][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                leves_1_shape = pmes_leve.shape[0]
                leves_1 = pmes_leve['OCORRENCIA']
                leves_1 = leves_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Moderadas' AND Calendario = '{salesprevx[4][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                moderadas_1_shape = pmes_leve.shape[0]
                moderadas_1 = pmes_leve['OCORRENCIA']
                moderadas_1 = moderadas_1.tolist()

                consulta3 = f"SELECT * FROM PCM WHERE LMC = 'Urgêntes' AND Calendario = '{salesprevx[4][6]} de {meses} de 2024'"
                pmes_leve = pd.read_sql_query(consulta3, conn)
                urgentes_1_shape = pmes_leve.shape[0]
                urgentes_1 = pmes_leve['OCORRENCIA']
                urgentes_1 = urgentes_1.tolist()
                
                with container.expander(f':green[Leves] {e} {leves_1_shape}'):
                    if leves_1_shape:
                        for i in range(leves_1_shape):
                            st.success(f'° {leves_1[i]}',icon='✔')
                    else:
                        st.success(f'')
                    
                with container.expander(f':orange[Moderadas] {e1}{moderadas_1_shape}'):
                    if moderadas_1_shape:
                        for i in range(moderadas_1_shape):
                            st.warning(f'° {moderadas_1[i]}',icon='✔')
                    else:
                        st.warning(f'')

                with container.expander(f':red[Urgêntes] {e2} {urgentes_1_shape}'):
                    if urgentes_1_shape:
                        for i in range(urgentes_1_shape):
                            st.error(f'° {urgentes_1[i]}',icon='✔')
                    else:
                        st.error(f'')
    calendario()

with tab3:
    st.header('👨‍💻Em construção👨‍💻')
