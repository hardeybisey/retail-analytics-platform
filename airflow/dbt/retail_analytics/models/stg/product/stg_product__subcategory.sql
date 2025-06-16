select
    id as product_subcategory_id,
    name as product_subcategory_name,
    category_id as product_category_id,
    created_date as product_subcategory_created_at,
    modified_date as product_subcategory_updated_at
from {{ ref('subcategory') }}
