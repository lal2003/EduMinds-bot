<<<<<<< HEAD
import openai
import streamlit as st


# Streamlit application
st.title("🤖EduMinds")
st.title("Your personal assistant")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()

def chat_interface():
    # Initialize session state if not already done
    if 'conversations' not in st.session_state:
        st.session_state.conversations = []

    # Display conversation history
    for user_input, response in st.session_state.conversations:
        st.markdown(f"### 🔣you:\n {user_input}")
        st.markdown(f"#### ⚙️EduMinds:\n {response}")
        st.markdown('---')

    # User input and Send button
    user_input_key = st.session_state.user_input_count if 'user_input_count' in st.session_state else 0
    user_input = st.text_input(f"🔣Your message to EduMinds:", key=f"user_input_{user_input_key}")
    send_button = st.button("Submit")

    if send_button and user_input:
        # Get response from GPT-3.5 Turbo
        response = chat_with_gpt(user_input)
        
        # Update conversation history
        st.session_state.conversations.append((user_input, response))
        
        # Clear the input field
        st.session_state.user_input_count = user_input_key + 1
        
        # Rerun the app to update the interface
        st.experimental_rerun()

if __name__ == "__main__":
    chat_interface()
=======
import streamlit as st

st.write('EduMinds')
>>>>>>> 36ce895 (uploaded)
