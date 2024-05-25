
# Chat with Gemini-Pro

This Streamlit application integrates Google's generative AI, Gemini-Pro, to facilitate a dynamic chat interface where users can engage in conversation with the AI. Additionally, the app includes sections for mental health support, allowing users to express their feelings, discuss their life experiences, and describe any current problems they are facing.

## Project Setup

### Prerequisites

- Python 3.8 or higher
- Pip package manager
- An active Google Cloud account with an API key for Gemini-Pro

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://yourrepository.git
   cd yourrepository
   ```

2. **Set up a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```

4. **Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add your API key for Google's Gemini-Pro API:
     ```plaintext
     GOOGLE_API_KEY='your_google_api_key_here'
     ```

### Running the Application

Execute the following command in your terminal:
```bash
streamlit run app.py
```

## Functionalities

- **Interactive Chat with Gemini-Pro:**
  - Users can enter questions or prompts, and the AI responds dynamically.
  - The chat history is displayed on the application interface, maintaining a record of the conversation.

- **Mental Health Support:**
  - Sections dedicated to allowing users to express their current feelings and challenges.
  - Users can submit detailed descriptions about their feelings, life situations, and main problems, which can be used to generate supportive responses from the AI.

## Usage Instructions

1. **Starting the App:**
   - Navigate to the application URL typically `http://localhost:8501` after starting the app.

2. **Engaging with the Chatbot:**
   - Use the chat input box to ask questions or engage in conversation.
   - View responses from Gemini-Pro as they appear in the chat interface.

3. **Mental Health Section:**
   - Fill out the text inputs under "Mental Health Support" to describe your feelings, current life situation, and main challenges.
   - Click "Submit" to see a summary of your responses and receive feedback based on your input.

4. **Resetting the Chat:**
   - Use the "Reset Conversation" button to clear the chat history and start a new session.

## Troubleshooting

- **API Key Issues:** Ensure your `.env` file contains the correct API key and that it's loaded properly. Restart the app if changes are made to the `.env` file.

- **Connectivity Issues:** Check your internet connection and API key restrictions if the app fails to communicate with Gemini-Pro.

## Contributing

Feel free to fork the repository and submit pull requests. We welcome enhancements to the chat functionality or mental health support features.

## License

This project is open-sourced under the MIT License.

---

For further assistance, please refer to the [Streamlit Documentation](https://docs.streamlit.io) or contact support for Google's generative AI APIs.
