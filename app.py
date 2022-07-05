import pyautogui
from flask import Flask, render_template, request, jsonify
from chat import get_response
import webbrowser,pyautogui
from threading import Timer 

app = Flask(__name__)


@app.route("/",methods=["GET"])
def index_get():
    #pyautogui.hotkey('ctrl', 'w')
    return render_template("base.html")

@app.route("/predict",methods=["POST"])
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid  
    response = get_response(text)  
    message = {"answer":response}
    return jsonify(message)

def open_browser():
    #print(request.remote_addr)
    webbrowser.open_new("http://192.168.137.176:5000/")

if __name__ == "__main__":
    open_browser()
    app.run(debug=True)
    
    

