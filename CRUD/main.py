import streamlit as st;

with st.form(key="include_client"):
    input_name = st.text_input(label="Digite seu nome:")
    input_age = st.number_input(label="Digite sua idade:", format="%d", step=1)
    input_occupation = st.selectbox("Selecione sua profissão" , ["Desenvolvedor", "Musico", "Arquiteto", "Engenheiro","Advogado"])
    input_submit = st.form_submit_button("Enviar")