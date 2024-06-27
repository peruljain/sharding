#!/bin/bash

# Wait for mysql1 to be ready
until docker exec sharding-mysql1-1 mysql -u root -proot -e "SELECT 1"; do
  echo "Waiting for mysql1 database connection..."
  sleep 5
done

# Create table in mysql1
docker exec sharding-mysql1-1 mysql -u root -proot -e "
CREATE TABLE user.user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);"

echo "Table created in mysql1."

# Wait for mysql2 to be ready
until docker exec sharding-mysql2-1 mysql -u root -proot -e "SELECT 1"; do
  echo "Waiting for mysql2 database connection..."
  sleep 5
done

# Create table in mysql2
docker exec sharding-mysql2-1 mysql -u root -proot -e "
CREATE TABLE user.user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);"

echo "Table created in mysql2."
