import streamlit as st
import json

# Load data from JSON file
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

# Main function to run the app
def main():
    st.title("User Information App")
    
    # Load user data
    data = load_data()
    
    # Input field for user ID
    user_id = st.text_input("Enter User ID:")
    
    # Submit button
    if st.button("Submit"):
        if user_id in data:
            user_info = data[user_id]
            st.write(f"**Name:** {user_info['name']}")
            st.write(f"**Email:** {user_info['email']}")
            st.write(f"**Age:** {user_info['age']}")
        else:
            st.error("User ID not found.")

if __name__ == "__main__":
    main()
