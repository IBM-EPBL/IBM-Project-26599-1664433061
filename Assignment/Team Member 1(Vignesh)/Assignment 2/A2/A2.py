from flask import Flask,redirect,url_for,render_template,request, send_file
import ibm_db
app=Flask(__name__, template_folder='.')

conn_string = ""
conn = ibm_db.connect(conn_string, "", "")

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit',methods=["POST"])
def submit():
    if request.method=="POST":  
        sql = "INSERT INTO USERS VALUES (?, ?, ?, ?)"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, request.form["email"])
        ibm_db.bind_param(stmt, 2, request.form["user"])
        ibm_db.bind_param(stmt, 3, request.form["roll"])
        ibm_db.bind_param(stmt, 4, request.form["pass"])
        ibm_db.execute(stmt)
        return redirect("/login")
        # return render_template('display.html',name = name, qual = qual, age = age, email = email)

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    if request.method == "POST":
        stmt = ibm_db.exec_immediate(conn, "SELECT * FROM USERS")
        row = True
        while row!= False:
            row = ibm_db.fetch_assoc(stmt)
            if not row: break
            if(row['USERNAME'] == request.form['user'] and row['PASSWORD'] == request.form['pass']):
                return render_template('welcome.html')
        return "<div>ERROR</div>"

if __name__=='__main__':
    app.run(debug=True)




