mysql -u root -p
Create database - create database employees;
use employees;
create table employeeDetails (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, dateOfBirth DATE, joiningDate DATE, salary DECIMAL(10, 2), department VARCHAR(255));
desc employeedetails;
INSERT INTO employeedetails (name, dateOfBirth, joiningDate, salary) VALUES ("Example Name", "2004-02-27", "2023-11-01", 5000.00);