CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email) VALUES
    ('john_doe', 'john.doe@example.com'),
    ('jane_smith', 'jane.smith@example.com'),
    ('alice_wonder', 'alice.wonder@example.com');

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO products (name, price) VALUES
    ('Laptop', 1200.00),
    ('Smartphone', 800.00),
    ('Headphones', 150.00);