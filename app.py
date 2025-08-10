# app.py
import streamlit as st
from regex_logic import extract_domain_name
from regex_explainer import explain_regex

st.title("Domain Extractor & Regex Explainer")

url = st.text_input("Enter a URL (for example: https://www.google.com)")

if st.button("Extract"):
    domain, pattern = extract_domain_name(url)

    if domain:
        st.success(f"Extracted domain: {domain}")
        st.subheader("Regex pattern used")
        st.code(pattern, language="regex")
        st.subheader("How the regex works")
        st.markdown(explain_regex(pattern))
    else:
        st.error("No valid domain found. Try another URL like 'https://www.google.com'")
