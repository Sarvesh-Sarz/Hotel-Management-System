import mysql.connector 
import time
from datetime import date


global conn,cursor
conn = mysql.connector.connect(host='localhost',database='hotel',user='root',password='root')
cursor = conn.cursor()

def clear(a=45):
  for _ in range(a):
     print()



def introduction():
    msg = '''
                                                       H O T E L    M A N A G E M E N T    S Y S T E M 
          
                    - An Introduction
          
                                     The project aims at creating Hotel Management System which can be used by
                                     admin. Admins can advise/publish the availability of rooms and other
                                     facilities. The administrative will also know the details of reservation.
                                                            
                                     The main objective of this project is to design a hotel management system
                                     for running a hotel business. The whole project is divided into four major
                                     parts ie addition of data, modification, searching and reporting. all these
                                     part are further divided into menus for easy navigation.

                                    NOTE: Python is case-SENSITIVE so type exact Column Name wherever required.

                        
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait=input('Press any key to continue.....')


def made_by():
    msg = ''' 
            Hotel management System made by             :  M.Sarvesh
                                 THANK YOU            
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)


def admin_login():
    clear()
    while True:
        uname = input('Enter your Admin id :')
        upass = input('Enter your Admin Password :')
        cursor.execute('select * from admin_login where Name="{}" and Passwd ="{}"'.format(uname,upass))
        cursor.fetchall();
        rows = cursor.rowcount
        if rows!=1:
            clear(66)
            print('\n\n\n')
            print('Invalid Login details..... Try again')
            print()
        else:
          break
       


def home():
  while True:
      clear()
      print(' H O T E L    M A N A G E M E N T    S Y S T E M')
      print('*'*100)
      print()
      print("------Bookings------")
      print("\n1.  Rooms")
      print("\n2.  Party Halls")
      print("\n3.  Conference Rooms")
      print('\n4.  Close application')
      print('\n\n')
      clear(25)
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        clear()
        Rooms()       

      if choice == 2:
        clear()
        Party_Halls()

      if choice == 3:
        clear()
        C_rooms()

      if choice == 4:
        clear()
        made_by()
        break


      




#------------------Rooms----------------------
def Rooms():
  clear(30)
  print('------------------Rooms----------------------')
  print("\n1.  Check In")
  print("\n2.  Check Out")
  print("\n3.  Display Records")
  print("\n4.  Customer Service")
  print("\n5.  Home")
  clear(28)
  choice1 = int(input(' Enter your choice ...: '))
  if choice1 == 1:
    Check_in_R()
  if choice1 == 2:
    Check_out_R()
  if choice1 == 3:
    Display_R()
  if choice1 == 4:
    cust_R()
  if choice1 == 5:
    home()


    
def Check_in_R():
    clear()
    cursor.execute('select * from rooms')
    z=cursor.fetchall()
    conn.commit()
    if len(z) == 20:
      clear(50)
      print("NO ROOMS AVAILABLE")
      home()
    else:
      print('-----Check_In-----')
      print()  
      Booking_name = input('Enter Name : ') 
      Room_no= int(input('Enter Room_no : '))
      for i in z:
        if i[2]==Room_no:
          print("Room Has Been Already Booked")
          Check_in_R()
          break
        else:
          continue
      Check_in = input('Enter Checkin Date (yyyy/mm/dd) : ')
      Check_out = input('Enter Checkout Date (yyyy/mm/dd) : ')
      phone  = int(input('Enter Phone No :'))
      Email_id  = input('Enter  mailid :')
      print()
      print()
      print(''' ----- ID -----
      1.AADHAR     
      2.PASSPORT         
      3.PAN CARD
      4.DRIVING LISCENCE       ''')
      print()
      print()
      Id = input('Enter ID type submitted : ')
      print()
      print()
      print(''' -----Available Room Types-----
      1.ULTRA ROYAL     Rs.10000
      2.ROYAL           Rs.7000
      3.BUDGET          Rs.3000   ''')
      print()
      print()
      room_type =int(input('Enter room choice : '))
      Meal_package = input('Enter Meal package(veg/Non-veg/Jain/Vegan/None : ')
      sql = 'insert into rooms(Booking_name,Room_No,Check_in,Check_out,PhNo,EmailId,IdentificationType,room_type,Meal_package) values \
            ("{}",{},"{}","{}","{}","{}","{}","{}","{}");'.format(Booking_name,Room_no,Check_in,Check_out,phone,Email_id,Id,room_type,Meal_package) 
      cursor.execute(sql)
      conn.commit()
      print('\n\n New Record added....')

      wait = input('\n\n\nPress any key to continue............')
    
      Rooms()



