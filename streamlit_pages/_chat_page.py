import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from config import BASE_PROMPT, HF_EMAIL, HF_PASS


# Login Credentials
hf_email = HF_EMAIL
hf_pass = HF_PASS

flag = 0


def chat_bot():

    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I help you?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Function for generating LLM response
    def generate_response(prompt_input, email, passwd):

        # Hugging Face Login
        sign = Login(email, passwd)
        cookies = sign.login()
        # Create ChatBot                            
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        global flag
        if flag<1:
            flag+=1
            prompt_input=BASE_PROMPT+prompt_input
        return str(chatbot.chat(prompt_input)).strip('`')

    # User-provided prompt
    if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, hf_email, hf_pass) 
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)