import pandas as pd
import streamlit as st
from PIL import Image
import time as time
import datetime as datetime
import webbrowser
import sqlite3
import openpyxl
import altair as alt
import pytz
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.customize_running import center_running
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.image_in_tables import table_with_images
from streamlit_extras.metric_cards import style_metric_cards

style_metric_cards()
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
        Fornecedor2 TEXT,
        Custo TEXT,
        Data_de_entrada DATE,
        Hora_de_entrada TIME,
        Mês 
        
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

    cl = st.button("DELETAR TABELAS")
    if cl:
        cursor12.execute("DROP TABLE Materiais")
        conn12.commit()

    conn = sqlite3.connect('./Data/Setores')
    cursor = conn.cursor()

st.header('Materiais e fornecedores de :blue[manutenção!]')
tab6, tab7,tab8= st.tabs(["📝 Cadastro de materiais", " 🚛 Fornecedores", "💰 Custos de materiais"])
with tab6:
    st.header('📝 Cadastro de :blue[Materiais]',divider='blue')
    col1,col2,col3,col4 = st.columns([2,8,4,0.1])
    with col1:
        with st.expander('💡'):
            Setor = st.radio(
            "Selecione",
            ['ALL','Elétrica',"Mecânica","Serralharia",'Ferramentaria','Produção'],
            index=0,
            )

    consulta3 = f"SELECT * FROM Materiais"
    numero1 = pd.read_sql_query(consulta3, conn12)
    numero2 = numero1.shape[0]
    x,x1 = st.columns([1,1])
    with x:
        st.metric(label='Total:',value=numero2)
    dt = numero1.drop(columns=['Mês'])
    def load_dataa():
        return pd.DataFrame(dt)
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
                Quantidade_update = st.number_input("Quantidade",min_value=0,max_value=1000,value=preenchimento[1],placeholder="Atualize o valor")
            else:
                Quantidade = st.number_input("Quantidade",min_value=0,max_value=1000,value=0,placeholder="Insira o valor")
            if  atd:
                Unidade_update = st.selectbox('Unidade',('UN','CM','MT','KG','G','L','M²','M³'),placeholder='Atualize a Unidade')
       
            else:
                Unidade = st.selectbox('Unidade',('UN','CM','MT','KG','G','L','M²','M³'),placeholder='Escolha uma Unidade')
            with col4:
                if  atd:
                    Setor_update = st.selectbox('Setor:',('Elétrica','Mecânica','Serralharia','Ferramentaria','Produção'),index=None, placeholder='Atualize o Setor')
                else:
                    Setor = st.selectbox('Setor:',('Elétrica','Mecânica','Serralharia','Ferramentaria','Produção'),index=None,placeholder='Escolha o Setor')
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
                codigo_update = st.text_input('Codigo TOTVS:',value=preenchimento[7],placeholder='Atualize o código')
            else:
                Fornecedor = st.text_input('Codigo TOTVS:',value='**.***.**-****',placeholder='Insira o código')
        with col9:
            if  atd:
                Solicitado_update = st.selectbox('Solicitado?:',('Sim','Não'),index=1,placeholder='Sim ou Não?')
            else:
                Solicitado = st.selectbox('Solicitado?:',('Sim','Não'),index=1,placeholder='Sim ou Não?',)

            if atd:
                solicitacao_update = st.number_input("N° da solicitação:",min_value=0,max_value=10000,value=preenchimento[9],placeholder="Insira um valor")
            else:
                solicitacao = st.number_input("N° da solicitação:",min_value=0,max_value=10000,placeholder="Atualize o valor")

            if atd:
                custo_update = st.number_input("Custo unitario:",value=0.0,step=0.1,placeholder="Insira um valor")
                custo_update= str(custo_update).replace(",", ".")
                custo_update = f"{custo_update} R$"
            else:
                custo = st.number_input("Custo unitario:",value=0.0,step=1.0,placeholder="Atualize o valor")
                custo = str(custo).replace(",", ".")
                custo = f"{custo} R$"       
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
            if not atd:
                omaga = [Unidade,Setor,Fabricante,Catalogo,descricao,custo]
                bools = []
                for busca in omaga:
                    if not busca:
                        bools.append(False)
                    else:
                        bools.append(True)
                if atd:
                    ''
                else:
                    if bools[0] == True and bools[1] == True and bools[2] == True and bools[3] == True and bools[4] == True and bools[5] == True:
                        btn = st.button('Enviar 📤')
                        atl = 0
                    else:
                        btn = 0
                        atl = 0
            else:
                btn = 0
                atl = 0
                atl = st.button('Enviar 📤')
                
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
        cursor12.execute("INSERT INTO Materiais (ID,Quantidade,Unidade,Setor,Fabricante,Catalogo,Descrição,Codigo,Solicitado,N°,Fornecedor,Fornecedor1,Custo,Data_de_entrada,Hora_de_entrada) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (ids,Quantidade,Unidade,Setor,Fabricante,Catalogo,descricao,Fornecedor,Solicitado,solicitacao,Fornecedor1,Fornecedor2,custo,datenow,timenow))
        conn12.commit()
    
    if atl:
        st.toast('Atualizando Linha...')
        time.sleep(1)
        st.toast('Linha Atualizada!')
        st.balloons()
        cursor12.execute("UPDATE Materiais SET Quantidade = ?,Unidade = ?,Setor = ?, Catalogo = ?, Descrição = ?, Codigo = ?, Solicitado =?, N° = ?, Fornecedor = ?, Fornecedor1 = ? ,Custo = ? WHERE ID = ?",(Quantidade_update,Unidade_update,Setor_update,Catalogo_update,descricao_update,codigo_update,Solicitado_update,solicitacao_update,Fornecedor1_update,Fornecedor2_update,custo_update,ids_update))
        conn12.commit()

with tab7:
    st.header('🚛 :blue[Fornecedores]',divider='blue')
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
        'Setor:es': ['PRODUÇÃO','FERRAMENTARIA', 'ADMINISTRATIVO', 'COMERCIAL', 'Serralharia', 'Elétrica', 'Mecânica','EXPEDIÇÃO','T.I'],
        'Valores': [read_0, read_1, read_2, read_3, read_4, read_5, read_6,read_7,read_8]
        })

        st.bar_chart(source,x='Setor:es',y='Valores',color= '#6346F5',width=190)

