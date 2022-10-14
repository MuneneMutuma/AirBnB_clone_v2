-- Create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_test@localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant user all privileges on db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the database perfomance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'; 
