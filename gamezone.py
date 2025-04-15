import streamlit as st
from streamlit_option_menu import option_menu
import random
import string
import time


def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;  
            background-position: center;
            background-repeat: no-repeat;}}</style>""",unsafe_allow_html=True)

image_url ="https://img.freepik.com/free-vector/gradient-black-background-with-wavy-lines_23-2149151738.jpg"
set_background(image_url)
   
def password_generator():
    st.title(":green[PASSWORD GENERATOR]")
    length = st.slider("Password Length:", min_value=8, max_value=32, value=12)
    include_lowercase = st.checkbox("Include Lowercase Letters", value=True)
    include_uppercase = st.checkbox("Include Uppercase Letters", value=True)
    include_digits = st.checkbox("Include Digits", value=True)
    include_symbols = st.checkbox("Include Symbols", value=True)
    if st.button(":green[Generate Password]"):
        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        if not characters:
            st.warning("Please select at least one character type.")
            return
        password = ''.join(random.choice(characters) for _ in range(length))
        st.subheader(":green[Generated Password:]")
        st.code(password, language="text")

def rock_paper_scissors():
    st.title(" :grey[Rock Paper Scissors] ✊🖐✌")
    choices = ["Rock", "Paper", "Scissors"]
    images = {"Rock": "r1.png","Paper": "r2.png","Scissors": "r3.png"}
    st.markdown("## Choose your move:")
    user_choice = st.radio("", choices, horizontal=True)
    if st.button("Play"):
        comp_placeholder = st.empty()
        comp_placeholder.info("computer is choosing...")
        time.sleep(1.5)
        comp_choice = random.choice(choices)
        comp_placeholder.empty()
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("You")
            st.image(images[user_choice], width=150)
        with col2:
            st.subheader("Computer")
            st.image(images[comp_choice], width=150)
        if user_choice == comp_choice:
            st.info("It's a tie!")
        elif ((user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Scissors" and comp_choice == "Paper")):
            st.success("You win!")
        else:
            st.error("Computer wins!")
    else:
        st.image(images["Rock"], width=150)
        st.info("Choose and click play to start the game!")

def word_scramble():
    st.title("🧠 :violet[WORD SCRAMBLE GAME]")
    word_list = ["python", "streamlit", "developer", "algorithm", "function", "variable", "interface", "keyboard", "project", "software"]

    if "original_word" not in st.session_state:
        st.session_state.original_word = random.choice(word_list)
        st.session_state.scrambled_word = "".join(random.sample(st.session_state.original_word, len(st.session_state.original_word)))

    st.subheader("🔀 Unscramble this word:")
    st.code(st.session_state.scrambled_word.upper())
    user_guess = st.text_input("Your Guess:")
    if st.button("Submit Guess"):
        if user_guess.lower() == st.session_state.original_word:
            st.success("🎉 Correct! You unscrambled it!")
        else:
            st.error("❌ Oops! Try again.")

    if st.button("New Word 🔁"):
        st.session_state.original_word = random.choice(word_list)
        st.session_state.scrambled_word = "".join(random.sample(st.session_state.original_word, len(st.session_state.original_word)))
        st.rerun()

def rolling_dice():
    st.title("🎲 :orange[DICE ROLLER GAME]")
    dice_images = { 1: "d1.png", 2: "d2.png", 3: "d3.png", 4: "d4.png", 5: "d5.png", 6: "d6.png" }
    dice_placeholder = st.empty()
    if st.button("Roll the Dice 🎲"):
        for _ in range(10):
            temp_roll = random.randint(1, 6)
            dice_placeholder.image(dice_images[temp_roll], width=150)
            time.sleep(0.1) 
        final_roll = random.randint(1, 6)
        dice_placeholder.image(dice_images[final_roll], width=150)
        st.success(f"You rolled a {final_roll}!")
    else:
        st.image("d1.png", width=150)
        st.info("Click the button to roll the dice!")   

def about_gamezone():
    st.title(":orange[ABOUT GAMEZONE]")
    st.markdown("---")
    st.write("Welcome to GameZone, your collection of simple and entertaining games built using the Streamlit framework in Python!")
    st.write("This project was created to showcase how basic Python can be used to build interactive web applications.")
    st.subheader("Games Included:")
    st.markdown("- **:green[Password Generator:]** A tool to create strong and secure passwords.")
    st.markdown("- **:orange[Rolling Dice:]** Dice throwing for ludo made easy.")
    st.markdown("- **:violet[Word Scramble:]** A fun word puzzle to test your vocabulary.")
    st.markdown("- **:grey[Rock Paper Scissors:]** The timeless game of chance against the computer.")
    st.markdown("---")
    st.write("Enjoy playing and feel free to explore the code!")

with st.sidebar:
    st.title(":red[GAMEZONE]")
    choice = option_menu("MENU:", ["Main Page","About","Password Generator","Rolling Dice", "Word Scramble", "Rock Paper Scissors"])
if choice == "Password Generator":
    password_generator()
elif choice == "Rolling Dice":
    rolling_dice()
elif choice == "Word Scramble":
    word_scramble()
elif choice == "Rock Paper Scissors":
    rock_paper_scissors()
elif choice == "About":
    about_gamezone()

else:
    st.title(":red[WELCOME TO GAMEZONE!]")
    st.subheader("Pick a game from the sidebar to start playing!")
    st.markdown("---")
    st.write("This is your one-stop shop for simple and fun games built with Python and Streamlit!")
    st.write("Enjoy Generating secure passwords, unscrambling words, dice rolling made easy and challenging the computer to Rock Paper Scissors.")
    st.markdown("---")
    st.write("Project Made By-LAKSHITA , MANASVI and KANIKA")
    