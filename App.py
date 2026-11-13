from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load OPENAI_API_KEY from .env
load_dotenv()

# 2. Initialize OpenAI model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a helpful nutritionist and chef. "
        "Suggest exactly 5 healthy, quick breakfast recipes name list only" )),
    ("user", "I have these ingredients: {ingredients}")
])

# 4. Build the LCEL chain
chain = prompt | llm | StrOutputParser()

# 5. Get input from the user and run the chain
if __name__ == "__main__":
    print("=== Healthy Breakfast Idea Generator ===")
    print("Type your ingredients anytime, or type 'quit' to exit.\n")

    while True:
        user_ingredients = input("Enter ingredients (separated by commas): ").strip()

        # Exit condition
        if user_ingredients.lower() in ["quit", "exit", "q"]:
            print("Goodbye! Enjoy your breakfast.")
            break

        # Skip if the user pressed Enter without typing anything
        if not user_ingredients:
            print("Please enter at least one ingredient.\n")
            continue

        print("\nCooking up 5 healthy ideas...\n")
        result = chain.invoke({"ingredients": user_ingredients})
        print(result)
        print("\n" + "=" * 50 + "\n")