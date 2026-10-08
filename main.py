
from crew import process_customer_query


customer_query = """
I want to return order ORD1002.
The reason is that I don't need the product anymore.
"""


result = process_customer_query(customer_query)


print("\n")
print("=" * 60)
print("FINAL CUSTOMER RESPONSE")
print("=" * 60)
print(result)

