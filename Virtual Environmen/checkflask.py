from itertools import count
from flask import redirect, render_template, url_for
from flask import Flask


app = Flask(__name__, template_folder="templates")

@app.route("/figur/<ny_figur>")

def figur(ny_figur):
    return 'yndlingsfigur %s' % ny_figur

#@app.route("/<name>")
#def home(name):
#    return render_template("demo.html", content=name)

@app.route("/<name>/<name1>/<name2>/<name3>/<name4>")
def home(name, name1, name2, name3, name4):
    return render_template("demo.html", content=name, content1=name1, content2=name2, content3=name3, content4 = name4)

@app.route("/opg")
def deez(count):
    return render_template("deez.html", count)

    

if __name__ == "__main__":
    app.run(port=5000)





