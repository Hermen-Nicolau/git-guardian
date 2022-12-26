from flask import Flask
app = Flask(__name__)
import os

# This is not the original app, this is the app.py after running the script. 
@app.route('/')
def hello_world():
    return 'Hello, GitGuardian!'
@app.route('/pod-id')
def pod_id():
   POD = os.getenv('POD_ID')
   return (POD)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')