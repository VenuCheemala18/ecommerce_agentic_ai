from crewai import Crew, Process

from agents import (
    customer_support_agent,
    order_agent,
    delivery_agent,
    logistics_agent,
    return_agent,
    refund_agent,
    policy_action_agent,
    resolution_agent
)

from tasks import (
    customer_support_task,
    order_task,
    delivery_task,
    logistics_task,
    return_task,
    refund_task,
    policy_action_task,
    resolution_task
)


# ============================================================
# CREATE CREW
# ============================================================

def create_crew():

    crew = Crew(

        agents=[
            customer_support_agent,
            order_agent,
            delivery_agent,
            logistics_agent,
            return_agent,
            refund_agent,
            policy_action_agent,
            resolution_agent
        ],

        tasks=[
            customer_support_task,
            order_task,
            delivery_task,
            logistics_task,
            return_task,
            refund_task,
            policy_action_task,
            resolution_task
        ],

        process=Process.sequential,

        verbose=True
    )

    return crew


# ============================================================
# CLASSIFY CUSTOMER QUERY
# ============================================================

def classify_customer_query(customer_query):

    return f"""
Customer query received:

{customer_query}

The Customer Support Agent will analyze the request
and identify the required specialist.
"""


# ============================================================
# PROCESS CUSTOMER QUERY
# ============================================================

def process_customer_query(customer_query):

    crew = create_crew()

    result = crew.kickoff(
        inputs={
            "customer_query": customer_query
        }
    )

    return result