select
    id as product_category_id,
    name as product_category_name,
    created_date as product_category_created_at,
    modified_date as product_category_updated_at
from {{ ref('category') }}
