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
import sqlite3
import openpyxl
import altair as alt
from pydub import AudioSegment

if 'banco_de_dados' == 'banco_de_dados':
    conn12 = sqlite3.connect('MATERIAS')
    cursor12 = conn12.cursor()
    cursor12.execute('''
        CREATE TABLE IF NOT EXISTS MATERIAS (
        ID INTEGER PRIMARY KEY,
        QUANTIDADE,
        UNIDADE,
        SETOR,
        FABRICANTE,
        CATALOGO TEXT,
        DESCRIÇÃO TEXT,
        CODIGO TEXT,
        SOLICITADO,
        N°,
        FORNECEDOR TEXT,
        FORNECEDOR1 TEXT
    
        )
    ''')
    
    conn13 = sqlite3.connect('SAIDA')
    cursor13 = conn13.cursor()
    cursor13.execute('''
    CREATE TABLE IF NOT EXISTS SAIDA (
        ID INTEGER PRIMARY KEY,
        QUANTIDADE,
        CATALOGO TEXT,
        DESCRIÇÃO TEXT,
        DATA_DE_SAIDA,
        HORA_DE_SAIDA

        )
    ''')

col1,col2,col3,col4 = st.columns([2,8,4,0.1])
with col1:
    with st.expander('💡'):
        setor = st.radio(
           "Selecione",
            ['ALL','ELÉTRICA',"MECÂNICA","SERRALHARIA"],
            index=0,
                )
with col3:
    busca = st.text_input('Buscar',placeholder='Faça uma busca 🔎')

if not busca:
    if setor == 'ALL':
        consulta3 = f"SELECT * FROM MATERIAS"
        numero1 = pd.read_sql_query(consulta3, conn12)
        numero2 = numero1.shape[0]
    else:
        if not busca:
            consulta3 = f"SELECT * FROM MATERIAS WHERE SETOR = '{setor}'"
            numero1 = pd.read_sql_query(consulta3, conn12)
            numero2 = numero1.shape[0]
        else:
            consulta3 = f"SELECT * FROM MATERIAS WHERE SETOR = '{setor}' AND DESCRIÇÃO = '{busca}'"
            numero1 = pd.read_sql_query(consulta3, conn12)
            numero2 = numero1.shape[0]
else:
    consulta3 = f"SELECT * FROM MATERIAS WHERE DESCRIÇÃO = '{busca}'"
    numero1 = pd.read_sql_query(consulta3, conn12)
    numero2 = numero1.shape[0]
    


tabela_drop = numero1.drop(columns=['ID'])
def load_dataa():
    return pd.DataFrame(tabela_drop)
st.checkbox("Estender", value=True, key="use_container_width1")
df = load_dataa()
st.dataframe(df, use_container_width =st.session_state.use_container_width1)


col1,col2,col4,col5,col8,col9,col11 = st.columns([2,2,2,2,2,2,2,])

incluir = st.toggle('Incluir Materias')
if incluir:
    atd = st.toggle('Atualizar os dados')
    with col1:
        if atd:
            ids_update  = st.number_input("ID",min_value=0,max_value=10000,value=0,placeholder="Insira um valor")
        else:
            ids = st.number_input("ID",min_value=numero2,max_value=numero2,value=numero2,placeholder="Atualize o valor")
    with col2:
        if  atd:
            quantidade_update = st.number_input("QUANTIDADE",min_value=0,max_value=5,placeholder="Insira um valor")

        else:
            quantidade = st.number_input("QUANTIDADE",min_value=0,max_value=5,value=0,placeholder="Atualize o valor")

        if  atd:
            unidade_update = st.selectbox('UNIDADE',('UN','CM','MT','KG','G','L','M2','M3'),placeholder='Escolha uma unidade')
       
        else:
            unidade = st.selectbox('UNIDADE',('UN','CM','MT','KG','G','L','M2','M3'),placeholder='Atualize a unidade')
        with col4:
            if  atd:
                setor_update = st.selectbox('SETOR',('ELÉTRICA','MECÂNICA','SERRALHARIA'),placeholder='Escolha o setor')
       
            else:
                setor = st.selectbox('SETOR',('ELÉTRICA','MECÂNICA','SERRALHARIA'),placeholder='Atualize o setor')
    with col5:
        if  atd:
            fabricante_update = st.text_input('FABRICANTE',placeholder='Defina o fabricante')

        else:
            fabricante = st.text_input('FABRICANTE',placeholder="Atualize o fabricante")
        if  atd:
            catalogo_update = st.text_input('CATALOGO',placeholder='Defina o catalogo')
       
        else:
            catalogo = st.text_input('CATALOGO',placeholder='Atualize o catalogo')

        if atd:
            descricao_update = st.text_input('DESCRIÇÃO',placeholder='Defina a descrição')
    
        else:
            descricao = st.text_input('DESCRIÇÃO',placeholder='Atualize a descrição')
    with col8:
        if  atd:
            fornecedor_update = st.text_input('CODIGO TOTVS',placeholder='Insira o código')
        else:
            fornecedor = st.text_input('CODIGO TOTVS',placeholder='Atualize o código')
    with col9:
        if  atd:
            solicitado_update = st.selectbox('SOLICITADO?',('SIM','NÃO'),placeholder='Sim ou Não?')
       
        else:
            solicitado = st.selectbox('SOLICITADO?',('SIM','NÃO'),index=1,placeholder='Sim ou Não?',)

        if atd:
            solicitacao_update = st.number_input("N° da solicitação",min_value=0,max_value=10000,placeholder="Insira um valor")
       
        else:
            solicitacao = st.number_input("N° da solicitação",min_value=0,max_value=10000,placeholder="Atualize o valor")
    with col11:
        if atd:
            fornecedor1_update = st.text_input('FORNECEDOR',placeholder='Insira o fornecedor')
        else:
            fornecedor1 = st.text_input('FORNECEDOR',placeholder='Atualize o fornecedor')   
        if atd:
            fornecedor2_update = st.text_input('FORNECEDOR1',placeholder='Insira o fornecedor')
    
        else:
            fornecedor2 = st.text_input('FORNECEDOR1',placeholder='Atualize o fornecedor')



    jmp,jmp1 = st.columns([1,13])
    with jmp:
        if atd:
            atl = st.button('Enviar 📤')
            btn = 0
        
        else:
            btn = st.button('Enviar 📤')
            atl = 0

    with jmp1:
        if atd:
            deletar_linha = st.button("Excluir 🗑")
            if deletar_linha:
                st.toast('Excluindo Linha...')
                time.sleep(1)
                st.toast('Linha Excluida!')
                cursor12.execute(f'DELETE FROM MATERIAS WHERE ID = {ids_update};')
                conn12.commit()
