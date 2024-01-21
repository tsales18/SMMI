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
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.customize_running import center_running
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.image_in_tables import table_with_images

#def example():
    #click = st.button("Observe where the 🏃‍♂️ running widget is now!")
    #if click:
        #center_running()
        #time.sleep(2)

#def example_one():
    #dataframe = generate_fake_dataframe(
        #size=500, cols="dfc", col_names=("date", "income", "person"), seed=1
    #)
    #filtered_df = dataframe_explorer(dataframe, case=False)
    #st.dataframe(filtered_df, use_container_width=True)

if 'banco_de_dados' == 'banco_de_dados':
    conn12 = sqlite3.connect('./Data/Materiais')
    cursor12 = conn12.cursor()
    cursor12.execute('''
    CREATE TABLE IF NOT EXISTS Materiais (
        ID INTEGER PRIMARY KEY,
        Quantidade,
        Unidade,
        Setor,
        Fabricante,
        Catalogo TEXT,
        Descrição TEXT,
        Codigo TEXT,
        Solicitado,
        N°,
        Fornecedor TEXT,
        Fornecedor1 TEXT,
        Fornecedor2 TEXT
        
        )
    ''')
    

    cursor12= conn12.cursor()
    cursor12.execute('''
    CREATE TABLE IF NOT EXISTS SAIDA (
        ID INTEGER PRIMARY KEY,
        Quantidade,
        Catalogo TEXT,
        Descrição TEXT,
        DATA_DE_SAIDA,
        HORA_DE_SAIDA

        )
    ''')


    cursor12= conn12.cursor()
    cursor12.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores (
        ID INTEGER PRIMARY KEY,
        Nome TEXT,
        CNPJ TEXT,
        Numero INTEGER,
        Vendedor TEXT,
        Endereço TEXT,
        Email TEXT,
        Material TEXT,
        Material1 TEXT,
        Material2 TEXT
                    
        )
    ''')

    

    conn = sqlite3.connect('./Data/Setores')
    cursor = conn.cursor()


tab6, tab7= st.tabs(["| Cadastro de materiais |", "| Fornecedores |"])
with tab6:
    col1,col2,col3,col4 = st.columns([2,8,4,0.1])
    with col1:
        with st.expander('💡'):
            Setor = st.radio(
            "Selecione",
            ['ALL','Elétrica',"MecÂnica","Serralharia"],
            index=0,
            )
    with col3:
        busca = st.text_input('Buscar',placeholder='Faça uma busca 🔎')

    if not busca:
        if Setor == 'ALL':
            consulta3 = f"SELECT * FROM Materiais"
            numero1 = pd.read_sql_query(consulta3, conn12)
            numero2 = numero1.shape[0]
        else:
            if not busca:
                consulta3 = f"SELECT * FROM Materiais WHERE Setor: = '{Setor:}'"
                numero1 = pd.read_sql_query(consulta3, conn12)
                numero2 = numero1.shape[0]
            else:
                consulta3 = f"SELECT * FROM Materiais WHERE Setor: = '{Setor:}' AND Descrição = '{busca}'"
                numero1 = pd.read_sql_query(consulta3, conn12)
                numero2 = numero1.shape[0]
    else:
        consulta3 = f"SELECT * FROM Materiais WHERE Descrição = '{busca}'"
        numero1 = pd.read_sql_query(consulta3, conn12)
        numero2 = numero1.shape[0]

    def load_dataa():
        return pd.DataFrame(numero1)
    st.checkbox("Estender", value=True, key="use_container_width1")
    df = load_dataa()
    st.dataframe(df, use_container_width =st.session_state.use_container_width1)

    col1,col2,col4,col5,col8,col9,col11 = st.columns([2,2,2,2,2,2,2,])
    incluir = st.toggle('Incluir Materiais')
    if incluir:
        atd = st.toggle('Atualizar os dados')
        with col1:
            if atd:
                ids_update  = st.number_input("ID",min_value=0,max_value=10000,value=0,placeholder="Insira um valor")
            else:
                ids = st.number_input("ID",min_value=numero2,max_value=numero2,value=numero2,placeholder="Atualize o valor")
                ids_update = 0

            consulta1 = "SELECT * FROM Materiais"
            ros_oc = pd.read_sql_query(consulta1, conn12)
            if not ros_oc.empty:
                preenchimento = ros_oc.loc[ids_update]
                preenchimento = preenchimento.tolist()
            else:
                preenchimento = [None,None,None,None,None,None,None,None,None,None,None,None,None,None]

        with col2:

            if  atd:
                Quantidade_update = st.number_input("Quantidade",min_value=0,max_value=5,placeholder="Atualize o valor")

            else:
                Quantidade = st.number_input("Quantidade",min_value=0,max_value=5,value=0,placeholder="Insira o valor")

            if  atd:
                Unidade_update = st.selectbox('Unidade',('UN','CM','MT','KG','G','L','M2','M3'),placeholder='Atualize a Unidade')
       
            else:
                Unidade = st.selectbox('Unidade',('UN','CM','MT','KG','G','L','M2','M3'),placeholder='Escolha uma Unidade')

            with col4:
                if  atd:
                    Setor_update = st.selectbox('Setor:',('Elétrica','Mecânica','Serralharia'),index=None, placeholder='Atualize o Setor')
                else:
                    Setor = st.selectbox('Setor:',('Elétrica','Mecânica','Serralharia'),index=None,placeholder='Escolha o Setor')

        with col5:
            if  atd:
                Fabricante_update = st.text_input('Fabricante:',value=preenchimento[4],placeholder='Atualize o Fabricante')
            else:
                Fabricante = st.text_input('Fabricante:',placeholder='Defina o Fabricante')

            if  atd:
                Catalogo_update = st.text_input('Catalogo:',value=preenchimento[5],placeholder='Atualize o Catalogo')
            else:
                Catalogo = st.text_input('Catalogo:',placeholder='Defina o Catalogo')

            if atd:
                descricao_update = st.text_input('Descrição:',value=preenchimento[6],placeholder='Atualize a Descrição')
            else:
                descricao = st.text_input('Descrição:',placeholder='Defina a Descrição')

        with col8:
            if  atd:
                Fornecedor_update = st.text_input('Codigo TOTVS:',value=preenchimento[7],placeholder='Atualize o código')
            else:
                Fornecedor = st.text_input('Codigo TOTVS:',placeholder='Insira o código')

        with col9:
            if  atd:
                Solicitado_update = st.selectbox('Solicitado?:',('SIM','NÃO'),index=None,placeholder='Sim ou Não?')
            else:
                Solicitado = st.selectbox('Solicitado?:',('SIM','NÃO'),index=None,placeholder='Sim ou Não?',)

            if atd:
                solicitacao_update = st.number_input("N° da solicitação:",min_value=0,max_value=10000,value=preenchimento[9],placeholder="Insira um valor")
            else:
                solicitacao = st.number_input("N° da solicitação:",min_value=0,max_value=10000,placeholder="Atualize o valor")

        with col11:
            if atd:
                Fornecedor1_update = st.text_input('Fornecedor:',value=preenchimento[10],placeholder='Atualize o Fornecedor')
            else:
                Fornecedor1 = st.text_input('Fornecedor:',placeholder='Insira o Fornecedor')   

            if atd:
                Fornecedor2_update = st.text_input('Fornecedor 1:',value=preenchimento[11],placeholder='Atualize o Fornecedor')
    
            else:    
                Fornecedor2 = st.text_input('Fornecedor 1:',placeholder='Insira o Fornecedor')

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
                    cursor12.execute(f'DELETE FROM Materiais WHERE ID = {ids_update};')
                    conn12.commit()
    else:
        btn = 0
        atl = 0

    base_de_dados = 'Materiais'

    if btn:
        st.toast('Inserindo Linha...')
        time.sleep(1)
        st.toast('Linha Inserida!')
        st.balloons()
        cursor12.execute("INSERT INTO Materiais (ID,Quantidade,Unidade,Setor,Fabricante,Catalogo,Descrição,Codigo,Solicitado,N°,Fornecedor,Fornecedor1) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (ids,Quantidade,Unidade,Setor,Fabricante,Catalogo,descricao,Fornecedor,Solicitado,solicitacao,Fornecedor1,Fornecedor2))
        conn12.commit()
    
    if atl:
        st.toast('Atualizando Linha...')
        time.sleep(1)
        st.toast('Linha Atualizada!')
        st.balloons()
        cursor12.execute("UPDATE Materiais SET Quantidade = ?,Unidade = ?,Setor = ?, Catalogo = ?, Descrição = ?, Codigo = ?, Solicitado =?, N° = ?, Fornecedor = ?, Fornecedor1 = ? WHERE ID = ?",(Quantidade_update,Unidade_update,Setor_update,Catalogo_update,descricao_update,Fornecedor_update,Solicitado_update,solicitacao_update,Fornecedor1_update,Fornecedor2_update,ids_update))
        conn12.commit()

with tab7:
    consulta3 = f"SELECT * FROM fornecedores"
    numero1 = pd.read_sql_query(consulta3, conn12)
    numero2 = numero1.shape[0]

    def load_dataa():
        return pd.DataFrame(numero1)
    st.checkbox("Estender", value=True, key="use_container_width2")
    df = load_dataa()
    st.dataframe(df, use_container_width =st.session_state.use_container_width2)

    col1,col2,col4,col5,col8,col9,col11 = st.columns([2,2,2,2,2,2,2,])
    incluirr = st.toggle('Incluir Fornecedor ')
    if incluirr:
        atd1 = st.toggle('Atualizar os dados  ')
        with col1:
            if atd1:
                ids_update = st.number_input("ID: ",min_value=0,max_value=10000,value=0,placeholder="Insira um valor")
            else:
                ids = st.number_input("ID: ",min_value=numero2,max_value=numero2,value=numero2,placeholder="Atualize o valor")
                ids_update = 0

            consulta3 = f"SELECT * FROM fornecedores"
            ros_oc = pd.read_sql_query(consulta3, conn12)
            if not ros_oc.empty:
                preenchimento = ros_oc.loc[ids_update]
                preenchimento = preenchimento.tolist()
            else:
                preenchimento = [None,None,None,None,None,None,None,None,None,None,None,None,None,None]

        with col2:
            if atd1:
                nome_update = st.text_input("Nome: ",placeholder="Atualize o nome")

            else:
                nome = st.text_input("Nome:  ",placeholder="Insira um nome")

        with col4:
            if atd1:
                cnpj_update = st.text_input("CNPJ: ",placeholder="Atualize o CNPJ")
            else:
                cnpj = st.text_input("CNPJ:  ",placeholder="Insira o CNPJ")

        with col5:
            if  atd1:
                numero_update = st.text_input('Numero de celular: ',value=preenchimento[4],placeholder='Atualize o numero de celular')
            else:
                numero = st.text_input('Numero de celular:  ',placeholder='Defina o numero de celular')

            if atd1:
                email_update = st.text_input('E-mail: ',value=preenchimento[6],placeholder='Atualize o E-mail')
            else:
                email = st.text_input('E-mail:  ',placeholder='Defina o E-mail')

        with col8:
            if  atd1:
                vendedor_update = st.text_input('Nome do vendedor: ',value=preenchimento[5],placeholder='Atualize o nome do vendedor')
            else:
                vendedor = st.text_input('Nome do vendedor:  ',placeholder='Defina o nome do vendedor')

        with col9:
            if  atd1:
                endereço_update = st.text_input('Endereço: ',value=preenchimento[5],placeholder='Atualize o endereço')
            else:
                endereço = st.text_input('Endereço:  ',placeholder= 'Defina o endereço')

        with col11:
            if atd1:
                material_update = st.text_input('Material de venda: ',value=preenchimento[10],placeholder='Atualize o material')
            else:
                material = st.text_input('Material de venda:  ',placeholder='Insira o material')   

            if atd1:
                material1_update  = st.text_input('Material de venda:  ',value=preenchimento[10],placeholder='Atualize o material')
            else:
                material1 = st.text_input('Material de venda:   ',placeholder='Insira o material')   

            if atd1:
                material2_update = st.text_input('Material de venda:   ',value=preenchimento[10],placeholder='Atualize o material')
            else:
                material2 = st.text_input('Material de venda:    ',placeholder='Insira o material')   

        jmp,jmp1 = st.columns([1,13])
        with jmp:
            if atd1:
                atl = st.button('Enviar 📤 ')
                btn = 0
            else:
                btn = st.button('Enviar 📤 ')
                atl = 0

        with jmp1:
            if atd1:
                deletar_linha = st.button("Excluir 🗑 ")
                if deletar_linha:
                    st.toast('Excluindo Linha...')
                    time.sleep(1)
                    st.toast('Linha Excluida!')
                    cursor12.execute(f'DELETE FROM fornecedores WHERE ID = {ids_update};')
                    conn12.commit()

    else:
        btn = 0
        atl = 0
    if btn:
        st.toast('Inserindo Linha...')
        time.sleep(1)
        st.toast('Linha Inserida!')
        st.balloons()
        cursor12.execute("INSERT INTO fornecedores (ID,Nome,CNPJ,Vendedor,Endereço,Email,Material,Material1,Material2) VALUES (?,?,?,?,?,?,?,?,?)", (ids,nome,cnpj,vendedor,endereço,email,material,material1,material2))
        conn12.commit()
    
    if atl:
        st.toast('Atualizando Linha...')
        time.sleep(1)
        st.toast('Linha Atualizada!')
        st.balloons()
        cursor12.execute("UPDATE fornecedores SET Nome = ?,CNPJ = ?,Vendedor = ?, Endereço = ?, Email = ?, Material = ?, Material1=?, Material2 = ? WHERE ID = ?",(nome_update,cnpj_update,vendedor_update,endereço_update,email_update,material_update,material1_update,material2_update,ids_update))
        conn12.commit()

if 1 == 0:
    consulta = f"SELECT * FROM {base_de_dados} WHERE Quantidade <= 1"
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
        'Setor:es': ['PRODUÇÃO','FERRAMENTARIA', 'ADMINISTRATIVO', 'COMERCIAL', 'Serralharia', 'Elétrica', 'MecÂnica','EXPEDIÇÃO','T.I'],
        'Valores': [read_0, read_1, read_2, read_3, read_4, read_5, read_6,read_7,read_8]
        })

        st.bar_chart(source,x='Setor:es',y='Valores',color= '#6346F5',width=190)


