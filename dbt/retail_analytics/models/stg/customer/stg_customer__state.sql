select
    id as state_id,
    name as state,
    country_iso_code,
    state_province_code
from {{ source('customer', 'state') }}