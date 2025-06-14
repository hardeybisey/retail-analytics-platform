select
    id as customer_id,
    address_id as customer_address_id,
    first_name,
    middle_name,
    last_name,
    email,
    gender,
    created_date as customer_created_at,
    modified_date as customer_updated_at
from {{ source('customer', 'customer') }}