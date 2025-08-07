import streamlit as st
import pandas as pd

# Initialize session state for score tracking
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'name' not in st.session_state:
    st.session_state.name = ""

# Function to ask a question
def ask_question(question, options, correct_option):
    st.write(question)
    choice = st.radio("Kies een antwoord:", options, key=question)
    if st.button("Bevestig", key=question + "_confirm"):
        if choice == correct_option:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Fout antwoord.")

# Title and name input
st.title("🔐 Escape Room: De Verloren Marktdata")
st.write("Welkom bij de escape room over marktonderzoek. Vul je naam in en los de puzzels op!")
st.session_state.name = st.text_input("Naam van leerling:")

if st.session_state.name:
    st.header("Kamer 1: Wat is marktonderzoek?")
    ask_question(
        "Wat is het doel van marktonderzoek?",
        ["Beslissingen nemen op basis van gevoel", "Waardevolle inzichten verkrijgen", "Producten willekeurig aanpassen"],
        "Waardevolle inzichten verkrijgen"
    )

    st.header("Kamer 2: Onderzoeksvraag")
    ask_question(
        "Welke van deze is een goede onderzoeksvraag?",
        ["Waarom is product X gedaald?", "Is product X slecht?", "Waarom kopen mensen niets?"],
        "Waarom is product X gedaald?"
    )

    st.header("Kamer 3: Onderzoeksmethoden")
    ask_question(
        "Wat is een voorbeeld van fieldresearch?",
        ["Statistieken van de overheid", "Enquête afnemen op straat", "Boekhouding analyseren"],
        "Enquête afnemen op straat"
    )

    st.header("Kamer 4: Validiteit & Betrouwbaarheid")
    ask_question(
        "Wat verhoogt de betrouwbaarheid van een onderzoek?",
        ["Elke respondent een andere vraag stellen", "Gestandaardiseerd meetinstrument gebruiken", "Resultaten negeren"],
        "Gestandaardiseerd meetinstrument gebruiken"
    )

    st.header("Kamer 5: Big Data")
    ask_question(
        "Wat is een risico bij big data?",
        ["Altijd correcte data", "Privacyproblemen", "Geen analyse nodig"],
        "Privacyproblemen"
    )

    # Show final score and save to CSV
    if st.button("Escape voltooid! Bekijk je score"):
        st.write(f"Bedankt {st.session_state.name}, je score is: {st.session_state.score}/5")

        # Save score to CSV
        result = pd.DataFrame([[st.session_state.name, st.session_state.score]], columns=["Naam", "Score"])
        if os.path.exists("escape_room_scores.csv"):
            existing = pd.read_csv("escape_room_scores.csv")
            updated = pd.concat([existing, result], ignore_index=True)
            updated.to_csv("escape_room_scores.csv", index=False)
        else:
            result.to_csv("escape_room_scores.csv", index=False)
