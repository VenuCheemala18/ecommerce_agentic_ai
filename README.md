# 🤖 E-Commerce AI Customer Support

An **Agentic AI-powered E-Commerce Customer Support System** built using **CrewAI, Python, and Streamlit**.

The system uses multiple specialized AI agents to understand customer queries and provide support for orders, delivery, logistics, returns, refunds, cancellation, policies, and final resolution.

## 🚀 Project Overview

Traditional customer-support systems usually depend on a single chatbot or fixed rules.

This project uses a **multi-agent architecture** where different AI agents are responsible for different e-commerce tasks.

The customer enters a question through the Streamlit chatbot.

The system sends the request to CrewAI, where specialized agents analyze the request and provide a final customer-friendly response.

## 🎯 Objectives

* Automate common e-commerce customer-support requests
* Use multiple specialized AI agents
* Check order information
* Provide delivery and tracking information
* Handle return requests
* Handle refund-related questions
* Provide cancellation support
* Answer policy-related questions
* Generate a final customer-friendly response
* Maintain conversation context for follow-up questions

## 🏗️ Architecture

```text
                    Customer
                       │
                       ▼
              Streamlit Chatbot
                       │
                       ▼
             Customer Support Agent
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Order Agent    Delivery Agent  Logistics Agent
        │              │              │
        └──────────────┼──────────────┘
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
        Return Agent  Refund Agent
              │        │
              └────┬───┘
                   ▼
             Policy Agent
                   │
                   ▼
           Resolution Agent
                   │
                   ▼
            Final Response
                   │
                   ▼
               Customer
```

## 🤖 AI Agents

The project contains 8 specialized agents.

### 1. Customer Support Agent

Understands the customer's request and identifies the type of support required.

### 2. Order Management Agent

Handles order-related information such as:

* Order ID
* Product
* Payment status
* Order status
* Order information

### 3. Delivery Agent

Handles delivery-related questions such as:

* Delivery status
* Expected delivery
* Tracking information

### 4. Logistics Agent

Handles logistics and shipment-related information.

### 5. Return Agent

Handles return requests and checks whether the customer's request can be processed according to the available information.

### 6. Refund Agent

Handles refund-related questions such as:

* Refund status
* Refund information
* Payment-related refund questions

### 7. Policy Agent

Provides information about e-commerce policies such as:

* Return policy
* Refund policy
* Cancellation policy

### 8. Resolution Agent

Combines the information from the other agents and produces the final customer-friendly response.

## 🛠️ Technologies Used

* Python
* CrewAI
* Streamlit
* Pandas
* LLM
* Agentic AI
* Multi-Agent Systems

## 📁 Project Structure

```text
ecommerce_agentic_ai/
│
├── agents.py
│       └── Contains the 8 CrewAI agents
│
├── tasks.py
│       └── Contains tasks assigned to the agents
│
├── crew.py
│       └── Creates and runs the CrewAI workflow
│
├── data.py
│       └── Contains sample e-commerce order data
│
├── streamlit_app.py
│       └── Streamlit chatbot interface
│
├── knowledge/
│       └── E-commerce knowledge/policy files
│
├── requirements.txt
│       └── Python dependencies
│
└── README.md
        └── Project documentation
```

## 💬 Example Customer Queries

### Order Status

```text
Where is my order ORD1001?
```

### Delivery Tracking

```text
Track my order ORD1001.
```

### Return

```text
I want to return order ORD1002.
```

### Refund

```text
What is the refund status for order ORD1002?
```

### Policy

```text
What is your return policy?
```

### Follow-up Question

```text
Where is my order ORD1001?
```

Then:

```text
When will it arrive?
```

The system uses the conversation history to understand that "it" refers to the previously mentioned order.

## 🖥️ Streamlit Interface

The application provides:

* E-commerce customer-support chatbot
* Chat history
* New Chat option
* Quick Actions
* Order checking
* Delivery tracking
* Return requests
* Refund questions
* Policy questions
* AI agent information
* Conversation context

## ⚙️ Installation

### 1. Clone or download the project

Open the project folder in PyCharm or another Python IDE.

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## 🔑 Environment Variables

If the project uses an API-based LLM, create a `.env` file.

Example:

```text
OPENAI_API_KEY=your_api_key_here
```

Do **not** upload your actual API key to GitHub.

Add `.env` to `.gitignore`.

## ▶️ Running the Application

Run the Streamlit application using:

```powershell
streamlit run streamlit_app.py
```

Streamlit will open the chatbot in your browser.

## 🔄 Application Workflow

```text
1. Customer enters a question
          ↓
2. Streamlit receives the question
          ↓
3. Conversation history is collected
          ↓
4. Query is sent to CrewAI
          ↓
5. Customer Support Agent analyzes the request
          ↓
6. Relevant specialized agents process the request
          ↓
7. Resolution Agent generates the final answer
          ↓
8. Streamlit displays the response
```

## 📊 Sample Order Data

The project contains sample e-commerce order information.

Example:

```text
Order ID: ORD1001
Customer: Venu
Product: Samsung Galaxy Phone
Payment Status: Paid
Order Status: Delivered
Tracking ID: TRK1001
```

The data can be used to demonstrate order-status and customer-support workflows.

## 🔐 Security

* API keys should be stored in `.env`
* `.env` should not be committed to GitHub
* Customer information should be protected
* Production applications should use secure databases and authentication

## 🌟 Key Features

* Multi-Agent AI architecture
* CrewAI-based agent orchestration
* Specialized e-commerce agents
* Streamlit chatbot interface
* Conversation history
* Quick customer-support actions
* Order information lookup
* Delivery support
* Return support
* Refund support
* Policy support
* Final AI-generated resolution

## 📌 Future Enhancements

Possible improvements include:

* Database integration
* Real-time order tracking
* Authentication
* Payment gateway integration
* Email notifications
* Human-agent escalation
* RAG-based policy retrieval
* Vector database
* Customer sentiment analysis
* Voice-based customer support
* Deployment to cloud
* Advanced analytics dashboard

## 👨‍💻 Project Purpose

This project demonstrates how **Agentic AI and Multi-Agent Systems** can be applied to automate e-commerce customer-support workflows.

It is designed as a practical project for demonstrating skills in:

* Python
* AI Agents
* CrewAI
* LLMs
* Agentic AI
* Streamlit
* E-Commerce domain
* Automation
* Multi-Agent orchestration
