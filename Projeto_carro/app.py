import streamlit as st

st.sidebar.image("img/logo.jpg") 
st.sidebar.markdown("# Vel'car")

lista_carros = ["Corsa","Marea","Uno da firma"]
detalhes_carro = {
    "Corsa":{"preço": 500, "portas":"2 Portas", "cor":"Prata"},
    "Marea":{"preço": 800, "portas":"4 Portas", "cor":"Preto"},
    "Uno da firma":{"preço": 550, "portas":"4 Portas", "cor":"Prata"}}

carro_selecionado = st.sidebar.selectbox("Selecione o carro que deseja", lista_carros)
detalhes_selecionado = detalhes_carro[carro_selecionado]

st.title("Bem vindo(a) a Vel'Car")
st.image(f"img/{carro_selecionado}.jpg")

st.subheader("🚗 Detalhes do Veículo")


col1, col2, col3 = st.columns(3)


col1.metric("Preço Diária", f'R$ {detalhes_selecionado["preço"]}')
col2.metric("Portas", detalhes_selecionado["portas"])
col3.metric("Cor", detalhes_selecionado["cor"])


st.divider()


qtd_dias = st.number_input("Quantos dias quer ficar com o carro?", 1)



if st.button("Alugar", type="primary"):
    st.success(f'O aluguel do carro vai custar: **R$ {qtd_dias * detalhes_selecionado["preço"]}**')