def Check_out_R():
  clear()
  print('-----Check_out-----')
  print()
  Room_no=input("Enter Room number: ")
  cursor.execute("Select * from rooms where Room_No='{}'".format(Room_no))
  record=cursor.fetchone()
  conn.commit()
  Name=record[1]
  Room_type=record[8]
  if Room_type==1:
    Room_Rent=10000
  elif Room_type==2:
    Room_Rent=7000
  elif Room_type==3:
    Room_Rent=3000
  else:
    print('Record not found')
  days=int(record[4][8]+record[4][9])-int(record[3][8]+record[3][9])
  Extras=int(input('Extras-'))
  GST=(0.12)*(Room_Rent)
  clear(30)
  print("----------BILL----------")
  print('Room Rent-',"       ",Room_Rent*days)
  print('GST-',"             ",GST)
  print('Extras-',"          ",Extras)
  print('------------------------')
  print('GRAND TOTAL-',"     ",(Room_Rent+GST+Extras))
  cursor.execute("Delete from rooms where Room_No='{}'".format(Room_no))
  conn.commit()
  print('\n\n\n')
  print("Room Number",Room_no,"has been vacated")
        
  wait = input('\n\n\nPress any key to continue............')
  Rooms()



def Display_R():
  clear()
  print('-----Booked Rooms-----')
  print()
  cursor.execute("Select * from rooms")
  record=cursor.fetchall()
  for i in record:
    print(i)
  conn.commit()
  wait = input('\n\n\nPress any key to continue............')
  Rooms()



def cust_R():
  clear()
  print('-----Customer_Service-----')
  print()
  print("\n1.  Add new Query")
  print("\n2.  View Query")
  print("\n3.  Remove Query")
  clear(25)
  choice1 = int(input(' Enter your choice ...: '))
  if choice1 == 1:
    print()
    print()
    name = input('Enter Name : ') 
    phone  = int(input('Enter Phone No :'))
    request  = input('Enter  your query :')
    Btype = input('Enter your Booking type : ')
    sql = 'insert into Customer_service(Name,ContactNo,Request,Booking_Type) values \
            ("{}",{},"{}","{}");'.format(name,phone,request,Btype) 
    cursor.execute(sql)
    conn.commit()

  if choice1 == 2:
    print()
    print()
    cursor.execute("Select * from Customer_service")
    record=cursor.fetchall()
    for i in record:
      print(i)
    conn.commit()
    wait = input('\n\n\nPress any key to continue............')
    Rooms()

  if choice1 == 3:
    print()
    print()
    Phone_no=int(input("Enter registered phone number: "))
    cursor.execute("Delete from rooms where PhNo='{}'".format(Phone_no))
    conn.commit()
    print('\n\n\n')
    print("Query has been removed")
        
    wait = input('\n\n\nPress any key to continue............')
    Rooms()
  
  print('\n\n New Record added....')

  wait = input('\n\n\nPress any key to continue............')
  

#--------------------Party Hall-------------------------




  

def Party_Halls():
  clear()
  print('------------------Party Hall----------------------')
  print("\n1.  Book Hall")
  print("\n2.  Remove Entry")
  print("\n3.  Display Records")
  print("\n4.  Customer Service")
  print("\n5.  Home")
  clear(25)
  choice1 = int(input(' Enter your choice ...: '))
  if choice1 == 1:
    Book_hall_P()
  if choice1 == 2:
    R_Entry_P()
  if choice1 == 3:
    Display_P()
  if choice1 == 4:
    cust_P()
  if choice1 == 5:
    home()



