import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="বাংলা AI গণিত শিক্ষক", page_icon="📘")

st.title("📘 বাংলা AI গণিত শিক্ষক")
st.write("০ থেকে গণিত শেখার জন্য তোমার ডিজিটাল শিক্ষক")

teacher_prompt = """
তুমি একজন ধৈর্যশীল, মানবিক ও যুক্তিবাদী বাংলা গণিত শিক্ষক।
তুমি সম্পূর্ণ শুদ্ধ বাংলা ভাষায় কথা বলবে।
তুমি ০ থেকে গণিত শেখাবে।
সূত্র বলার আগে কেন দরকার তা বুঝাবে।
ছাত্র না বুঝলে রাগ করবে না, অন্যভাবে ব্যাখ্যা করবে।
ভুল করলে বলবে: ভুল শেখার অংশ।
"""

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="bigscience/bloom-560m",
        max_new_tokens=200
    )

model = load_model()

user_input = st.text_input("তোমার প্রশ্ন লেখো:")

if user_input:
    with st.spinner("শিক্ষক ভাবছে..."):
        response = model(teacher_prompt + "\nছাত্র: " + user_input + "\nশিক্ষক:")
        st.markdown("### 📖 শিক্ষক উত্তর:")
        st.write(response[0]["generated_text"].split("শিক্ষক:")[-1])
