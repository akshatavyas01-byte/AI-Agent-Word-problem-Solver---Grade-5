import streamlit as st
from agent import agent
import streamlit as st
from agent import agent
from langchain_core.messages import HumanMessage

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Word Problem Solver Grade-5")
st.subheader("Enter the word Problem and receive the solution:")

problem = st.text_input("Enter the problem")

placeholder = st.empty()
stream_text = ""

if st.button("Solve") and problem:
    with st.spinner("Thinking..."):

        for chunk in agent.stream(
            {"messages": [HumanMessage(content=problem)]}
        ):
            # st.write(chunk)
            if "model" in chunk:
                messages = chunk["model"]["messages"]
                msg = messages[-1]

                if msg.content:
                    stream_text = msg.content
                    placeholder.write(stream_text)


    message = {
        "Human_message": problem,
        "AI_message": stream_text
    }

    st.session_state.messages.append(message)

if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown("**Question**")
        st.write(msg["Human_message"])

        st.markdown("**Answer**")
        st.write(msg["AI_message"])
        st.divider()
