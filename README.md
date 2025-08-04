# 🤖 Valura AI Financial Planning Assistant

### _Your AI-powered financial advisor with advanced calculation tools_

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink)
![Google AI](https://img.shields.io/badge/Google%20AI-4285F4?style=for-the-badge&logo=google)

</div>

---

## 🎯 **Project Overview**

The Financial Planning Assistant is an intelligent conversational agent built for **Valura.ai** that helps users with financial calculations through natural language interactions. It combines proven financial formulas with Google's Gemini 2.0 Flash model to deliver clear, actionable financial calculations.

### 🚀 **Key Features**

<table>
<tr>
<td width="50%">

#### 🤖 **AI-Powered Chat Interface**

- Natural language financial queries
- Intelligent tool selection
- Real-time calculation processing
- Contextual conversation memory

#### 🧮 **Financial Calculation Tools**

- Future Value & Present Value calculations
- Annuity computations (FV & PV)
- Rule of 72 estimates
- NPER (Number of Periods) calculations
- Detailed calculation explanations

</td>
<td width="50%">

#### 💬 **Interactive UI**

- Streamlit-powered chat interface
- Visual animations and progress indicators
- Tool usage detection and feedback
- Responsive design with custom styling

#### 🔧 **Backend API**

- FastAPI REST endpoints
- Structured request/response handling
- Error handling and validation
- Chat history management

</td>
</tr>
</table>

---

## 🏗️ **System Architecture**

<div align="center">

### 🎨 **Application Flow**

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          🌐 STREAMLIT FRONTEND                               │
├──────────────────────────────────────────────────────────────────────────────┤
│  👨‍💼 User Input  ──────────►  💬 Chat Interface  ──────────►  🎨 UI Animations │
│                              │                                              │
│                              ▼                                              │
│                    📡 HTTP Request to Backend                               │
│                         (POST /chat)                                        │
└──────────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                           🔄 FASTAPI BACKEND                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│                         ⚡ main.py (API Server)                              │
│                    ┌─────────────────────────────┐                          │
│                    │    📝 Request Validation    │                          │
│                    │    🔄 Chat History Format   │                          │
│                    │    📤 Response Formatting   │                          │
│                    └─────────────────────────────┘                          │
└──────────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                        🧠 FINANCIAL AGENT LAYER                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                    🤖 financial_agent.py                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐              │
│  │  📋 Chat Format │  │  🎯 Agent Build │  │  💭 AI Invoke   │              │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘              │
│                               │                                              │
│                               ▼                                              │
│              ┌─────────────────────────────────────────┐                     │
│              │          🌟 Gemini 2.0 Flash           │                     │
│              │         (via gemini.py)                │                     │
│              └─────────────────────────────────────────┘                     │
└──────────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                         🧮 CALCULATION TOOLS                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│                       📊 tools/formulas.py                                   │
│                                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ 📈 future_  │  │ 📉 present_ │  │ ⏰ rule_    │  │ 💰 fv_      │        │
│  │   value     │  │   value     │  │   of_72     │  │   annuity   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                         │
│  │ 💰 pv_      │  │ 🎯 nper     │  │ 📝 explain_ │                         │
│  │   annuity   │  │             │  │   calculation│                         │
│  └─────────────┘  └─────────────┘  └─────────────┘                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 🔄 **Tool Execution Flow**

```
💬 User Query
       │
       ▼
🤖 Gemini Analysis ────────► 🎯 Tool Detection
       │                           │
       ▼                           ▼
📝 Prompt Processing          🧮 Tool Selection
       │                           │
       ▼                           ▼
🔧 Tool Execution ◄─────────── ⚡ Parameter Mapping
       │
       ▼
📊 Calculation Result
       │
       ▼
💬 Natural Language Response
```

</div>

---

## 📁 **Project Structure**

```
📦 FINANCIAL_PLANNING_APP/
├── 🔧 src/
│   ├── 📱 app.py                     # Streamlit Frontend Application
│   ├── 🤖 financial_agent.py        # Core Agent Logic & Tool Integration
│   ├── 🌐 gemini.py                 # Google AI Integration & LLM Setup
│   ├── 📝 prompts.py                # System Prompts & Instructions
│   └── 🛠️ tools/
│       ├── 📊 formulas.py            # Financial Calculation Functions
│       └── 🔧 __init__.py           # Package Initialization
├── 🚀 app/
│   └── 📡 api/
│       └── ⚡ main.py               # FastAPI Backend Server
├── 🧪 tests/
├── 📋 requirements.txt              # Python Dependencies
├── 🔒 .env                         # Environment Variables
├── 🐍 .python-version              # Python Version Specification
└── 📖 README.md                    # Project Documentation
```

---

## 🛠️ **Tech Stack**

### **Backend Architecture**

<table>
<tr>
<td align="center" width="20%">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="60"><br/>
<strong>FastAPI</strong><br/>
<em>High-performance API</em>
</td>
<td align="center" width="20%">
<img src="https://python-langchain.readthedocs.io/en/latest/_static/wordmark.png" width="60"><br/>
<strong>LangChain</strong><br/>
<em>AI Framework</em>
</td>
<td align="center" width="20%">
<img src="https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg" width="60"><br/>
<strong>Gemini 2.0</strong><br/>
<em>Language Model</em>
</td>
<td align="center" width="20%">
<img src="https://docs.pydantic.dev/latest/logo-white.svg" width="60"><br/>
<strong>Pydantic</strong><br/>
<em>Data Validation</em>
</td>
<td align="center" width="20%">
<img src="https://python.org/static/community_logos/python-logo.png" width="60"><br/>
<strong>Python 3.12+</strong><br/>
<em>Core Language</em>
</td>
</tr>
</table>

### **Frontend Architecture**

<table>
<tr>
<td align="center" width="33%">
<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="60"><br/>
<strong>Streamlit</strong><br/>
<em>Interactive UI</em>
</td>
<td align="center" width="33%">
<img src="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations/css-animations.png" width="60"><br/>
<strong>CSS Animations</strong><br/>
<em>Visual Effects</em>
</td>
<td align="center" width="33%">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="60"><br/>
<strong>HTML5</strong><br/>
<em>Rich Content</em>
</td>
</tr>
</table>

---

## ⚙️ **Installation & Setup**

### **1. Prerequisites**

```bash
# Python 3.12+ required
python --version

# Git for cloning
git --version
```

### **2. Clone Repository**

```bash
git clone https://github.com/your-username/financial-planning-assistant.git
cd financial-planning-assistant
```

### **3. Environment Setup**

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **4. Configuration**

```bash
# Create .env file
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
```

### **5. Run the Application**

#### **Start Backend Server:**

```bash
cd app/api
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

#### **Start Frontend (New Terminal):**

```bash
cd src
streamlit run app.py
```

---

## 🧮 **Available Financial Tools**

<div align="center">

<table>
<tr>
<td width="50%">

### **🔢 Core Calculations**

| Tool              | Function          | Formula                             |
| ----------------- | ----------------- | ----------------------------------- |
| **Future Value**  | `future_value()`  | `FV = PV × (1 + r)^n`               |
| **Present Value** | `present_value()` | `PV = FV ÷ (1 + r)^n`               |
| **FV Annuity**    | `fv_annuity()`    | `FV = PMT × [((1 + r)^n - 1) ÷ r]`  |
| **PV Annuity**    | `pv_annuity()`    | `PV = PMT × [1 - (1 + r)^(-n)] ÷ r` |
| **Rule of 72**    | `rule_of_72()`    | `Years ≈ 72 ÷ rate%`                |
| **NPER**          | `nper()`          | `n = ln(FV÷PV) ÷ ln(1+r)`           |

</td>
<td width="50%">

### **🎯 Use Cases**

- 🏠 **Retirement Planning**
- 💳 **Investment Growth Analysis**
- 🎓 **Education Savings Goals**
- 🏡 **Mortgage vs Investment Decisions**
- 📈 **Portfolio Value Projections**
- ⏰ **Time-to-Goal Calculations**
- 📊 **Interest Rate Comparisons**

</td>
</tr>
</table>

</div>

---

## 💬 **Example Interactions**

### **Investment Analysis**

```
User: "What's the future value of $50,000 invested at 7% for 20 years?"
Assistant: 🔧 Running financial calculations...
Result: Future Value: $193,484.22
        (Principal: $50,000, Annual Rate: 7%, Time Period: 20 years)
```

### **Retirement Planning**

```
User: "How much do I need to save monthly to have $1 million in 30 years at 6% return?"
Assistant: 💰 Monthly Payment Required: $1,025.73
           (Future Value Goal: $1,000,000, Rate: 6%, Periods: 30 years)
```

### **Quick Estimates**

```
User: "How long to double my money at 8% interest?"
Assistant: ⏰ Rule of 72 Calculation: 9 years
           (72 ÷ 8% = 9 years to double your investment)
```

---

## 🎨 **UI Features**

<div align="center">

<table>
<tr>
<td width="50%">

### **🎭 Visual Feedback**

- 🔄 **Thinking animations** during processing
- ⚡ **Tool usage indicators** with progress tracking
- 🎨 **Gradient backgrounds** and modern styling
- 💫 **Smooth transitions** between states
- ✅ **Success animations** for completed calculations

### **📱 Interactive Elements**

- 💡 **Example query buttons** for quick testing
- 🗑️ **Clear chat** functionality
- 🔄 **Refresh** capabilities
- 🔌 **Backend status** monitoring

</td>
<td width="50%">

### **🚀 Smart Features**

- 🎯 **Keyword detection** for tool activation
- 📊 **Enhanced response formatting**
- 🛡️ **Error handling** with user-friendly messages
- 💾 **Session state** management
- 📝 **Chat history** persistence

### **♿ User Experience**

- 🎨 **Intuitive interface** design
- 📖 **Clear instructions** and examples
- 🔍 **Tool availability** display
- 🎛️ **Control panel** for chat management

</td>
</tr>
</table>

</div>

---

## 🔧 **API Endpoints**

### **Chat Endpoint**

```python
POST /chat
Content-Type: application/json

{
    "message": "Calculate future value of $1000 at 5% for 10 years",
    "chat_history": [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi! I'm here to help with financial calculations."}
    ]
}
```

### **Response Format**

```python
{
    "message": "Future Value: $1,628.89 (Principal: $1000, Rate: 5%, Periods: 10)",
    "chat_history": [...] # Updated history with new conversation
}
```

---

## 🔄 **How It Works**

### **1. User Interaction**

- User enters financial question in Streamlit interface
- UI detects potential tool usage based on keywords
- Visual animations provide feedback during processing

### **2. Backend Processing**

- FastAPI receives request and validates input
- `financial_agent.py` formats chat history for LangChain
- Request forwarded to Gemini 2.0 Flash model

### **3. AI Analysis**

- Gemini analyzes query and determines required tools
- LangChain binds appropriate financial calculation functions
- Tool selection happens automatically based on query context

### **4. Tool Execution**

- Selected tools execute with extracted parameters
- Results returned to AI for natural language formatting
- Response generated with calculation details and explanations

### **5. Response Delivery**

- Formatted response sent back through API
- Streamlit displays results with enhanced styling
- Chat history updated for context in future interactions

---

## 🚀 **Deployment**

### **Development Mode**

```bash
# Terminal 1: Backend
cd app/api
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2: Frontend
cd src
streamlit run app.py --server.port 8501
```

### **Production Considerations**

- Environment variable management for API keys
- CORS configuration for cross-origin requests
- Error logging and monitoring
- Session management and user authentication (if needed)

---

## 🤝 **Contributing**

### **Development Workflow**

1. 🍴 **Fork** the repository
2. 🌿 **Create** feature branch (`git checkout -b feature/new-tool`)
3. ✨ **Commit** changes (`git commit -m 'Add new financial tool'`)
4. 📤 **Push** to branch (`git push origin feature/new-tool`)
5. 🔄 **Open** Pull Request

### **Code Standards**

- 🐍 **PEP 8** compliance for Python code
- 📝 **Type hints** for function parameters
- 🧪 **Test coverage** for new tools
- 📖 **Documentation** for API changes

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- 🏢 **Valura.ai** for the project opportunity
- 🤖 **Google AI** for Gemini 2.0 Flash model access
- 🦜 **LangChain** for the excellent AI framework
- 🚀 **Streamlit** for rapid UI development capabilities

---

<div align="center">

### 💰 **Built with ❤️ for Financial Empowerment**

_Helping users make informed financial decisions through intelligent automation_

[🌟 Star this repo](https://github.com/your-username/financial-planning-assistant) • [🐛 Report Bug](https://github.com/your-username/financial-planning-assistant/issues) • [💡 Request Feature](https://github.com/your-username/financial-planning-assistant/issues)

</div>
