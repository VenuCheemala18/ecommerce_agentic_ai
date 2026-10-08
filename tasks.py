from crewai import Task

from agents import (
    customer_support_agent,
    order_agent,
    delivery_agent,
    resolution_agent,
    policy_action_agent,
    return_agent,
    refund_agent,
    logistics_agent
)


# ============================================================
# 1. CUSTOMER SUPPORT TASK
# ============================================================

customer_support_task = Task(
    description="""
    Analyze the customer's request.

    Customer request:
    {customer_query}

    Identify:
    1. What the customer wants.
    2. The order ID if provided.
    3. Which specialist area is required.

    Possible areas:
    - Order
    - Payment
    - Delivery
    - Logistics
    - Return
    - Refund
    - Replacement
    - Cancellation
    - Policy
    - Human Support

    Do not invent information.
    """,

    expected_output="""
    Provide:
    - Customer intent
    - Order ID if available
    - Required specialist
    - Short explanation of the problem
    """,

    agent=customer_support_agent
)


# ============================================================
# 2. ORDER MANAGEMENT TASK
# ============================================================

order_task = Task(
    description="""
    Handle the order-related part of the customer's request.

    Use the customer request and the Customer Support Agent's
    analysis from the previous task.

    If an order ID is available, use the Check Order tool.

    Check:
    - Customer
    - Product
    - Amount
    - Payment status
    - Order status
    - Delivery date
    - Tracking ID

    If the customer asks about payment, use the Check Payment tool.

    If the customer asks to cancel an order, use the Cancel Order tool
    only when appropriate.

    Never invent order information.
    """,

    expected_output="""
    Accurate order information and a simple explanation
    of the order situation.
    """,

    agent=order_agent,

    context=[
        customer_support_task
    ]
)


# ============================================================
# 3. DELIVERY TASK
# ============================================================

delivery_task = Task(
    description="""
    Handle delivery-related questions.

    Use the customer's original request and the information
    provided by the previous agents.

    If a tracking ID is available, use the Track Shipment tool.

    Check:
    - Courier
    - Shipment status
    - Current location
    - Expected delivery date

    Never guess delivery information.
    """,

    expected_output="""
    Accurate shipment and delivery information
    with a simple explanation.
    """,

    agent=delivery_agent,

    context=[
        customer_support_task,
        order_task
    ]
)


# ============================================================
# 4. LOGISTICS TASK
# ============================================================

logistics_task = Task(
    description="""
    Analyze the logistics situation.

    Use the customer request, order information and delivery
    information from the previous tasks.

    Use the Track Shipment tool when shipment information
    is required.

    Identify:
    - Courier
    - Shipment status
    - Current location
    - Expected delivery
    - Possible logistics issue

    Do not invent information.
    """,

    expected_output="""
    A clear logistics analysis explaining the shipment
    situation and any logistics issue.
    """,

    agent=logistics_agent,

    context=[
        customer_support_task,
        order_task,
        delivery_task
    ]
)


# ============================================================
# 5. RETURN TASK
# ============================================================

return_task = Task(
    description="""
    Handle the customer's return request.

    Use the customer request and previous task information.

    If the customer wants to return a product:

    1. Identify the order ID.
    2. Understand the return reason.
    3. Check that the order exists.
    4. Use the Create Return tool when appropriate.
    5. Do not invent return information.
    """,

    expected_output="""
    A clear return result containing:
    - Order ID
    - Return reason
    - Return ID if created
    - Return status
    - Next action
    """,

    agent=return_agent,

    context=[
        customer_support_task,
        order_task
    ]
)


# ============================================================
# 6. REFUND TASK
# ============================================================

refund_task = Task(
    description="""
    Handle the customer's refund request.

    Use the customer request and previous task information.

    If the customer requests a refund:

    1. Identify the order ID.
    2. Check that the order exists.
    3. Use the Process Refund tool when appropriate.
    4. Never invent refund information.
    """,

    expected_output="""
    A clear refund result containing:
    - Order ID
    - Refund ID if created
    - Refund amount
    - Refund status
    - Next action
    """,

    agent=refund_agent,

    context=[
        customer_support_task,
        order_task
    ]
)


# ============================================================
# 7. POLICY TASK
# ============================================================

policy_action_task = Task(
    description="""
    Check the company policy related to the customer's request.

    Use the customer's original request and information from
    the previous specialist tasks.

    Use the Search Policy tool.

    Search for the relevant policy such as:
    - Return policy
    - Refund policy
    - Cancellation policy
    - Replacement policy

    Do not invent company rules.
    Use only information retrieved from the policy knowledge base.
    """,

    expected_output="""
    Provide:
    - Applicable policy
    - Relevant policy conditions
    - Whether the requested action is allowed
    - Explanation
    """,

    agent=policy_action_agent,

    context=[
        customer_support_task,
        order_task,
        return_task,
        refund_task
    ]
)


# ============================================================
# 8. RESOLUTION TASK
# ============================================================

resolution_task = Task(
    description="""
    Provide the final resolution to the customer.

    Analyze the information produced by the previous agents.

    Determine:
    1. What the customer's problem is.
    2. What happened.
    3. What action is possible.
    4. What the customer should do next.

    If the issue cannot be resolved automatically,
    recommend human escalation.

    Do not invent information.
    """,

    expected_output="""
    A simple customer-friendly final response containing:

    - Understanding of the customer's problem
    - Relevant information
    - What happened
    - Resolution
    - Next action
    """,

    agent=resolution_agent,

    context=[
        customer_support_task,
        order_task,
        delivery_task,
        logistics_task,
        return_task,
        refund_task,
        policy_action_task
    ]
)
