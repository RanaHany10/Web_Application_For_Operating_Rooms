import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="0000",
  database="General_Operating_Room"
 
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE medrec (ssn VARCHAR(255), gender VARCHAR(255), location VARCHAR(255), date VARCHAR(255), Family_History_of_Diabetes VARCHAR(255), Diabetes_Mellitus VARCHAR(255), Hypertension VARCHAR(255), Myocardial_Infarction VARCHAR(255),CerebroVascular_Accident VARCHAR(255),Amputation VARCHAR(255),Smoker VARCHAR(255),PRIMARY KEY(ssn))")

# mycursor.execute("CREATE TABLE medrec (ssn VARCHAR(255),gender VARCHAR(255), location VARCHAR(255), date VARCHAR(255),Family_History VARCHAR(255), Past_Medical_History VARCHAR(255), Past_Surgical_History VARCHAR(255), Social_History VARCHAR(255), PRIMARY KEY(ssn))")
# mycursor.execute("SELECT * FROM sign_up")
# myresult=mycursor.fetchall()
# print(myresult)
# def create_users_table():
#     cursor = mysql.connection.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             username VARCHAR(50) UNIQUE NOT NULL,
#             password VARCHAR(100) NOT NULL,
#             email VARCHAR(100) UNIQUE NOT NULL
#         )
#     ''')
#     mysql.connection.commit()
# mycursor.execute("CREATE DATABASE General_Operating_Room")
# print(mydb) 
# mycursor.execute("CREATE TABLE patient (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     smoking ENUM('Yes', 'No')
#     -- other columns
# )")
# mycursor.execute("CREATE TABLE medrec (ssn VARCHAR(255),gender VARCHAR(255),location VARCHAR(255),date VARCHAR(255),family_history VARCHAR(255),past_med_history VARCHAR(255),past_sur_history VARCHAR(255),social_history VARCHAR(255),PRIMARY KEY(ssn))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE medrec (ssn VARCHAR(255), gender VARCHAR(255), location VARCHAR(255), date VARCHAR(255), family_history VARCHAR(10), past_med_history VARCHAR(10), past_sur_history VARCHAR(10), social_history VARCHAR(10), PRIMARY KEY(ssn))")
# mycursor.execute("INSERT INTO medrec (ssn, gender, location, date, family_history, past_med_history, past_sur_history, social_history) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", ('123456789', 'Male', 'Location 1', '2023-06-19', 'Yes', 'Med History', 'Sur History', 'Social History'))

# mycursor.execute("CREATE TABLE supplies (name VARCHAR(255),quantity VARCHAR(255),expiration_date VARCHAR(255),room_no INT,PRIMARY KEY(name),FOREIGN KEY (room_no) REFERENCES operating_room(room_no))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE Supporting_staff (staff_id INT AUTO_INCREMENT,n_ssn VARCHAR(255),fname VARCHAR(255),mname VARCHAR(255),lname VARCHAR(255), PRIMARY KEY(staff_id))")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE nurses (nurse_id INT ,n_ssn VARCHAR(255),fname VARCHAR(255),mname VARCHAR(255),lname VARCHAR(255),phone VARCHAR(255),B_date VARCHAR(255),staff_id INT,PRIMARY KEY(staff_id),FOREIGN KEY (staff_id) REFERENCES Supporting_staff(staff_id))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE doctor (id INT AUTO_INCREMENT,Fname VARCHAR(255),Mname VARCHAR(255),Lname VARCHAR(255),specialization VARCHAR(255),ssn VARCHAR(255),title VARCHAR(255),phone VARCHAR(255),B_date VARCHAR(255),staff_id INT,PRIMARY KEY(id),FOREIGN KEY (staff_id) REFERENCES Supporting_staff(staff_id))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE patient (fname VARCHAR(255),mname VARCHAR(255),lname VARCHAR(255),id INT AUTO_INCREMENT,ssn VARCHAR(255),sex VARCHAR(255),phone VARCHAR(255),B_date VARCHAR(255),PRIMARY KEY(id))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("CREATE TABLE operating_room(room_no INT,capacity VARCHAR(255),status VARCHAR(255),location VARCHAR(255),PRIMARY KEY(room_no))")
# mycursor.execute("SELECT * FROM sign_up")
# for x in mycursor:
#   for y in x[0]:
#     print(y) 

# print([x[0] for x in mycursor])
sql = "DELETE FROM medrec"

# val=(5,'10','2','available')
mycursor.execute(sql)

mydb.commit()

# print(mycursor.rowcount, "record inserted.")

    

# mycursor = mydb.cursor()
# sql = "INSERT INTO doctor (fname,mname,lname,staff_id,ssn,title,specialization,B_date) VALUES (%s,%s,%s,%s,%s, %s, %s, %s)"
# #  val =[
# # val=('Ahmed','Maher','Ali','gynecology and obstetrics','01118426183','13/1/1987')
# val=[('reem','ayman','ali','3','30202252101758','surgeon','cardio','17/5/1978'),
#      ('yasmeen','hany','ali','2','30202252101389','surgeon','cardio','16/4/1999')
#       ]
    
    #     ('Gana','Ayman','Ali','cardiothoracic ','01118456373','14/3/1988')
    #  ]
# sql = "INSERT INTO supporting_staff () VALUES ()"
# val=()
# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# sql = "DELETE FROM doctor WHERE id = 3"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")
# alter_table_query = "ALTER TABLE patient AUTO_INCREMENT=9210"
# mycursor.execute(alter_table_query)