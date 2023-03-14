import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import mysql.connector as mysql#database
import random #create userid
import base64 
import io


st.title('`Kindly Enter The Details Below`')
st.warning('Kindly Enter The Registered Details!:point_down:')
Username=st.text_input('Enter name:')
u1=str(Username.lower())
Useremail=st.text_input('Enter emailID:')
ID=st.text_input('Enter UserID')


    

mydb=mysql.connect(user="root",password="<password>",
 host="localhost",database='userinfo')
my_cursor=mydb.cursor()
y=f"SELECT * FROM customer_details WHERE name='{Username}' AND email='{Useremail}' AND userid='{ID}'"
my_cursor.execute(y)
db=my_cursor.fetchall()
g=[]
for i in db:
            g.append(i)



def new():
    p_in=[] 
    n= random.randint(1000,9999)
    st.write('Your UserId is: ',n)
    p_in.append(str(n))
    
    
    mydb=mysql.connect(user="root",password="<password>",host="localhost",database='userinfo')
    my_cursor=mydb.cursor()
    query=f"INSERT INTO customer_details (name,email,userid) VALUES (%s,%s,%s)"
    records=(Username,Useremail,p_in[-1])
    my_cursor.execute(query,records)
    mydb.commit()
    st.success('You are registered! Enter the UserID to Login  ')

if len(g)==0:       
        st.subheader('New registration') 
        st.warning('Enter your Name ,EmailID and type any 4 chars in UserID field:point_up_2: and then click Generate UserID button below')       
        st.button('Generate UserID',on_click=new)


elif len(g)!=0:
    st.header(f'`Welcome {Username} `:blush:')
    #title
    st.header("Easy OCR -Optical Character Recognition ")

    #subtitle
    st.header("Extract Text from Images")

    #st.markdown("")

    @st.cache
    def load_model(): 
            reader = ocr.Reader(['en'],model_storage_directory='.')
            return reader 

    reader = load_model() #load model
    image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])
   
    if image is not None:
                input_image = Image.open(image) #read image
                st.image(input_image) #display image
                u=image.name
                #saving the image
                with open(image.name,'wb') as f:
                    f.write(image.getbuffer())
                 # Open a file in binary mode
                file = open(u,'rb').read()
                
                # We must encode the file to get base64 string
                file = base64.b64encode(file)
                
                result_text = [] #empty list for results
                with st.spinner(":robot_face: AI is at Work! "):
                        

                    result = reader.readtext(np.array(input_image))

                    result_text = [] #empty list for results


                    for text in result: 
                            result_text.append(text[1])
                
                
                #st.write(result_text)

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
                photo=[file]
                
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

                end={'Company':(' '.join(b)),'CardHolder':CardHolderName,'Designation':Designation,
                    'mobile':('/').join(MobileNo),'Email':Email[0],'Website':Website[0],
                    'Pin':Pincode[0],'State':State[0],'District':District[0],
                    'Area':Area[0],'bizcard_photo':file}
                st.subheader('Extracted Text Details')
                st.balloons()
                st.write(end)
                
                def update():
                    st.subheader('Edit Information')
                    form=st.form('TEXT EXTRACTION')
                    w00=form.text_input("Edit Company Name",placeholder=str(end['Company']))  
                    if w00!='':
                        end['Company']=w00
                    
                    w0=form.text_input("Edit Name",placeholder=str(end['CardHolder']))
                    if w0!='':
                        end['CardHolder']=w0
                    
                    w1=form.text_input("Edit Designation",placeholder=str(end['Designation']))  
                    if w1!='':
                        end['Designation']=w1
                        
                    w2=form.text_input("Edit Mobile number",placeholder=str(end['mobile']))  
                    if w2!='':
                        end['mobile']=w2
                        
                    w3=form.text_input("Edit Email",placeholder=str(end['Email']))  
                    if w3!='':
                        end['Email']=w3
                        
                    w4=form.text_input("Edit Website",placeholder=str(end['Website']))  
                    if w4!='':
                        end['Website']=w4
                        
                    w5=form.text_input("Edit Pincode",placeholder=str(end['Pin']))  
                    if w5!='':
                        end['Pin']=w5
                    
                    w6=form.text_input("Edit State",placeholder=str(end['State']))  
                    if w6!='':
                        end['State']=w6  
                        
                    w7=form.text_input("Edit District",placeholder=str(end['District']))  
                    if w7!='':
                        end['District']=w7  
                    
                    w8=form.text_input("Edit Area",placeholder=str(end['Area']))  
                    if w8!='':
                        end['Area']=w8
                    form.form_submit_button('update')
                    
                    def up():
                            st.header('Updated Information')
                            st.write(end)
                            data=st.button('Upload to database' )
                            sql=(Username,Useremail,ID,end['Company'],end['CardHolder'],end['Designation'],
                                end['mobile'],end['Email'],end['Website'],
                                end['Pin'],end['State'],end['District'],
                                end['Area'],end['bizcard_photo'])
                            if data:
                                #mydb=mysql.connect(user="root",password="<password>",host="localhost",database='userinfo')
                                my_cursor=mydb.cursor()
                                detail=f"INSERT INTO bizcard_details (registered_name,registered_email,registered_userid,company,cardholder,designation,mobile ,email ,website ,pincode ,state ,district,area,bizcard_photo ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                record=(sql)
                                my_cursor.execute(detail,record)
                                mydb.commit()
                                st.success('Successfully Uploaded')
                                
                    
                        
                    z=st.radio('Display updated details',options=('no','yes'))
                    if z=='yes':
                            up()
                    
                        
                rad=st.radio('Edit details',options=('No','Yes'))
                if rad=='Yes':
                    update()
                if rad=='No':
                    data=st.button('Upload to database?' )
                    sql=(Username,Useremail,ID,end['Company'],end['CardHolder'],end['Designation'],
                        end['mobile'],end['Email'],end['Website'],
                        end['Pin'],end['State'],end['District'],
                        end['Area'],end['bizcard_photo'])
                    if data:
                        #mydb=mysql.connect(user="root",password="<password>",host="localhost",database='userinfo')
                        my_cursor=mydb.cursor()
                        detail=f"INSERT INTO bizcard_details (registered_name,registered_email,registered_userid,company,cardholder,designation,mobile ,email ,website ,pincode ,state ,district,area,bizcard_photo ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        record=(sql)
                        my_cursor.execute(detail,record)
                        mydb.commit()
                        st.success('Successfully Uploaded')
                    
                
    else:
        st.write(":point_up_2:Upload an Image")
        

