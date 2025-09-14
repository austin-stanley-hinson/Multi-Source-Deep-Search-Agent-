import streamlit as st
from main import graph  # Assuming your graph and functions are in main.py

st.title("Planty Multi-Source Deep Research Agent")

user_input = st.text_input("Ask me anything:")

if st.button("Send") and user_input:
    # Initialize state
    state = {
        "messages": [{"role": "user", "content": user_input}],
        "user_question": user_input,
        "google_results": None,
        "bing_results": None,
        "reddit_results": None,
        "selected_reddit_urls": None,
        "reddit_post_data": None,
        "google_analysis": None,
        "bing_analysis": None,
        "reddit_analysis": None,
        "final_answer": None,
    }

    st.write("🔍 Running parallel research...")
    final_state = graph.invoke(state)

    if final_state.get("final_answer"):
        st.write("**Final Answer:**")
        st.write(final_state["final_answer"])
