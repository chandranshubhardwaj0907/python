from flask import Flask  ,request , render_template
 
app = Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def hello_world():
    if(request.method == 'POST'):
        with open("file.txt", "w") as file:
            file.write(f"the name is {request.form['name']} and the email is {request.form['email']}")
    print(request.method)
    print(request.form)
    return render_template("index.html")
app.run(port = 8000 ,debug=True)