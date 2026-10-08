# data.py

orders = {
    "ORD1001": {
        "customer": "Venu",
        "product": "Samsung Galaxy Phone",
        "amount": 25000,
        "payment_status": "Paid",
        "order_status": "Delivered",
        "delivery_date": "2026-10-04",
        "tracking_id": "TRK1001"
    },

    "ORD1002": {
        "customer": "Rahul",
        "product": "Wireless Headphones",
        "amount": 3000,
        "payment_status": "Paid",
        "order_status": "Shipped",
        "delivery_date": None,
        "tracking_id": "TRK1002"
    },

    "ORD1003": {
        "customer": "Anil",
        "product": "Laptop",
        "amount": 65000,
        "payment_status": "Paid",
        "order_status": "Delivered",
        "delivery_date": "2026-10-03",
        "tracking_id": "TRK1003"
    }
}


shipments = {
    "TRK1001": {
        "courier": "FastExpress",
        "status": "Delivered",
        "location": "Hyderabad",
        "expected_delivery": "2026-10-04"
    },

    "TRK1002": {
        "courier": "QuickDelivery",
        "status": "In Transit",
        "location": "Bangalore",
        "expected_delivery": "2026-10-08"
    },

    "TRK1003": {
        "courier": "FastExpress",
        "status": "Delivered",
        "location": "Hyderabad",
        "expected_delivery": "2026-10-03"
    }
}


returns = {}

refunds = {}

replacements = {}