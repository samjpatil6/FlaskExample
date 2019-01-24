from flask import Flask, render_template
app = Flask(__name__)
	
@app.route("/")
def user_page():
        marks = {"Maths":70,"C++":80,"JAVA":75}
        return render_template("hello.html", name = marks)
	
if __name__=="__main__":
    app.run(debug=True)	
