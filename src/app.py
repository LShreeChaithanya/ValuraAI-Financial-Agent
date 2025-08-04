import streamlit as st
import requests

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/chat"

def send_to_backend(message, chat_history):
    """Send message to backend - try different payload formats"""
    try:
        # Try the exact format that works in Postman
        # Adjust this payload to match what works in your Postman
        payload = {
            "message": message,
            "chat_history": chat_history
        }
        
        response = requests.post(BACKEND_URL, json=payload, timeout=10)
        
        # Debug: Print response details
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            # Adjust this based on your backend response structure
            return result.get("response", result.get("message", str(result)))
        else:
            return f"Backend error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Chat")

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Send current message and chat history to backend
            response = send_to_backend(prompt, st.session_state.messages[:-1])  # Exclude current user message
            st.write(response)
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

# Debug section (remove this once working)
with st.expander("🔧 Debug - Remove this later"):
    st.write("**Current chat history:**")
    st.json(st.session_state.messages)
    
    st.write("**What Postman payload looks like (paste your working Postman request):**")
    st.code("""
    // Paste your exact working Postman JSON here
    // Example:
    {
        "message": "Hello",
        "history": [...]
    }
    """)
    
    if st.button("Test Backend Connection"):
        try:
            test_response = requests.get("http://127.0.0.1:8000")
            st.success(f"Backend reachable: {test_response.status_code}")
        except:
            st.error("Cannot reach backend")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()