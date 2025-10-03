# 🤖 AI Intent Classifier

An interactive web application that uses Google's Gemini API to classify user intent from natural language queries. This project showcases the use of Large Language Models (LLMs) for understanding user requests and determining the appropriate action.

## ✨ Live Demo

**You can try the live application here:** [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)
*(Replace with your actual Streamlit link after deploying)*



## 📋 About The Project

This application serves as an intelligent front-end for a hypothetical assistant. When a user types a query (e.g., "What's the weather like in London?" or "Who wrote Hamlet?"), the application does the following:

1.  Sends the query to the Gemini Pro model with a carefully engineered prompt.
2.  Receives a structured JSON response containing the classified `intent`, a boolean for `internet` access, and a specific `action`.
3.  Presents the result to the user, either as a direct answer or as a suggested web search link.

## 🚀 Key Features

-   **Intent Classification**: Categorizes queries into intents like `GET_WEATHER`, `ANSWER_QUESTION`, `SEARCH_WEB`, etc.
-   **Dynamic Action Generation**: Provides direct answers for general knowledge questions or generates ready-to-use Google search URLs.
-   **LLM-Powered**: Leverages the power of Google's Gemini API for advanced natural language understanding.
-   **Interactive UI**: Built with Streamlit for a clean, responsive, and easy-to-use web interface.

## 🛠️ Tech Stack

-   **Backend**: Python
-   **AI Model**: Google Gemini API (`google-generativeai`)
-   **Frontend/UI**: Streamlit

## ⚙️ How to Run Locally

To run this project on your own machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    Create a file at `.streamlit/secrets.toml` and add your Gemini API key to it:
    ```toml
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"
    ```

4.  **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```