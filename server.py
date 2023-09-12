from flask import Flask, render_template, request, redirect, url_for, flash,redirect,session

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="0000",
  database="General_Operating_Room"
 
)
mycursor = mydb.cursor()

app = Flask(__name__)
app.config['SECRET_KEY']='mohammed@2023'



@app.route('/validation',methods = ['POST', 'GET'])
def validation():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      print(username)
      print(password)
      mycursor.execute("SELECT email FROM sign_up")
      usernames=[x[0] for x in mycursor]
      myresult = mycursor.fetchall()
      if (username in usernames):
        mycursor.execute(f"SELECT password FROM sign_up WHERE email = '{username}'")
        passwords=[x[0] for x in mycursor]
        pass_valid = mycursor.fetchall()
        if(password in passwords):
            session["username"]=username 
            session["password"]=password
            return redirect(url_for("home"))
        else:
            return render_template("login.html")
      else:
        return render_template("login.html")








@app.route('/',methods = ['POST', 'GET'])
def login():
   return render_template('login.html')

   
      
   
@app.route('/signup',methods = ['POST', 'GET'])
def signup():
   if request.method == 'POST':
      em = request.form['email']
      ps = request.form['psw']
      rps = request.form['psw-repeat']
      print(em)
      print(rps)
      sql = "INSERT INTO sign_up (email,password,confirm_password) VALUES (%s, %s, %s)"
      val = (em,ps,rps)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html')
   else:
      return render_template('signup.html')

@app.route('/logout')
def logout():
   return   render_template('login.html',pagetitle="login")

@app.route('/home')
def home():
   return render_template('home.html',pagetitle="Home Page")

@app.route('/doctors')
def doctors():
   #3ayez aselect eldata w ab3atha w azherha betareea kwayesaa
   mycursor.execute("SELECT * FROM doctor")
   row_headers=[x[0] for x in mycursor.description] 
   myresult = mycursor.fetchall()
   data={
         'message':"data retrieved",
         'rec':myresult,
          'header':row_headers}
   
   return render_template('doctors.html',data=myresult,pagetitle="Docotrs")
#3mlt var dtata 3lashan ab3tha ll doctor

@app.route('/search_doctor', methods=['GET', 'POST'])
def search_doctor():
    if request.method == 'POST':
        keyword = request.form['search']
        # Perform the search query using the keyword
        mycursor.execute("SELECT * FROM doctor WHERE id LIKE %s", ('%' + keyword + '%',))
        
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
         data = {
               'message': "Data retrieved",
               'rec': myresult,
               'header': row_headers
         }
         return render_template('doctors.html', data=myresult, keyword=keyword, header=row_headers,pagetitle="Doctor")
        else:
            error_message = "ID not found. Please enter a valid ID."
            return (error_message)
    else:
        # Render the server template without search results
        return render_template('doctors.html',pagetitle="Doctors")

@app.route('/deletedoc', methods = ['POST', 'GET'])
def delete_doc():
   if request.method=="POST":
      # Retrieve the ID from the form data
      id = request.form['delete']

      # Create a cursor to interact with the database
      

      # try:
      #    # Execute the delete query
      delete_query = "DELETE FROM doctor WHERE id = %s"
      try:
         mycursor.execute(delete_query,(id,))
         mydb.commit()
         if mycursor.rowcount > 0:
            return render_template('home.html',pagetitle="Doctors")
         else:
            return "ID not found. Please enter a valid ID."
      # except:
      #    # Handle the case where the delete operation fails
      except Exception as e:
         mydb.rollback()
         return "Failed to delete record. Error: " + str(e)
   else:
      return render_template('doctors.html',pagetitle="Doctors")

