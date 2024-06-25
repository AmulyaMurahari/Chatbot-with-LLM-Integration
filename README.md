# Chatbot-with-LLM-Integration

This repository contains the setup and configuration for two language models: Llama3 and Phi3. Follow the instructions below to set up and run these models locally.

## Part 1 of Assignment

## Table of Contents

- Llama3 Setup
- Phi3 Setup
- Scripts and Configuration Files
- Usage
- Troubleshooting

## Llama3 Setup

### Prerequisites

- Docker
- Ollama (for Llama3)

### Steps

1. **Download and install Ollama:**

2. **Run Llama3:**

   ```ollama run llama3```
3. **Test with cURL:**

  ```curl -X POST http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{"model": "llama3", "messages": [{ "role": "user", "content": "How is a rainbow formed?" }],"stream": false}'```

## Phi3 Setup

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- Required Python packages (transformers, flask, torch)

### Steps

1. **Download and install Ollama:**

2. **Pull Phi3:**

   ```ollama pull phi3```
   
3. **Run Phi3:**

   ```ollama run phi3```
   
4. **Test with cURL:**

  ```curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{"model": "phi3", "prompt": "Tell me a joke.", "stream": false }'```

## Part 2 of assignment

1. **Run Gemma**

   ```ollama run gemma:2b```
   
2. **Run the python file using Streamlit**
   
   ```streamlit run app.py```

### Domain : Tech Domain
#### Questions asked :
* What is the role of AI in modern cybersecurity?
* How does blockchain technology ensure data security?
* How can machine learning improve healthcare outcomes?

