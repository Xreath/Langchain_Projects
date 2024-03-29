import Langchain_Helper.lc_helper as lch
import streamlit as st

st.title("Pets Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?",("Cat","Dog","Cow","Hamster"))
language_tpye = st.sidebar.selectbox("What is your Language",("English","Spanish","German","Turkish"))
if animal_type == "Dog":
  pet_color = st.sidebar.text_area(
    label="What color is your dog?",
    max_chars=15
    )

if animal_type == "Cat":
  pet_color = st.sidebar.text_area(
    label="What color is your cat?",
    max_chars=15
    )

if animal_type == "Hamster":
  pet_color = st.sidebar.text_area(
    label="What color is your hamster?",
    max_chars = 15
    )

if animal_type == "Cow":
  pet_color = st.sidebar.text_area(label="What color is your cow?", max_chars = 25)


if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color, language_tpye)
    st.text(response)