select
    a.address_id,
    a.address_line1,
    a.address_line2,
    a.city,
    a.postal_code,
    s.state,
    s.state_province_code,
    c.country_iso_code,
    c.country_name,
    a.address_created_at,
    a.address_updated_at
from {{ ref('stg_customer__address') }} as a
left join {{ ref('stg_customer__state') }} as s
    on a.state_id = s.state_id
left join {{ ref('stg_customer__country') }} as c
    on s.country_iso_code = c.country_iso_code
