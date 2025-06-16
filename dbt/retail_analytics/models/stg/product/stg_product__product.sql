select
    id as product_id,
    sku_no as product_sku_no,
    name as product_name,
    cost_price as product_cost,
    list_price as product_list_price,
    weight as product_weight,
    class as product_class,
    stock_level as product_stock_level,
    reorder_threshold as product_reorder_threshold,
    subcategory_id as product_subcategory_id,
    created_date as product_created_at,
    modified_date as product_updated_at
from {{ source('product', 'product') }}