def Book_hall_P():
  clear()
  cursor.execute('select * from party_hall')
  z=cursor.fetchall()
  conn.commit()
  if len(z) == 2:
    clear(50)
    print("NO HALLS AVAILABLE")
    home()  
  else:
    print('-----Book Hall-----')
    print()
    Booking_name = input('Enter Name : ') 
    Hall_No= int(input('Enter Hall_no : '))
    for i in z:
      if i[2]==Hall_No:
        print("Hall Has Been Already Booked")
        Book_hall_P()
        break
      else:
        continue
    Slot = input('Enter slot (yyyy/mm/dd) : ')
    phone = int(input('Enter Phone No :'))
    print()
    print()
    print('Hall   Rs.25000  (Capacity 1000 (* for more capacity extra amount will be charged))')
    print()
    print()
    capacity = int(input('Enter Capacity :'))
    sql = 'insert into party_hall(Booking_name,Hall_No,Slot,ContactNo,Capacity) values \
          ("{}",{},"{}","{}","{}");'.format(Booking_name,Hall_No,Slot,phone,capacity)
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Record added....')
    wait = input('\n\n\nPress any key to continue............')
    Party_Halls()



def R_Entry_P():
  clear()
  print('-----Remove Entry-----')
  print()
  Hall_no=int(input("Enter Hall number: "))
  cursor.execute("Select Hall_no from party_hall ")
  record=cursor.fetchall()
  conn.commit()
  x=True
  for i in record:
    if i[0]==Hall_no:
      Hall_Rent=25000
      Extras=int(input('Extras-'))
      GST=(0.12)*(Hall_Rent)
      clear(30)
      print("----------BILL----------")
      print('Hall Rent-',"       ",Hall_Rent)
      print('GST-',"             ",GST)
      print('Extras-',"          ",Extras)
      print('------------------------')
      print('GRAND TOTAL-',"     ",(Hall_Rent+GST+Extras))
      cursor.execute("Delete from party_hall where Hall_No='{}'".format(Hall_no))
      conn.commit()
      print('\n\n\n')
      print("Hall",Hall_no,"is vacant")
      x=False
  if x==True:
    print("Enter valid Hall Number-")
    R_Entry_P()
  else:
    Party_Halls()
  
        
 

def Display_P():
  clear()
  print('-----Display-----')
  print()
  cursor.execute("Select * from party_hall")
  record=cursor.fetchall()
  for i in record:
    print(i)
  conn.commit()
  wait = input('\n\n\nPress any key to continue............')
  Party_Halls()

def cust_P():
  clear()
  print('-----Customer_Service-----')
  print()
  print("\n1.  Add new Query")
  print("\n2.  View Query")
  print("\n3.  Remove Query")
  clear(25)
  choice1 = int(input(' Enter your choice ...: '))
  if choice1 == 1:
    print()
    print()
    name = input('Enter Name : ') 
    phone  = int(input('Enter Phone No :'))
    request  = input('Enter  your query :')
    Btype = input('Enter your Booking type : ')
    sql = 'insert into Customer_service(Name,ContactNo,Request,Booking_Type) values \
            ("{}",{},"{}","{}");'.format(name,phone,request,Btype) 
    cursor.execute(sql)
    conn.commit()

  if choice1 == 2:
    print()
    print()
    cursor.execute("Select * from Customer_service")
    record=cursor.fetchall()
    for i in record:
      print(i)
    conn.commit()
    wait = input('\n\n\nPress any key to continue............')
    Party_Halls()

  if choice1 == 3:
    print()
    print()
    Phone_no=int(input("Enter registered phone number: "))
    cursor.execute("Delete from rooms where PhNo='{}'".format(Phone_no))
    conn.commit()
    print('\n\n\n')
    print("Query has been removed")
        
    wait = input('\n\n\nPress any key to continue............')
    Party_Halls()
  
  print('\n\n New Record added....')

  wait = input('\n\n\nPress any key to continue............')






  
  
#------------------Conference Rooms-----------------


def C_rooms():
  clear()
  print('------------------Conference Room----------------------')
  print("\n1.  Book conference room")
  print("\n2.  Remove Entry")
  print("\n3.  Display Records")
  print("\n4.  Customer Service")
  print("\n5.  Home")
  clear(25)
  choice1 = int(input(' Enter your choice ...: '))
  if choice1 == 1:
    Book_room_C()
  if choice1 == 2:
    R_Entry_C()
  if choice1 == 3:
    Display_C()
  if choice1 == 4:
    cust_C()
  if choice1 == 5:
    home()



