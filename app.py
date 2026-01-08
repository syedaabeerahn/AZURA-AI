from llm import call_gemini
from memory import init_db, save_message, load_messages
from prompt import SYSTEM_PROMPT

init_db()

print("Welcome to AZURA ! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    # Save user input
    save_message("user", user_input)
    
    # Load memory
    history = load_messages(limit=10)
    
    # Build messages for Gemini
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
    
    # Get reply
    reply = call_gemini(messages)
    
    # Save reply
    save_message("assistant", reply)
    
    print(f"AZURA: {reply}")
