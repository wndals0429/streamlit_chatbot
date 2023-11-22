import streamlit as st
import openai
st.title("chatbot with openai gpt")
st.caption("made by wisdom")

with st.sidebar:
    st.markdown("[get an openai api key](https://platform.openai.com/account/api-keys)")

client = openai(api_key=st.secrets["openai_api_key"])
st.write(st.secrets["nonexistent_key"])
if "openai_model" not in at.session_state:
    st.session_state["openai_model"]="gpt-3.5-turbo"
if"messages" not in st.session_state:
    st.session_state.message = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("what is up?"):
    st.session_state.message.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response =""
        for response in client.chat.cinpletions.create(
            model=st.session_state["openai_model"],
            messages={
                {"role": m["fole"], "content": m["content"]}
                for m in st.session_state,messages
            },
            stream=True,
        ):
            full_response +=(response.choices[0].delta.content or"")
            message_placeholder.markdown(full_response+ "")
        message_placeholder.markdown(full_response)
    st.session_state.messges.append({"role": "assistant", "content":full_response})