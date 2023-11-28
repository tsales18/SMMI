import pandas as pd
import numpy as np
import sqlite3
import altair as alt
import streamlit as st
import datetime
from datetime import datetime, timedelta

if 'BANCOS' == 'BANCOS':
    
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
'''   )
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
        HORAF,
        MANUTENTOR
       
                   
    )
''')



    conn5 = sqlite3.connect('PRODUCAO')
    cursor5 = conn5.cursor()
    cursor5.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCAO (
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

    conn6 = sqlite3.connect('ADMINISTRATIVO')
    cursor6 = conn6.cursor()
    cursor6.execute('''
    CREATE TABLE IF NOT EXISTS ADMINISTRATIVO (
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

    conn7 = sqlite3.connect('COMERCIAL')
    cursor7 = conn7.cursor()
    cursor7.execute('''
    CREATE TABLE IF NOT EXISTS COMERCIAL (
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

    conn8 = sqlite3.connect('EXPEDICAO')
    cursor8 = conn8.cursor()
    cursor8.execute('''
    CREATE TABLE IF NOT EXISTS EXPEDICAO (
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

    conn9 = sqlite3.connect('SERRALHARIA')
    cursor9 = conn9.cursor()
    cursor9.execute('''
    CREATE TABLE IF NOT EXISTS SERRALHARIA (
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

col1,col2,col3 = st.columns([4,4,8])
with col1:
    with st.expander('DEFINA'):
        genre = st.radio("Selecione",["SEMANALMENTE","MENSALMENTE"],index=0)
with col2:
    with st.expander('Escolha os graficos'):
        oimaioa = st.radio('Selecione',["O.S de manutenção","Horas de manuteção"])

if genre == 'SEMANALMENTE':
    numero_de_datas = 30
    numero_de_dias = 5
if genre == 'MENSALMENTE':
    numero_de_datas = 30
    numero_de_dias = 30

data_inicial = st.date_input('Escolha a data')
data_inicial1 = str(data_inicial)
banco_de_dados = st.selectbox('Selecione o setor',('GERAL','ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRATIVO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'),index=0)
banco_de_dados1 = str(banco_de_dados)

def gerar_datas_seguidas(data_inicial1,numero_de_datas,banco_de_dados1,numero_de_dias):
    datas_geradas = []
    data_atual = datetime.strptime(data_inicial1, '%Y-%m-%d')  

    for _ in range(numero_de_datas):
        datas_geradas.append(data_atual.strftime('%Y-%m-%d'))  
        data_atual += timedelta(days=1)
    
    if banco_de_dados1 == 'GERAL':
        DB = 'ROSIVALDO' 
        DB1 = 'FERRAMENTARIA'
        DB2 = 'PRODUCAO'
        DB3 = 'ADMINISTRATIVO'
        DB4 = 'COMERCIAL'
        DB5 = 'EXPEDICAO'
        DB6 = 'SERRALHARIA'
        DB7 = 'TI'
        DB8 = 'CESAR'
        DBx = 9
        ######ELÉTRICA######
        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[0]}'"
        numero1 = pd.read_sql_query(consulta3, conn1)
        numero2 = numero1.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[1]}'"
        numero3 = pd.read_sql_query(consulta3, conn1)
        numero4 = numero3.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[2]}'"
        numero5 = pd.read_sql_query(consulta3, conn1)
        numero6 = numero5.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[3]}'"
        numero7 = pd.read_sql_query(consulta3, conn1)
        numero8 = numero7.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[4]}'"
        numero9 = pd.read_sql_query(consulta3, conn1)
        numero10 = numero9.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[5]}'"
        numero11 = pd.read_sql_query(consulta3, conn1)
        numero12 = numero11.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[6]}'"
        numero13 = pd.read_sql_query(consulta3, conn1)
        numero14 = numero13.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[7]}'"
        numero15 = pd.read_sql_query(consulta3, conn1)
        numero16 = numero15.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[8]}'"
        numero17 = pd.read_sql_query(consulta3, conn1)
        numero18 = numero17.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[9]}'"
        numero19 = pd.read_sql_query(consulta3, conn1)
        numero20 = numero19.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[10]}'"
        numero21= pd.read_sql_query(consulta3, conn1)
        numero22 = numero21.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[11]}'"
        numero23 = pd.read_sql_query(consulta3, conn1)
        numero24 = numero23.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[12]}'"
        numero25 = pd.read_sql_query(consulta3, conn1)
        numero26 = numero25.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[13]}'"
        numero27 = pd.read_sql_query(consulta3, conn1)
        numero28 = numero27.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[14]}'"
        numero29 = pd.read_sql_query(consulta3, conn1)
        numero30 = numero29.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[15]}'"
        numero31 = pd.read_sql_query(consulta3, conn1)
        numero32 = numero31.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[16]}'"
        numero33 = pd.read_sql_query(consulta3, conn1)
        numero34 = numero33.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[17]}'"
        numero35 = pd.read_sql_query(consulta3, conn1)
        numero36 = numero35.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[18]}'"
        numero37 = pd.read_sql_query(consulta3, conn1)
        numero38 = numero37.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[19]}'"
        numero39 = pd.read_sql_query(consulta3, conn1)
        numero40 = numero39.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[20]}'"
        numero41 = pd.read_sql_query(consulta3, conn1)
        numero42 = numero41.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[21]}'"
        numero43 = pd.read_sql_query(consulta3, conn1)
        numero44 = numero43.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[22]}'"
        numero45 = pd.read_sql_query(consulta3, conn1)
        numero46 = numero45.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[23]}'"
        numero47 = pd.read_sql_query(consulta3, conn1)
        numero48 = numero47.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[24]}'"
        numero49 = pd.read_sql_query(consulta3, conn1)
        numero50 = numero49.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[25]}'"
        numero51 = pd.read_sql_query(consulta3, conn1)
        numero52 = numero51.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[26]}'"
        numero53 = pd.read_sql_query(consulta3, conn1)
        numero54 = numero53.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[27]}'"
        numero55 = pd.read_sql_query(consulta3, conn1)
        numero56 = numero55.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[28]}'"
        numero57 = pd.read_sql_query(consulta3, conn1)
        numero58 = numero57.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[29]}'"
        numero69 = pd.read_sql_query(consulta3, conn1)
        numero70 = numero69.shape[0]

        elétrica_dataframes = [numero1, numero3, numero5, numero7,numero9,numero11,numero13,numero15,numero17,numero19,numero21,numero23,numero25,numero27,numero29,numero31,numero33,numero35,numero37,numero39,numero41,numero43,numero45,numero47,numero49,numero51,numero53,numero55,numero57,numero69]

        if numero_de_dias == 5:
            OS_semanais_elétrica = numero2 + numero4 + numero6 + numero8 + numero10
        if numero_de_dias == 30:
            OS_semanais_elétrica = numero2+numero4+numero6+numero8+numero10+numero12+numero14+numero16+numero18+numero20+numero22+numero24+numero26+numero28+numero30+numero32+numero34+numero36+numero38+numero40+numero42+numero44+numero46+numero48+numero50+numero52+numero54+numero56+numero58+numero70

        ##############FERRAMENTARIA##########################
        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[0]}'"
        numero71 = pd.read_sql_query(consulta3, conn4)
        numero72 = numero71.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[1]}'"
        numero73 = pd.read_sql_query(consulta3, conn4)
        numero74 = numero73.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[2]}'"
        numero75 = pd.read_sql_query(consulta3, conn4)
        numero76 = numero75.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[3]}'"
        numero77 = pd.read_sql_query(consulta3, conn4)
        numero78 = numero77.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[4]}'"
        numero79 = pd.read_sql_query(consulta3, conn4)
        numero80 = numero79.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[5]}'"
        numero81 = pd.read_sql_query(consulta3, conn4)
        numero82 = numero81.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[6]}'"
        numero83 = pd.read_sql_query(consulta3, conn4)
        numero84 = numero83.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[7]}'"
        numero85 = pd.read_sql_query(consulta3, conn4)
        numero86 = numero85.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[8]}'"
        numero87 = pd.read_sql_query(consulta3, conn4)
        numero88 = numero87.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[9]}'"
        numero89 = pd.read_sql_query(consulta3, conn4)
        numero90 = numero89.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[10]}'"
        numero91= pd.read_sql_query(consulta3, conn4)
        numero92 = numero91.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[11]}'"
        numero93 = pd.read_sql_query(consulta3, conn4)
        numero94 = numero93.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[12]}'"
        numero95 = pd.read_sql_query(consulta3, conn4)
        numero96 = numero95.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[13]}'"
        numero97 = pd.read_sql_query(consulta3, conn4)
        numero98 = numero97.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[14]}'"
        numero99 = pd.read_sql_query(consulta3, conn4)
        numero100 = numero99.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[15]}'"
        numero101 = pd.read_sql_query(consulta3, conn4)
        numero102 = numero101.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[16]}'"
        numero103 = pd.read_sql_query(consulta3, conn4)
        numero104 = numero103.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[17]}'"
        numero105 = pd.read_sql_query(consulta3, conn4)
        numero106 = numero105.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[18]}'"
        numero107 = pd.read_sql_query(consulta3, conn4)
        numero108 = numero107.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[19]}'"
        numero109 = pd.read_sql_query(consulta3, conn4)
        numero110 = numero109.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[20]}'"
        numero111 = pd.read_sql_query(consulta3, conn4)
        numero112 = numero111.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[21]}'"
        numero113 = pd.read_sql_query(consulta3, conn4)
        numero114 = numero113.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[22]}'"
        numero115 = pd.read_sql_query(consulta3, conn4)
        numero116 = numero115.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[23]}'"
        numero117 = pd.read_sql_query(consulta3, conn4)
        numero118 = numero117.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[24]}'"
        numero119 = pd.read_sql_query(consulta3, conn4)
        numero120 = numero119.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[25]}'"
        numero121 = pd.read_sql_query(consulta3, conn4)
        numero122 = numero121.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[26]}'"
        numero123 = pd.read_sql_query(consulta3, conn4)
        numero124 = numero123.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[27]}'"
        numero125 = pd.read_sql_query(consulta3, conn4)
        numero126 = numero125.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[28]}'"
        numero127 = pd.read_sql_query(consulta3, conn4)
        numero128 = numero127.shape[0]

        consulta3 = f"SELECT * FROM {DB1} WHERE DATA = '{datas_geradas[29]}'"
        numero129 = pd.read_sql_query(consulta3, conn4)
        numero130 = numero129.shape[0]
        if numero_de_dias == 5:
            OS_semanais_ferramentaria = numero72 + numero74 + numero76 + numero78 + numero80
        if numero_de_dias == 30:
            OS_semanais_ferramentaria = numero72+numero74+numero76+numero78+numero80+numero82+numero84+numero86+numero88+numero90+numero92+numero94+numero96+numero98+numero90+numero92+numero94+numero96+numero98+numero100+numero102+numero104+numero106+numero108+numero110+numero112+numero114+numero116+numero118+numero120+numero122+numero124+numero126+numero128+numero130
        
        ferramentaria_dataframes = [numero71, numero73, numero75, numero77, numero79, numero81, numero83, numero85, numero87, numero89, numero91, numero93, numero95, numero97, numero99, numero101, numero103, numero105, numero107, numero109, numero111, numero113, numero115, numero117, numero119, numero121, numero123, numero125, numero127, numero129]

        #####PRODUÇÃO#####
        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[0]}'"
        numero131 = pd.read_sql_query(consulta3, conn5)
        numero132 = numero131.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[1]}'"
        numero133 = pd.read_sql_query(consulta3, conn5)
        numero134 = numero133.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[2]}'"
        numero135 = pd.read_sql_query(consulta3, conn5)
        numero136 = numero135.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[3]}'"
        numero137 = pd.read_sql_query(consulta3, conn5)
        numero138 = numero137.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[4]}'"
        numero139 = pd.read_sql_query(consulta3, conn5)
        numero140 = numero139.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[5]}'"
        numero141 = pd.read_sql_query(consulta3, conn5)
        numero142 = numero141.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[6]}'"
        numero143 = pd.read_sql_query(consulta3, conn5)
        numero144 = numero143.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[7]}'"
        numero145 = pd.read_sql_query(consulta3, conn5)
        numero146 = numero145.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[8]}'"
        numero147 = pd.read_sql_query(consulta3, conn5)
        numero148 = numero147.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[9]}'"
        numero149 = pd.read_sql_query(consulta3, conn5)
        numero150 = numero149.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[10]}'"
        numero151= pd.read_sql_query(consulta3, conn5)
        numero152 = numero151.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[11]}'"
        numero153 = pd.read_sql_query(consulta3, conn5)
        numero154 = numero153.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[12]}'"
        numero155 = pd.read_sql_query(consulta3, conn5)
        numero156 = numero155.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[13]}'"
        numero157 = pd.read_sql_query(consulta3, conn5)
        numero158 = numero157.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[14]}'"
        numero159 = pd.read_sql_query(consulta3, conn5)
        numero160 = numero159.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[15]}'"
        numero161 = pd.read_sql_query(consulta3, conn5)
        numero162 = numero161.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[16]}'"
        numero163 = pd.read_sql_query(consulta3, conn5)
        numero164 = numero163.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[17]}'"
        numero165 = pd.read_sql_query(consulta3, conn5)
        numero166 = numero165.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[18]}'"
        numero167 = pd.read_sql_query(consulta3, conn5)
        numero168 = numero167.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[19]}'"
        numero169 = pd.read_sql_query(consulta3, conn5)
        numero170 = numero169.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[20]}'"
        numero171 = pd.read_sql_query(consulta3, conn5)
        numero172 = numero171.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[21]}'"
        numero173 = pd.read_sql_query(consulta3, conn5)
        numero174 = numero173.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[22]}'"
        numero175 = pd.read_sql_query(consulta3, conn5)
        numero176 = numero175.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[23]}'"
        numero177 = pd.read_sql_query(consulta3, conn5)
        numero178 = numero177.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[24]}'"
        numero179 = pd.read_sql_query(consulta3, conn5)
        numero180 = numero179.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[25]}'"
        numero181 = pd.read_sql_query(consulta3, conn5)
        numero182 = numero181.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[26]}'"
        numero183 = pd.read_sql_query(consulta3, conn5)
        numero184 = numero183.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[27]}'"
        numero185 = pd.read_sql_query(consulta3, conn5)
        numero186 = numero185.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[28]}'"
        numero187 = pd.read_sql_query(consulta3, conn5)
        numero188 = numero187.shape[0]

        consulta3 = f"SELECT * FROM {DB2} WHERE DATA = '{datas_geradas[29]}'"
        numero189 = pd.read_sql_query(consulta3, conn5)
        numero190 = numero189.shape[0]
        if numero_de_dias == 5:
            OS_semanais_produção = numero132 + numero134+ numero136 + numero138 + numero140
        if numero_de_dias == 30:
            OS_semanais_produção = numero132+numero134+numero136+numero138+numero140+numero142+numero144+numero146+numero148+numero150+numero152+numero154+numero156+numero158+numero160+numero162+numero164+numero166+numero168+numero170+numero172+numero174+numero176+numero178+numero180+numero182+numero184+numero186+numero188+numero190
        
        produção_dataframes = [numero131, numero133, numero135, numero137, numero139, numero141, numero143, numero145, numero147, numero149, numero151, numero153, numero155, numero157, numero159, numero161, numero163, numero165, numero167, numero169, numero171, numero173, numero175, numero177, numero179, numero181, numero183, numero185, numero187, numero189]

        #######ADMINISTRATIVO##############
        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[0]}'"
        numero191 = pd.read_sql_query(consulta3, conn6)
        numero192 = numero191.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[1]}'"
        numero193 = pd.read_sql_query(consulta3, conn6)
        numero194 = numero193.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[2]}'"
        numero195 = pd.read_sql_query(consulta3, conn6)
        numero196 = numero195.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[3]}'"
        numero197 = pd.read_sql_query(consulta3, conn6)
        numero198 = numero197.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[4]}'"
        numero199 = pd.read_sql_query(consulta3, conn6)
        numero200 = numero199.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[5]}'"
        numero201 = pd.read_sql_query(consulta3, conn6)
        numero202 = numero201.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[6]}'"
        numero203 = pd.read_sql_query(consulta3, conn6)
        numero204 = numero203.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[7]}'"
        numero205 = pd.read_sql_query(consulta3, conn6)
        numero206 = numero205.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[8]}'"
        numero207 = pd.read_sql_query(consulta3, conn6)
        numero208 = numero207.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[9]}'"
        numero209 = pd.read_sql_query(consulta3, conn6)
        numero210 = numero209.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[10]}'"
        numero211= pd.read_sql_query(consulta3, conn6)
        numero212 = numero211.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[11]}'"
        numero213 = pd.read_sql_query(consulta3, conn6)
        numero214 = numero213.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[12]}'"
        numero215 = pd.read_sql_query(consulta3, conn6)
        numero216 = numero215.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[13]}'"
        numero217 = pd.read_sql_query(consulta3, conn6)
        numero218 = numero217.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[14]}'"
        numero219 = pd.read_sql_query(consulta3, conn6)
        numero220 = numero219.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[15]}'"
        numero221 = pd.read_sql_query(consulta3, conn6)
        numero222 = numero221.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[16]}'"
        numero223 = pd.read_sql_query(consulta3, conn6)
        numero224 = numero223.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[17]}'"
        numero225 = pd.read_sql_query(consulta3, conn6)
        numero226 = numero225.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[18]}'"
        numero227 = pd.read_sql_query(consulta3, conn6)
        numero228 = numero227.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[19]}'"
        numero229 = pd.read_sql_query(consulta3, conn6)
        numero230 = numero229.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[20]}'"
        numero231 = pd.read_sql_query(consulta3, conn6)
        numero232 = numero231.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[21]}'"
        numero233 = pd.read_sql_query(consulta3, conn6)
        numero234 = numero233.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[22]}'"
        numero235 = pd.read_sql_query(consulta3, conn6)
        numero236 = numero235.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[23]}'"
        numero237 = pd.read_sql_query(consulta3, conn6)
        numero238 = numero237.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[24]}'"
        numero239 = pd.read_sql_query(consulta3, conn6)
        numero240 = numero239.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[25]}'"
        numero241 = pd.read_sql_query(consulta3, conn6)
        numero242 = numero241.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[26]}'"
        numero243 = pd.read_sql_query(consulta3, conn6)
        numero244 = numero243.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[27]}'"
        numero245 = pd.read_sql_query(consulta3, conn6)
        numero246 = numero245.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[28]}'"
        numero247 = pd.read_sql_query(consulta3, conn6)
        numero248 = numero247.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[29]}'"
        numero249 = pd.read_sql_query(consulta3, conn6)
        numero250 = numero249.shape[0]
        if numero_de_dias == 5:
            OS_semanais_administraivo = numero192 + numero194 + numero196 + numero198 + numero200
        if numero_de_dias == 30:
            OS_semanais_administraivo = numero192+numero194+numero196+numero198+numero200+numero202+numero204+numero206+numero208+numero210+numero212+numero214+numero216+numero218+numero220+numero222+numero224+numero226+numero228+numero230+numero232+numero234+numero236+numero238+numero240+numero242+numero244+numero246+numero248+numero250
        
        administrativo_dataframes= [numero191, numero193, numero195, numero197, numero199, numero201, numero203, numero205, numero207, numero209, numero211, numero213, numero215, numero217, numero219, numero221, numero223, numero225, numero227, numero229, numero231, numero233, numero235, numero237, numero239, numero241, numero243, numero245, numero247, numero249]


        #########COMERCIAL############
        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[0]}'"
        numero251 = pd.read_sql_query(consulta3, conn7)
        numero252 = numero251.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[1]}'"
        numero253 = pd.read_sql_query(consulta3, conn7)
        numero254 = numero253.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[2]}'"
        numero255 = pd.read_sql_query(consulta3, conn7)
        numero256 = numero255.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[3]}'"
        numero257 = pd.read_sql_query(consulta3, conn7)
        numero258 = numero257.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[4]}'"
        numero259 = pd.read_sql_query(consulta3, conn7)
        numero260 = numero259.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[5]}'"
        numero261 = pd.read_sql_query(consulta3, conn7)
        numero262 = numero261.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[6]}'"
        numero263 = pd.read_sql_query(consulta3, conn7)
        numero264 = numero263.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[7]}'"
        numero265 = pd.read_sql_query(consulta3, conn7)
        numero266 = numero265.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[8]}'"
        numero267 = pd.read_sql_query(consulta3, conn7)
        numero268 = numero267.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[9]}'"
        numero269 = pd.read_sql_query(consulta3, conn7)
        numero270 = numero269.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[10]}'"
        numero271= pd.read_sql_query(consulta3, conn7)
        numero272 = numero271.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[11]}'"
        numero273 = pd.read_sql_query(consulta3, conn7)
        numero274 = numero273.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[12]}'"
        numero275 = pd.read_sql_query(consulta3, conn7)
        numero276 = numero275.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[13]}'"
        numero277 = pd.read_sql_query(consulta3, conn7)
        numero278 = numero277.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[14]}'"
        numero279 = pd.read_sql_query(consulta3, conn7)
        numero280 = numero279.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[15]}'"
        numero281 = pd.read_sql_query(consulta3, conn7)
        numero282 = numero281.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[16]}'"
        numero283 = pd.read_sql_query(consulta3, conn7)
        numero284 = numero283.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[17]}'"
        numero285 = pd.read_sql_query(consulta3, conn7)
        numero286 = numero285.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[18]}'"
        numero287 = pd.read_sql_query(consulta3, conn7)
        numero288 = numero287.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[19]}'"
        numero289 = pd.read_sql_query(consulta3, conn7)
        numero290 = numero289.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[20]}'"
        numero291 = pd.read_sql_query(consulta3, conn7)
        numero292 = numero291.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[21]}'"
        numero293 = pd.read_sql_query(consulta3, conn7)
        numero294 = numero293.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[22]}'"
        numero295 = pd.read_sql_query(consulta3, conn7)
        numero296 = numero295.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[23]}'"
        numero297 = pd.read_sql_query(consulta3, conn7)
        numero298 = numero297.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[24]}'"
        numero299 = pd.read_sql_query(consulta3, conn7)
        numero300 = numero299.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[25]}'"
        numero301 = pd.read_sql_query(consulta3, conn7)
        numero302 = numero301.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[26]}'"
        numero303 = pd.read_sql_query(consulta3, conn7)
        numero304 = numero303.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[27]}'"
        numero305 = pd.read_sql_query(consulta3, conn7)
        numero306 = numero305.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[28]}'"
        numero307 = pd.read_sql_query(consulta3, conn7)
        numero308 = numero307.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[29]}'"
        numero309 = pd.read_sql_query(consulta3, conn7)
        numero310 = numero309.shape[0]
        if numero_de_dias == 5:
            OS_semanais_comercial = numero252 + numero254 + numero256 + numero258 + numero260
        if numero_de_dias == 30:
            OS_semanais_comercial = numero252+numero254+numero256+numero258+numero260+numero262+numero264+numero266+numero268+numero270+numero272+numero274+numero276+numero278+numero280+numero282+numero284+numero286+numero288+numero290+numero292+numero294+numero296+numero298+numero300+numero302+numero304+numero306+numero308+numero310
        
        comercial_dataframes =[numero251, numero253, numero255, numero257, numero259, numero261, numero263, numero265, numero267, numero269, numero271, numero273, numero275, numero277, numero279, numero281, numero283, numero285, numero287, numero289, numero291, numero293, numero295, numero297, numero299, numero301, numero303, numero305, numero307, numero309]

        ###########EXPEDIÇÃO############
        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[0]}'"
        numero311 = pd.read_sql_query(consulta3, conn8)
        numero312 = numero311.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[1]}'"
        numero313 = pd.read_sql_query(consulta3, conn8)
        numero314 = numero313.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[2]}'"
        numero315 = pd.read_sql_query(consulta3, conn8)
        numero316 = numero315.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[3]}'"
        numero317 = pd.read_sql_query(consulta3, conn8)
        numero318 = numero317.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[4]}'"
        numero319 = pd.read_sql_query(consulta3, conn8)
        numero320 = numero319.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[5]}'"
        numero321 = pd.read_sql_query(consulta3, conn8)
        numero322 = numero321.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[6]}'"
        numero323 = pd.read_sql_query(consulta3, conn8)
        numero324 = numero323.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[7]}'"
        numero325 = pd.read_sql_query(consulta3, conn8)
        numero326 = numero325.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[8]}'"
        numero327 = pd.read_sql_query(consulta3, conn8)
        numero328 = numero327.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[9]}'"
        numero329 = pd.read_sql_query(consulta3, conn8)
        numero330 = numero329.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[10]}'"
        numero331 = pd.read_sql_query(consulta3, conn8)
        numero332 = numero331.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[11]}'"
        numero333 = pd.read_sql_query(consulta3, conn8)
        numero334 = numero333.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[12]}'"
        numero335 = pd.read_sql_query(consulta3, conn8)
        numero336 = numero335.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[13]}'"
        numero337 = pd.read_sql_query(consulta3, conn8)
        numero338 = numero337.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[14]}'"
        numero339 = pd.read_sql_query(consulta3, conn8)
        numero340 = numero339.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[15]}'"
        numero341 = pd.read_sql_query(consulta3, conn8)
        numero342 = numero341.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[16]}'"
        numero343 = pd.read_sql_query(consulta3, conn8)
        numero344 = numero343.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[17]}'"
        numero345 = pd.read_sql_query(consulta3, conn8)
        numero346 = numero345.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[18]}'"
        numero347 = pd.read_sql_query(consulta3, conn8)
        numero348 = numero347.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[19]}'"
        numero349 = pd.read_sql_query(consulta3, conn8)
        numero350 = numero349.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[20]}'"
        numero351 = pd.read_sql_query(consulta3, conn8)
        numero352 = numero351.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[21]}'"
        numero353 = pd.read_sql_query(consulta3, conn8)
        numero354 = numero353.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[22]}'"
        numero355 = pd.read_sql_query(consulta3, conn8)
        numero356 = numero355.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[23]}'"
        numero357 = pd.read_sql_query(consulta3, conn8)
        numero358 = numero357.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[24]}'"
        numero359 = pd.read_sql_query(consulta3, conn8)
        numero360 = numero359.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[25]}'"
        numero361 = pd.read_sql_query(consulta3, conn8)
        numero362 = numero361.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[26]}'"
        numero363 = pd.read_sql_query(consulta3, conn8)
        numero364 = numero363.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[27]}'"
        numero365 = pd.read_sql_query(consulta3, conn8)
        numero366 = numero365.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[28]}'"
        numero367 = pd.read_sql_query(consulta3, conn8)
        numero368 = numero367.shape[0]

        consulta3 = f"SELECT * FROM {DB5} WHERE DATA = '{datas_geradas[29]}'"
        numero369 = pd.read_sql_query(consulta3, conn8)
        numero370 = numero369.shape[0]
        if numero_de_dias == 5:
            OS_semanais_expedição = numero312 + numero314 + numero316 + numero318 + numero320
        if numero_de_dias == 30:
            OS_semanais_expedição = numero312+numero314+numero316+numero318+numero320+numero322+numero324+numero326+numero328+numero330+numero332+numero334+numero336+numero338+numero340+numero342+numero344+numero346+numero348+numero350+numero352+numero354+numero356+numero358+numero360+numero362+numero364+numero366+numero368+numero370 
        
        expedição_dataframes = [numero311, numero313, numero315, numero317, numero319, numero321, numero323, numero325, numero327, numero329, numero331, numero333, numero335, numero337, numero339, numero341, numero343, numero345, numero347, numero349, numero351, numero353, numero355, numero357, numero359, numero361, numero363, numero365, numero367, numero369]


        ##########SERRALHARIA###########
        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[0]}'"
        numero371 = pd.read_sql_query(consulta3, conn9)
        numero372 = numero371.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[1]}'"
        numero373 = pd.read_sql_query(consulta3, conn9)
        numero374 = numero373.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[2]}'"
        numero375 = pd.read_sql_query(consulta3, conn9)
        numero376 = numero375.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[3]}'"
        numero377 = pd.read_sql_query(consulta3, conn9)
        numero378 = numero377.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[4]}'"
        numero379 = pd.read_sql_query(consulta3, conn9)
        numero380 = numero379.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[5]}'"
        numero381 = pd.read_sql_query(consulta3, conn9)
        numero382 = numero381.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[6]}'"
        numero383 = pd.read_sql_query(consulta3, conn9)
        numero384 = numero383.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[7]}'"
        numero385 = pd.read_sql_query(consulta3, conn9)
        numero386 = numero385.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[8]}'"
        numero387 = pd.read_sql_query(consulta3, conn9)
        numero388 = numero387.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[9]}'"
        numero389 = pd.read_sql_query(consulta3, conn9)
        numero390 = numero389.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[10]}'"
        numero391 = pd.read_sql_query(consulta3, conn9)
        numero392 = numero391.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[11]}'"
        numero393 = pd.read_sql_query(consulta3, conn9)
        numero394 = numero393.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[12]}'"
        numero395 = pd.read_sql_query(consulta3, conn9)
        numero396 = numero395.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[13]}'"
        numero397 = pd.read_sql_query(consulta3, conn9)
        numero398 = numero397.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[14]}'"
        numero399 = pd.read_sql_query(consulta3, conn9)
        numero400 = numero399.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[15]}'"
        numero401 = pd.read_sql_query(consulta3, conn9)
        numero402 = numero401.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[16]}'"
        numero403 = pd.read_sql_query(consulta3, conn9)
        numero404 = numero403.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[17]}'"
        numero405 = pd.read_sql_query(consulta3, conn9)
        numero406 = numero405.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[18]}'"
        numero407 = pd.read_sql_query(consulta3, conn9)
        numero408 = numero407.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[19]}'"
        numero409 = pd.read_sql_query(consulta3, conn9)
        numero410 = numero409.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[20]}'"
        numero411 = pd.read_sql_query(consulta3, conn9)
        numero412 = numero411.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[21]}'"
        numero413 = pd.read_sql_query(consulta3, conn9)
        numero414 = numero413.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[22]}'"
        numero415 = pd.read_sql_query(consulta3, conn9)
        numero416 = numero415.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[23]}'"
        numero417 = pd.read_sql_query(consulta3, conn9)
        numero418 = numero417.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[24]}'"
        numero419 = pd.read_sql_query(consulta3, conn9)
        numero420 = numero419.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[25]}'"
        numero421 = pd.read_sql_query(consulta3, conn9)
        numero422 = numero421.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[26]}'"
        numero423 = pd.read_sql_query(consulta3, conn9)
        numero424 = numero423.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[27]}'"
        numero425 = pd.read_sql_query(consulta3, conn9)
        numero426 = numero425.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[28]}'"
        numero427 = pd.read_sql_query(consulta3, conn9)
        numero428 = numero427.shape[0]

        consulta3 = f"SELECT * FROM {DB6} WHERE DATA = '{datas_geradas[29]}'"
        numero429 = pd.read_sql_query(consulta3, conn9)
        numero430 = numero429.shape[0]
        if numero_de_dias == 5:
            OS_semanais_serralharia = numero312 + numero314 + numero316 + numero318 + numero320
        if numero_de_dias == 30:
            OS_semanais_serralharia = numero372+numero374+numero376+numero378+numero380+numero382+numero384+numero386+numero388+numero390+numero392+numero394+numero396+numero398+numero400+numero402+numero404+numero406+numero408+numero410+numero412+numero414+numero416+numero418+numero420+numero422+numero424+numero426+numero428+numero430
        
        serralharia_dataframes  = [numero371, numero373, numero375, numero377, numero379, numero381, numero383, numero385, numero387, numero389, numero391, numero393, numero395, numero397, numero399, numero401, numero403, numero405, numero407, numero409, numero411, numero413, numero415, numero417, numero419, numero421, numero423, numero425, numero427, numero429]


        ########TI########
        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[0]}'"
        numero431 = pd.read_sql_query(consulta3, conn11)
        numero432 = numero431.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[1]}'"
        numero433 = pd.read_sql_query(consulta3, conn11)
        numero434 = numero433.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[2]}'"
        numero435 = pd.read_sql_query(consulta3, conn11)
        numero436 = numero435.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[3]}'"
        numero437 = pd.read_sql_query(consulta3, conn11)
        numero438 = numero437.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[4]}'"
        numero439 = pd.read_sql_query(consulta3, conn11)
        numero440 = numero439.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[5]}'"
        numero441 = pd.read_sql_query(consulta3, conn11)
        numero442 = numero441.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[6]}'"
        numero443 = pd.read_sql_query(consulta3, conn11)
        numero444 = numero443.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[7]}'"
        numero445 = pd.read_sql_query(consulta3, conn11)
        numero446 = numero445.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[8]}'"
        numero447 = pd.read_sql_query(consulta3, conn11)
        numero448 = numero447.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[9]}'"
        numero449 = pd.read_sql_query(consulta3, conn11)
        numero450 = numero449.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[10]}'"
        numero451 = pd.read_sql_query(consulta3, conn11)
        numero452 = numero451.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[11]}'"
        numero453 = pd.read_sql_query(consulta3, conn11)
        numero454 = numero453.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[12]}'"
        numero455 = pd.read_sql_query(consulta3, conn11)
        numero456 = numero455.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[13]}'"
        numero457 = pd.read_sql_query(consulta3, conn11)
        numero458 = numero457.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[14]}'"
        numero459 = pd.read_sql_query(consulta3, conn11)
        numero460 = numero459.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[15]}'"
        numero461 = pd.read_sql_query(consulta3, conn11)
        numero462 = numero461.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[16]}'"
        numero463 = pd.read_sql_query(consulta3, conn11)
        numero464 = numero463.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[17]}'"
        numero465 = pd.read_sql_query(consulta3, conn11)
        numero466 = numero465.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[18]}'"
        numero467 = pd.read_sql_query(consulta3, conn11)
        numero468 = numero467.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[19]}'"
        numero469 = pd.read_sql_query(consulta3, conn11)
        numero470 = numero469.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[20]}'"
        numero471 = pd.read_sql_query(consulta3, conn11)
        numero472 = numero471.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[21]}'"
        numero473 = pd.read_sql_query(consulta3, conn11)
        numero474 = numero473.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[22]}'"
        numero475 = pd.read_sql_query(consulta3, conn11)
        numero476 = numero475.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[23]}'"
        numero477 = pd.read_sql_query(consulta3, conn11)
        numero478 = numero477.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[24]}'"
        numero479 = pd.read_sql_query(consulta3, conn11)
        numero480 = numero479.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[25]}'"
        numero481 = pd.read_sql_query(consulta3, conn11)
        numero482 = numero481.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[26]}'"
        numero483 = pd.read_sql_query(consulta3, conn11)
        numero484 = numero483.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[27]}'"
        numero485 = pd.read_sql_query(consulta3, conn11)
        numero486 = numero485.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[28]}'"
        numero487 = pd.read_sql_query(consulta3, conn11)
        numero488 = numero487.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[29]}'"
        numero489 = pd.read_sql_query(consulta3, conn11)
        numero490 = numero489.shape[0]
        if numero_de_dias == 5:
            OS_semanais_TI = numero432 + numero434 + numero436 + numero438 + numero440
        if numero_de_dias == 30:
            OS_semanais_TI = numero432+numero434+numero436+numero438+numero440+numero442+numero444+numero446+numero448+numero450+numero452+numero454+numero456+numero458+numero460+numero462+numero464+numero466+numero468+numero470+numero472+numero474+numero476+numero478+numero480+numero482+numero484+numero486+numero488+numero490

        ti_dataframes = [numero431, numero433, numero435, numero437, numero439, numero441, numero443, numero445, numero447, numero449, numero451, numero453, numero455, numero457, numero459, numero461, numero463, numero465, numero467, numero469, numero471, numero473, numero475, numero477, numero479, numero481, numero483, numero485, numero487, numero489]


        ############MECÂNICA###############
        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[0]}'"
        numero491 = pd.read_sql_query(consulta3, conn10)
        numero492 = numero491.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[1]}'"
        numero493 = pd.read_sql_query(consulta3, conn10)
        numero494 = numero493.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[2]}'"
        numero495 = pd.read_sql_query(consulta3, conn10)
        numero496 = numero495.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[3]}'"
        numero497 = pd.read_sql_query(consulta3, conn10)
        numero498 = numero497.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[4]}'"
        numero499 = pd.read_sql_query(consulta3, conn10)
        numero500 = numero499.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[5]}'"
        numero501 = pd.read_sql_query(consulta3, conn10)
        numero502 = numero501.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[6]}'"
        numero503 = pd.read_sql_query(consulta3, conn10)
        numero504 = numero503.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[7]}'"
        numero505 = pd.read_sql_query(consulta3, conn10)
        numero506 = numero505.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[8]}'"
        numero507 = pd.read_sql_query(consulta3, conn10)
        numero508 = numero507.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[9]}'"
        numero509 = pd.read_sql_query(consulta3, conn10)
        numero510 = numero509.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[10]}'"
        numero511 = pd.read_sql_query(consulta3, conn10)
        numero512 = numero511.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[11]}'"
        numero513 = pd.read_sql_query(consulta3, conn10)
        numero514 = numero513.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[12]}'"
        numero515 = pd.read_sql_query(consulta3, conn10)
        numero516 = numero515.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[13]}'"
        numero517 = pd.read_sql_query(consulta3, conn10)
        numero518 = numero517.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[14]}'"
        numero519 = pd.read_sql_query(consulta3, conn10)
        numero520 = numero519.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[15]}'"
        numero521 = pd.read_sql_query(consulta3, conn10)
        numero522 = numero521.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[16]}'"
        numero523 = pd.read_sql_query(consulta3, conn10)
        numero524 = numero523.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[17]}'"
        numero525 = pd.read_sql_query(consulta3, conn10)
        numero526 = numero525.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[18]}'"
        numero527 = pd.read_sql_query(consulta3, conn10)
        numero528 = numero527.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[19]}'"
        numero529 = pd.read_sql_query(consulta3, conn10)
        numero530 = numero529.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[20]}'"
        numero531 = pd.read_sql_query(consulta3, conn10)
        numero532 = numero531.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[21]}'"
        numero533 = pd.read_sql_query(consulta3, conn10)
        numero534 = numero533.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[22]}'"
        numero535 = pd.read_sql_query(consulta3, conn10)
        numero536 = numero535.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[23]}'"
        numero537 = pd.read_sql_query(consulta3, conn10)
        numero538 = numero537.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[24]}'"
        numero539 = pd.read_sql_query(consulta3, conn10)
        numero540 = numero539.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[25]}'"
        numero541 = pd.read_sql_query(consulta3, conn10)
        numero542 = numero541.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[26]}'"
        numero543 = pd.read_sql_query(consulta3, conn10)
        numero544 = numero543.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[27]}'"
        numero545 = pd.read_sql_query(consulta3, conn10)
        numero546 = numero545.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[28]}'"
        numero547 = pd.read_sql_query(consulta3, conn10)
        numero548 = numero547.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[29]}'"
        numero549 = pd.read_sql_query(consulta3, conn10)
        numero550 = numero549.shape[0]

        if numero_de_dias == 5:
            OS_semanais_mecânica = numero492 + numero494 + numero496 + numero498 + numero500
        if numero_de_dias == 30:
            OS_semanais_mecânica = numero492+numero494+numero496+numero498+numero500+numero502+numero504+numero506+numero508+numero510+numero512+numero514+numero516+numero518+numero520+numero522+numero524+numero526+numero528+numero530+numero532+numero534+numero536+numero538+numero540+numero542+numero544+numero546+numero548+numero550

        mecânica_dataframes = [numero431, numero433, numero435, numero437, numero439, numero441, numero443, numero445, numero447, numero449, numero451, numero453, numero455, numero457, numero459, numero461, numero463, numero465, numero467, numero469, numero471, numero473, numero475, numero477, numero479, numero481, numero483, numero485, numero487, numero489]

        OS_totais = OS_semanais_administraivo + OS_semanais_comercial + OS_semanais_elétrica + OS_semanais_expedição + OS_semanais_ferramentaria + OS_semanais_produção + OS_semanais_serralharia + OS_semanais_TI
    
    if banco_de_dados1 == 'ELÉTRICA':
        DB = 'ROSIVALDO'
        DBx = 1
        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[0]}'"
        numero1 = pd.read_sql_query(consulta3, conn10)
        numero2 = numero1.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[1]}'"
        numero3 = pd.read_sql_query(consulta3, conn10)
        numero4 = numero3.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[2]}'"
        numero5 = pd.read_sql_query(consulta3, conn10)
        numero6 = numero5.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[3]}'"
        numero7 = pd.read_sql_query(consulta3, conn10)
        numero8 = numero7.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[4]}'"
        numero9 = pd.read_sql_query(consulta3, conn10)
        numero10 = numero9.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[5]}'"
        numero11 = pd.read_sql_query(consulta3, conn10)
        numero12 = numero11.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[6]}'"
        numero13 = pd.read_sql_query(consulta3, conn10)
        numero14 = numero13.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[7]}'"
        numero15 = pd.read_sql_query(consulta3, conn10)
        numero16 = numero15.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[8]}'"
        numero17 = pd.read_sql_query(consulta3, conn10)
        numero18 = numero17.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[9]}'"
        numero19 = pd.read_sql_query(consulta3, conn10)
        numero20 = numero19.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[10]}'"
        numero21= pd.read_sql_query(consulta3, conn10)
        numero22 = numero21.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[11]}'"
        numero23 = pd.read_sql_query(consulta3, conn10)
        numero24 = numero23.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[12]}'"
        numero25 = pd.read_sql_query(consulta3, conn10)
        numero26 = numero25.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[13]}'"
        numero27 = pd.read_sql_query(consulta3, conn10)
        numero28 = numero27.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[14]}'"
        numero29 = pd.read_sql_query(consulta3, conn10)
        numero30 = numero29.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[15]}'"
        numero31 = pd.read_sql_query(consulta3, conn10)
        numero32 = numero31.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[16]}'"
        numero33 = pd.read_sql_query(consulta3, conn10)
        numero34 = numero33.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[17]}'"
        numero35 = pd.read_sql_query(consulta3, conn10)
        numero36 = numero35.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[18]}'"
        numero37 = pd.read_sql_query(consulta3, conn10)
        numero38 = numero37.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[19]}'"
        numero39 = pd.read_sql_query(consulta3, conn10)
        numero40 = numero39.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[20]}'"
        numero41 = pd.read_sql_query(consulta3, conn10)
        numero42 = numero41.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[21]}'"
        numero43 = pd.read_sql_query(consulta3, conn10)
        numero44 = numero43.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[22]}'"
        numero45 = pd.read_sql_query(consulta3, conn10)
        numero46 = numero45.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[23]}'"
        numero47 = pd.read_sql_query(consulta3, conn10)
        numero48 = numero47.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[24]}'"
        numero49 = pd.read_sql_query(consulta3, conn10)
        numero50 = numero49.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[25]}'"
        numero51 = pd.read_sql_query(consulta3, conn10)
        numero52 = numero51.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[26]}'"
        numero53 = pd.read_sql_query(consulta3, conn10)
        numero54 = numero53.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[27]}'"
        numero55 = pd.read_sql_query(consulta3, conn10)
        numero56 = numero55.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[28]}'"
        numero57 = pd.read_sql_query(consulta3, conn10)
        numero58 = numero57.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[29]}'"
        numero69 = pd.read_sql_query(consulta3, conn10)
        numero70 = numero69.shape[0]

        OS_semanais_elétrica = numero2 + numero4 + numero6 + numero8 + numero10
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_administraivo =  0
        OS_semanais_comercial = 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_semanais_TI = 0
        OS_totais = 0

    if banco_de_dados == 'FERRAMENTARIA':
        DB = 'FERRAMENTARIA'
        DBx = 2
        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[0]}'"
        numero71 = pd.read_sql_query(consulta3, conn4)
        numero72 = numero71.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[1]}'"
        numero73 = pd.read_sql_query(consulta3, conn4)
        numero74 = numero73.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[2]}'"
        numero75 = pd.read_sql_query(consulta3, conn4)
        numero76 = numero75.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[3]}'"
        numero77 = pd.read_sql_query(consulta3, conn4)
        numero78 = numero77.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[4]}'"
        numero79 = pd.read_sql_query(consulta3, conn4)
        numero80 = numero79.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[5]}'"
        numero81 = pd.read_sql_query(consulta3, conn4)
        numero82 = numero81.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[6]}'"
        numero83 = pd.read_sql_query(consulta3, conn4)
        numero84 = numero83.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[7]}'"
        numero85 = pd.read_sql_query(consulta3, conn4)
        numero86 = numero85.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[8]}'"
        numero87 = pd.read_sql_query(consulta3, conn4)
        numero88 = numero87.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[9]}'"
        numero89 = pd.read_sql_query(consulta3, conn4)
        numero90 = numero89.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[10]}'"
        numero91= pd.read_sql_query(consulta3, conn4)
        numero92 = numero91.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[11]}'"
        numero93 = pd.read_sql_query(consulta3, conn4)
        numero94 = numero93.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[12]}'"
        numero95 = pd.read_sql_query(consulta3, conn4)
        numero96 = numero95.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[13]}'"
        numero97 = pd.read_sql_query(consulta3, conn4)
        numero98 = numero97.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[14]}'"
        numero99 = pd.read_sql_query(consulta3, conn4)
        numero100 = numero99.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[15]}'"
        numero101 = pd.read_sql_query(consulta3, conn4)
        numero102 = numero101.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[16]}'"
        numero103 = pd.read_sql_query(consulta3, conn4)
        numero104 = numero103.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[17]}'"
        numero105 = pd.read_sql_query(consulta3, conn4)
        numero106 = numero105.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[18]}'"
        numero107 = pd.read_sql_query(consulta3, conn4)
        numero108 = numero107.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[19]}'"
        numero109 = pd.read_sql_query(consulta3, conn4)
        numero110 = numero109.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[20]}'"
        numero111 = pd.read_sql_query(consulta3, conn4)
        numero112 = numero111.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[21]}'"
        numero113 = pd.read_sql_query(consulta3, conn4)
        numero114 = numero113.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[22]}'"
        numero115 = pd.read_sql_query(consulta3, conn4)
        numero116 = numero115.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[23]}'"
        numero117 = pd.read_sql_query(consulta3, conn4)
        numero118 = numero117.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[24]}'"
        numero119 = pd.read_sql_query(consulta3, conn4)
        numero120 = numero119.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[25]}'"
        numero121 = pd.read_sql_query(consulta3, conn4)
        numero122 = numero121.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[26]}'"
        numero123 = pd.read_sql_query(consulta3, conn4)
        numero124 = numero123.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[27]}'"
        numero125 = pd.read_sql_query(consulta3, conn4)
        numero126 = numero125.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[28]}'"
        numero127 = pd.read_sql_query(consulta3, conn4)
        numero128 = numero127.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[29]}'"
        numero129 = pd.read_sql_query(consulta3, conn4)
        numero130 = numero129.shape[0]

        OS_semanais_ferramentaria = numero22 + numero24 + numero26 + numero28 + numero30
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_administraivo =  0
        OS_semanais_comercial = 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_semanais_TI = 0
        OS_totais = 0
        OS_semanais_produção = 0

    if banco_de_dados == 'PRODUÇÃO':
        DB = 'PRODUCAO'
        DBx = 3
        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[0]}'"
        numero131 = pd.read_sql_query(consulta3, conn5)
        numero132 = numero131.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[1]}'"
        numero133 = pd.read_sql_query(consulta3, conn5)
        numero134 = numero133.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[2]}'"
        numero135 = pd.read_sql_query(consulta3, conn5)
        numero136 = numero135.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[3]}'"
        numero137 = pd.read_sql_query(consulta3, conn5)
        numero138 = numero137.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[4]}'"
        numero139 = pd.read_sql_query(consulta3, conn5)
        numero140 = numero139.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[5]}'"
        numero141 = pd.read_sql_query(consulta3, conn5)
        numero142 = numero141.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[6]}'"
        numero143 = pd.read_sql_query(consulta3, conn5)
        numero144 = numero143.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[7]}'"
        numero145 = pd.read_sql_query(consulta3, conn5)
        numero146 = numero145.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[8]}'"
        numero147 = pd.read_sql_query(consulta3, conn5)
        numero148 = numero147.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[9]}'"
        numero149 = pd.read_sql_query(consulta3, conn5)
        numero150 = numero149.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[10]}'"
        numero151= pd.read_sql_query(consulta3, conn5)
        numero152 = numero151.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[11]}'"
        numero153 = pd.read_sql_query(consulta3, conn5)
        numero154 = numero153.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[12]}'"
        numero155 = pd.read_sql_query(consulta3, conn5)
        numero156 = numero155.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[13]}'"
        numero157 = pd.read_sql_query(consulta3, conn5)
        numero158 = numero157.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[14]}'"
        numero159 = pd.read_sql_query(consulta3, conn5)
        numero160 = numero159.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[15]}'"
        numero161 = pd.read_sql_query(consulta3, conn5)
        numero162 = numero161.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[16]}'"
        numero163 = pd.read_sql_query(consulta3, conn5)
        numero164 = numero163.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[17]}'"
        numero165 = pd.read_sql_query(consulta3, conn5)
        numero166 = numero165.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[18]}'"
        numero167 = pd.read_sql_query(consulta3, conn5)
        numero168 = numero167.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[19]}'"
        numero169 = pd.read_sql_query(consulta3, conn5)
        numero170 = numero169.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[20]}'"
        numero171 = pd.read_sql_query(consulta3, conn5)
        numero172 = numero171.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[21]}'"
        numero173 = pd.read_sql_query(consulta3, conn5)
        numero174 = numero173.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[22]}'"
        numero175 = pd.read_sql_query(consulta3, conn5)
        numero176 = numero175.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[23]}'"
        numero177 = pd.read_sql_query(consulta3, conn5)
        numero178 = numero177.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[24]}'"
        numero179 = pd.read_sql_query(consulta3, conn5)
        numero180 = numero179.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[25]}'"
        numero181 = pd.read_sql_query(consulta3, conn5)
        numero182 = numero181.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[26]}'"
        numero183 = pd.read_sql_query(consulta3, conn5)
        numero184 = numero183.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[27]}'"
        numero185 = pd.read_sql_query(consulta3, conn5)
        numero186 = numero185.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[28]}'"
        numero187 = pd.read_sql_query(consulta3, conn5)
        numero188 = numero187.shape[0]

        consulta3 = f"SELECT * FROM {DB} WHERE DATA = '{datas_geradas[29]}'"
        numero189 = pd.read_sql_query(consulta3, conn5)
        numero190 = numero189.shape[0]
        OS_semanais_produção = numero22 + numero24 + numero26 + numero28 + numero30
        OS_semanais_produção = numero22 + numero24 + numero26 + numero28 + numero30
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_administraivo =  0
        OS_semanais_comercial = 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_semanais_TI = 0
        OS_totais = 0
    
    if banco_de_dados == 'ADMINISTRATIVO':
        DB3 = 'ADMINISTRATIVO'
        DBx = 4
        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[0]}'"
        numero191 = pd.read_sql_query(consulta3, conn6)
        numero192 = numero191.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[1]}'"
        numero193 = pd.read_sql_query(consulta3, conn6)
        numero194 = numero193.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[2]}'"
        numero195 = pd.read_sql_query(consulta3, conn6)
        numero196 = numero195.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[3]}'"
        numero197 = pd.read_sql_query(consulta3, conn6)
        numero198 = numero197.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[4]}'"
        numero199 = pd.read_sql_query(consulta3, conn6)
        numero200 = numero199.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[5]}'"
        numero201 = pd.read_sql_query(consulta3, conn6)
        numero202 = numero201.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[6]}'"
        numero203 = pd.read_sql_query(consulta3, conn6)
        numero204 = numero203.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[7]}'"
        numero205 = pd.read_sql_query(consulta3, conn6)
        numero206 = numero205.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[8]}'"
        numero207 = pd.read_sql_query(consulta3, conn6)
        numero208 = numero207.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[9]}'"
        numero209 = pd.read_sql_query(consulta3, conn6)
        numero210 = numero209.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[10]}'"
        numero211= pd.read_sql_query(consulta3, conn6)
        numero212 = numero211.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[11]}'"
        numero213 = pd.read_sql_query(consulta3, conn6)
        numero214 = numero213.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[12]}'"
        numero215 = pd.read_sql_query(consulta3, conn6)
        numero216 = numero215.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[13]}'"
        numero217 = pd.read_sql_query(consulta3, conn6)
        numero218 = numero217.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[14]}'"
        numero219 = pd.read_sql_query(consulta3, conn6)
        numero220 = numero219.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[15]}'"
        numero221 = pd.read_sql_query(consulta3, conn6)
        numero222 = numero221.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[16]}'"
        numero223 = pd.read_sql_query(consulta3, conn6)
        numero224 = numero223.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[17]}'"
        numero225 = pd.read_sql_query(consulta3, conn6)
        numero226 = numero225.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[18]}'"
        numero227 = pd.read_sql_query(consulta3, conn6)
        numero228 = numero227.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[19]}'"
        numero229 = pd.read_sql_query(consulta3, conn6)
        numero230 = numero229.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[20]}'"
        numero231 = pd.read_sql_query(consulta3, conn6)
        numero232 = numero231.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[21]}'"
        numero233 = pd.read_sql_query(consulta3, conn6)
        numero234 = numero233.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[22]}'"
        numero235 = pd.read_sql_query(consulta3, conn6)
        numero236 = numero235.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[23]}'"
        numero237 = pd.read_sql_query(consulta3, conn6)
        numero238 = numero237.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[24]}'"
        numero239 = pd.read_sql_query(consulta3, conn6)
        numero240 = numero239.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[25]}'"
        numero241 = pd.read_sql_query(consulta3, conn6)
        numero242 = numero241.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[26]}'"
        numero243 = pd.read_sql_query(consulta3, conn6)
        numero244 = numero243.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[27]}'"
        numero245 = pd.read_sql_query(consulta3, conn6)
        numero246 = numero245.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[28]}'"
        numero247 = pd.read_sql_query(consulta3, conn6)
        numero248 = numero247.shape[0]

        consulta3 = f"SELECT * FROM {DB3} WHERE DATA = '{datas_geradas[29]}'"
        numero249 = pd.read_sql_query(consulta3, conn6)
        numero250 = numero249.shape[0]
        OS_semanais_administraivo =  numero32 + numero34 + numero36 + numero38 + numero40
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_comercial = 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_semanais_TI = 0
        OS_totais = 0

    if banco_de_dados == 'COMERCIAL':
        DB4 = 'COMERCIAL'
        DBx = 5
        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[0]}'"
        numero251 = pd.read_sql_query(consulta3, conn7)
        numero252 = numero251.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[1]}'"
        numero253 = pd.read_sql_query(consulta3, conn7)
        numero254 = numero253.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[2]}'"
        numero255 = pd.read_sql_query(consulta3, conn7)
        numero256 = numero255.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[3]}'"
        numero257 = pd.read_sql_query(consulta3, conn7)
        numero258 = numero257.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[4]}'"
        numero259 = pd.read_sql_query(consulta3, conn7)
        numero260 = numero259.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[5]}'"
        numero261 = pd.read_sql_query(consulta3, conn7)
        numero262 = numero261.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[6]}'"
        numero263 = pd.read_sql_query(consulta3, conn7)
        numero264 = numero263.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[7]}'"
        numero265 = pd.read_sql_query(consulta3, conn7)
        numero266 = numero265.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[8]}'"
        numero267 = pd.read_sql_query(consulta3, conn7)
        numero268 = numero267.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[9]}'"
        numero269 = pd.read_sql_query(consulta3, conn7)
        numero270 = numero269.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[10]}'"
        numero271= pd.read_sql_query(consulta3, conn7)
        numero272 = numero271.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[11]}'"
        numero273 = pd.read_sql_query(consulta3, conn7)
        numero274 = numero273.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[12]}'"
        numero275 = pd.read_sql_query(consulta3, conn7)
        numero276 = numero275.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[13]}'"
        numero277 = pd.read_sql_query(consulta3, conn7)
        numero278 = numero277.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[14]}'"
        numero279 = pd.read_sql_query(consulta3, conn7)
        numero280 = numero279.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[15]}'"
        numero281 = pd.read_sql_query(consulta3, conn7)
        numero282 = numero281.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[16]}'"
        numero283 = pd.read_sql_query(consulta3, conn7)
        numero284 = numero283.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[17]}'"
        numero285 = pd.read_sql_query(consulta3, conn7)
        numero286 = numero285.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[18]}'"
        numero287 = pd.read_sql_query(consulta3, conn7)
        numero288 = numero287.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[19]}'"
        numero289 = pd.read_sql_query(consulta3, conn7)
        numero290 = numero289.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[20]}'"
        numero291 = pd.read_sql_query(consulta3, conn7)
        numero292 = numero291.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[21]}'"
        numero293 = pd.read_sql_query(consulta3, conn7)
        numero294 = numero293.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[22]}'"
        numero295 = pd.read_sql_query(consulta3, conn7)
        numero296 = numero295.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[23]}'"
        numero297 = pd.read_sql_query(consulta3, conn7)
        numero298 = numero297.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[24]}'"
        numero299 = pd.read_sql_query(consulta3, conn7)
        numero300 = numero299.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[25]}'"
        numero301 = pd.read_sql_query(consulta3, conn7)
        numero302 = numero301.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[26]}'"
        numero303 = pd.read_sql_query(consulta3, conn7)
        numero304 = numero303.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[27]}'"
        numero305 = pd.read_sql_query(consulta3, conn7)
        numero306 = numero305.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[28]}'"
        numero307 = pd.read_sql_query(consulta3, conn7)
        numero308 = numero307.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[29]}'"
        numero309 = pd.read_sql_query(consulta3, conn7)
        numero310 = numero309.shape[0]
        OS_semanais_comercial =  numero42 + numero44 + numero46 + numero48 + numero50
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_administraivo = 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_semanais_TI = 0
        OS_totais = 0
    
    if banco_de_dados == 'EXPEDIÇÃO':
        DB4 = 'EXPEDICAO'
        DBx = 6
        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[0]}'"
        numero311 = pd.read_sql_query(consulta3, conn8)
        numero312 = numero311.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[1]}'"
        numero313 = pd.read_sql_query(consulta3, conn8)
        numero314 = numero313.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[2]}'"
        numero315 = pd.read_sql_query(consulta3, conn8)
        numero316 = numero315.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[3]}'"
        numero317 = pd.read_sql_query(consulta3, conn8)
        numero318 = numero317.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[4]}'"
        numero319 = pd.read_sql_query(consulta3, conn8)
        numero320 = numero319.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[5]}'"
        numero321 = pd.read_sql_query(consulta3, conn8)
        numero322 = numero321.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[6]}'"
        numero323 = pd.read_sql_query(consulta3, conn8)
        numero324 = numero323.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[7]}'"
        numero325 = pd.read_sql_query(consulta3, conn8)
        numero326 = numero325.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[8]}'"
        numero327 = pd.read_sql_query(consulta3, conn8)
        numero328 = numero327.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[9]}'"
        numero329 = pd.read_sql_query(consulta3, conn8)
        numero330 = numero329.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[10]}'"
        numero331 = pd.read_sql_query(consulta3, conn8)
        numero332 = numero331.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[11]}'"
        numero333 = pd.read_sql_query(consulta3, conn8)
        numero334 = numero333.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[12]}'"
        numero335 = pd.read_sql_query(consulta3, conn8)
        numero336 = numero335.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[13]}'"
        numero337 = pd.read_sql_query(consulta3, conn8)
        numero338 = numero337.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[14]}'"
        numero339 = pd.read_sql_query(consulta3, conn8)
        numero340 = numero339.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[15]}'"
        numero341 = pd.read_sql_query(consulta3, conn8)
        numero342 = numero341.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[16]}'"
        numero343 = pd.read_sql_query(consulta3, conn8)
        numero344 = numero343.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[17]}'"
        numero345 = pd.read_sql_query(consulta3, conn8)
        numero346 = numero345.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[18]}'"
        numero347 = pd.read_sql_query(consulta3, conn8)
        numero348 = numero347.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[19]}'"
        numero349 = pd.read_sql_query(consulta3, conn8)
        numero350 = numero349.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[20]}'"
        numero351 = pd.read_sql_query(consulta3, conn8)
        numero352 = numero351.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[21]}'"
        numero353 = pd.read_sql_query(consulta3, conn8)
        numero354 = numero353.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[22]}'"
        numero355 = pd.read_sql_query(consulta3, conn8)
        numero356 = numero355.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[23]}'"
        numero357 = pd.read_sql_query(consulta3, conn8)
        numero358 = numero357.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[24]}'"
        numero359 = pd.read_sql_query(consulta3, conn8)
        numero360 = numero359.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[25]}'"
        numero361 = pd.read_sql_query(consulta3, conn8)
        numero362 = numero361.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[26]}'"
        numero363 = pd.read_sql_query(consulta3, conn8)
        numero364 = numero363.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[27]}'"
        numero365 = pd.read_sql_query(consulta3, conn8)
        numero366 = numero365.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[28]}'"
        numero367 = pd.read_sql_query(consulta3, conn8)
        numero368 = numero367.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[29]}'"
        numero369 = pd.read_sql_query(consulta3, conn8)
        numero370 = numero369.shape[0]
        OS_semanais_expedição=  numero52 + numero54 + numero56 + numero58 
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_administraivo = 0
        OS_semanais_comercial= 0
        OS_semanais_serralharia = 0
        OS_semanais_TI= 0
        OS_totais = 0
    
    if banco_de_dados == 'SERRALHARIA':
        DB4 = 'SERRALHARIA'
        DBx = 7
        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[0]}'"
        numero371 = pd.read_sql_query(consulta3, conn9)
        numero372 = numero371.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[1]}'"
        numero373 = pd.read_sql_query(consulta3, conn9)
        numero374 = numero373.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[2]}'"
        numero375 = pd.read_sql_query(consulta3, conn9)
        numero376 = numero375.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[3]}'"
        numero377 = pd.read_sql_query(consulta3, conn9)
        numero378 = numero377.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[4]}'"
        numero379 = pd.read_sql_query(consulta3, conn9)
        numero380 = numero379.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[5]}'"
        numero381 = pd.read_sql_query(consulta3, conn9)
        numero382 = numero381.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[6]}'"
        numero383 = pd.read_sql_query(consulta3, conn9)
        numero384 = numero383.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[7]}'"
        numero385 = pd.read_sql_query(consulta3, conn9)
        numero386 = numero385.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[8]}'"
        numero387 = pd.read_sql_query(consulta3, conn9)
        numero388 = numero387.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[9]}'"
        numero389 = pd.read_sql_query(consulta3, conn9)
        numero390 = numero389.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[10]}'"
        numero391 = pd.read_sql_query(consulta3, conn9)
        numero392 = numero391.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[11]}'"
        numero393 = pd.read_sql_query(consulta3, conn9)
        numero394 = numero393.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[12]}'"
        numero395 = pd.read_sql_query(consulta3, conn9)
        numero396 = numero395.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[13]}'"
        numero397 = pd.read_sql_query(consulta3, conn9)
        numero398 = numero397.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[14]}'"
        numero399 = pd.read_sql_query(consulta3, conn9)
        numero400 = numero399.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[15]}'"
        numero401 = pd.read_sql_query(consulta3, conn9)
        numero402 = numero401.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[16]}'"
        numero403 = pd.read_sql_query(consulta3, conn9)
        numero404 = numero403.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[17]}'"
        numero405 = pd.read_sql_query(consulta3, conn9)
        numero406 = numero405.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[18]}'"
        numero407 = pd.read_sql_query(consulta3, conn9)
        numero408 = numero407.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[19]}'"
        numero409 = pd.read_sql_query(consulta3, conn9)
        numero410 = numero409.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[20]}'"
        numero411 = pd.read_sql_query(consulta3, conn9)
        numero412 = numero411.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[21]}'"
        numero413 = pd.read_sql_query(consulta3, conn9)
        numero414 = numero413.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[22]}'"
        numero415 = pd.read_sql_query(consulta3, conn9)
        numero416 = numero415.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[23]}'"
        numero417 = pd.read_sql_query(consulta3, conn9)
        numero418 = numero417.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[24]}'"
        numero419 = pd.read_sql_query(consulta3, conn9)
        numero420 = numero419.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[25]}'"
        numero421 = pd.read_sql_query(consulta3, conn9)
        numero422 = numero421.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[26]}'"
        numero423 = pd.read_sql_query(consulta3, conn9)
        numero424 = numero423.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[27]}'"
        numero425 = pd.read_sql_query(consulta3, conn9)
        numero426 = numero425.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[28]}'"
        numero427 = pd.read_sql_query(consulta3, conn9)
        numero428 = numero427.shape[0]

        consulta3 = f"SELECT * FROM {DB4} WHERE DATA = '{datas_geradas[29]}'"
        numero429 = pd.read_sql_query(consulta3, conn9)
        numero430 = numero429.shape[0]
        OS_semanais_serralharia =  numero62 + numero64 + numero66 + numero68 + numero70
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_administraivo = 0
        OS_semanais_comercial= 0
        OS_semanais_expedição = 0
        OS_semanais_TI = 0
        OS_totais = 0
    
    if banco_de_dados == 'T.I':
        DB7 = 'TI'
        DBx = 8
        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[0]}'"
        numero431 = pd.read_sql_query(consulta3, conn11)
        numero432 = numero431.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[1]}'"
        numero433 = pd.read_sql_query(consulta3, conn11)
        numero434 = numero433.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[2]}'"
        numero435 = pd.read_sql_query(consulta3, conn11)
        numero436 = numero435.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[3]}'"
        numero437 = pd.read_sql_query(consulta3, conn11)
        numero438 = numero437.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[4]}'"
        numero439 = pd.read_sql_query(consulta3, conn11)
        numero440 = numero439.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[5]}'"
        numero441 = pd.read_sql_query(consulta3, conn11)
        numero442 = numero441.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[6]}'"
        numero443 = pd.read_sql_query(consulta3, conn11)
        numero444 = numero443.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[7]}'"
        numero445 = pd.read_sql_query(consulta3, conn11)
        numero446 = numero445.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[8]}'"
        numero447 = pd.read_sql_query(consulta3, conn11)
        numero448 = numero447.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[9]}'"
        numero449 = pd.read_sql_query(consulta3, conn11)
        numero450 = numero449.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[10]}'"
        numero451 = pd.read_sql_query(consulta3, conn11)
        numero452 = numero451.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[11]}'"
        numero453 = pd.read_sql_query(consulta3, conn11)
        numero454 = numero453.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[12]}'"
        numero455 = pd.read_sql_query(consulta3, conn11)
        numero456 = numero455.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[13]}'"
        numero457 = pd.read_sql_query(consulta3, conn11)
        numero458 = numero457.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[14]}'"
        numero459 = pd.read_sql_query(consulta3, conn11)
        numero460 = numero459.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[15]}'"
        numero461 = pd.read_sql_query(consulta3, conn11)
        numero462 = numero461.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[16]}'"
        numero463 = pd.read_sql_query(consulta3, conn11)
        numero464 = numero463.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[17]}'"
        numero465 = pd.read_sql_query(consulta3, conn11)
        numero466 = numero465.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[18]}'"
        numero467 = pd.read_sql_query(consulta3, conn11)
        numero468 = numero467.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[19]}'"
        numero469 = pd.read_sql_query(consulta3, conn11)
        numero470 = numero469.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[20]}'"
        numero471 = pd.read_sql_query(consulta3, conn11)
        numero472 = numero471.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[21]}'"
        numero473 = pd.read_sql_query(consulta3, conn11)
        numero474 = numero473.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[22]}'"
        numero475 = pd.read_sql_query(consulta3, conn11)
        numero476 = numero475.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[23]}'"
        numero477 = pd.read_sql_query(consulta3, conn11)
        numero478 = numero477.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[24]}'"
        numero479 = pd.read_sql_query(consulta3, conn11)
        numero480 = numero479.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[25]}'"
        numero481 = pd.read_sql_query(consulta3, conn11)
        numero482 = numero481.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[26]}'"
        numero483 = pd.read_sql_query(consulta3, conn11)
        numero484 = numero483.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[27]}'"
        numero485 = pd.read_sql_query(consulta3, conn11)
        numero486 = numero485.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[28]}'"
        numero487 = pd.read_sql_query(consulta3, conn11)
        numero488 = numero487.shape[0]

        consulta3 = f"SELECT * FROM {DB7} WHERE DATA = '{datas_geradas[29]}'"
        numero489 = pd.read_sql_query(consulta3, conn11)
        numero490 = numero489.shape[0]

        OS_semanais_TI =  numero72 + numero74 + numero76 + numero78 + numero80
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_administraivo = 0
        OS_semanais_comercial= 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_totais = 0
          
    if banco_de_dados == 'MECÂNICA':
        DB = 'CESAR'
        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[0]}'"
        numero491 = pd.read_sql_query(consulta3, conn10)
        numero492 = numero491.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[1]}'"
        numero493 = pd.read_sql_query(consulta3, conn10)
        numero494 = numero493.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[2]}'"
        numero495 = pd.read_sql_query(consulta3, conn10)
        numero496 = numero495.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[3]}'"
        numero497 = pd.read_sql_query(consulta3, conn10)
        numero498 = numero497.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[4]}'"
        numero499 = pd.read_sql_query(consulta3, conn10)
        numero500 = numero499.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[5]}'"
        numero501 = pd.read_sql_query(consulta3, conn10)
        numero502 = numero501.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[6]}'"
        numero503 = pd.read_sql_query(consulta3, conn10)
        numero504 = numero503.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[7]}'"
        numero505 = pd.read_sql_query(consulta3, conn10)
        numero506 = numero505.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[8]}'"
        numero507 = pd.read_sql_query(consulta3, conn10)
        numero508 = numero507.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[9]}'"
        numero509 = pd.read_sql_query(consulta3, conn10)
        numero510 = numero509.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[10]}'"
        numero511 = pd.read_sql_query(consulta3, conn10)
        numero512 = numero511.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[11]}'"
        numero513 = pd.read_sql_query(consulta3, conn10)
        numero514 = numero513.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[12]}'"
        numero515 = pd.read_sql_query(consulta3, conn10)
        numero516 = numero515.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[13]}'"
        numero517 = pd.read_sql_query(consulta3, conn10)
        numero518 = numero517.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[14]}'"
        numero519 = pd.read_sql_query(consulta3, conn10)
        numero520 = numero519.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[15]}'"
        numero521 = pd.read_sql_query(consulta3, conn10)
        numero522 = numero521.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[16]}'"
        numero523 = pd.read_sql_query(consulta3, conn10)
        numero524 = numero523.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[17]}'"
        numero525 = pd.read_sql_query(consulta3, conn10)
        numero526 = numero525.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[18]}'"
        numero527 = pd.read_sql_query(consulta3, conn10)
        numero528 = numero527.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[19]}'"
        numero529 = pd.read_sql_query(consulta3, conn10)
        numero530 = numero529.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[20]}'"
        numero531 = pd.read_sql_query(consulta3, conn10)
        numero532 = numero531.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[21]}'"
        numero533 = pd.read_sql_query(consulta3, conn10)
        numero534 = numero533.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[22]}'"
        numero535 = pd.read_sql_query(consulta3, conn10)
        numero536 = numero535.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[23]}'"
        numero537 = pd.read_sql_query(consulta3, conn10)
        numero538 = numero537.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[24]}'"
        numero539 = pd.read_sql_query(consulta3, conn10)
        numero540 = numero539.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[25]}'"
        numero541 = pd.read_sql_query(consulta3, conn10)
        numero542 = numero541.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[26]}'"
        numero543 = pd.read_sql_query(consulta3, conn10)
        numero544 = numero543.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[27]}'"
        numero545 = pd.read_sql_query(consulta3, conn10)
        numero546 = numero545.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[28]}'"
        numero547 = pd.read_sql_query(consulta3, conn10)
        numero548 = numero547.shape[0]

        consulta3 = f"SELECT * FROM {DB8} WHERE DATA = '{datas_geradas[29]}'"
        numero549 = pd.read_sql_query(consulta3, conn10)
        numero550 = numero549.shape[0]
        OS_semanais_mecânica =  numero82 + numero84 + numero86 + numero88 + numero90
        OS_semanais_elétrica = 0
        OS_semanais_ferramentaria = 0
        OS_semanais_produção = 0
        OS_semanais_administraivo = 0
        OS_semanais_comercial= 0
        OS_semanais_expedição = 0
        OS_semanais_serralharia = 0
        OS_semanais_TI = 0 

    return datas_geradas,OS_semanais_elétrica,OS_semanais_ferramentaria,OS_semanais_produção,OS_semanais_administraivo,OS_semanais_comercial,OS_semanais_expedição,OS_semanais_serralharia,OS_semanais_TI,OS_totais,DBx,OS_semanais_mecânica,elétrica_dataframes,mecânica_dataframes,produção_dataframes,administrativo_dataframes,comercial_dataframes,expedição_dataframes,serralharia_dataframes,ti_dataframes,ferramentaria_dataframes

