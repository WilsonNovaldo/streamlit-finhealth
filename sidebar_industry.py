import streamlit as st

def sidebar_industry():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Choose year 🔢\n"  # noqa: E501
            "2. Choose sector 🏭\n"
            "3. Press generate plot 👆\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "💵 Industry analysis allows you to compare PE ratio, ROE, and ROCE of company from the same sector."
            "This analysis helps investors identify stocks that may be undervalued or have better financial performance compared to their peers, assisting in making informed investment decisions."
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by Wilson Novaldo")
        st.markdown("---")
