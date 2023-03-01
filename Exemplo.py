import streamlit as st

try:
    st.title('Sistema de Recomendações - Case 7')
    menu = ['','Recomendações de Itens','Recomendações de Usuários']

    st.sidebar.title('Selecione uma das opções abaixo')
    o = st.sidebar.selectbox('Selecione uma opção', options=menu)

    if o == 'Recomendações de Itens':
        st.subheader('Recomendação de Itens')
        st.markdown('Digite abaixo o ID do usuário para receber as recomendações de itens:')

        with st.form(key='Recomendar Item'):
            idu = st.text_input(label = 'Digite o ID do usuário')
        
            verificar_id = st.form_submit_button('Recomendar Item')
        
        if verificar_id:
            if idu == '':

                st.warning('ID não preenchido')
            
            elif idu.isnumeric():
                st.success(f'A recomendação para o id {idu} é o Item X')
            
            else:
                st.warning('ID inválido')
        
    if o == 'Recomendações de Usuários':
        st.subheader('Recomendação de Usuários')
        st.markdown('Digite abaixo o ID do item para receber as recomendações de usuários:')

        with st.form(key='Recomendar'):
            idi = st.text_input(label = 'Digite o ID do item')
        
            verificar_item = st.form_submit_button('Recomendar')
        
        if verificar_item:
            if idi == '':

                st.warning('ID não preenchido')
            
            elif idu.isnumeric():
                st.success(f'A recomendação para o id {idi} é o Usuário X')
            
            else:
                st.warning('ID inválido')

except:
    st.experimental_rerun