datas_geradas = gerar_datas_seguidas(data_inicial1,numero_de_datas,banco_de_dados1,numero_de_dias)
nmr = datas_geradas[10]

st.metric('O.S Desta semana',value=datas_geradas[nmr])

source = pd.DataFrame({
    'Setores': ['PRODUÇÃO','FERRAMENTARIA', 'ADMINISTRATIVO', 'COMERCIAL', 'SERRALHARIA', 'ELÉTRICA', 'MECÂNICA','EXPEDIÇÃO','T.I'],
    'Valores': [datas_geradas[3], datas_geradas[2], datas_geradas[4], datas_geradas[5], datas_geradas[7], datas_geradas[1], datas_geradas[11],datas_geradas[6],datas_geradas[8]]
})

st.bar_chart(source,x='Setores',y='Valores',color= '#6346F5',width=190)
st.header('Solicitações de O.S por periodos', divider='rainbow')
if numero_de_dias == 5:
    with st.expander(datas_geradas[0][0]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][0])
        with tab1:
            st.write(datas_geradas[13][0])
        with tab2:
            st.write(datas_geradas[14][0])
        with tab3:
            st.write(datas_geradas[15][0])
        with tab4:
            st.write(datas_geradas[16][0])
        with tab5:
            st.write(datas_geradas[17][0])
        with tab6:
            st.write(datas_geradas[18][0])
        with tab7:
            st.write(datas_geradas[19][0])
        with tab8:
            st.write(datas_geradas[20][0])

    
    with st.expander(datas_geradas[0][1]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][1])
        with tab1:
            st.write(datas_geradas[13][1])
        with tab2:
            st.write(datas_geradas[14][1])
        with tab3:
            st.write(datas_geradas[15][1])
        with tab4:
            st.write(datas_geradas[16][1])
        with tab5:
            st.write(datas_geradas[17][1])
        with tab6:
            st.write(datas_geradas[18][1])
        with tab7:
            st.write(datas_geradas[19][1])
        with tab8:
            st.write(datas_geradas[20][1])

    with st.expander(datas_geradas[0][2]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        
        with tab:
            st.write(datas_geradas[12][2])
        with tab1:
            st.write(datas_geradas[13][2])
        with tab2:
            st.write(datas_geradas[14][2])
        with tab3:
            st.write(datas_geradas[15][2])
        with tab4:
            st.write(datas_geradas[16][2])
        with tab5:
            st.write(datas_geradas[17][2])
        with tab6:
            st.write(datas_geradas[18][2])
        with tab7:
            st.write(datas_geradas[19][2])
        with tab8:
            st.write(datas_geradas[20][2])

    with st.expander(datas_geradas[0][3]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        
        with tab:
            st.write(datas_geradas[12][3])
        with tab1:
            st.write(datas_geradas[13][3])
        with tab2:
            st.write(datas_geradas[14][3])
        with tab3:
            st.write(datas_geradas[15][3])
        with tab4:
            st.write(datas_geradas[16][3])
        with tab5:
            st.write(datas_geradas[17][3])
        with tab6:
            st.write(datas_geradas[18][3])
        with tab7:
            st.write(datas_geradas[19][3])
        with tab8:
            st.write(datas_geradas[20][3])
            
    with st.expander(datas_geradas[0][4]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        
        with tab:
            st.write(datas_geradas[12][4])
        with tab1:
            st.write(datas_geradas[13][4])
        with tab2:
            st.write(datas_geradas[14][4])
        with tab3:
            st.write(datas_geradas[15][4])
        with tab4:
            st.write(datas_geradas[16][4])
        with tab5:
            st.write(datas_geradas[17][4])
        with tab6:
            st.write(datas_geradas[18][4])
        with tab7:
            st.write(datas_geradas[19][4])
        with tab8:
            st.write(datas_geradas[20][4])

    with st.expander(datas_geradas[0][5]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][5])
        with tab1:
            st.write(datas_geradas[13][5])
        with tab2:
            st.write(datas_geradas[14][5])
        with tab3:
            st.write(datas_geradas[15][5])
        with tab4:
            st.write(datas_geradas[16][5])
        with tab5:
            st.write(datas_geradas[17][5])
        with tab6:
            st.write(datas_geradas[18][5])
        with tab7:
            st.write(datas_geradas[19][5])
        with tab8:
            st.write(datas_geradas[20][5])

if numero_de_dias == 30:
    with st.expander(datas_geradas[0][0]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][0])
        with tab1:
            st.write(datas_geradas[13][0])
        with tab2:
            st.write(datas_geradas[14][0])
        with tab3:
            st.write(datas_geradas[15][0])
        with tab4:
            st.write(datas_geradas[16][0])
        with tab5:
            st.write(datas_geradas[17][0])
        with tab6:
            st.write(datas_geradas[18][0])
        with tab7:
            st.write(datas_geradas[19][0])
        with tab8:
            st.write(datas_geradas[20][0])
            
    with st.expander(datas_geradas[0][1]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][1])
        with tab1:
            st.write(datas_geradas[13][1])
        with tab2:
            st.write(datas_geradas[14][1])
        with tab3:
            st.write(datas_geradas[15][1])
        with tab4:
            st.write(datas_geradas[16][1])
        with tab5:
            st.write(datas_geradas[17][1])
        with tab6:
            st.write(datas_geradas[18][1])
        with tab7:
            st.write(datas_geradas[19][1])
        with tab8:
            st.write(datas_geradas[20][1])
            
    with st.expander(datas_geradas[0][2]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][2])
        with tab1:
            st.write(datas_geradas[13][2])
        with tab2:
            st.write(datas_geradas[14][2])
        with tab3:
            st.write(datas_geradas[15][2])
        with tab4:
            st.write(datas_geradas[16][2])
        with tab5:
            st.write(datas_geradas[17][2])
        with tab6:
            st.write(datas_geradas[18][2])
        with tab7:
            st.write(datas_geradas[19][2])
        with tab8:
            st.write(datas_geradas[20][2])
            
    with st.expander(datas_geradas[0][3]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][3])
        with tab1:
            st.write(datas_geradas[13][3])
        with tab2:
            st.write(datas_geradas[14][3])
        with tab3:
            st.write(datas_geradas[15][3])
        with tab4:
            st.write(datas_geradas[16][3])
        with tab5:
            st.write(datas_geradas[17][3])
        with tab6:
            st.write(datas_geradas[18][3])
        with tab7:
            st.write(datas_geradas[19][3])
        with tab8:
            st.write(datas_geradas[20][3])
            
    with st.expander(datas_geradas[0][4]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][4])
        with tab1:
            st.write(datas_geradas[13][4])
        with tab2:
            st.write(datas_geradas[14][4])
        with tab3:
            st.write(datas_geradas[15][4])
        with tab4:
            st.write(datas_geradas[16][4])
        with tab5:
            st.write(datas_geradas[17][4])
        with tab6:
            st.write(datas_geradas[18][4])
        with tab7:
            st.write(datas_geradas[19][4])
        with tab8:
            st.write(datas_geradas[20][4])
            
    with st.expander(datas_geradas[0][5]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][5])
        with tab1:
            st.write(datas_geradas[13][5])
        with tab2:
            st.write(datas_geradas[14][5])
        with tab3:
            st.write(datas_geradas[15][5])
        with tab4:
            st.write(datas_geradas[16][5])
        with tab5:
            st.write(datas_geradas[17][5])
        with tab6:
            st.write(datas_geradas[18][5])
        with tab7:
            st.write(datas_geradas[19][5])
        with tab8:
            st.write(datas_geradas[20][5])
            
    with st.expander(datas_geradas[0][6]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][6])
        with tab1:
            st.write(datas_geradas[13][6])
        with tab2:
            st.write(datas_geradas[14][6])
        with tab3:
            st.write(datas_geradas[15][6])
        with tab4:
            st.write(datas_geradas[16][6])
        with tab5:
            st.write(datas_geradas[17][6])
        with tab6:
            st.write(datas_geradas[18][6])
        with tab7:
            st.write(datas_geradas[19][6])
        with tab8:
            st.write(datas_geradas[20][6])
            
    with st.expander(datas_geradas[0][7]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][7])
        with tab1:
            st.write(datas_geradas[13][7])
        with tab2:
            st.write(datas_geradas[14][7])
        with tab3:
            st.write(datas_geradas[15][7])
        with tab4:
            st.write(datas_geradas[16][7])
        with tab5:
            st.write(datas_geradas[17][7])
        with tab6:
            st.write(datas_geradas[18][7])
        with tab7:
            st.write(datas_geradas[19][7])
        with tab8:
            st.write(datas_geradas[20][7])
            
    with st.expander(datas_geradas[0][8]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][8])
        with tab1:
            st.write(datas_geradas[13][8])
        with tab2:
            st.write(datas_geradas[14][8])
        with tab3:
            st.write(datas_geradas[15][8])
        with tab4:
            st.write(datas_geradas[16][8])
        with tab5:
            st.write(datas_geradas[17][8])
        with tab6:
            st.write(datas_geradas[18][8])
        with tab7:
            st.write(datas_geradas[19][8])
        with tab8:
            st.write(datas_geradas[20][8])
            
    with st.expander(datas_geradas[0][9]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][9])
        with tab1:
            st.write(datas_geradas[13][9])
        with tab2:
            st.write(datas_geradas[14][9])
        with tab3:
            st.write(datas_geradas[15][9])
        with tab4:
            st.write(datas_geradas[16][9])
        with tab5:
            st.write(datas_geradas[17][9])
        with tab6:
            st.write(datas_geradas[18][9])
        with tab7:
            st.write(datas_geradas[19][9])
        with tab8:
            st.write(datas_geradas[20][9])
            
    with st.expander(datas_geradas[0][10]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][10])
        with tab1:
            st.write(datas_geradas[13][10])
        with tab2:
            st.write(datas_geradas[14][10])
        with tab3:
            st.write(datas_geradas[15][10])
        with tab4:
            st.write(datas_geradas[16][10])
        with tab5:
            st.write(datas_geradas[17][10])
        with tab6:
            st.write(datas_geradas[18][10])
        with tab7:
            st.write(datas_geradas[19][10])
        with tab8:
            st.write(datas_geradas[20][10])
            
    with st.expander(datas_geradas[0][11]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][11])
        with tab1:
            st.write(datas_geradas[13][11])
        with tab2:
            st.write(datas_geradas[14][11])
        with tab3:
            st.write(datas_geradas[15][11])
        with tab4:
            st.write(datas_geradas[16][11])
        with tab5:
            st.write(datas_geradas[17][11])
        with tab6:
            st.write(datas_geradas[18][11])
        with tab7:
            st.write(datas_geradas[19][11])
        with tab8:
            st.write(datas_geradas[20][11])
            
    with st.expander(datas_geradas[0][12]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][12])
        with tab1:
            st.write(datas_geradas[13][12])
        with tab2:
            st.write(datas_geradas[14][12])
        with tab3:
            st.write(datas_geradas[15][12])
        with tab4:
            st.write(datas_geradas[16][12])
        with tab5:
            st.write(datas_geradas[17][12])
        with tab6:
            st.write(datas_geradas[18][12])
        with tab7:
            st.write(datas_geradas[19][12])
        with tab8:
            st.write(datas_geradas[20][12])
            
    with st.expander(datas_geradas[0][13]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][13])
        with tab1:
            st.write(datas_geradas[13][13])
        with tab2:
            st.write(datas_geradas[14][13])
        with tab3:
            st.write(datas_geradas[15][13])
        with tab4:
            st.write(datas_geradas[16][13])
        with tab5:
            st.write(datas_geradas[17][13])
        with tab6:
            st.write(datas_geradas[18][13])
        with tab7:
            st.write(datas_geradas[19][13])
        with tab8:
            st.write(datas_geradas[20][13])
            
    with st.expander(datas_geradas[0][14]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][14])
        with tab1:
            st.write(datas_geradas[13][14])
        with tab2:
            st.write(datas_geradas[14][14])
        with tab3:
            st.write(datas_geradas[15][14])
        with tab4:
            st.write(datas_geradas[16][14])
        with tab5:
            st.write(datas_geradas[17][14])
        with tab6:
            st.write(datas_geradas[18][14])
        with tab7:
            st.write(datas_geradas[19][14])
        with tab8:
            st.write(datas_geradas[20][14])
            
    with st.expander(datas_geradas[0][15]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][15])
        with tab1:
            st.write(datas_geradas[13][15])
        with tab2:
            st.write(datas_geradas[14][15])
        with tab3:
            st.write(datas_geradas[15][15])
        with tab4:
            st.write(datas_geradas[16][15])
        with tab5:
            st.write(datas_geradas[17][15])
        with tab6:
            st.write(datas_geradas[18][15])
        with tab7:
            st.write(datas_geradas[19][15])
        with tab8:
            st.write(datas_geradas[20][15])
            
    with st.expander(datas_geradas[0][16]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][16])
        with tab1:
            st.write(datas_geradas[13][16])
        with tab2:
            st.write(datas_geradas[14][16])
        with tab3:
            st.write(datas_geradas[15][16])
        with tab4:
            st.write(datas_geradas[16][16])
        with tab5:
            st.write(datas_geradas[17][16])
        with tab6:
            st.write(datas_geradas[18][16])
        with tab7:
            st.write(datas_geradas[19][16])
        with tab8:
            st.write(datas_geradas[20][16])
            
    with st.expander(datas_geradas[0][17]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][17])
        with tab1:
            st.write(datas_geradas[13][17])
        with tab2:
            st.write(datas_geradas[14][17])
        with tab3:
            st.write(datas_geradas[15][17])
        with tab4:
            st.write(datas_geradas[16][17])
        with tab5:
            st.write(datas_geradas[17][17])
        with tab6:
            st.write(datas_geradas[18][17])
        with tab7:
            st.write(datas_geradas[19][17])
        with tab8:
            st.write(datas_geradas[20][17])
            
    with st.expander(datas_geradas[0][18]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][18])
        with tab1:
            st.write(datas_geradas[13][18])
        with tab2:
            st.write(datas_geradas[14][18])
        with tab3:
            st.write(datas_geradas[15][18])
        with tab4:
            st.write(datas_geradas[16][18])
        with tab5:
            st.write(datas_geradas[17][18])
        with tab6:
            st.write(datas_geradas[18][18])
        with tab7:
            st.write(datas_geradas[19][18])
        with tab8:
            st.write(datas_geradas[20][18])
            
    with st.expander(datas_geradas[0][19]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][19])
        with tab1:
            st.write(datas_geradas[13][19])
        with tab2:
            st.write(datas_geradas[14][19])
        with tab3:
            st.write(datas_geradas[15][19])
        with tab4:
            st.write(datas_geradas[16][19])
        with tab5:
            st.write(datas_geradas[17][19])
        with tab6:
            st.write(datas_geradas[18][19])
        with tab7:
            st.write(datas_geradas[19][19])
        with tab8:
            st.write(datas_geradas[20][19])
            
    with st.expander(datas_geradas[0][20]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][20])
        with tab1:
            st.write(datas_geradas[13][20])
        with tab2:
            st.write(datas_geradas[14][20])
        with tab3:
            st.write(datas_geradas[15][20])
        with tab4:
            st.write(datas_geradas[16][20])
        with tab5:
            st.write(datas_geradas[17][20])
        with tab6:
            st.write(datas_geradas[18][20])
        with tab7:
            st.write(datas_geradas[19][20])
        with tab8:
            st.write(datas_geradas[20][20])
            
    with st.expander(datas_geradas[0][21]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][21])
        with tab1:
            st.write(datas_geradas[13][21])
        with tab2:
            st.write(datas_geradas[14][21])
        with tab3:
            st.write(datas_geradas[15][21])
        with tab4:
            st.write(datas_geradas[16][21])
        with tab5:
            st.write(datas_geradas[17][21])
        with tab6:
            st.write(datas_geradas[18][21])
        with tab7:
            st.write(datas_geradas[19][21])
        with tab8:
            st.write(datas_geradas[20][21])
            
    with st.expander(datas_geradas[0][22]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7 ,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][22])
        with tab1:
            st.write(datas_geradas[13][22])
        with tab2:
            st.write(datas_geradas[14][22])
        with tab3:
            st.write(datas_geradas[15][22])
        with tab4:
            st.write(datas_geradas[16][22])
        with tab5:
            st.write(datas_geradas[17][22])
        with tab6:
            st.write(datas_geradas[18][22])
        with tab7:
            st.write(datas_geradas[19][22])
        with tab8:
            st.write(datas_geradas[20][22])
            
    with st.expander(datas_geradas[0][23]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][23])
        with tab1:
            st.write(datas_geradas[13][23])
        with tab2:
            st.write(datas_geradas[14][23])
        with tab3:
            st.write(datas_geradas[15][23])
        with tab4:
            st.write(datas_geradas[16][23])
        with tab5:
            st.write(datas_geradas[17][23])
        with tab6:
            st.write(datas_geradas[18][23])
        with tab7:
            st.write(datas_geradas[19][23])
        with tab8:
            st.write(datas_geradas[20][23])
            
    with st.expander(datas_geradas[0][24]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][24])
        with tab1:
            st.write(datas_geradas[13][24])
        with tab2:
            st.write(datas_geradas[14][24])
        with tab3:
            st.write(datas_geradas[15][24])
        with tab4:
            st.write(datas_geradas[16][24])
        with tab5:
            st.write(datas_geradas[17][24])
        with tab6:
            st.write(datas_geradas[18][24])
        with tab7:
            st.write(datas_geradas[19][24])
        with tab8:
            st.write(datas_geradas[20][24])
            
    with st.expander(datas_geradas[0][25]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][25])
        with tab1:
            st.write(datas_geradas[13][25])
        with tab2:
            st.write(datas_geradas[14][25])
        with tab3:
            st.write(datas_geradas[15][25])
        with tab4:
            st.write(datas_geradas[16][25])
        with tab5:
            st.write(datas_geradas[17][25])
        with tab6:
            st.write(datas_geradas[18][25])
        with tab7:
            st.write(datas_geradas[19][25])
        with tab8:
            st.write(datas_geradas[20][25])
            
    with st.expander(datas_geradas[0][26]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][26])
        with tab1:
            st.write(datas_geradas[13][26])
        with tab2:
            st.write(datas_geradas[14][26])
        with tab3:
            st.write(datas_geradas[15][26])
        with tab4:
            st.write(datas_geradas[16][26])
        with tab5:
            st.write(datas_geradas[17][26])
        with tab6:
            st.write(datas_geradas[18][26])
        with tab7:
            st.write(datas_geradas[19][26])
        with tab8:
            st.write(datas_geradas[20][26])
            
    with st.expander(datas_geradas[0][27]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][27])
        with tab1:
            st.write(datas_geradas[13][27])
        with tab2:
            st.write(datas_geradas[14][27])
        with tab3:
            st.write(datas_geradas[15][27])
        with tab4:
            st.write(datas_geradas[16][27])
        with tab5:
            st.write(datas_geradas[17][27])
        with tab6:
            st.write(datas_geradas[18][27])
        with tab7:
            st.write(datas_geradas[19][27])
        with tab8:
            st.write(datas_geradas[20][27])
            
    with st.expander(datas_geradas[0][28]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][28])
        with tab1:
            st.write(datas_geradas[13][28])
        with tab2:
            st.write(datas_geradas[14][28])
        with tab3:
            st.write(datas_geradas[15][28])
        with tab4:
            st.write(datas_geradas[16][28])
        with tab5:
            st.write(datas_geradas[17][28])
        with tab6:
            st.write(datas_geradas[18][28])
        with tab7:
            st.write(datas_geradas[19][28])
        with tab8:
            st.write(datas_geradas[20][28])
            
    with st.expander(datas_geradas[0][29]):
        tab,tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['ELÉTRICA','MECÂNICA','PRODUÇÃO','ADMINISTRAÇÃO','COMERCIAL','EXPEDIÇÃO','SERRALHARIA','T.I','FERRAMENTARIA'])
        with tab:
            st.write(datas_geradas[12][29])
        with tab1:
            st.write(datas_geradas[13][29])
        with tab2:
            st.write(datas_geradas[14][29])
        with tab3:
            st.write(datas_geradas[15][29])
        with tab4:
            st.write(datas_geradas[16][29])
        with tab5:
            st.write(datas_geradas[17][29])
        with tab6:
            st.write(datas_geradas[18][29])
        with tab7:
            st.write(datas_geradas[19][29])
        with tab8:
            st.write(datas_geradas[20][29])

