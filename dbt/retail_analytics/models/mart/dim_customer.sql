select
    customer_id,
    customer_address_id,
    first_name,
    middle_name,
    last_name,
    email,
    gender,

    customer_created_at,
    customer_updated_at
from {{ ref('stg_customer__customer') }}
