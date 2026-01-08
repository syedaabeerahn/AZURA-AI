import streamlit as st
from llm import call_gemini
from memory import init_db, save_message, load_messages
from prompt import SYSTEM_PROMPT

# --- 1. THEME & SESSION INITIALIZATION ---
if "theme_color" not in st.session_state:
    st.session_state.theme_color = "#ff9a9e" # Default pink

if "messages" not in st.session_state:
    st.session_state.messages = load_messages(limit=10)

# --- 2. DYNAMIC STYLING ---
st.set_page_config(page_title="AZURA AI", page_icon="✨", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.theme_color}10 !important; 
    }}
    [data-testid="stSidebar"] {{
        background-color: {st.session_state.theme_color} !important;
    }}
    .header-pink {{
        background-color: {st.session_state.theme_color}; 
        padding: 40px;
        text-align: center;
        border-radius: 0px 0px 40px 40px;
        margin-top: -60px;
        margin-bottom: 20px;
        color: white;
    }}
    </style>
    <div class="header-pink">
        <h1 style="font-family: serif; letter-spacing: 5px;">AZURA</h1>
    </div>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: MAGIC CONTROLS & NEW CHAT ---
with st.sidebar:
    st.title("🎨 Magic Controls")
    
    # NEW CHAT BUTTON
    if st.button("➕ Start New Adventure"):
        st.session_state.messages = [] # Clears the current screen
        st.rerun()
    
    st.markdown("---")
    
    # COLOR PICKER
    new_color = st.color_picker("Change Azura's Color:", st.session_state.theme_color)
    if new_color != st.session_state.theme_color:
        st.session_state.theme_color = new_color
        st.rerun()
        
    st.markdown("---")
    st.title("📜 Chat History")
    past_chats = load_messages(limit=20)
    if past_chats:
        for chat in past_chats:
            icon = "👤" if chat["role"] == "user" else "✨"
            st.write(f"{icon} {chat['content'][:25]}...")
    else:
        st.write("No memories yet!")

# --- 4. YOUR ORIGINAL UNTOUCHED LOGIC ---
init_db()

st.title("✨ AZURA - Your AI Tutor")
st.markdown("---")

# Display the chat history on the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
if prompt := st.chat_input("What would you like to learn today?"):
    st.chat_message("user").markdown(prompt)
    save_message("user", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    history = load_messages(limit=10)
    context = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    with st.chat_message("assistant"):
        with st.spinner("Azura is gathering stardust..."):
            response = call_gemini(context)
            st.markdown(response)
    
    save_message("assistant", response)
    st.session_state.messages.append({"role": "assistant", "content": response})

