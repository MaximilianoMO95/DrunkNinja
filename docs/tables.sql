CREATE TABLE user (
    user_id     NUMBER PRIMARY KEY,
    username    VARCHAR2(50) NOT NULL,
    password    VARCHAR2(100) NOT NULL,
    email       VARCHAR2(100) NOT NULL
);

CREATE TABLE shopping_cart (
    cart_id NUMBER PRIMARY KEY,
    user_id NUMBER UNIQUE,

    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE orders (
    order_id NUMBER PRIMARY KEY,
    user_id NUMBER,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_status VARCHAR2(20) NOT NULL, 

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE category (
    category_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL
);

CREATE TABLE product (
    product_id  NUMBER PRIMARY KEY,
    category_id NUMBER NOT NULL,

    name        VARCHAR2(100) NOT NULL,
    price       NUMBER(6) NOT NULL,
    description CLOB,

    FOREIGN KEY (category_id) REFERENCES category(category_id)
);
