select
    p.product_id,
    p.product_name,
    p.product_sku_no,
    p.product_cost,
    p.product_list_price,
    p.product_stock_level,
    p.product_reorder_threshold,
    coalsece(c.product_category_name, "No Category") as product_category_name,
    coalsece(s.product_subcategory_name, "No Subcategory") as product_subcategory_name,
    p.product_created_at,
    p.product_updated_at
from {{ ref('stg_product__product') }} as p
left join {{ ref('stg_product__subcategory') }} as s
    on p.product_subcategory_id = s.product_subcategory_id
left join {{ ref('stg_product__category') }} as c
    on s.product_category_id = c.product_category_id
