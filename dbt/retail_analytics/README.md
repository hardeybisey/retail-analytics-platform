# Analytics Project: Dimensional Modelling with dbt for Retail Analytics

## 📘 Table of Contents  
1. [Introduction](#introduction)  
2. [Dimensional Modelling](#dimensional-modelling)  
3. [dbt Overview](#dbt-overview)  
4. [Project Walkthrough](#project-walkthrough)  
   1. [Setup & Environment](#setup--environment)  
   2. [Identifying Business Process & Grain](#step-1-identify-business-process-and-grain)  
   3. [Designing Fact & Dimension Tables](#step-2-identify-dimension-and-fact-tables)  
   4. [Implementing Models](#step-3-building-the-dimensional-model-with-dbt)
        1. [Defining Sources](#31-defining-sources)
        2. [Creating Staging Models](#32-creating-staging-models)
        3. [Developing Dimension Models](#33-developing-dimension-models)
        4. [Constructing Fact Tables](#34-constructing-fact-tables)
        5. [Materialisation Strategy](#35-choosing-materialization-types)
        6. [Testing & Documentation](#36-implementing-documentation-and-tests)

---

## Introduction

This project demonstrates the end-to-end process of designing and implementing a dimensional model for analytics using **dbt** and **DuckDB**. The aim is to document each step clearly so future users can follow and replicate this work.


## Dimensional Modelling

Dimensional modelling (Ralph Kimball, *The Data Warehouse Toolkit*, 1996) transforms raw 3NF data into user-friendly **fact** and **dimension** tables for analytics and business intelligence workoads. While it's one of several approaches (**Data Vault**, **Third Normal Form**, and **One Big Table**) of data modelling,dimensional modelling is particularly favored for its user-friendliness and performance in analytical querying.


The key benefits of adopting dimensional modelling include:
- **Simplicity**: Dimensional models are designed for ease of understanding. Users typically don't need to perform complex joins; interactions between fact and dimension tables are streamlined through the use of surrogate keys.
- **Reusability (Don't Repeat Yourself - DRY)**: Dimensions can be shared across multiple fact tables. These are known as "conformed dimensions" and help avoid duplication of effort and ensure consistent analytical perspectives.
- **Performance**: Analytical queries executed against a dimensional model are often significantly faster than those against a highly normalized model (like 3NF). This is because many data transformations, such as joins and pre-aggregations, can be built into the model's ETL (Extract, Transform, Load) process.  
- **Business alignment**: The structure of dimensional models directly reflects business processes and associated metrics. This ensures that the data is not only accessible but also readily usable and interpretable by business users.

We’ll apply these principles to build our first dimensional model using dbt.


## dbt Overview

Data Build Tool (dbt) is a powerful open-source tool widely adopted in data engineering. Its primary function is to empower data teams to transform raw data already within a data warehouse into clean, structured, and analysis-ready datasets.

Key features of dbt that make it invaluable for projects like this include:

- **SQL-centric Transformations:** dbt allows data engineers and analysts to implement complex data transformation logic primarily using SQL queries, which are then compiled and executed against the target data warehouse. It also supports Python for more complex transformation tasks.
- **Testable and Version-Controlled Code:** dbt promotes software engineering best practices by enabling testing of data models, version control (via integration with tools like Git), and modular, manageable SQL code.
- **Code Reusability:** dbt models (which represent data transformation logic) can be referenced and reused across multiple projects and applications. This modularity streamlines development and enhances maintainability.
- **Automated Documentation and Lineage:** dbt can automatically generate documentation for your data models and visualize data lineage, making it easier to understand data flows and dependencies.

## Project Walkthrough

This section details the setup of the necessary tools for this project. We will be using dbt with the `dbt-duckdb` adapter, which allows dbt to run transformations on DuckDB, an in-process analytical data management system.

For a detailed guide, refer to the official documentation: [Connect to DuckDB](https://docs.getdbt.com/docs/core/connect-data-platform/duckdb-setup).

### Setup & Environment

1.  **Install dbt-core and dbt-duckdb:**
    ```bash
    python -m pip install dbt-core dbt-duckdb
    ```
2.  **Install pre-commit and SQLFluff (Optional for linting and formatting):**
    ```bash
    pip install pre-commit sqlfluff sqlfluff-templater-dbt
    ```

3. **Recommended versions (ensure compatibility with your environment):**
    ```
    # dbt-core==1.4.5
    # dbt-duckdb==1.4.1
    # sqlfluff==2.0.4
    # sqlfluff-templater-dbt==2.0.4
    ```
    *(Note: The versions above are examples from your original text; always consider using the latest compatible versions for new projects.)*

<!-- ### Project Initialization and Basic Commands

1.  **Initialize your dbt project:**
    This command sets up the basic directory structure and configuration files for a new dbt project.
    ```bash
    dbt init your_project_name
    ```
2.  **Key dbt commands used in this project:**
    *   `dbt seed`: Loads data from CSV files (defined in the `seeds` directory) into your data warehouse. Useful for static or lookup data.
    *   `dbt run`: Executes your dbt models to transform data.
    *   `dbt test`: Runs data quality tests defined on your models (e.g., uniqueness, not null).
    *   *Unit Testing*: While `dbt test` covers data tests, dbt also supports unit testing for macros using packages like `dbt-unit-testing`.
    *   *Macros*: Reusable pieces of SQL logic defined in dbt. -->


### The Dimensional Modelling Process

The following sections walk through the thought process and practical steps involved in creating a dimensional model for our scenario.

### Step 1: Identify Business Process and Grain

To effectively model data, we must first understand the business process we are analyzing. Consider the following business requirement:

> The Retail Analytics Platform is an e-commerce website that sells bicycles, shipping them to customers worldwide. As the CEO, I need to understand year-over-year revenue generation, with breakdowns by:
>
> *   Product category and subcategory
> *   Customer
> *   Order status
> *   Shipping country, state, and city

From this request, the core business process is clearly the **Sales Process**.

The next critical step is to define the **grain** of our fact table. The grain specifies exactly what an individual row in a fact table represents. For the sales process, common grains could be:
*   Each individual order line item.
*   Each complete order.
*   Daily sales summaries.

Choosing the most detailed (atomic) grain feasible provides the greatest flexibility for analysis, as data can always be aggregated up, but not easily disaggregated down.

### Step 2: Identify Dimension and Fact Tables

Based on the CEO's requirements, we aim to design a dimensional model for the Sales process that allows slicing and dicing data by:

*   Product category and subcategory
*   Customer details
*   Order status
*   Shipping geography (country, state, city)
*   Date attributes (year, month, day)

#### Fact Tables: Capturing Business Events

[Fact tables](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/facts-for-measurement/) are central to a dimensional model. They store the quantitative measures (facts) related to a specific business process event. Each row in a fact table corresponds to an event at the defined grain. Examples include:

*   An item being sold.
*   A click on a website.

For our Sales process, we examine the source `sales` schema. Two tables are of particular interest for constructing our fact table:

*   `sales.order`: Contains header-level information for an order, such as credit card details, shipping address, and customer information. Each record represents a distinct order, which may comprise multiple order details.
*   `sales.order_details`: Contains information about individual products within an order, including quantity and unit price, which are essential for calculating revenue. Each record here represents a single line item on an order.

**Defining the Grain:** We aim to design our dimensional model at the lowest possible level of detail. This provides maximum flexibility for stakeholders, enabling them to slice and dice the data across various dimensions without being constrained by pre-aggregated data. Therefore, the grain of our sales fact table will be **each individual order line item**. While we might create aggregated views on top of this fact table for common analyses, users should retain access to the granular data.

#### Dimension Tables: Providing Context

[Dimension tables](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/dimensions-for-context/) provide the descriptive context for the facts in a fact table. They answer the "who, what, where, when, why, and how" related to a business process event. Examples:

*   **Customer details:** Who placed a particular order?
*   **Product details:** What product was added to the cart?

Based on the business questions, we can identify several source tables that contain valuable contextual information:

*   `customer.customer`
*   `customer.address`
*   `customer.country`
*   `product.product`
*   `product.category`
*   `sales.order` (some fields might be denormalized into dimensions or used to link to dimensions)
*   `sales.order_details` (similarly, some fields provide context)
*   And potentially many more depending on the richness of the source data.

#### Schema Design: Choosing the Star Schema

There are multiple ways to structure dimension tables. One approach involves linking dimension tables to other dimension tables in a normalized fashion, as shown below.

![](img/snowflake-schema.png)
*Figure 1: Snowflake Schema Example*

This is known as a **snowflake schema**. While it reduces data redundancy within the dimensions, it can lead to more complex queries requiring numerous joins for analysts.

An alternative, and often preferred approach for analytical performance and simplicity, is the **star schema**. In this design, dimension tables are denormalized (by pre-joining related tables) and connect directly to the central fact table.

![](img/star-schema.png)
*Figure 2: Star Schema Example*

The star schema simplifies queries and generally improves query performance for end-users by reducing the number of joins needed at query time.

For this project, we will adopt the star schema approach. Based on the analytical requirements, we identify the following six key dimensions:

![](img/dimension-tables.png)
*Figure 3: Planned Dimension Tables*

*   `dim_product`: A consolidated dimension joining `product`, `productsubcategory`, and `productcategory` tables.
*   `dim_address`: A dimension combining `address`, `stateprovince`, and `countryregion` information.
*   `dim_customer`: A dimension joining `customer` and related tables (e.g., `person`, `store` if applicable, though your example focuses on `customer`).
*   `dim_credit_card`: A dimension created from the `creditcard` table.
*   `dim_order_status`: A dimension derived by taking distinct statuses from `salesorderheader` (or `sales.order`).
*   `dim_date`: A specially generated dimension table containing various date attributes (e.g., year, quarter, month, day, day of week). This can be built using packages like [dbt_date](https://hub.getdbt.com/calogica/dbt_date/latest/) or custom SQL.
    *   *Note: As stated, since DuckDB might not be supported by certain dbt packages like `dbt_date` at the time of writing, this table might be manually seeded or generated using compatible dbt macros/SQL.*

### Step 3: Building the Dimensional Model with dbt

This section details the dbt implementation steps to create the fact and dimension tables.

#### 3.1: Defining Sources

The first step in dbt is to declare your raw source tables. While in a production system these tables would already exist in your data warehouse, dbt needs to know about them to build a lineage graph and allow you to reference them. This is done by defining them in `.yml` files, typically within the `models/sources/` directory (though the exact path and naming are conventions).

**Project Organization:** For this project, source definitions are organized by creating a `.yml` file for each source schema (e.g., `product.yml`, `customer.yml`) inside `models/sources/`. This promotes clarity and logical grouping.


retail_analytics/models/
└── sources
├── product.yml
├── customer.yml
└── ...

**Example `customer.yml`:**
```yaml
version: 2

sources:
  - name: customer
    database: retail_analytics  
    schema: customer  
    tables:
      - name: customer

```

#### 3.2: Creating Staging Models

Once sources are defined, it's best practice to create staging models. These models typically perform light transformations on source data, such as:

- Renaming columns (e.g., to follow a consistent naming convention).
- Basic data type conversions.
- Casting columns to appropriate types.
- Simple calculations if necessary (though complex logic is usually deferred to intermediate or mart models).

Staging models provide a clean, consistent layer on top of your raw data and act as a crucial debugging step. If issues arise later, you can more easily determine if the problem originates from the source data or subsequent transformations.

Naming Convention and Location: Staging models for this project are placed in a models/staging/ directory and prefixed with stg_<source_name>__<table_name>.sql (e.g., stg_customer__customer.sql). This self-documenting convention aids navigation.

Staging models reference source tables using dbt's {{ source() }} function, which helps maintain data lineage.

**Example `stg_customer__address.sql`:**
```sql
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
```

#### 3.3: Developing Dimension Models

Dimension models transform data (usually from staging models) into the denormalized dimension tables defined in our star schema. They use dbt's {{ ref() }} function to reference upstream models (e.g., staging models), creating a Directed Acyclic Graph (DAG) of dependencies.

Surrogate Keys: It is a best practice to use surrogate keys (system-generated unique identifiers) as primary keys in dimension tables, rather than natural keys from the source systems. Surrogate keys help insulate the data warehouse from changes in source system keys and can improve join performance. These can be simple sequential IDs or, more robustly, generated using functions like dbt_utils.generate_surrogate_key, which creates a hash based on one or more columns (typically the natural key).

**Example `dim_product.sql` (located in models/marts or similar):**
```sql
select
    {{ dbt_utils.generate_surrogate_key(['p.product_id']) }} as product_key, 
    p.product_id,
    p.product_name,
    p.product_sku_no,
    p.product_cost,
    p.product_list_price,
    p.product_stock_level,
    p.product_reorder_threshold,
    c.product_category_name,
    s.product_subcategory_name,
    p.product_created_at,
    p.product_updated_at
from {{ ref('stg_product__product') }} as p
left join {{ ref('stg_product__subcategory') }} as s
    on p.product_subcategory_id = s.product_subcategory_id
left join {{ ref('stg_product__category') }} as c
    on s.product_category_id = c.product_category_id
```


#### 3.4: Constructing Fact Tables

Fact tables are built by joining relevant dimension tables (using their surrogate keys) to the measures derived from staging (or intermediate) models that represent the business process at the defined grain.

Our grain is the individual product line item on an order. The stg_sales__order_detail table will be central, joined with stg_sales__order for header-level information and then linked to the dimension tables.

**Example `fct_sales.sql` (located in models/marts or similar):**
```sql
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
    (lit.line_total / o.order_total_due) * o.order_shipping_cost as shipping_allocated,
    (lit.line_total / o.order_total_due) * o.order_tax_amount as tax_allocated

from {{ ref('stg_sales__order') }} as o
inner join {{ ref('stg_sales__order_detail') }} as od
    on o.order_id = od.order_id
inner join line_item_total as lit
    on od.order_detail_id = lit.order_detail_id
inner join {{ ref('dim_date') }} as d
    on o.order_created_at = d.full_date
``` 

**Note: The exact joins to dimensions depend on the natural keys available in your `stg_sales__order` and `stg_sales__order_detail` tables and how you've defined your dimension keys.**

#### 3.5: Choosing Materialization Types

dbt supports several materialization types for your models, determining how they are persisted in the data warehouse:

- **View:** The model is rebuilt as a SQL view. Queries against views always fetch the latest data by executing the underlying SQL.
- **Table:** The model's results are built into a new table. This is generally faster to query than views for complex transformations but requires explicit rebuilding (`dbt run`) to update.
- **Incremental:** Models are built as tables, but dbt only processes new or changed data on subsequent runs, which can significantly speed up build times for large datasets.
- **Ephemeral:** Models are not directly built in the database but are used as CTEs in downstream models.

Dimension tables often have relatively small data volumes and can be materialized as `table` or `view`. For this project, we'll materialize dimension models in the `marts` schema as `table` for query performance. This can be configured in `dbt_project.yml`:

```yaml
models:
  your_project_name: 
    marts: 
      +materialized: table
      +schema: marts 
```

Fact tables, especially large ones, are often good candidates for incremental materialization after the initial build.

#### 3.6: Implementing Documentation and Tests

Documenting your models and defining data tests are crucial best practices. dbt allows you to add descriptions and tests directly in .yml files alongside your model configurations.

Example of model documentation and tests in a schema .yml file (e.g., models/sources/product.yml or models/marts/dimensions/dim_product.yml):

```yaml
version: 2

sources:
  - name: product
    database: retail_analytics  
    schema: product  
    tables:
      - name: product
        description: >
          "Product information table"
        columns: 
          - name: id
            description: integer
            tests:
              - unique
              - not_null
          - name: subcategory_id
            description: integer
          - name: sku_no
            description: varchar
            tests:
              - not_null

```


You can find more about defining tests and documentation here: dbt Docs - Tests and dbt Docs - Documentation.

Run dbt docs generate to compile your documentation and dbt docs serve to view it locally. Run dbt test to execute your defined data tests.