else:
    btn = 0
    atl = 0

base_de_dados = 'MATERIAS'

if btn:
    st.toast('Inserindo Linha...')
    time.sleep(1)
    st.toast('Linha Inserida!')
    st.balloons()
    cursor12.execute("INSERT INTO MATERIAS (ID,QUANTIDADE,UNIDADE,SETOR,FABRICANTE,CATALOGO,DESCRIÇÃO,CODIGO,SOLICITADO,N°,FORNECEDOR,FORNECEDOR1) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (ids,quantidade,unidade,setor,fabricante,catalogo,descricao,fornecedor,solicitado,solicitacao,fornecedor1,fornecedor2))
    conn12.commit()
    
if atl:
    st.toast('Atualizando Linha...')
    time.sleep(1)
    st.toast('Linha Atualizada!')
    st.balloons()
    cursor12.execute("UPDATE MATERIAS SET QUANTIDADE = ?,UNIDADE = ?,SETOR = ?, CATALOGO = ?, DESCRIÇÃO = ?, CODIGO = ?, SOLICITADO =?, N° = ?, FORNECEDOR = ?, FORNECEDOR1 = ? WHERE ID = ?",(quantidade_update,unidade_update,setor_update,catalogo_update,descricao_update,fornecedor_update,solicitado_update,solicitacao_update,fornecedor1_update,fornecedor2_update,ids_update))
    conn12.commit()

if 1 == 0:
    consulta = f"SELECT * FROM {base_de_dados} WHERE QUANTIDADE <= 1"
    read = pd.read_sql_query(consulta, conn12)
    shape = read.shape[0]

    count = 0
    for sales in range(shape):
        if count == 0:
            read_0 = read.loc[count]
        count = count + 1
        if count == 1:
            read_1 = read.loc[count]
        if count == 2:
            read_2 = read.loc[count]
        if count == 3:
            read_3 = read.loc[count]
        if count == 4:
            read_4 = read.loc[count]
        if count == 5:
            read_5 = read.loc[count]
        if count == 6:
            read_6 = read.loc[count]
        if count == 7:
            read_7 = read.loc[count]
        if count == 8:
            read_8 = read.loc[count]
        if count == 9:
            read_9 = read.loc[count]
        if count == 10:
            read_10 = read.loc[count]
        if count == 11:
            read_11 = read.loc[count]
        if count == 12:
            read_12 = read.loc[count]
        if count == 13:
            read_13 = read.loc[count]
        if count == 14:
            read_14 = read.loc[count]
        if count == 15:
            read_15 = read.loc[count]
        if count == 16:
            read_16 = read.loc[count]
        if count == 17:
            read_17 = read.loc[count]
        if count == 18:
            read_18 = read.loc[count]
        if count == 19:
            read_19 = read.loc[count]
        if count == 20:
            read_20 = read.loc[count]
        
        conn12.close()

        source = pd.DataFrame({
        'Setores': ['PRODUÇÃO','FERRAMENTARIA', 'ADMINISTRATIVO', 'COMERCIAL', 'SERRALHARIA', 'ELÉTRICA', 'MECÂNICA','EXPEDIÇÃO','T.I'],
        'Valores': [read_0, read_1, read_2, read_3, read_4, read_5, read_6,read_7,read_8]
        })

        st.bar_chart(source,x='Setores',y='Valores',color= '#6346F5',width=190)


