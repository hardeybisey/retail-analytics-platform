with line_item_total as (
    select
        order_detail_id,
        (unit_price - unit_price_discount) * quantity as line_total
    from {{ ref('stg_sales__order_detail') }}
)

select
    -- tid,
    o.order_id,
    o.customer_id,
    od.product_id,
    od.order_detail_id,
    d.date_key,


    o.shipping_address_id,
    o.billing_address_id,
    o.order_due_date,
    o.order_status,
    od.unit_price,
    od.unit_price_discount,


    od.quantity,
    (lit.line_total / o.order_total_due) * o.order_shipping_cost as shipping_cost_allocated,
    (lit.line_total / o.order_total_due) * o.order_tax_amount as tax_cost_allocated

from {{ ref('stg_sales__order') }} as o
inner join {{ ref('stg_sales__order_detail') }} as od
    on o.order_id = od.order_id
inner join line_item_total as lit
    on od.order_detail_id = lit.order_detail_id
inner join {{ ref('dim_date') }} as d
    on o.order_created_at = d.full_date