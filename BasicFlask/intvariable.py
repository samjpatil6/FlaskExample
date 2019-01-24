from flask import Flask
app = Flask(__name__)

@app.route("/hi/<int:no>")
def print_name(no):
    return 'Roll number is %d!' %no

if __name__=="__main__":
    app.run(debug=True)	
