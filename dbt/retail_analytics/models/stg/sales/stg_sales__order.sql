select
    id as order_id,
    customer_id,
    shipping_address_id,
    billing_address_id,
    order_date as order_created_at,
    modified_date as order_updated_at,
    due_date as order_due_date,
    order_status,
    order_total as order_total_amount,
    shipping_cost as order_shipping_cost,
    tax_due as order_tax_amount,
    total_due as order_total_due
from {{ source('sales', 'order') }}