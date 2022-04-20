from flask import Flask, redirect, render_template
from udlaan import UdlaanForm

app=Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'noget hemmeligt'




@app.route("/", methods=['GET', 'post'])
def yeet():
    uform = UdlaanForm()
    if uform.validate_on_submit():
        print(uform.customerID.data)
        print(uform.inventoryID.data)
        print(uform.staffID.data)
        return redirect("dumbb.html")
    return render_template("form.html", afrm = uform)


if __name__ == "__main__":
    app.run(port=5000)
    