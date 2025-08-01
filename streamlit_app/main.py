import streamlit as st
import requests

st.title("FamilySearch Addon")

uploaded = st.file_uploader("Upload image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded is not None:
    st.image(uploaded, caption="Uploaded document")

    if st.button("Process with backend"):
        files = {"file": uploaded.getvalue()}
        resp = requests.post("http://localhost:8000/upload", files=files)
        if resp.status_code == 200:
            data = resp.json()
            st.subheader("Extracted JSON")
            st.json(data["json"])
            st.subheader("GEDCOM")
            st.code(data["gedcom"], language="text")
        else:
            st.error(f"Backend error: {resp.text}")
