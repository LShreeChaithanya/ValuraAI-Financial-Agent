import streamlit as st
import requests
import time

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/chat"

def send_to_backend(message, chat_history):
    """Send message to backend"""
    try:
        payload = {
            "message": message,
            "chat_history": chat_history
        }
        
        response = requests.post(BACKEND_URL, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", result.get("message", str(result)))
        else:
            return f"Backend error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"

def check_tool_usage(message):
    """Check if message might trigger tool usage based on keywords"""
    financial_keywords = [
        'future value', 'present value', 'investment', 'calculate', 'compound',
        'interest', 'return', 'fv', 'pv', 'annuity', 'rule of 72', 'periods',
        'growth', 'savings', 'retirement', '$', 'dollars', 'years', 'rate',
        'percentage', '%', 'monthly', 'payment'
    ]
    
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in financial_keywords)

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Page config
st.set_page_config(
    page_title="Financial Planning Assistant",
    page_icon="💰",
    layout="centered"
)

# Header
st.title("💰 Financial Planning Assistant")
st.markdown("*Your AI-powered financial advisor with calculation tools*")

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about investments, savings, or financial calculations..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        # Determine loading message based on content
        might_use_tools = check_tool_usage(prompt)
        
        if might_use_tools:
            with st.spinner("🔧 Using financial calculation tools..."):
                # Add a brief delay to show the tool usage message
                time.sleep(0.5)
                response = send_to_backend(prompt, st.session_state.messages[:-1])
        else:
            with st.spinner("🤔 Thinking..."):
                response = send_to_backend(prompt, st.session_state.messages[:-1])
        
        st.write(response)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with helpful info
with st.sidebar:
    st.header("💡 What I can help with:")
    st.markdown("""
    **Financial Calculations:**
    - Future Value calculations
    - Present Value analysis  
    - Annuity calculations
    - Rule of 72 estimates
    - Investment growth projections
    
    **Examples to try:**
    - "What's the future value of $1000 at 5% for 10 years?"
    - "How much should I save monthly for retirement?"
    - "Calculate the present value of $50,000 in 15 years at 6%"
    """)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    # Connection status
    st.header("🔌 Connection Status")
    try:
        test_response = requests.get("http://127.0.0.1:8000", timeout=5)
        st.success("✅ Backend Connected")
    except:
        st.error("❌ Backend Disconnected")

# Footer
st.markdown("""
---
<div style='text-align: center; color: #666; font-size: 0.8em;'>
💰 Financial Planning Assistant • Powered by AI & Financial Tools
</div>
""", unsafe_allow_html=True)