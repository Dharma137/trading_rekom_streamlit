modal = st.number_input("Modal akun ($):", min_value=0.0)
risk_persen = st.number_input("Risk per trade (%):", min_value=0.0, max_value=100.0, value=1.0)
stop_loss_poin = st.number_input("Jarak Stop Loss (poin):", min_value=0.0)import streamlit as st

st.title("Rekomendasi Entry Trading + Kalkulasi Lot")

# Input harga
harga_sekarang = st.number_input("Masukkan harga saat ini:", min_value=0.0)

# Input modal dan risk
modal = st.number_input("Modal akun ($):", min_value=0.0)
risk_persen = st.number_input("Risk per trade (%):", min_value=0.0, max_value=100.0, value=1.0)
stop_loss_poin = st.number_input("Jarak Stop Loss (poin):", min_value=0.0)

if harga_sekarang and modal and stop_loss_poin:
    # Hitung risk per trade dalam dollar
    risk_dollar = modal * (risk_persen / 100)

    # Asumsi nilai per poin = $1 per lot
    lot_size = risk_dollar / stop_loss_poin

    st.write(f"**Risk per trade:** ${risk_dollar:.2f}")
    st.write(f"**Lot size ideal:** {lot_size:.2f} lot")

    # Rekomendasi sederhana
    if harga_sekarang < 50000:
        st.success("Rekomendasi: BUY")
        st.write("Take Profit di:", harga_sekarang + 1000)
        st.write("Stop Loss di:", harga_sekarang - stop_loss_poin)
    elif harga_sekarang > 60000:
        st.error("Rekomendasi: SELL")
        st.write("Take Profit di:", harga_sekarang - 1000)
        st.write("Stop Loss di:", harga_sekarang + stop_loss_poin)
    else:
        st.info("Rekomendasi: WAIT & SEE")
