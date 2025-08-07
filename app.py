import streamlit as st

st.set_page_config(page_title="Period Pal")
st.title("Period Pal")
menu = ["Home", "New Entry"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.header("Welcome to Period Pal")
    df = load_entries()
    if df.empty:
        st.warning("No entries found. Add an entry in 'New Entry'")
    else:
        st.subheader("will add stuff here")
elif choice == "New Entry":
    st.header("Add a New Entry")

    entry_date = st.date_input("Select Date", date.today())
    on_period = st.checkbox("Period Today?")
    mood = st.radio("How do you feel?", ['😁', '🙂', '😐','😔', '😖'])
    journal = st.text_area("Journal Entry", max_chars=500)
    if st.button("Save Entry"):
        sentiment = analyze_sentiment(journal)
        save_entry(entry_date, on_period, mood, journal)


