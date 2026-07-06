import streamlit as st
import random
from german_words_500 import german_words

st.title("🇩🇪 German Vocabulary Quiz")

if "word" not in st.session_state:
    st.session_state.word = random.choice(list(german_words.keys()))

word = st.session_state.word
correct_answer = german_words[word]

st.header(word)

answer = st.text_input("Enter the English meaning:")

if st.button("Check"):
    if answer.strip().lower() == correct_answer.lower():
        st.success("Correct! 🎉")
        st.session_state.word = random.choice(list(german_words.keys()))
        st.rerun()
    else:
        st.error("Kyu nahi ho rahe padhaye 😭")
        st.write(f"Correct answer: **{correct_answer}**")