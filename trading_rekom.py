import streamlit as st

st.title("Rekomendasi Entry Trading")

# Input harga dari user
harga_sekarang = st.number_input("Masukkan harga saat ini:", min_value=0.0)

# Logika sederhana rekomendasi
if harga_sekarang:
    if harga_sekarang < 50000:
        st.success("Rekomendasi: BUY")
        st.write("Take Profit di:", harga_sekarang + 1000)
        st.write("Stop Loss di:", harga_sekarang - 500)
    elif harga_sekarang > 60000:
        st.error("Rekomendasi: SELL")
        st.write("Take Profit di:", harga_sekarang - 1000)
        st.write("Stop Loss di:", harga_sekarang + 500)
    else:
        st.info("Rekomendasi: WAIT & SEE")
