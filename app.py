import ollama as client
import streamlit as st
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)




def stream_data(stream):
     for chunk in stream:
        yield chunk['message']['content'] + ""

def main():
    st.sidebar.image("C:/Users/hp\Downloads/test (2)/ollama-chatbot-main/ollama-chatbot-main/logo.png", use_column_width=True)
    st.sidebar.write("##")
    st.sidebar.write("##")
    default_value = "home"

    if st.sidebar.button("Ask from my data"):
        default_value = "mydata"
    st.title("FGIL AI Chat 💬")

    if "llm_model" not in st.session_state:
        st.session_state["llm_model"] = "Llama2"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat(
                model=st.session_state["llm_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )

            response = st.write_stream(stream_data(stream))
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()