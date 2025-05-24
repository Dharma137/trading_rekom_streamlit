import streamlit as st

st.title("Rekomendasi Entry, Stop Loss & Take Profit")

posisi = st.selectbox("Pilih posisi:", ["Buy", "Sell"])

support = st.number_input("Masukkan level Support:", format="%.2f")
resistance = st.number_input("Masukkan level Resistance:", format="%.2f")

risk_reward_ratio = st.slider("Pilih Risk-Reward Ratio:", 1.0, 3.0, 1.5, 0.1)

if st.button("Hitung Rekomendasi"):
    if posisi == "Buy":
        entry = support
        stop_loss = support - (resistance - support) / (risk_reward_ratio + 1)
        take_profit = resistance
    else:  # Sell
        entry = resistance
        stop_loss = resistance + (resistance - support) / (risk_reward_ratio + 1)
        take_profit = support

    st.write(f"**Entry:** {entry:.2f}")
    st.write(f"**Stop Loss:** {stop_loss:.2f}")
    st.write(f"**Take Profit:** {take_profit:.2f}")