@app.route('/adddoc',methods = ['POST', 'GET'])
def adddoc():
   if request.method == 'POST':
      fn = request.form['firstname']
      mn=request.form['midname']
      ln = request.form['lastname']
      # id = request.form['ID']
      sid = request.form['sID']
      ssn = request.form['SSN']
      tit = request.form['title']
      spec = request.form['specialization']
      bdate = request.form['Dbdate']
      print(fn,mn, ln, sid, ssn, tit, spec, bdate)
      sql = "INSERT INTO doctor (fname ,mname ,lname ,staff_id  ,ssn ,title ,specialization ,B_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      val = (fn,mn, ln,sid, ssn, tit, spec, bdate)
      mycursor.execute(sql, val)
      mydb.commit()   
      return render_template('home.html',pagetitle="Home Page")
   else:
      return render_template('adddoc.html',pagetitle="Add Doctor")

@app.route('/equipment')
def equipment():
    mycursor.execute("SELECT * FROM equipments")
    row_headers=[x[0] for x in mycursor.description] 
    myresult = mycursor.fetchall()
    data={
         'message':"data retrieved",
         'rec':myresult,
          'header':row_headers}
    return render_template('equipment.html',data=myresult,pagetitle="Equipment")

@app.route('/search_equipment', methods=['GET', 'POST'])
def search_equipment():
    if request.method == 'POST':
        keyword = request.form['search']
        # Perform the search query using the keyword
        mycursor.execute("SELECT * FROM equipments WHERE id_code LIKE %s", ('%' + keyword + '%',))
        
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
         data = {
               'message': "Data retrieved",
               'rec': myresult,
               'header': row_headers
         }
         return render_template('equipment.html', data=myresult, keyword=keyword, header=row_headers,pagetitle="Equipment")
        else:
            error_message = "ID not found. Please enter a valid ID."
            return (error_message)
    else:
        # Render the server template without search results
        return render_template('equipment.html',pagetitle="Equipment")

@app.route('/delequip', methods = ['POST', 'GET'])
def delete_eq():
   if request.method=="POST":
      id = request.form['delete']
      delete_query = "DELETE FROM equipments WHERE id_code = %s"
      try:
         mycursor.execute(delete_query,(id,))
         mydb.commit()
         if mycursor.rowcount > 0:
            return render_template('home.html',pagetitle="Equipment")
         else:
            return "ID not found. Please enter a valid ID."
      except Exception as e:
         mydb.rollback()
         return "Failed to delete record. Error: " + str(e)
   else:
      return render_template('doctors.html',pagetitle="Doctors")

@app.route('/addequip',methods = ['POST', 'GET'])
def addequip():
   if request.method == 'POST':
      name = request.form['name']
      # id = request.form['ID']
      supp = request.form['supplier']
      pur = request.form['purchasedate']
      warr = request.form['warranty']
      main = request.form['maintanance']
      modelno = request.form['modelno']
      roomno = request.form['roomnum']
      print(name,id )
      sql = "INSERT INTO equipments (name ,supplier ,purchasedate ,warranty ,maintenance ,model_number,room_no  ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (name, supp,pur, warr, main,modelno, roomno)
      mycursor.execute(sql, val)
      mydb.commit()
           
      return render_template('home.html',pagetitle="Home Page")
   else:
      return render_template('addequip.html',pagetitle="Add Equipment")
   


@app.route('/supplies')
def supplies():
    mycursor.execute("SELECT * FROM supplies")
    row_headers=[x[0] for x in mycursor.description] 
    myresult = mycursor.fetchall()
    data={
         'message':"data retrieved",
         'rec':myresult,
          'header':row_headers}
    return render_template('supplies.html',data=myresult)

