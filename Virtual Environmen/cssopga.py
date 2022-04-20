from flask import Flask, render_template

app=Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def yeet():
    return render_template("strat.html")
if __name__ == "__main__":
    app.run(port=5000)
    