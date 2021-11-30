import mysql.connector as conn

def connect_mysql( host="localhost", user='root', password="", database=''):

    try:
        if database != '':
           mydb = conn.connect(
               host="host", 
               user="user", 
               password=password, 
               database=database
            )
        else:
            mydb = conn.connect(
               host="host", 
               user="user", 
               password=password, 
              
            )

        print(mydb)
        return mydb   
    except Exception as e:
      print(e)  
    

def create_database(dbname):
    try:
        connection = connect_mysql()
        cursor = connection.cursor() 
        sql = "CREATE DATABASE "+dbname
        cursor.execute(sql)

    except Exception as e:
        print(e)      



def create_table(table_name):
    try:
         connection = connect_mysql(dbname = 'unversity')  
         cursor = connection.cursor() 
         sql = "CREATE TABLE "+table_name+"(id integer auto-increment, name varchar(255), dept varchar(255))"
         cursor.execute(sql)     
 
    except Exception as e:
        print(e) 

def insert_data(table_name, name, dept):
    try:
         connection = connect_mysql(dbname = 'unversity')  
         cursor = connection.cursor() 
         sql = "INSERT INTO "+table_name+"(name, dept ) VALUES(%s %s)"
         val = (name, dept)
         cursor.execute(sql)     
 
    except Exception as e:
        print(e) 


def show_data(table_name):
    try:
         connection = connect_mysql(dbname = 'unversity')  
         cursor = connection.cursor() 
         sql = "SELECT * FROM " + table_name
         cursor.execute(sql) 
         result = cursor.fetchall() 
         for i in result:
             print(i)  
 
    except Exception as e:
        print(e) 

create_database('university')
create_table('student')      
insert_data('student','Sumon', 'CSE')  
insert_data('student','Sumon Khan', 'SE')  
insert_data('student','Sumon Ali', 'SWE')  
show_data('student')