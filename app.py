import os
import json
import google.generativeai as genai
import streamlit as st # Import Streamlit

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Intent Classifier",
    page_icon="🤖",
    layout="centered"
)

# --- Securely Get API Key ---
# This is the correct way to handle secrets!
# We'll set this in Streamlit's settings later.
try:
    api_key = st.secrets["API-KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error configuring the API. Please make sure you have set your GEMINI_API_KEY secret. Error: {e}")

# Initialize the Gemini Pro model
model = genai.GenerativeModel('gemini-pro') # Using a stable, recommended model

def get_intent(user_query: str) -> dict:
    """
    Classifies the user's query using the Gemini model.
    This function is mostly the same as your original one.
    """
    list_of_intents = [
        "GET_WEATHER", "SEARCH_WEB", "SET_ALARM", "PLAY_MUSIC",
        "OPEN_YOUTUBE", "TELL_JOKE", "GET_NEWS", "ANSWER_QUESTION",
        "ADD_REMINDER", "UNKNOWN"
    ]
    prompt = f"""
    You are an intelligent assistant that functions as an expert intent classifier. 
    Your task is to analyze a user's query and provide a structured JSON output.
    Your response MUST be a valid JSON object and nothing else.
    The JSON object must have the following three fields:
    1. "internet": A boolean (`true` or `false`). Set to `false` for direct answers or local actions, and `true` for web searches.
    2. "intent": A string. It must be one of the intents from this list: {list_of_intents}.
    3. "action": A string.
       - If 'intent' is 'ANSWER_QUESTION', this field MUST contain the direct, concise answer.
       - If 'intent' is 'SEARCH_WEB', 'GET_WEATHER', or 'OPEN_YOUTUBE', this field MUST contain a complete, well-formed search URL (e.g., https://www.google.com/search?q=your+query).
       - For other intents, it should contain a description of the action.

    --- EXAMPLES ---
    Query: "What is the height of Mount Everest?"
    Response: {{"internet": false, "intent": "ANSWER_QUESTION", "action": "The official elevation of Mount Everest is 8,848.86 meters (29,031.7 feet) above sea level."}}
    Query: "What is the latest news about the Mars rover?"
    Response: {{"internet": true, "intent": "SEARCH_WEB", "action": "https://www.google.com/search?q=latest+news+about+Mars+rover"}}
    Query: "Wake me up at 7 AM"
    Response: {{"internet": false, "intent": "SET_ALARM", "action": "set alarm for 7:00 AM"}}
    --- USER QUERY ---
    Query: "{user_query}"
    Response:
    """
    try:
        response = model.generate_content(prompt)
        cleaned_response = response.text.strip().replace("```json", "").replace("```", "")
        intent_data = json.loads(cleaned_response)
        return intent_data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"internet": None, "intent": "error", "action": str(e)}

# --- Streamlit App Interface ---

st.title("🤖 AI Intent Classifier")
st.markdown("Enter a query, and the AI will classify its intent and determine the necessary action. This demo showcases the power of LLMs for understanding user requests.")

# Instead of input(), we use st.text_input()
user_input = st.text_input("Enter your query here:", placeholder="e.g., What is the capital of India?")

if user_input:
    with st.spinner("Classifying intent..."):
        result = get_intent(user_input)
    
    st.subheader("Classification Result")

    # Instead of print(), we use st.write(), st.success(), etc.
    if result.get("intent") == "error":
        st.error(f"An error occurred: {result.get('action')}")
    else:
        # Display the results in a more organized way
        st.write(f"**Intent:** `{result.get('intent')}`")

        if result.get("intent") == "ANSWER_QUESTION":
            st.success(f"💡 **Direct Answer:** {result.get('action')}")
        elif result.get("internet"):
            url = result.get('action')
            st.info(f"🌐 **Web Action Required**")
            # This is how you display a clickable link instead of opening a browser
            st.markdown(f"Click here to perform the search: [{url}]({url})")
        else:
            st.info(f"⚙️ **Local Action:** {result.get('action')}")