# import streamlit as st
# import requests
# import json

# # Streamlit app title
# st.title("Streamlit Chatbot with Local LLM")

# # Input text box for user query
# user_input = st.text_input("You:", "")

# # Initialize conversation history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # Function to get response from local LLM
# def get_llm_response(query):
#     try:
#         url = "http://localhost:11434/api/generate"
#         payload = {
#             "model": "llama3",
#             "prompt": query,
#             "stream": False
#         }
#         headers = {
#             'Content-Type': 'application/json'
#         }
#         response = requests.post(url, headers=headers, data=json.dumps(payload))
#         if response.status_code == 200:
#             raw_response_text = response.text
#             # st.write("Debug: Raw Server Response", raw_response_text)  # Print the raw response for debugging
            
#             try:
#                 # Attempt to parse the JSON response
#                 response_data = json.loads(raw_response_text)
#                 # st.write("Debug: Parsed JSON Response", response_data)  # Print the parsed JSON for further inspection
                
#                 # Adjust based on actual response structure
#                 if "response" in response_data:
#                     return response_data["response"]
#                 else:
#                     return "Error: Unexpected response structure."
#             except json.JSONDecodeError as e:
#                 return f"JSON Decode Error: {str(e)}"

#         else:
#             return f"Error: Unable to get response from the LLM. Status code: {response.status_code}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Process user input and get LLM response
# if user_input:
#     bot_response = get_llm_response(user_input)
#     st.session_state.history.append({"user": user_input, "bot": bot_response})

# # Display conversation history
# for chat in st.session_state.history:
#     st.write(f"**You**: {chat['user']}")
#     st.write(f"**Bot**: {chat['bot']}")
#     st.write("---")


import streamlit as st
import requests
import json

# Streamlit app title
st.title("Streamlit Chatbot with Local LLM")

# Input text box for user query
user_input = st.text_input("You:", "")

# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Define prompting patterns
prompting_patterns = {
    "None": lambda q: q,
    "Persona": lambda q: f"You are an expert in {st.text_input('Specify the field: ', 'AI')}. Answer the following question: {q}",
    "Flipped Interaction": lambda q: f"Instead of answering, ask me a question related to: {q}",
    "Cognitive Verifier": lambda q: f"Verify the following information: {q}",
    "Template": lambda q: f"Given this template, provide the necessary details: [Template] {q}",
    "Chain of Thought": lambda q: f"Explain your reasoning step by step for the following query: {q}"
}

# Dropdown menu for selecting prompting pattern
selected_pattern = st.selectbox("Select a prompting pattern:", list(prompting_patterns.keys()))

# Function to get response from local LLM
def get_llm_response(query):
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "gemma:2b",
            "prompt": query,
            "stream": False
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            raw_response_text = response.text
            # st.write("Debug: Raw Server Response", raw_response_text)  # Print the raw response for debugging
            
            try:
                # Attempt to parse the JSON response
                response_data = json.loads(raw_response_text)
                # st.write("Debug: Parsed JSON Response", response_data)  # Print the parsed JSON for further inspection
                
                # Adjust based on actual response structure
                if "response" in response_data:
                    return response_data["response"]
                else:
                    return "Error: Unexpected response structure."
            except json.JSONDecodeError as e:
                return f"JSON Decode Error: {str(e)}"

        else:
            return f"Error: Unable to get response from the LLM. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Process user input and get LLM response
if user_input:
    # Apply the selected prompting pattern
    pattern_applied_input = prompting_patterns[selected_pattern](user_input)
    bot_response = get_llm_response(pattern_applied_input)
    st.session_state.history.append({"user": user_input, "bot": bot_response})

# Display conversation history
for chat in st.session_state.history:
    st.write(f"**You**: {chat['user']}")
    st.write(f"**Bot**: {chat['bot']}")
    st.write("---")
