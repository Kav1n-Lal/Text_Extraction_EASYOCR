# Text_Extraction_EASYOCR
Create an environment in anaconda navigator as env_easyocr
-pip install easyocr
-Download all the necessary packages
-Also install pytorch for cpu in this environment

# MYSQL WORKBENCH
Create database under the name userinfo
-CREATE TABLE customer_details
  (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),email VARCHAR(50),userid VARCHAR(4));
- CREATE TABLE bizcard_details
  (id INT AUTO_INCREMENT PRIMARY KEY,registered_name VARCHAR(30),registered_email VARCHAR(50),registered_userid VARCHAR(4),
  company VARCHAR(100),cardholder VARCHAR(50),designation VARCHAR(75),mobile VARCHAR(100),email VARCHAR(50),
  website VARCHAR(100),pincode VARCHAR(6),state VARCHAR(50),district VARCHAR(50),area VARCHAR(100),bizcard_photo MEDIUMBLOB NOT NULL);
  
 -Create a folder and copy craft_mlt.pth,english_g2.pth files and cudacheck.py file 
 -Inside the cudacheck.py file in the lines 21 and 40 type your mysql <password> in it
  -Run streamlit run cudacheck.py
