# tools.py

from pathlib import Path

from crewai.tools import tool

from data import (
    orders,
    shipments,
    returns,
    refunds,
    replacements
)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# ORDER TOOL
# =========================================================

@tool("Check Order")
def check_order(order_id: str) -> str:
    """Check customer order details using order ID."""

    order = orders.get(order_id)

    if not order:
        return f"Order {order_id} was not found."

    return f"""
ORDER INFORMATION

Order ID: {order_id}
Customer: {order['customer']}
Product: {order['product']}
Amount: ₹{order['amount']}
Payment Status: {order['payment_status']}
Order Status: {order['order_status']}
Delivery Date: {order['delivery_date']}
Tracking ID: {order['tracking_id']}
"""


# =========================================================
# LOGISTICS / DELIVERY TOOL
# =========================================================

@tool("Track Shipment")
def track_shipment(tracking_id: str) -> str:
    """Track shipment using tracking ID."""

    shipment = shipments.get(tracking_id)

    if not shipment:
        return f"Tracking ID {tracking_id} was not found."

    return f"""
SHIPMENT INFORMATION

Tracking ID: {tracking_id}
Courier: {shipment['courier']}
Status: {shipment['status']}
Current Location: {shipment['location']}
Expected Delivery: {shipment['expected_delivery']}
"""


# =========================================================
# POLICY RAG TOOL
# =========================================================

@tool("Search Policy")
def search_policy(query: str) -> str:
    """Search company policy knowledge base using TF-IDF retrieval."""

    policy_path = Path("knowledge/policies.txt")

    if not policy_path.exists():
        return "Policy knowledge base was not found."

    with open(policy_path, "r", encoding="utf-8") as file:
        policy_text = file.read()

    documents = [
        paragraph.strip()
        for paragraph in policy_text.split("\n\n")
        if paragraph.strip()
    ]

    if not documents:
        return "No policy information available."

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        documents + [query]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )[0]

    top_indexes = similarity.argsort()[-3:][::-1]

    results = []

    for index in top_indexes:
        results.append(documents[index])

    return "\n\n".join(results)


# =========================================================
# RETURN TOOL
# =========================================================

# =========================================================
# RETURN TOOL
# =========================================================

@tool("Create Return")
def create_return(order_id: str, reason: str) -> str:
    """Create a return request for an eligible order."""

    order = orders.get(order_id)

    if not order:
        return f"Return failed. Order {order_id} does not exist."

    if order["order_status"] == "Cancelled":
        return f"Return failed. Order {order_id} is cancelled."

    # Check whether a return already exists
    for return_id, return_data in returns.items():
        if return_data["order_id"] == order_id:
            return (
                f"Return already exists for order {order_id}. "
                f"Return ID: {return_id}, "
                f"Status: {return_data['status']}"
            )

    return_id = f"RET{1001 + len(returns)}"

    returns[return_id] = {
        "order_id": order_id,
        "reason": reason,
        "status": "Return Requested"
    }

    return f"""
RETURN CREATED

Return ID: {return_id}
Order ID: {order_id}
Product: {order['product']}
Amount: ₹{order['amount']}
Reason: {reason}
Status: Return Requested
"""


# =========================================================
# REPLACEMENT TOOL
# =========================================================

@tool("Create Replacement")
def create_replacement(order_id: str, reason: str) -> str:
    """Create a replacement request."""

    if order_id not in orders:
        return "Replacement failed. Order does not exist."

    replacement_id = f"REP{1001 + len(replacements)}"

    replacements[replacement_id] = {
        "order_id": order_id,
        "reason": reason,
        "status": "Replacement Requested"
    }

    return f"""
REPLACEMENT CREATED

Replacement ID: {replacement_id}
Order ID: {order_id}
Reason: {reason}
Status: Replacement Requested
"""


# =========================================================
# REFUND TOOL
# =========================================================

@tool("Process Refund")
def process_refund(order_id: str) -> str:
    """Initiate refund for an order."""

    order = orders.get(order_id)

    if not order:
        return "Refund failed. Order does not exist."

    refund_id = f"REF{1001 + len(refunds)}"

    refunds[refund_id] = {
        "order_id": order_id,
        "amount": order["amount"],
        "status": "Refund Initiated"
    }

    return f"""
REFUND INITIATED

Refund ID: {refund_id}
Order ID: {order_id}
Amount: ₹{order['amount']}
Status: Refund Initiated
"""


# =========================================================
# PAYMENT TOOL
# =========================================================

@tool("Check Payment")
def check_payment(order_id: str) -> str:
    """Check payment status for an order."""

    order = orders.get(order_id)

    if not order:
        return "Order does not exist."

    return f"""
PAYMENT INFORMATION

Order ID: {order_id}
Payment Status: {order['payment_status']}
Amount: ₹{order['amount']}
"""


# =========================================================
# CANCELLATION TOOL
# =========================================================

@tool("Cancel Order")
def cancel_order(order_id: str) -> str:
    """Cancel an eligible order."""

    order = orders.get(order_id)

    if not order:
        return "Cancellation failed. Order does not exist."

    if order["order_status"] == "Delivered":
        return "Order cannot be cancelled because it has already been delivered."

    if order["order_status"] == "Cancelled":
        return "Order is already cancelled."

    order["order_status"] = "Cancelled"

    return f"""
ORDER CANCELLED

Order ID: {order_id}
Status: Cancelled
"""


# =========================================================
# HUMAN ESCALATION TOOL
# =========================================================

@tool("Escalate To Human")
def escalate_to_human(reason: str) -> str:
    """Escalate a complex issue to human customer support."""

    return f"""
HUMAN ESCALATION CREATED

Reason: {reason}

Status: Escalated to Human Support
"""