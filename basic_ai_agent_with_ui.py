# ## Basic Web based AI Agent with Memory
# import streamlit as st
# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM

# # Load AI Model

# llm= OllamaLLM(model="mistral")

# # Initialize Momory
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history= ChatMessageHistory()

# # Define Ai Prompt Tamplate
# prompt= PromptTemplate(
   
#     input_variables=("chat_history","question"),
#     template= "Previous Cenversation:  {chat_history}\nUser: {question}\nAI:"
# )

# #Function Ai Chat with Memory
# def run_chain(question):
#     #Retrive past Chat History 
#     chat_history_text= "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.message])

#     #Run the AI Response Generation
#     response= llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

#     #Store new user input and Ai response in memory
#     st.session_state.chat_history.add_user_message(question)
#     st.session_state.chat_history.add_ai_message(response)

#     return response

# #Streamlit UI

# st.title("\n AI Chatbot with Memory")
# st.write("Ask me anything!")

# user_input=st.text_input("Your Question:")
# if user_input:
#     response=run_chain(user_input)
#     st.write("**You** {user_input}")
#     st.write("**AI** {response}")

# #Show Full Chat History
# st.subheader(" Chat History")
# for msg in st.session_state.chat_history.message:
#     st.write(f"**{msg.type.capitalize()}**: {msg.content}")

    




import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="mistral")

# Initialize Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

# Define Prompt Template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous Conversation:\n{chat_history}\nUser: {question}\nAI:"
)

# Function: AI Chat with Memory
def run_chain(question):
    # Convert history into readable text
    chat_history_text = "\n".join(
        [f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages]
    )

    # Generate response
    response = llm.invoke(
        prompt.format(chat_history=chat_history_text, question=question)
    )

    # Store messages
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

# Streamlit UI
st.title("🤖 AI Chatbot with Memory")
st.write("Ask me anything!")

user_input = st.text_input("Your Question:")

if user_input:
    response = run_chain(user_input)
    st.write(f"**You:** {user_input}")
    st.write(f"**AI:** {response}")

# Display Conversation History
st.subheader("Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")
