import streamlit as st
from password_generators import RandomPasswordGenerator, MemorablePasswordGenerator, PinCodeGenerator
from nltk.corpus import words

# Title of the application
st.image('./images/banner.jpeg')
st.title(":zap: Password Generator")

option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Random Password':
    length = st.slider("Length", min_value=5, max_value=50, value=8)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")

    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
elif option == 'Memorable Password':
    no_of_words = st.slider("Number of Words", min_value=2, max_value=10, value=5)
    separator = st.text_input("Separator", value='-')
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(no_of_words, separator, capitalization, words.words())
else:
    length = st.slider("Length", min_value=2, max_value=10, value=4)

    generator = PinCodeGenerator(length)

password = generator.generate()
st.write("Your password is:")
st.header(fr"``` {password} ```")
