CORRECTIONS FOR app.py

1) Fix wrong_gifs:
Add a comma after:

"https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",

2) Paste this block ABOVE 'if submitted:':

# ---------------- QUIZ ----------------

word = st.session_state.word

word_info = german_words[word]

correct_answer = word_info['meanings']
example_de = word_info['example_de']
example_en = word_info['example_en']

st.header(word)

if st.button("📖 Show Example Sentence"):
    if example_de:
        st.info(example_de)
        st.info(example_en)
    else:
        st.warning(
            "No example sentence available yet."
        )

with st.form("quiz_form"):
    answer = st.text_input(
        "Enter the English meaning:"
    )

    submitted = st.form_submit_button(
        "Check"
    )
