CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;
-- ==========================================
-- Student Management System Database Script
-- ==========================================

-- Create Database
CREATE DATABASE IF NOT EXISTS student_management;

-- Select Database
USE student_management;

-- Drop table if it already exists (Optional)
DROP TABLE IF EXISTS student;

-- Create Student Table
CREATE TABLE student (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    SEMESTER INT NOT NULL,
    BRANCH VARCHAR(100) NOT NULL,
    ADDRESS VARCHAR(300) NOT NULL
);

-- Insert Sample Student Data
INSERT INTO student (NAME, SEMESTER, BRANCH, ADDRESS) VALUES
('Rahul Sharma', 1, 'Computer Science', 'Jaipur'),
('Priya Verma', 2, 'Information Technology', 'Delhi'),
('Amit Kumar', 3, 'Mechanical Engineering', 'Lucknow'),
('Sneha Gupta', 4, 'Electronics Engineering', 'Bhopal'),
('Rohit Singh', 5, 'Civil Engineering', 'Kota'),
('Neha Sharma', 6, 'Computer Science', 'Ajmer'),
('Arjun Patel', 7, 'Electrical Engineering', 'Ahmedabad'),
('Pooja Yadav', 8, 'Information Technology', 'Indore'),
('Vikas Meena', 2, 'Mechanical Engineering', 'Udaipur'),
('Anjali Jain', 3, 'Computer Science', 'Jodhpur'),
('Mohit Saini', 4, 'Civil Engineering', 'Alwar'),
('Kavita Sharma', 5, 'Electronics Engineering', 'Jaipur'),
('Deepak Kumar', 6, 'Electrical Engineering', 'Patna'),
('Riya Mishra', 7, 'Computer Science', 'Kanpur'),
('Nikhil Joshi', 8, 'Mechanical Engineering', 'Nagpur'),
('Simran Kaur', 1, 'Information Technology', 'Chandigarh'),
('Harsh Agarwal', 2, 'Computer Science', 'Noida'),
('Meena Kumari', 3, 'Civil Engineering', 'Ranchi'),
('Sourabh Sharma', 4, 'Electrical Engineering', 'Gwalior'),
('Ankit Verma', 5, 'Electronics Engineering', 'Agra');

-- Verify Data
SELECT * FROM student;