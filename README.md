# Goose Goose Go - CS348 Project

## Description
This project aims to develop a web application for tracking menus, ingredients, and prices of various food places in Waterloo.

## Database Setup
For our project, we have decided to use AWS RDS running MySQL. 

### Connection
1. To connect to the database, first download MySQL Workbench ```https://www.mysql.com/products/workbench/```
2. Create a new connection by clicking the '+' sign beside "MySQL Connections"
3. Enter a connection name, the hostname is the RDS endpoint, the username and the password.
4. Test connection to make sure everything is working and click OK.
You are now connected to the RDS database!

### Create Sample Database
Here are the queries necessary to create a sample database

Create a database and use it for upcoming queries
```sql
CREATE DATABASE sample_db;
USE sample_db;
```
Create table for `food_items`
```sql
CREATE TABLE food_items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT
)
```
Load sample data into the database
```sql
INSERT INTO food_items (name, price, description) VALUES ('RiceNoodle', 0.00, 'rice noodle refils are free at Yunshang');
INSERT INTO food_items (name, price, description) VALUES ('Foodie Sushi', 16.00, 'foodie fruity has a varity of selection including sushis');
```

The database has been loaded with sample data!
