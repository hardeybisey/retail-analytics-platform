# retail-analytics-platform
Retail Analytics Platform


Data Source
This dataset provides an in-depth look at the profitability of e-commerce sales. It contains data on a variety of sales channels, including Shiprocket and INCREFF, as well as financial information on related expenses and profits. The columns contain data such as SKU codes, design numbers, stock levels, product categories, sizes and colors. In addition to this we have included the MRPs across multiple stores like Ajio MRP , Amazon MRP , Amazon FBA MRP , Flipkart MRP , Limeroad MRP Myntra MRP and PaytmMRP along with other key parameters like amount paid by customer for the purchase , rate per piece for every individual transaction Also we have added transactional parameters like Date of sale months category fulfilledby B2b Status Qty Currency Gross amt . This is a must-have dataset for anyone trying to uncover the profitability of e-commerce sales in today's marketplace

* https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data?select=May-2022.csv

Data Models:
* Products: Product ID, name, category, supplier info, price, description.
* Customers: Customer ID, name, email, address, registration date.
* Transaction: Transaction ID, customer ID, product ID, quantity, price, transaction date, store ID.
* Stores: Store_id, store_name, store_size.
* Inventory: Product ID, store ID, stock level, last updated.
* Date Dimension: www.kimballgroup.com
* Time-of-day dimension

<!-- https://docs.getdbt.com/blog/kimball-dimensional-model -->

product
product_category
product_subcategory
Customer
Address
country
state
region
Sales
order
orderdetail
paymentmmethod
cardinformation


<: one-to-many. E.g: users.id < posts.user_id
>: many-to-one. E.g: posts.user_id > users.id
-: one-to-one. E.g: users.id - user_infos.user_id
<>: many-to-many. E.g: authors.id <> books.id



# Install DBT and setup duckdb adapter
Guide : https://docs.getdbt.com/docs/core/connect-data-platform/duckdb-setup
    * python -m pip install dbt-core dbt-duckdb
    * pip install pre-commit sqlfluff sqlfluff-templater-dbt

    <!-- dbt-core==1.4.5
    dbt-postgres==1.4.5
    dbt-duckdb==1.4.1
    sqlfluff==2.0.4
    sqlfluff-templater-dbt==2.0.4 -->
    * dbt init


    * dbt seed
    * dbt test
    * dbt unit test
    * dbt macro

    <!-- https://astronomer.github.io/astronomer-cosmos/getting_started/open-source.html -->
