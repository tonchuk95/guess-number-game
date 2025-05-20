import streamlit as st
import random

st.title("🎯 Гра 'Вгадай число'")

# ініціалізація "секретного числа" в сесії
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 10)
    st.session_state.tries = 0
    st.session_state.solved = False

if not st.session_state.solved:
    guess = st.number_input("Введи число від 1 до 10", min_value=1, max_value=10, step=1)
    if st.button("Перевірити"):
        st.session_state.tries += 1
        if guess < st.session_state.secret:
            st.warning("🔼 Більше!")
        elif guess > st.session_state.secret:
            st.warning("🔽 Менше!")
        else:
            st.success(f"🎉 Ти вгадав з {st.session_state.tries}-ї спроби!")
            st.session_state.solved = True
else:
    if st.button("Почати заново"):
        st.session_state.secret = random.randint(1, 10)
        st.session_state.tries = 0
        st.session_state.solved = False
