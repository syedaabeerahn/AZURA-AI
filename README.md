✨ AZURA AI: The Voice of Wonder
Azura is a whimsical, agentic AI tutor designed to make learning a magical adventure for children under the age of 10. Built with Python and Streamlit, it uses the Gemini 1.5 Flash model to provide safe, bite-sized, and narrative-driven educational support.

🌟 Key Features
Whimsical Persona: Azura acts as a gentle mentor, using metaphors and "Voice of Wonder" to explain the world.

Child Safety: Built-in guardrails ensure all content is strictly age-appropriate, avoiding adult themes or harmful advice.

Interactive Themes: Users can customize the interface color (Pink, Blue, etc.) through a sidebar theme picker.

Persistent Memory: A SQLite database stores chat history, allowing children to revisit their past "adventures".

Gemini-Powered Brain: Uses the latest Gemini 1.5 Flash model for high-speed, intelligent responses.

🛠️ Technical Stack
Frontend: Streamlit (Web UI)

LLM Integration: OpenAI SDK (Compatible with Google Gemini API)

Database: SQLite3 (Local persistent storage)

Logic: Python with python-dotenv for secret management.

🚀 Deployment
This project is optimized for deployment on Streamlit Community Cloud.

Requirements: Ensure requirements.txt includes streamlit, openai, and python-dotenv.

Secrets: Store your GEMINI_API_KEY in the Streamlit Cloud "Secrets" management tool.
