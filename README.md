# 🍳 Healthy Breakfast Idea Generator

A beginner-friendly Generative AI web application built with **Python**, **LangChain**, **OpenAI**, and **Streamlit**. Enter the ingredients you have on hand, and the app generates 5 quick, healthy breakfast ideas.

## ✨ Features
- **Ingredient-Based Suggestions:** Generates 5 tailored, healthy breakfast recipes from whatever ingredients you type.
- **LCEL Pipeline:** Uses modern LangChain Expression Language (`prompt | llm | StrOutputParser()`).
- **Interactive Web UI:** Clean Streamlit interface that automatically clears the input box after generating results.
- **Secure API Handling:** Uses `.env` to keep your OpenAI API key out of source code.

## 🛠️ Prerequisites
- Python 3.10 or higher
- An OpenAI API key ([Get one here](https://platform.openai.com/))

## 🚀 Setup & Installation

1. **Clone or create the project folder:**
   ```bash
   mkdir healthy-breakfast-app
   cd healthy-breakfast-app