@app.route('/search_supplies', methods=['GET', 'POST'])
def search_supplies():
    if request.method == 'POST':
        keyword = request.form['search']
        # Perform the search query using the keyword
        mycursor.execute("SELECT * FROM supplies WHERE name LIKE %s", ('%' + keyword + '%',))
        
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        
        data = {
            'message': "Data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('supplies.html', data=myresult,pagetitle="Supplies", keyword=keyword, header=row_headers)
    else:
        # Render the server template without search results
        return render_template('supplies.html',pagetitle="Supplies")

@app.route('/delsupp', methods = ['POST', 'GET'])
def delete_sup():
   if request.method=="POST":
      id = request.form['delete']
      delete_query = "DELETE FROM supplies WHERE name = %s"
      try:
         mycursor.execute(delete_query,(id,))
         mydb.commit()
         if mycursor.rowcount > 0:
            return render_template('home.html',pagetitle="Supplies")
         else:
            return "Name not found. Please enter a valid name."
      except Exception as e:
         mydb.rollback()
         return "Failed to delete record. Error: " + str(e)
   else:
      return render_template('supplies.html',pagetitle="Supplies")


@app.route('/addsup',methods = ['POST', 'GET'])
def addsup():
   if request.method == 'POST':
      name = request.form['name']
      quan = request.form['quantity']
      roomno = request.form['roomnum']
      ex = request.form['expdate']
      print(name,quan)  
      sql = "INSERT INTO supplies (name ,quantity ,room_no ,expiration_date   ) VALUES (%s, %s, %s, %s)"
      val = (name, quan,roomno, ex)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html',pagetitle="Home Page")
   else:
      return render_template('addsup.html',pagetitle="Add Supplies")

@app.route('/nurses')
def nurses():
    #3ayez aselect eldata w ab3atha w azherha betareea kwayesaa
   mycursor.execute("SELECT * FROM nurses")
   row_headers=[x[0] for x in mycursor.description] 
   myresult = mycursor.fetchall()
   data={
         'message':"data retrieved",
         'rec':myresult,
          'header':row_headers}
   return render_template('nurses.html',data=myresult,pagetitle="Nurses")

@app.route('/search_nurse', methods=['GET', 'POST'])
def search_nurse():
    if request.method == 'POST':
        keyword = request.form['search']
        # Perform the search query using the keyword
        mycursor.execute("SELECT * FROM nurses WHERE id LIKE %s", ('%' + keyword + '%',))
        
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
         data = {
            'message': "Data retrieved",
            'rec': myresult,
            'header': row_headers
         }
         return render_template('nurses.html', data=myresult, keyword=keyword, header=row_headers,pagetitle="Nurses")
        else:
            error_message = "ID not found. Please enter a valid ID."
            return (error_message)
    else:
        # Render the server template without search results
        return render_template('nurses.html',pagetitle="Nurses")

@app.route('/delnurses', methods = ['POST', 'GET'])
def delete_nurses():
   if request.method=="POST":
      id = request.form['delete']
      delete_query = "DELETE FROM nurses WHERE id = %s"
      try:
         mycursor.execute(delete_query,(id,))
         mydb.commit()
         if mycursor.rowcount > 0:
            return render_template('home.html',pagetitle="Nurses")
         else:
            return "ID not found. Please enter a valid ID."
      except Exception as e:
         mydb.rollback()
         return "Failed to delete record. Error: " + str(e)
   else:
      return render_template('nurses.html',pagetitle="Nurses")


@app.route('/addnur',methods = ['POST', 'GET'])
def addnur():
   if request.method == 'POST':
      fn = request.form['firstname']
      ln = request.form['midname']
      sl = request.form['lastname']
      # id = request.form['ID']
      sid = request.form['sID']
      ssn = request.form['SSN']
      ph = request.form['phone']
      nbdate = request.form['Nbdate']
      print(fn,ph)
      sql = "INSERT INTO nurses (fname ,mname ,lname,staff_id ,ssn ,phone ,B_date ) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
      val = (fn, ln,sl, sid, ssn,ph, nbdate)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html',pagetitle="Home Page")
   else:
      return render_template('addnur.html',pagetitle="Add Nurses")
   
@app.route('/patient')
def patient():
   mycursor.execute("SELECT * FROM patient")
   row_headers=[x[0] for x in mycursor.description] 
   myresult = mycursor.fetchall()
   data={
         'message':"data retrieved",
         'rec':myresult,
          'header':row_headers}
   return render_template('patient.html', data=myresult,pagetitle="Patient")

@app.route('/search_patient', methods=['GET', 'POST'])
def search_patient():
    if request.method == 'POST':
        keyword = request.form['search']
        mycursor.execute("SELECT * FROM patient WHERE id LIKE %s", ('%' + keyword + '%',))
        
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        if len(myresult) > 0:
         data = {
               'message': "Data retrieved",
               'rec': myresult,
               'header': row_headers
         }
         return render_template('patient.html', data=myresult, keyword=keyword, header=row_headers,pagetitle="Patient")
        else:
               error_message = "ID not found. Please enter a valid ID."
               return (error_message)
    else:
        return render_template('patient.html',pagetitle="Patient")

@app.route('/delpatient', methods = ['POST', 'GET'])
def delete_patient():
   if request.method=="POST":
      id = request.form['delete']
      delete_query = "DELETE FROM patient WHERE id = %s"
      try:
         mycursor.execute(delete_query,(id,))
         mydb.commit()
         if mycursor.rowcount > 0:
            return render_template('home.html',pagetitle="Patient")
         else:
            return "ID not found. Please enter a valid ID."
      except Exception as e:
         mydb.rollback()
         return "Failed to delete record. Error: " + str(e)
   else:
      return render_template('patient.html',pagetitle="Patient")

@app.route('/addpat',methods = ['POST', 'GET'])
def addpat():
   if request.method == 'POST':
      fn = request.form['firstname']
      ln = request.form['lastname']
      pl = request.form['lastname']
      ssn = request.form['SSN']
      sex = request.form['sex']
      ph = request.form['phone']
      pbdate = request.form['Pbdate']
      print(fn,ssn)  
      sql = "INSERT INTO patient (fname ,mname ,lname,ssn ,sex ,phone,B_date ) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
      val = (fn, ln,pl, ssn, sex,ph, pbdate)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html',pagetitle="Home Page")
   else:
      return render_template('addpat.html',pagetitle="Add Patient")
   
@app.route('/medicalrec')
def medicalrec():
   mycursor.execute("SELECT date,location,ssn,gender,Family_History_of_Diabetes FROM medrec")
   myresult = mycursor.fetchall()
   return render_template('medicalrec.html', data=myresult)

@app.route('/addmed',methods = ['POST', 'GET'])
def addmed():
   if request.method == 'POST':
      pssn = request.form['Pssn']
      gen = request.form['gender']
      loc = request.form['Location']
      date = request.form['date']
      c1 = request.form['c1']
      c3 = request.form['c3']
      c4 = request.form['c4']
      c5 = request.form['c5']
      c6 = request.form['c6']
      c7 = request.form['c7']
      c8 = request.form['c8']
      print(pssn,c7)
      sql = "INSERT INTO medrec (ssn, gender, location, date, Family_History_of_Diabetes , Diabetes_Mellitus , Hypertension , Myocardial_Infarction ,CerebroVascular_Accident ,Amputation ,Smoker ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      val = (pssn, gen,loc, date, c1,c3,c4,c5,c6,c7,c8)
      mycursor.execute(sql, val)
      mydb.commit() 
      return render_template('home.html')
   else:
      return render_template('addmed.html')
   
@app.route('/oproom')
def oproom():
   mycursor.execute("SELECT * FROM operating_room")
   myresult = mycursor.fetchall()
   return render_template('oproom.html', data=myresult)
   # return render_template('oproom.html')

@app.route('/search_operatingroom', methods=['GET', 'POST'])
def search_operatingroom():
    if request.method == 'POST':
        keyword = request.form['search']
        # Perform the search query using the keyword
        mycursor.execute("SELECT * FROM operating_room WHERE room_no LIKE %s", ('%' + keyword + '%',))
        
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        
        data = {
            'message': "Data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('oproom.html', data=myresult, keyword=keyword, header=row_headers,pagetitle="Operating Room")
    else:
        # Render the server template without search results
        return render_template('oproom.html',pagetitle="Operating Room")

if __name__ == '__main__':
   app.run()