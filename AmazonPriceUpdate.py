#Check the Price of a prodcut from Amazon shopping site and raise an Alert if matches expectations.
#importing all the necessary required libraries
import requests
import smtplib
from bs4 import BeautifulSoup

#here im going to check for OnePlus 7 Pro mobile phone price. so i picked it. 
url = 'https://www.amazon.in/Test-Exclusive-607/dp/B07HGJKDQB/ref=sr_1_1?crid=1ORQDC1G78EY4&keywords=oneplus+7+pro+mobile&qid=1569733464&s=electronics&smid=A23AODI1X2CEAE&sprefix=oneplus%2Celectronics%2C362&sr=1-1'
#to get your user agent google for MY USER AGENT
headers={"user-agent":'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.1111.22 Safari/587.xx'}

page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
product = soup.find(id="productTitle").get_text()
#Extracting the deal price,don't get confused..that can be changed since i developed it during amazon festival i used it.
#cleansed the data in a proper way by removing the comma's and rupee sympol.
Price = soup.find(id="priceblock_dealprice").get_text().replace(",", "").replace("₹ ", "")

#cleansed the product data.
product=product.strip()
#converted the cleansed price data from string to float for validation purposes.
Price=float(Price)

#cross-verfying the data
print(product)
print(Price)

#function to trigger the email if the price goes down !!

def mail_sender(subject : str,body : str):  
  mail_msg = 'Subject: {}\n{}'.format(subject,body)   
  # creating a SMTP session from the imported library
  s = smtplib.SMTP('smtp.gmail.com', 587) 
    
  # starting TLS for security reasons
  s.starttls() 
    
  # Authentication(followed two factor authentication)
  # Note: make sure to allow acces to less secured accounts
  s.login("Sender_mail", "Sender_pswd")    
    
  # sending the e mail 
  s.sendmail("Sender_mail", "Receiver_mail", mail_msg) 
    
  # Quiting the email once done.
  s.quit()

#price check condition , the price mentioned here gonna change according to the product and need. 
if Price < 60000:
  print("its a go for buy")
  subject="price came down - Alert!"
  body="Hey Nanba,\n \n The price of '%s' came down to" %(product)
  body1="'%f'.\nCheck the below link asap..!!!" %(Price)
  body+=body1
  body2="\n'%s'" %(url)
  body+=body2
  #mail_msg = 'Subject: {}\n\n{}'.format(subject, body)   
  mail_sender(subject,body)
else:
  print("no buy")
  
#note: please ignore the Varaible namings, if you prefer you can change it, its simply because im just lame...!  
  

  
