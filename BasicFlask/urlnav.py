from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def admin_page():
    return 'This page is for Administrator.'

@app.route("/guest/<guest>")
def guest_page(guest):
    return 'Hello Guest ' + guest
	
@app.route("/user/<name>")
def user_page(name):
	if name == "admin":
		return redirect(url_for("admin_page"))
	else:
		return redirect(url_for("guest_page",guest=name))
	
if __name__=="__main__":
    app.run(debug=True)	
