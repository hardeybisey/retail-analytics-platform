CREATE TABLE product (
    id integer PRIMARY KEY,
    subcategory_id integer,
    sku_no varchar,
    name varchar,
    color varchar,
    cost_price numeric,
    list_price numeric,
    weight numeric,
    class varchar,
    product_line varchar,
    stock_level smallint,
    reorder_threshold smallint,
    created_date timestamp,
    modified_date timestamp
);

CREATE TABLE subcategory (
    id integer PRIMARY KEY,
    category_id integer,
    name varchar,
    created_date timestamp,
    modified_date timestamp
);

CREATE TABLE category (
    id integer PRIMARY KEY,
    name varchar,
    created_date timestamp,
    modified_date timestamp
);

CREATE TABLE customer (
    id integer PRIMARY KEY,
    address_id integer,
    title varchar,
    first_name varchar,
    middle_name varchar,
    last_name varchar,
    email varchar,
    gender varchar,
    created_date timestamp,
    modified_date timestamp
);

CREATE TABLE address (
    id integer PRIMARY KEY,
    state_id integer,
    address_line1 varchar,
    address_line2 varchar,
    city varchar,
    postal_code varchar,
    created_date timestamp,
    modified_date timestamp,
    address_type varchar
);

CREATE TABLE state (
    id integer PRIMARY KEY,
    name varchar,
    country_iso_code varchar,
    state_province_code varchar
);

CREATE TABLE country (
    iso_code varchar PRIMARY KEY,
    name varchar
);

CREATE TABLE "order" (
    id integer PRIMARY KEY,
    customer_id integer,
    shipping_address_id integer,
    billing_address_id integer,
    order_date timestamp,
    modified_date timestamp,
    ship_date timestamp,
    due_date timestamp,
    credit_card_id integer,
    order_total float,
    order_status varchar,
    shipping_cost float,
    tax_due float,
    total_due float
);

CREATE TABLE order_detail (
    id integer PRIMARY KEY,
    order_id integer,
    product_id integer,
    unit_price float,
    unit_price_discount float,
    quantity integer,
    created_date timestamp,
    modified_date timestamp
);

CREATE TABLE card_information (
    id integer PRIMARY KEY,
    customer_id integer,
    card_type varchar,
    card_number varchar,
    expiry_year integer,
    expiry_month integer,
    created_date timestamp,
    modified_date timestamp
);

COMMENT ON COLUMN address.address_type IS 'Billing, Shipping, Both';

ALTER TABLE product ADD FOREIGN KEY (
    subcategory_id
) REFERENCES subcategory (id);

ALTER TABLE subcategory ADD FOREIGN KEY (
    category_id
) REFERENCES category (id);

ALTER TABLE customer ADD FOREIGN KEY (address_id) REFERENCES address (
    id
);

ALTER TABLE address ADD FOREIGN KEY (state_id) REFERENCES state (id);

ALTER TABLE state ADD FOREIGN KEY (country_iso_code) REFERENCES country (
    iso_code
);

ALTER TABLE "order" ADD FOREIGN KEY (customer_id) REFERENCES customer (
    id
);

ALTER TABLE "order" ADD FOREIGN KEY (
    shipping_address_id
) REFERENCES address (id);

ALTER TABLE "order" ADD FOREIGN KEY (
    billing_address_id
) REFERENCES address (id);

ALTER TABLE "order" ADD FOREIGN KEY (
    credit_card_id
) REFERENCES card_information (id);

ALTER TABLE order_detail ADD FOREIGN KEY (order_id) REFERENCES "order" (
    id
);

ALTER TABLE order_detail ADD FOREIGN KEY (
    product_id
) REFERENCES product (id);

ALTER TABLE card_information ADD FOREIGN KEY (
    customer_id
) REFERENCES customer (id);
