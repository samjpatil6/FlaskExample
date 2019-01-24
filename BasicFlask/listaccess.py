from flask import Flask, render_template
app = Flask(__name__)
	
@app.route("/")
def user_page():
        numlist=[1,2,3,4,5,6]
        return render_template("hello.html",name=numlist)
	
if __name__=="__main__":
    app.run(debug=True)	
