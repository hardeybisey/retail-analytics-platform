with f_transaction as (
    select * from {{ ref('fact_transaction') }}
),

d_customer as (
    select * from {{ ref('dim_customer') }}
),

d_address as (
    select * from {{ ref('dim_address') }}
),

d_product as (
    select * from {{ ref('dim_product') }}
),

d_date as (
    select * from {{ ref('dim_date') }}
)

select
    {{ dbt_utils.star(from=ref('fact_transaction'), relation_alias='f_transaction', except=[
        "product_id", "customer_id", "order_id", "shipping_address_id", "billing_address_id", "date_key"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_product'), relation_alias='d_product', except=["product_id"]) }},
    {{ dbt_utils.star(from=ref('dim_customer'), relation_alias='d_customer', except=["customer_id"]) }},
    {{ dbt_utils.star(from=ref('dim_address'), relation_alias='d_address', except=["address_id"]) }},
    {{ dbt_utils.star(from=ref('dim_date'), relation_alias='d_date', except=["date_key"]) }}
from f_transaction
left join d_product on f_transaction.product_id = d_product.product_id
left join d_customer on f_transaction.customer_id = d_customer.customer_id
left join d_address on f_transaction.shipping_address_id = d_address.address_id
left join d_date on f_transaction.order_date_key = d_date.date_key
