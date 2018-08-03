CREATE DATABASE "real_estate"
    WITH OWNER "postgres"
    ENCODING 'UTF8';
\c real_estate
CREATE TABLE real_estate.public.estate (
        estate_title TEXT,
        estate_address TEXT,
        estate_area TEXT,
        estate_description TEXT,
        estate_price TEXT,
        estate_type TEXT,
        estate_tag TEXT,
        estate_date TEXT,
        estate_seller_name TEXT,
        estate_seller_address TEXT,
        estate_seller_phone TEXT,
        estate_seller_mobile TEXT,
        estate_seller_email TEXT
);

