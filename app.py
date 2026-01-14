import streamlit as st
from transformers import pipeline

# Load Hugging Face sentiment model
tone_classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Tone detection
def detect_tone(text):
    result = tone_classifier(text)[0]
    label = result['label']
    text_lower = text.lower()
    if label == "POSITIVE":
        if any(word in text_lower for word in ["hey", "hi", "thanks", "cheers"]):
            return "Friendly"
        else:
            return "Formal"
    else:
        if any(word in text_lower for word in ["sorry", "apologize"]):
            return "Apologetic"
        else:
            return "Aggressive"

# Suggestions
def improvement_suggestion(text, tone):
    if tone == "Aggressive":
        return "Consider softening your language or using polite phrasing."
    elif tone == "Friendly":
        return "You can keep it casual but ensure clarity."
    elif tone == "Formal":
        return "Looks good. Ensure no ambiguous words."
    elif tone == "Apologetic":
        return "Your apology is clear. You may add a solution or next step."

# Chatbot function
def email_chatbot(text):
    tone = detect_tone(text)
    suggestion = improvement_suggestion(text, tone)
    return f"Tone: {tone}\nSuggestion: {suggestion}"

# Streamlit UI
st.title("AI-Powered Email Tone Checker Chatbot")
user_input = st.text_area("Paste your email here:")
if st.button("Analyze"):
    st.write(email_chatbot(user_input))