with tab8:
    st.header('💰 Custo de :blue[Materiais]',divider='blue')
    col,col1 = st.columns([1,1])
    with col:
        container= st.container(border=True)
        consulta3 = f"SELECT * FROM Materiais"
        numero1 = pd.read_sql_query(consulta3, conn12)
        numero2 = numero1.shape[0]
        new_data = numero1.drop(columns=['ID','Unidade','Descrição','Fabricante','N°','Fornecedor','Fornecedor1','Fornecedor2','Mês'])
        container.metric(label='Total:',value=numero2)
        container.header(':red[Materiais e preços!]',divider='blue')
        def load_dataa():
            return pd.DataFrame(new_data)
        container.checkbox("Estender", value=False, key="use_container_width")
        df = load_dataa()
        container.dataframe(df, use_container_width =st.session_state.use_container_width)
        custo = df['Custo']
        soma = 0
        for i in custo:
            valor_sem_simbolo = i.replace("R$", "").strip()
            soma += float(valor_sem_simbolo)
    with col1:
        container = st.container(border=True)
        consulta3 = f"SELECT * FROM Materiais WHERE Setor = 'Elétrica'"
        e = pd.read_sql_query(consulta3, conn12)
        e = e['Custo']
        c1 = 0
        for a in e:
            valor_sem_simbolo = a.replace("R$", "").strip()
            c1 += float(valor_sem_simbolo)
            
        consulta3 = f"SELECT * FROM Materiais WHERE Setor = 'Mecânica'"
        m = pd.read_sql_query(consulta3, conn12)
        m = m['Custo']
        c2 = 0
        for b in m:
            valor_sem_simbolo = b.replace("R$", "").strip()
            c2 += float(valor_sem_simbolo)
            
        consulta3 = f"SELECT * FROM Materiais WHERE Setor = 'Serralharia'"
        s = pd.read_sql_query(consulta3, conn12)
        s = s['Custo']
        c3 = 0
        for c in s:
            valor_sem_simbolo = c.replace("R$", "").strip()
            c3 += float(valor_sem_simbolo)

        consulta3 = f"SELECT * FROM Materiais WHERE Setor = 'Ferramentaria'"
        f = pd.read_sql_query(consulta3, conn12)
        f = f['Custo']
        c4 = 0
        for d in f:
            valor_sem_simbolo = d.replace("R$", "").strip()
            c4 += float(valor_sem_simbolo)

        consulta3 = f"SELECT * FROM Materiais WHERE Setor = 'Produção'"
        p = pd.read_sql_query(consulta3, conn12)
        p = p['Custo']
        c5 = 0
        for g in p:
            valor_sem_simbolo = g.replace("R$", "").strip()
            c5 += float(valor_sem_simbolo)

        def get_chart_63301528():
            import plotly.graph_objects as go
            labels = ['Elétrica','Mecânica','Serralharia','Ferramentaria','Produção']     
            values = [c1,c2,c3,c4,c5]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
            oi =  container.plotly_chart(fig, theme="streamlit")
            return oi
        soma = "{:,.1f}".format(float(soma)).replace(".", ",",1).replace(",", ".", 1)
        container.metric(label='Total:',value=f'{soma} R$')
        #with container.expander('alou'):
        container.header(':red[Valores de materiais por setor!]',divider='blue')
        get_chart_63301528()
        x,x1 = container.columns([0.1,8])