consulta3 = f"SELECT * FROM ROSIVALDO ORDER BY DATA"
umero491 = pd.read_sql_query(consulta3, conn1)
numero492 = umero491.shape[0]

teste = umero491.drop(columns=['SOLICITANTE','SETOR','OCORRENCIA','OS','DATA','GRAU','FINALIZADA','DATAF','HORAF','AÇÃO'])
teste
test1 = teste.loc[3]
test2 = np.array(test1)
test3 = str(test2)
test4 = test3[2:-2]
st.write(test4)

teste5 = umero491.drop(columns=['SOLICITANTE','SETOR','OCORRENCIA','OS','GRAU','HORA','DATA','FINALIZADA','DATAF','AÇÃO'])
teste5
test6 = teste5.loc[3]
test7 = np.array(test6)
test8 = str(test7)
test9 = test8[2:-2]
st.write(test9)

# Criar objetos de tempo
hora1 = datetime.strptime(str(test4), '%H:%M:%S')

hora3 = datetime.strptime(str(test9), '%H:%M:%S')

delta_tempo1 = timedelta(hours=hora1.hour, minutes=hora1.minute, seconds=hora1.second)

delta_tempo3 = timedelta(hours=hora3.hour, minutes=hora3.minute, seconds=hora3.second)

novo_tempo = (datetime.min - (delta_tempo1 - delta_tempo3)).time()

novo_tempo1 = (datetime.min - (delta_tempo1 - delta_tempo3)).time()

horass = [1,1,1,1,1,1,1,1,1,1,1]
testee = [1,1,1,1,1,1,1,1,1,1,1]

soma_horas = hora1 + timedelta(minutes=30)
subtrai_horas = hora1 - timedelta(minutes=30)
diferenca_entre_horas = hora1 - hora3

st.write(soma_horas)
subtrai_horas
diferenca_entre_horas

chart_data = pd.DataFrame(
   {
       "col1": horass,
       "col2": testee,
       "col3": np.random.choice(["A", "B"], 11),
   }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

if oimaioa == "Horas de manuteção":
    st.write('puta que pariuo')

james = np.random.randn(20, 3)
st.write(james)