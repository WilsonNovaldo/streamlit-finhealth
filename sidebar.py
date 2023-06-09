import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload your csv or excel file on the bottom of the page 📄\n"  # noqa: E501
            "2. Press predict 🔑\n"
            "3. That's it! 💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "💵 FinHealth Classifier allows you to classify whether a company "
            "has a good or bad financial health based on the indicator we have. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by Wilson Novaldo")
        st.markdown("---")
