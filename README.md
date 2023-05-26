# App Demo
*Click Below Link to view app demonstration video*
https://drive.google.com/file/d/13IyHs2RnZ6tAPn-AzY0YnaPsE0DSXzkc/view?usp=drive_link

## Some screenshots from the app

**Initial look**
![Screenshot (172)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/956a1c65-64ae-425d-8171-cb4fbf98124e)

**After entering credentials**
![Screenshot (173)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/a3f5355d-2342-4910-add0-0022c161579e)

**After loading the image and its corresponding extracted text**
![Screenshot (175)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/fd56a2b0-ee7c-4b51-8a68-0e71369353ef)


# Text_Extraction_EASYOCR
- Create an environment in anaconda navigator as env_easyocr
- pip install easyocr
- Download all the necessary packages
- Also install pytorch for cpu in this environment

# MYSQL WORKBENCH
- Create database under the name userinfo
- CREATE TABLE customer_details
  (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),email VARCHAR(50),userid VARCHAR(4));
- CREATE TABLE bizcard_details
  (id INT AUTO_INCREMENT PRIMARY KEY,registered_name VARCHAR(30),registered_email VARCHAR(50),registered_userid VARCHAR(4),
  company VARCHAR(100),cardholder VARCHAR(50),designation VARCHAR(75),mobile VARCHAR(100),email VARCHAR(50),
  website VARCHAR(100),pincode VARCHAR(6),state VARCHAR(50),district VARCHAR(50),area VARCHAR(100),bizcard_photo MEDIUMBLOB NOT NULL);
 
 # OTHERS 
- Create a folder and copy craft_mlt.pth,english_g2.pth files and cudacheck.py file 
- Inside the cudacheck.py file in the lines 21,40and 330 type your mysql password in it
- Run streamlit run cudacheck.py
