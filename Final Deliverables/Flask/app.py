from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

import pickle
model = pickle.load(open(r'Model_one.pkl', 'rb'))

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route('/')
def helloworld():
    return render_template("home.html")


@app.route('/login', methods = ['POST'])
def login():
    a = request.form["age"]
    b = request.form["bp"]
    c = request.form["sg"]
    d = request.form["alb"]
    e = request.form["sugar"]
    f = request.form["RBC"]
    g = request.form["bacteria"]
    h = request.form["bgr"]
    i = request.form["bu"]
    j = request.form["sc"]
    k = request.form["sodium"]
    l = request.form["haemo"]
    m = request.form["pcv"]
    n = request.form["rbc-count"]
    o = request.form["hypertension"]
    p = request.form["pe"]

    t = [[float(a), float(b), float(c), float(d), float(e), float(f), float(g), float(h), float(i), float(j), float(k), float(l), float(m), float(n), float(o), float(p)]]
    output = model.predict(t)
    print(output)

    return render_template("home.html", y = "The predicted result is: "  + str(output[0]))

@app.route('/admin')
def admin():
    return "Hey Admin How are you?"

app.run(host='localhost', port=5000)
if __name__ == '__main__' :
    app.run(debug = True)