import psycopg2

#creating a connection with database and creating the table
def create_table():
    conn = psycopg2.connect(dbname="studentdb", port="5432", user="postgres", password="raj161", host="localhost")
    print("Connection Successful!!")
    curs = conn.cursor() #curs is pointing to your DB
    curs.execute('''
        create table test(ID serial, Name text, age int, address text);
    ''')
    print("Table Created successfully!!!")
    conn.commit()
    conn.close()

#creating a connection with database and inserting the values into the table
def insert_data(): #Hardcoded values
    conn = psycopg2.connect(dbname="studentdb", port="5432", user="postgres", password="raj161", host="localhost")
    curs = conn.cursor() #curs is pointing to your DB
    curs.execute('''
        INSERT INTO test(Name,age,address) VALUES('Riya',25,'JPR');
    ''')
    print("Data inserted successfully!!!")
    conn.commit()
    conn.close()

#creating a connection with database and inserting the values into the table dynamically
def insert_data_dynamic(): #Dynamic values
    conn = psycopg2.connect(dbname="studentdb", port="5432", user="postgres", password="raj161", host="localhost")
    curs = conn.cursor() #curs is pointing to your DB
    name = input("Please enter your name : ")
    age = input("Please enter your age : ")
    add = input("Please enter your address : ")
    query = '''INSERT INTO test(Name,age,address) VALUES(%s, %s, %s);'''
    curs.execute(query,(name,age,add))
    print()
    print("Data captured successfully!!!")
    conn.commit()
    conn.close()

insert_data_dynamic()