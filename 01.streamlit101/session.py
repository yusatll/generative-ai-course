import streamlit as st
import pandas as pd

st.header("Session state mekanizması")

if "satir_sayisi" not in st.session_state:
    st.session_state.satir_sayisi = 10

df = pd.read_csv("data.csv", sep=",")

st.table(df.head(st.session_state.satir_sayisi))

# callback func
def artir():
    st.session_state.satir_sayisi += 1

def azalt():
    st.session_state.satir_sayisi -= 1

artir_btn = st.button(label="Arttır", on_click=artir)
azalt_btn = st.button(label="Azalt", on_click=azalt)

st.divider()
st.header(st.session_state.satir_sayisi)

# import streamlit as st

# st.session_state.mesaj = "bilgilendirme mesajı"
# st.session_state.yil = 2024


# st.write(st.session_state)

# st.session_state.eposta = st.text_input(label="Eposta girin")
# st.text_input(label="Şifre girin", type="password", key="sifre")

# goruntule_btn = st.button(label="Görüntüle")

# if goruntule_btn:
#     st.info(st.session_state.eposta)
#     st.info(st.session_state.sifre)