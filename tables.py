import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists hotel;")
mycursor.execute("use hotel;")

mycursor.execute("DROP TABLE IF EXISTS rooms;")
mycursor.execute("CREATE table if not exists rooms(SNo int(10) primary key auto_increment, Booking_name char(50) not null, Room_No int(5), Check_in char(10), Check_out char(10),PhNo bigint(10) not null, EmailId char(50) not null, IdentificationType char(20) not null, room_type int(3) not null, Meal_package varchar(11) not null);")
mycursor.execute("INSERT into rooms values (1, 'Joey',101,'2025-09-11 ','2025-09-20', 9878765765 , 'Joey1425@gmail.com','Passport',1,'Veg'),(2, 'Jack',69,'2025-09-20','2025-09-25 ', 98787806765 , 'jack123@gmail.com','Aadhar',2,'NON-Veg')")
mydb.commit()


mycursor.execute("DROP TABLE IF EXISTS conference_room;")
mycursor.execute("CREATE table if not exists conference_room(SNo int(10) primary key auto_increment, Company_name char(50) not null,Room_No int(5), Slot datetime, EmailId char(50) not null, Capacity int(10),Requests char(100));")                                           
mycursor.execute("INSERT into conference_room values (1, 'Morgan Stanley',2,'2025-09-11 13:00:00', 'Morganstanleyofficial@gmail.com',50,'Snacks');")
mydb.commit()


mycursor.execute("DROP TABLE IF EXISTS party_hall;")
mycursor.execute("CREATE table if not exists party_hall(SNo int(10) primary key auto_increment, Booking_name char(50) not null,Hall_No int(5), Slot datetime, ContactNo bigint(10) not null, Capacity int(10))")                                           
mycursor.execute("INSERT into party_hall values (1, 'Frankie', 3 ,'2025-11-11 20:00:00', 9887656787 , 2000);")
mydb.commit()


mycursor.execute("DROP table if exists admin_login")
mycursor.execute("CREATE TABLE IF NOT EXISTS admin_login (id int(10) Primary key,Name char(20) Not null,Passwd char(10) Not Null);")
mycursor.execute("INSERT into admin_login values (001,'Sarvesh','000');")
mydb.commit()


mycursor.execute("DROP TABLE IF EXISTS Customer_service;")
mycursor.execute("CREATE table if not exists Customer_service(SNo int(3) primary key auto_increment, Name char(50) not null, ContactNo bigint(10) not null, Request char(100),Booking_Type char(50));")                                           
mycursor.execute("INSERT into Customer_service values (1, 'Frankie',898989809,'Lost Device - Phone - iphone 13, Red - on 2025-11-11, partyhall no 3','room');")
mydb.commit()

