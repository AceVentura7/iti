import streamlit as st
import prompt as pmt


def main():
    st.title("Travel Itinerary Generator")
    
    # Prompt the user for inputs, preferences, personal information, occupation, and dietary habits
    city = st.text_input("Enter the city you want to visit:")
    num_days = st.number_input("Enter the number of days for your trip:", min_value=1, step=1)
    has_excursions = st.checkbox("Include excursions or outdoor events")
    likes_museums = st.checkbox("I like museums")
    likes_cultural_events = st.checkbox("I like cultural events")
    likes_concerts = st.checkbox("I like concerts")
    likes_parties = st.checkbox("I like parties")
    age = st.number_input("Enter your age:", min_value=1, step=1)
    gender = st.selectbox("Select your gender:", ("Male", "Female", "Other"))
    budget = st.number_input("Enter your budget (in USD):", min_value=0, step=10)
    occupation = st.text_input("Enter your occupation:")
    dietary_habits = st.selectbox("Select your dietary habits:", ("Non-Vegetarian", "Vegetarian", "Vegan"))
    
    # Create the itinerary based on user inputs, preferences, personal information, occupation, and dietary habits
    if st.button("Generate Itinerary"):
        with st.spinner('generating'):
                
            likings = (has_excursions, likes_museums, likes_cultural_events, likes_concerts, likes_parties)
            st.write(likings)
            if city and num_days:
                init = pmt.initial_response(city, num_days, str(likings), age, gender, budget, occupation, dietary_habits)
                reply = pmt.get_assistant_reply(init)
                st.write(reply)
                
            else:
                st.warning("Please provide the required inputs.")
        
if __name__ == '__main__':
    main()