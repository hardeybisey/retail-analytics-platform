select
    iso_code as country_iso_code,
    name as country_name
from {{ source('customer', 'country') }}