st.subheader(':point_down:1.To View Previously Entered Data ')
modify=st.button('Press Here ') 
def mq():
        
            my_cursor=mydb.cursor()
            y=f'SELECT * FROM bizcard_details WHERE registered_name="{Username}" AND registered_email="{Useremail}" AND registered_userid="{ID}"'
            my_cursor.execute(y)
            db=my_cursor.fetchall()
            k=[]
            for i in db:
                k.append(i)
                
            
            im=[]
            for i in range(0,len(k)):
                im.append(k[i][-1])
            
            photo_display=[]
            for j in range(len(im)):
                # Decode the string
                binary_data = base64.b64decode(im[j])
                
                # Convert the bytes into a PIL image
                pic = Image.open(io.BytesIO(binary_data))
                photo_display.append(pic)
           
            st.subheader('Here is your uploaded data!')
            for l in range(len(photo_display)):
                # Display the image
                st.image(photo_display[l])
                #Display other informations
                st.json({'ID: ':k[l][0],'UserID: ':k[l][3]})
                
                st.json(k[l][4:-1])    
if modify:
    mq()
       
        


st.subheader(':point_down:2.To Delete entire details of a particular card')   

forme=st.form('k')
x=forme.number_input('Enter the ID number of the cardholder you want to delete')
x1=int(x)
#y=st.text_input('Enter the NAME of the cardholder you want to delete')
z=forme.text_input('Enter the USERID of the cardholder you want to delete')
d=forme.form_submit_button('delete')
    
if d:
    mydb=mysql.connect(user="root",password="<password>",host="localhost",database='userinfo')
    my_cursor=mydb.cursor()
    detail=f'DELETE FROM bizcard_details WHERE id={x1} AND registered_userid="{z}"'
    #record=(sql)
    my_cursor.execute(detail)
    f=mydb.commit()
    if f:
        st.success('Deleted Successfully!')
    else:
        st.success('View Records to confirm deletion')


 


    

            
