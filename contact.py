Name=[]
phoneNo=[]
email=[]
address=[]
while True:
 choice=int(input("choose your action:\n1.enter your details\n2.view all contects\n3.search contact\n4.update contact\n5.delete contact\n"))

 if choice == 1:
       name=input ("enter your name:")
       phone=input ("enter your phone number:")
       mail=input("enter your email:")
       pta=input("enter you address:")
       Name.append(name)
       phoneNo.append(phone)
       email.append(mail)
       address.append(pta)
 elif choice == 2:
    i=0;
    while i<len(Name):
       print("Name:"+Name[i]+"\tPhone number:"+phoneNo[i]+"\temail:"+email[i]+"\taddres:"+address[i])
       i=i+1;
 elif choice == 3:
    name=input("enter the name of which person you want to see the details:")
    if name in Name:
      index = Name.index(name)
      print("Name:"+Name[index]+"\tphone number:"+phoneNo[index]+"\temail:"+email[index]+"\tadderss:"+address[index])
    else:
        print("not in list")
 elif choice == 4:
    name=input("enter the name of which person you want to update the detail:")
    if name in Name:
     detail=int(input("enter what you want to update:\n1.name\n2.phone\n3.email\n4.address\n"))
     index = Name.index(name)
     update=input("enter the updated detail:")
     if detail == 1:
       Name[index]=update
     elif detail == 2:
        phoneNo[index]=update
     elif detail == 3:
        email[index]=update
     elif detail == 4:
        address[index]=update
    else:
     print("not in list")
 elif choice == 5:
    name=input("enter the name of which person you want to delete the details:")
    if name in Name:
     index=Name.index(name)
     del Name[index]
     del phoneNo[index]
     del email[index]
     del address[index]
    else:
      print("not in list")