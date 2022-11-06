from flask import Flask,redirect,url_for,render_template,request, send_file
app=Flask(__name__, template_folder='.')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit',methods=["POST"])
def submit():
    if request.method=="POST":
        name=request.form["name"]
        qual = request.form["qual"]
        age = request.form["age"]
        email = request.form["email"]
        return render_template('display.html',name = name, qual = qual, age = age, email = email)

if __name__=='__main__':
    app.run(debug=True)