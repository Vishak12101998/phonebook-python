
pb={}
def addcontact():
    name=input("enter a name :")
    number=int(input("enter your number :"))
    person={
        "name"  : name.lower(),
        "number" : number 
        }
    pb[name.lower()]=person
def viewcontact():
    search_person=input("enter a name to search :")  
    if search_person in pb.keys():
        print("person name :"  ,pb[search_person]["name"])
        print("person number :" ,pb[search_person]["number"])
def delete():
    delete_person=input("enter a person to delete :").lower()  
    if delete_person in pb.keys():
        del pb[delete_person]
        
def editnumber():          
    n=input("enter a name")  
    if n in pb.keys():
        changed_num=int(input("enter a number :")) 
        pb[n]['number']=changed_num
    else:
        print("not found")

def edituser():
    person_name=input("enter a name").lower()  
    if person_name in pb.keys():
        changed_name=input("enter a new name: ").lower()           
        pb[person_name]['name']=changed_name.lower()
        poped_person=pb.pop(person_name)
        pb[changed_name]=poped_person
    else:
        print("not found")    

pb={}
while True:
            print('''  
1-> add a person to phonebook
2-> view single person
3-> delete a person from phonebook                                   
4-> change a person phone number
5-> change a person name
6-> show all users
7-> quit 
  ''')
            option=int(input("enter your choice :"))  
            if option==1:
                addcontact()   
            elif option==2:
                viewcontact()
            elif option==3:
                 view_all()  
            elif option==4:
                 editnumber()
            elif option==5:
                 edituser()
            elif option==6:
                 delete()
            elif option==7:
                 break                  
