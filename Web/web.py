#instalar o streamlit
#pip install streamlit

#importando a biblioteca
import streamlit as st

st.title("Calculadora de IMC")

peso = st.number_input("Digite seu peso (kg)", min_value=1.0, value=70.0)
altura = st.number_input("Digite sua altura (m)", min_value=0.1, value=1.75)

if st.button("Calcular"):
  imc = peso / (altura**2)
  st.write(f"Seu IMC é: {imc:.2f}")

  if imc < 18.5:
    st.warning("Abaixo do peso")
  elif imc < 25:
    st.success("Peso normal")
  elif imc < 30:
    st.warning("Sobrepeso")
  else:
    st.error("Obesidade")