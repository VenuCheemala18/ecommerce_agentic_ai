import streamlit as st

from crew import process_customer_query


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-Commerce AI Customer Support",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

st.title("🤖 E-Commerce AI Customer Support")


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋\n\n"
                "I'm your **E-Commerce AI Customer Support Assistant**.\n\n"
                "I can help you with:\n\n"
                "📦 Order status\n"
                "🚚 Delivery tracking\n"
                "🔄 Returns\n"
                "💰 Refunds\n"
                "❌ Cancellation\n"
                "📋 Policies\n\n"
                "How can I help you today?"
            )
        }
    ]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🛒 E-Commerce Support</div>',
        unsafe_allow_html=True
    )

    st.write("")


    # ========================================================
    # NEW CHAT
    # ========================================================

    if st.button(
        "🆕 New Chat",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! 👋\n\n"
                    "How can I help you today?"
                )
            }
        ]

        st.rerun()


    st.divider()


    # ========================================================
    # QUICK ACTIONS
    # ========================================================

    st.subheader("⚡ Quick Actions")


    if st.button(
        "📦 Check Order",
        use_container_width=True
    ):

        st.session_state.quick_message = (
            "Where is my order ORD1001?"
        )


    if st.button(
        "🚚 Track Delivery",
        use_container_width=True
    ):

        st.session_state.quick_message = (
            "Track my order ORD1001."
        )


    if st.button(
        "🔄 Return Order",
        use_container_width=True
    ):

        st.session_state.quick_message = (
            "I want to return order ORD1002. "
            "The reason is that I don't need the product anymore."
        )


    if st.button(
        "💰 Ask Refund",
        use_container_width=True
    ):

        st.session_state.quick_message = (
            "What is the refund status for order ORD1002?"
        )


    if st.button(
        "📋 Return Policy",
        use_container_width=True
    ):

        st.session_state.quick_message = (
            "What is your return policy?"
        )


    st.divider()


    # ========================================================
    # AI AGENTS
    # ========================================================

    st.subheader("🤖 AI Agents")

    st.write(
        """
        Your request can be handled by multiple specialized
        AI agents:

        • Customer Support Agent
        • Order Management Agent
        • Delivery Agent
        • Logistics Agent
        • Return Agent
        • Refund Agent
        • Policy Agent
        • Resolution Agent
        """
    )


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    role = message["role"]

    with st.chat_message(role):

        st.markdown(message["content"])


# ============================================================
# GET USER INPUT
# ============================================================

customer_query = st.chat_input(
    "Ask me about your order, delivery, return, refund..."
)


# ============================================================
# QUICK MESSAGE
# ============================================================

if "quick_message" in st.session_state:

    customer_query = st.session_state.quick_message

    del st.session_state.quick_message


# ============================================================
# PROCESS MESSAGE
# ============================================================

if customer_query:

    # --------------------------------------------------------
    # DISPLAY USER MESSAGE
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(customer_query)


    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": customer_query
        }
    )


    # --------------------------------------------------------
    # BUILD CONVERSATION CONTEXT
    # --------------------------------------------------------

    conversation_history = ""

    for message in st.session_state.messages[-10:]:

        role = message["role"]

        content = message["content"]

        conversation_history += (
            f"{role.upper()}: {content}\n"
        )


    # --------------------------------------------------------
    # SEND QUERY TO CREWAI
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "🤖 AI agents are analyzing your request..."
        ):

            try:

                enhanced_query = f"""
Conversation History:

{conversation_history}

Current Customer Request:

{customer_query}

Instructions:

Use the conversation history to understand the customer's
current request.

If an order ID was mentioned earlier and the customer refers
to "my order", "that order", "it", or similar words, use the
previous order ID when appropriate.

Provide a clear and helpful final response to the customer.

Do not expose internal agent reasoning.
Do not expose CrewAI task details.
Do not expose token usage.
"""

                result = process_customer_query(
                    enhanced_query
                )


                # ------------------------------------------------
                # GET FINAL RESPONSE
                # ------------------------------------------------

                if hasattr(result, "raw"):

                    assistant_response = result.raw

                else:

                    assistant_response = str(result)


            except Exception as e:

                assistant_response = (
                    "Sorry, I couldn't process your request. "
                    "Please try again.\n\n"
                    f"Error: {str(e)}"
                )


        # ----------------------------------------------------
        # DISPLAY AI RESPONSE
        # ----------------------------------------------------

        st.markdown(assistant_response)


    # --------------------------------------------------------
    # SAVE AI RESPONSE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )