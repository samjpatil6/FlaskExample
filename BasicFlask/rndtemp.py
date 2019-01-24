from flask import Flask, render_template
app = Flask(__name__)
	
@app.route("/")
def user_page():
        name = "Sameer"
        return render_template("hello.html",name=name)
	
if __name__=="__main__":
    app.run(debug=True)	
