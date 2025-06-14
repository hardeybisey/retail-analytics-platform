select
    id as address_id,
    address_line1,
    address_line2,
    city,
    postal_code,
    state_id,
    address_type,
    created_date as address_created_at,
    modified_date as address_updated_at
from {{ source('customer', 'address') }}