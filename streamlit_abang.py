import streamlit as st
import math

def hitung_luas_bujursangkar(s):
    luas = s * s
return luas

st.title("lagi bikin kalkulator")

s = st.number_input("Masukkan panjang sisinya (cm) : ")

if st.button("Ayo hitung luasnya"):
  result = hitung_luas_bujursangkar(s)
  st.success(f"Luas bujur sangkar adalah {result} cm^2")
  
  
