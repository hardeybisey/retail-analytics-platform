select
    id as credit_card_id,
    customer_id,
    card_number,
    card_type,
    expiry_year,
    created_date as credit_card_created_at,
    modified_date as credit_card_updated_at
from {{ source('sales', 'card_information') }}