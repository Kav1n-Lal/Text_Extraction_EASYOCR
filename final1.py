import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import mysql.connector as mysql
import random




st.title(':blue[TEXT EXTRACTION]')
st.subheader(':red[login]')
form=st.form('BIZCARD TEXT EXTRACTION')
Username=st.text_input(':violet[Enter Name]')
Useremail=st.text_input(':violet[EmailID]')

p_in=[]  
q=[]
p=['@','.','gmail','com']
for h in p:
        if h in Useremail:
                q.append(h)

if len(q)==0:
                st.warning('Enter valid EmailID')
else:
        n= random.randint(1000,9999)
        st.write('Your UserId is: ',n)
        p_in.append(str(n))
        mydb=mysql.connect(user="root",password="AccountsandRoles@78",
                host="localhost",database='userinfo')
        my_cursor=mydb.cursor()
        detail=f"INSERT INTO customer_details (name,email,userid) VALUES (%s,%s,%s)"
        record=(Username,Useremail,p_in[-1])
        my_cursor.execute(detail,record)
        mydb.commit()

     
st.title('`KINDLY FILL THE FIELDS BELOW`')
#st.subheader(':Green[Register]')
form1=st.form('TEXT EXTRACTION')
Username=form1.text_input('Name')
u1=str(Username.lower())
Useremail=form1.text_input('EmailID')
ID=form1.text_input('Enter UserID')
st.warning('Type any four values to proceed if you dont have userID ')
ok=form1.form_submit_button('OK')

       
okay=[]

n_user=[]


    



if ok:  
        
        if len(u1)==0 or len(Useremail)==0 or len(ID)==0:
                st.warning('Enter values in all fields')
        elif len(ID)!=4:
                st.warning('UserID must have 4 digits')
        elif len(q)==0:
                st.warning('Enter valid EmailID')
        else:   

                mydb=mysql.connect(user="root",password="AccountsandRoles@78",
                                        host="localhost",database='userinfo')
                my_cursor=mydb.cursor()
                y=f"SELECT * FROM customer_details WHERE name='{u1}' AND email='{Useremail}' AND userid='{ID}'"
                my_cursor.execute(y)
                db=my_cursor.fetchall()
                g=[]
                h=' '.join(g)
                for i in db:
                         g.append(i)
                if len(g)>0:
                            okay.append('1')

                elif len(g)==0:
                        def pin():
                                n= random.randint(1000,9999)
                                st.write('Your UserId is: ',n)
                                p_in.append(str(n))
                                mydb=mysql.connect(user="root",password="AccountsandRoles@78",
                                        host="localhost",database='userinfo')
                                my_cursor=mydb.cursor()
                                detail=f"INSERT INTO customer_details (name,email,userid) VALUES (%s,%s,%s)"
                                record=(u1,Useremail,p_in[-1])
                                my_cursor.execute(detail,record)
                                mydb.commit()
                        st.warning('Username Not Found! Kindly Register')
                        st.button('Generate Pin to Login',on_click=pin)
                                
                        

      
z=[]
if len(okay)==1:
        st.subheader(f'Welcome {Username} :blush:')
                        #title
        st.header("Easy OCR - Extract Text from Images")

                        #subtitle
        st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

        st.markdown("")
        
        @st.cache
        def load_model(): 
                reader = ocr.Reader(['en'],gpu=True,model_storage_directory='.')
                return reader 
        
        reader = load_model() #load model
        image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])
        
        if image is not None:
                #image uploader
                    input_image = Image.open(image) #read image
                    st.image(input_image) #display image

                    result_text = [] #empty list for results
                    with st.spinner("🤖 AI is at Work! "):
                            

                        result = reader.readtext(np.array(input_image))

                        result_text = [] #empty list for results


                        for text in result: 
                                z.append(text[1])
                    
                    
                    #st.write(result_text)

        else:
                st.write("Upload an Image")
        
st.write(z)




