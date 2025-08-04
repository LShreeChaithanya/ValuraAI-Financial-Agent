import streamlit as st
import requests
import time
import json

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/chat"

def send_to_backend(message, chat_history):
    """Send message to backend with progress tracking"""
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
        'growth', 'savings', 'retirement',  'dollars', 'years', 'rate',
        'percentage', '%', 'monthly', 'payment', 'loan', 'mortgage', 'double'
    ]
    
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in financial_keywords)

def show_thinking_animation():
    """Show animated thinking process"""
    thinking_container = st.empty()
    
    thinking_messages = [
        "🤔 Analyzing your question...",
        "💭 Processing financial data...",
        "🧠 Thinking through the solution..."
    ]
    
    for i, msg in enumerate(thinking_messages):
        thinking_container.markdown(f"""
        <div style='text-align: center; padding: 10px; 
                    background: linear-gradient(90deg, #f0f2f6, #e8eaf0); 
                    border-radius: 10px; margin: 5px 0;
                    animation: pulse 1.5s infinite;'>
            <span style='color: #1f77b4; font-weight: 500;'>{msg}</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.8)
    
    thinking_container.empty()

def show_tool_usage_animation():
    """Show animated tool usage with visual effects"""
    tool_container = st.empty()
    
    # Step 1: Tool Detection
    tool_container.markdown("""
    <div style='text-align: center; padding: 15px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px; margin: 10px 0; color: white;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
                animation: slideInUp 0.5s ease-out;'>
        <div style='font-size: 1.2em; font-weight: bold; margin-bottom: 5px;'>
            🔧 Financial Tools Activated
        </div>
        <div style='font-size: 0.9em; opacity: 0.9;'>
            Initializing calculation engines...
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1)
    
    # Step 2: Tool Processing
    tool_container.markdown("""
    <div style='text-align: center; padding: 15px; 
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                border-radius: 15px; margin: 10px 0; color: white;
                box-shadow: 0 4px 15px rgba(240, 147, 251, 0.3);
                animation: slideInUp 0.5s ease-out;'>
        <div style='font-size: 1.2em; font-weight: bold; margin-bottom: 5px;'>
            ⚡ Running Financial Calculations
        </div>
        <div style='font-size: 0.9em; opacity: 0.9;'>
            Processing compound interest, annuities, and growth projections...
        </div>
        <div style='margin-top: 10px;'>
            <div style='width: 100%; background: rgba(255,255,255,0.3); border-radius: 10px; height: 6px;'>
                <div style='width: 0%; height: 100%; background: rgba(255,255,255,0.8); border-radius: 10px; 
                           animation: progressBar 2s ease-out forwards;'></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1.5)
    
    # Step 3: Results Ready
    tool_container.markdown("""
    <div style='text-align: center; padding: 15px; 
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                border-radius: 15px; margin: 10px 0; color: white;
                box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
                animation: slideInUp 0.5s ease-out;'>
        <div style='font-size: 1.2em; font-weight: bold; margin-bottom: 5px;'>
            ✅ Calculations Complete
        </div>
        <div style='font-size: 0.9em; opacity: 0.9;'>
            Preparing your personalized financial analysis...
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(0.8)
    
    tool_container.empty()

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Page config
st.set_page_config(
    page_title="Valura Financial Planning Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    @keyframes slideInUp {
        from {
            transform: translateY(30px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    @keyframes progressBar {
        from { width: 0%; }
        to { width: 100%; }
    }
    
    .main-header {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-style: italic;
        margin-bottom: 30px;
    }
    
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
    }
    
    /* Custom sidebar styling */
    .sidebar-content {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">💰 Financial Planning Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI-powered financial advisor with advanced calculation tools</div>', unsafe_allow_html=True)

# Display messages with enhanced styling
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about investments, savings, or financial calculations..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get AI response with enhanced visual feedback
    with st.chat_message("assistant"):
        # Determine if tools will be used
        might_use_tools = check_tool_usage(prompt)
        
        if might_use_tools:
            # Show tool usage animation
            show_tool_usage_animation()
        else:
            # Show thinking animation
            show_thinking_animation()
        
        # Get response from backend
        response = send_to_backend(prompt, st.session_state.messages[:-1])
        
        # Display response with success animation
        if response and not response.startswith("Error") and not response.startswith("Backend error"):
            st.markdown("""
            <div style='padding: 10px; border-left: 4px solid #4CAF50; 
                        background: linear-gradient(90deg, #f8fff8, #f0f8f0);
                        border-radius: 5px; margin: 10px 0;'>
            """, unsafe_allow_html=True)
            st.write(response)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(response)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Enhanced Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-content">
        <h2 style='color: #333; text-align: center; margin-bottom: 15px;'>
            💡 What I Can Calculate
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Financial Tools Section
    with st.expander("🔧 Financial Tools Available", expanded=True):
        st.markdown("""
        **Investment Calculations:**
        - 📈 Future Value Analysis
        - 📉 Present Value Discounting  
        - 💰 Annuity Calculations
        - ⏰ Rule of 72 Estimates
        - 📊 Growth Projections
        - 🎯 Period Calculations
        """)
    
    # Example Queries
    with st.expander("💬 Try These Examples", expanded=False):
        examples = [
            "What's the future value of $1000 at 5% for 10 years?",
            "How much should I save monthly for retirement?", 
            "Calculate present value of $50,000 in 15 years at 6%",
            "How long to double my money at 8% interest?",
            "What's the future value of $500 monthly for 20 years?"
        ]
        
        for example in examples:
            if st.button(f"💡 {example}", key=example, use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": example})
                st.rerun()
    
    st.divider()
    
    # Control Panel
    st.markdown("### 🎛️ Control Panel")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()
    
    # Connection Status with enhanced styling
    st.markdown("### 🔌 System Status")
    try:
        test_response = requests.get("http://127.0.0.1:8000", timeout=5)
        st.success("✅ Backend Online")
        st.markdown("""
        <div style='text-align: center; padding: 8px; 
                    background: linear-gradient(90deg, #d4edda, #c3e6cb);
                    border-radius: 8px; margin: 5px 0;'>
            <span style='color: #155724; font-size: 0.9em;'>🚀 All systems operational</span>
        </div>
        """, unsafe_allow_html=True)
    except:
        st.error("❌ Backend Offline")
        st.markdown("""
        <div style='text-align: center; padding: 8px; 
                    background: linear-gradient(90deg, #f8d7da, #f1b0b7);
                    border-radius: 8px; margin: 5px 0;'>
            <span style='color: #721c24; font-size: 0.9em;'>⚠️ Please start the backend server</span>
        </div>
        """, unsafe_allow_html=True)

# Footer with enhanced styling
st.markdown("""
<div style='margin-top: 50px; padding: 20px; text-align: center; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px; color: white;'>
    <div style='font-size: 1.1em; font-weight: bold; margin-bottom: 5px;'>
        💰 Financial Planning Assistant
    </div>
    <div style='font-size: 0.9em; opacity: 0.9;'>
        Powered by AI & Advanced Financial Tools • Built with ❤️
    </div>
</div>
""", unsafe_allow_html=True)