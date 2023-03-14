import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import mysql.connector as mysql
import random

def login():
  st.title(':blue[TEXT EXTRACTION]')
  st.subheader(':red[login]')
  form=st.form('BIZCARD TEXT EXTRACTION')
  Username=form.text_input(':violet[EmailID]')
  UserID= form.number_input(':violet[UserID]',max_value=9999)
  ok=form.form_submit_button('OK')
  
         
st.title('`KINDLY FILL THE FIELDS BELOW`')
#st.subheader(':Green[Register]')
form1=st.form('TEXT EXTRACTION')
Username=form1.text_input('Name')
u1=str(Username.lower())
Useremail=form1.text_input('EmailID')
ID=form1.text_input('Enter UserID')
st.warning('Type any four values to proceed if you dont have userID ')
ok=form1.form_submit_button('OK')

p_in=[]
n_user=[]


        


q=[]
p=['@','.','gmail','com']
for h in p:
        if h in Useremail:
                q.append(h)
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
                        st.subheader(f'Welcome {Username} :blush:')
                        #title
                        st.header("Easy OCR - Extract Text from Images")

                        #subtitle
                        st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

                        st.markdown("")

                        #image uploader
                        image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


                        @st.cache
                        def load_model(): 
                                reader = ocr.Reader(['en'],model_storage_directory='.')
                                return reader 

                        reader = load_model() #load model

                        if image is not None:

                                input_image = Image.open(image) #read image
                                st.image(input_image) #display image

                                result_text = [] #empty list for results
                                with st.spinner("🤖 AI is at Work! "):
                                        

                                        result = reader.readtext(np.array(input_image))

                                        result_text = [] #empty list for results


                                        for text in result:
                                                result_text.append(text[1])
                                        
                                        
                                        st.write(result_text)
                                #st.success("Here you go!")
                                
                                v=[result_text[0],result_text[1]]
                                CardHolderName=(result_text[0])
                                Designation=(result_text[1])
                                MobileNo=[]
                                Email=[]
                                Website=[]
                                Pincode=[]
                                State=[]
                                District=[]
                                Area=[]

                                def mob():
                                        for i in result_text:
                                                if '+' and '-' in i:
                                                        MobileNo.append(i)
                                                        result_text.remove(i)
                                                        mob()
                                mob()

                                for j in result_text:
                                        if '@' in j:
                                                Email.append(j)
                                                result_text.remove(j)

                                for k in result_text:
                                        if ('ww' or 'wW' ) in k:
                                                Website.append(k)
                                                result_text.remove(k)
                                        elif ('Ww' or 'WWW') and '.com' in k:
                                                Website.append(k)
                                                result_text.remove(k)

                                for l in result_text:
                                        if l[-1].isnumeric()==True and len(l)==6:
                                                Pincode.append(l)
                                                result_text.remove(l)
                                        elif l[-1].isnumeric()==True:
                                                h=l.split(' ')
                                                Pincode.append(h[-1])
                                                State.append(h[-2])
                                                result_text.remove(l)




                                result_text.pop(0)
                                result_text.pop(0)

                                a=result_text
                                b=[]

                                for i in a:
                                        v=i.split(',')
                                        for j in v:
                                
                                                if (';' or ',') in j:
                                                        b.append(j[:-1].strip())
                                                elif j=='' or j==' ':
                                                        pass
                                                else:
                                                        b.append(j.strip())




                                states=['andhrapradesh','arunachalpradesh','assam','bihar','chhattisgarh','goa','gujarat','haryana',
                                'himachalpradesh','jharkhand','karnataka','kerala','madhyapradesh','maharashtra','manipur','meghalaya','mizoram',
                                'nagaland','odisha','punjab','rajasthan','sikkim','tamilnadu','telangana','tripura','uttarakhand','uttarPradesh','westbengal']

                                for k in b:
                                        if k.lower() in states:
                                                State.append(k)
                                                b.remove(k)
                                        elif k[0].isnumeric()==True:
                                                Area.append(k)
                                                b.remove(k)

                                District.append(b[0])
                                b.remove(b[0])

                                st.write('company :',(' '.join(b)))
                                st.write('CardHolder: ',CardHolderName)
                                st.write('Designation: ',Designation)
                                st.write('mobile: ',('/').join(MobileNo))
                                st.write('email: ',Email[0])
                                st.write('web: ',Website[0])
                                st.write('pin: ',Pincode[0])
                                st.write('state:',State[0])
                                st.write('dist:',District[0])
                                st.write('area:',Area[0])
                        else:
                                st.write("Upload an Image")

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
                                
                        