def Book_room_C():
  clear()
  cursor.execute('select * from conference_room')
  z=cursor.fetchall()
  conn.commit()
  if len(z) == 20:
    clear(50)
    print("NO ROOMS AVAILABLE")
    home()
  else:   
    print('-----Book Room-----')
    print()
    Company_name = input('Enter Name : ') 
    Room_No= int(input('Enter Conference_room_no : '))
    for i in z:
      if i[2]==Room_No:
        print("Room Has Been Already Booked")
        Book_room_C()
        break
      else:
        continue
    Slot = input('Enter slot (yyyy/mm/dd) : ')
    Email_ID =input('Enter Email ID :')
    print()
    print()
    print('Conference Room   Rs.15000  (Capacity 100 (* for more capacity extra amount will be charged))')
    print()
    print()
    capacity = int(input('Enter Capacity :'))
    Requests =input('Enter Requests :')
    sql = 'insert into conference_room(Company_name,Room_No,Slot,EmailId,Capacity,Requests) values \
          ("{}",{},"{}","{}","{}","{}");'.format(Company_name,Room_No,Slot,Email_ID,capacity,Requests)
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Record added....')
    wait = input('\n\n\nPress any key to continue............')
    C_rooms()



def R_Entry_C():
  clear()
  print('-----Remove Entry-----')
  print()
  Room_no=int(input("Enter Room number: "))
  cursor.execute("Select Room_no from conference_room ")
  record=cursor.fetchall()
  conn.commit()
  x=True
  for i in record:
    if i[0]==Room_no:
      room_Rent=15000
      Extras=int(input('Extras-'))
      GST=(0.12)*(room_Rent)
      clear(30)
      print("----------BILL----------")
      print('Room Rent-',"       ",room_Rent)
      print('GST-',"             ",GST)
      print('Extras-',"          ",Extras)
      print('------------------------')
      print('GRAND TOTAL-',"     ",(room_Rent+GST+Extras))
      cursor.execute("Delete from conference_room where Room_No='{}'".format(Room_no))
      conn.commit()
      print('\n\n\n')
      print("Room",Room_no,"is vacant")
      x=False
  if x==True:
    print("Enter valid Room Number-")
    R_Entry_C()
  else:
    C_rooms()
    
        


def Display_C():
  clear()
  print('-----Display-----')
  print()
  cursor.execute("Select * from conference_room")
  record=cursor.fetchall()
  for i in record:
    print(i)
  conn.commit()
  wait = input('\n\n\nPress any key to continue............')
  C_rooms()

def cust_C():
  clear()
  print('-----Customer_Service-----')
  print()
  print("\n1.  Add new Query")
  print("\n2.  View Query")
  print("\n3.  Remove Query")
  clear(25)
  choice1 = int(input(' Enter your choice ...: '))
  if choice1 == 1:
    print()
    print()
    name = input('Enter Name : ') 
    phone  = int(input('Enter Phone No :'))
    request  = input('Enter  your query :')
    Btype = input('Enter your Booking type : ')
    sql = 'insert into Customer_service(Name,ContactNo,Request,Booking_Type) values \
            ("{}",{},"{}","{}");'.format(name,phone,request,Btype) 
    cursor.execute(sql)
    conn.commit()

  if choice1 == 2:
    print()
    print()
    cursor.execute("Select * from Customer_service")
    record=cursor.fetchall()
    for i in record:
      print(i)
    conn.commit()
    wait = input('\n\n\nPress any key to continue............')
    C_rooms()

  if choice1 == 3:
    print()
    print()
    Phone_no=int(input("Enter registered phone number: "))
    cursor.execute("Delete from rooms where PhNo='{}'".format(Phone_no))
    conn.commit()
    print('\n\n\n')
    print("Query has been removed")
        
    wait = input('\n\n\nPress any key to continue............')
    C_rooms()
  
  print('\n\n New Record added....')

  wait = input('\n\n\nPress any key to continue............')



  
#-------------------Main----------------------

def main_menu():
    clear(19)
    introduction()
    admin_login()
    clear()
    home()
    

if __name__ == "__main__":
    main_menu()























      
