select
    id as order_detail_id,
    order_id,
    product_id,
    unit_price,
    unit_price_discount,
    quantity,
    created_date as order_detail_created_at,
    modified_date as order_detail_updated_at
from {{ source('sales', 'order_detail') }}