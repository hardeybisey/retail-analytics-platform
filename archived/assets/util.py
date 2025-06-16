import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

fake = Faker()

# Helper functions


def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


def random_bool():
    return random.choice([True, False])


# Regions, Countries, States
regions = pd.DataFrame([{"id": i + 1, "name": f"Region {i + 1}"} for i in range(3)])
countries = pd.DataFrame(
    [
        {"id": i + 1, "name": fake.country(), "iso_code": fake.country_code()}
        for i in range(3)
    ]
)
states = pd.DataFrame(
    [
        {"id": i + 1, "name": fake.state(), "region_id": random.choice(regions["id"])}
        for i in range(5)
    ]
)

# Addresses
addresses = pd.DataFrame(
    [
        {
            "id": i + 1,
            "street": fake.street_address(),
            "city": fake.city(),
            "postcode": fake.postcode(),
            "state_id": random.choice(states["id"]),
            "country_id": random.choice(countries["id"]),
        }
        for i in range(10)
    ]
)

# Customers
customers = pd.DataFrame(
    [
        {
            "id": i + 1,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address_id": random.choice(addresses["id"]),
            "created_at": datetime.now(),
        }
        for i in range(10)
    ]
)

# Customer Addresses
customer_addresses = pd.DataFrame(
    [
        {
            "customer_id": c_id,
            "address_id": random.choice(addresses["id"]),
            "address_type": random.choice(["billing", "shipping", "both"]),
            "is_default": random_bool(),
        }
        for c_id in customers["id"]
    ]
)

# Return Policies
return_policies = pd.DataFrame(
    [
        {"id": i + 1, "returnable": 1, "return_window_days": 30, "restocking_fee": 5}
        for i in range(3)
    ]
)

# Product Category and Subcategory
categories = pd.DataFrame(
    [{"id": i + 1, "name": f"Category {i + 1}"} for i in range(3)]
)
subcategories = pd.DataFrame(
    [
        {
            "id": i + 1,
            "name": f"Subcategory {i + 1}",
            "category_id": random.choice(categories["id"]),
            "created_at": datetime.now(),
        }
        for i in range(5)
    ]
)

# Products
products = pd.DataFrame(
    [
        {
            "id": i + 1,
            "name": f"Product {i + 1}",
            "price": round(random.uniform(5.0, 200.0), 2),
            "description": fake.text(50),
            "is_active": random_bool(),
            "is_promoted": random_bool(),
            "category_id": random.choice(categories["id"]),
            "subcategory_id": random.choice(subcategories["id"]),
            "return_policy_id": random.choice(return_policies["id"]),
            "created_at": datetime.now(),
        }
        for i in range(20)
    ]
)

# Fulfillment Centres
centres = pd.DataFrame(
    [
        {
            "id": i + 1,
            "name": f"Centre {i + 1}",
            "address_id": random.choice(addresses["id"]),
            "capacity": random.randint(100, 1000),
            "is_active": random_bool(),
        }
        for i in range(3)
    ]
)

# Inventory
inventory = pd.DataFrame(
    [
        {
            "id": i + 1,
            "product_id": random.choice(products["id"]),
            "centre_id": random.choice(centres["id"]),
            "stock_level": random.randint(0, 100),
            "reorder_threshold": 10,
            "last_updated": datetime.now(),
            "is_backorderable": random_bool(),
        }
        for i in range(30)
    ]
)

# Inventory Log
inventory_logs = pd.DataFrame(
    [
        {
            "id": i + 1,
            "product_id": random.choice(products["id"]),
            "change_type": random.choice(["restock", "purchase", "return"]),
            "quantity_change": random.randint(-10, 10),
            "change_timestamp": int(datetime.now().timestamp()),
            "reference_order_id": None,
        }
        for i in range(30)
    ]
)

# Shipping Carriers and Methods
carriers = pd.DataFrame(
    [{"id": i + 1, "name": name} for i, name in enumerate(["fedex", "amazon", "ups"])]
)
shipping_methods = pd.DataFrame(
    [
        {
            "id": i + 1,
            "method_name": name,
            "carrier_id": random.choice(carriers["id"]),
            "estimated_days": random.randint(1, 5),
            "cost": random.randint(5, 20),
        }
        for i, name in enumerate(["standard", "express", "next day"])
    ]
)

# Payment Methods
payment_methods = pd.DataFrame(
    [
        {"id": i + 1, "name": name}
        for i, name in enumerate(["CC", "PayPal", "Apple Pay", "Klarna", "Coupon"])
    ]
)

# Orders
orders = pd.DataFrame(
    [
        {
            "id": i + 1,
            "customer_id": random.choice(customers["id"]),
            "order_date": str(datetime.now()),
            "payment_method_id": random.choice(payment_methods["id"]),
            "shipping_address_id": random.choice(addresses["id"]),
            "billing_address_id": random.choice(addresses["id"]),
        }
        for i in range(10)
    ]
)

# Order Details
order_details = pd.DataFrame(
    [
        {
            "id": i + 1,
            "order_id": random.choice(orders["id"]),
            "product_id": random.choice(products["id"]),
            "shipping_id": random.choice(shipping_methods["id"]),
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(5.0, 200.0), 2),
            "discount": round(random.uniform(0, 10), 2),
        }
        for i in range(20)
    ]
)

# Card Information
card_info = pd.DataFrame(
    [
        {
            "id": i + 1,
            "customer_id": random.choice(customers["id"]),
            "payment_provider_id": random.choice(payment_methods["id"]),
            "card_type": random.choice(["Visa", "MasterCard", "Amex"]),
            "last_four_digits": random.randint(1000, 9999),
            "expiry_month": random.randint(1, 12),
            "expiry_year": random.randint(2025, 2030),
        }
        for i in range(10)
    ]
)

# Output sample data size
{
    "products": len(products),
    "customers": len(customers),
    "orders": len(orders),
    "order_details": len(order_details),
    "inventory": len(inventory),
}
