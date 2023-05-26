# App Demo
*Click Link to view app demonstration video*
https://drive.google.com/file/d/13IyHs2RnZ6tAPn-AzY0YnaPsE0DSXzkc/view?usp=sharing

## Some screenshots from the app
![Screenshot (203)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/21b05c8a-010c-4bb1-868f-54e867e8d97a)
![Screenshot (204)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/7e0f2345-c87a-4f4e-ba3d-6e25b00ab40b)
![Screenshot (205)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/e6e7622c-ae63-483e-8428-840c6849c19e)
![Screenshot (206)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/0038f332-86cb-4744-9e85-f8702174b5df)
![Screenshot (207)](https://github.com/Kav1n-Lal/Text_Extraction_EASYOCR/assets/116146011/6caba409-712b-4ce0-9916-41c74a305d12)


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
