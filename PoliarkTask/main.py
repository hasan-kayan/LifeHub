from flask import Flask, render_template
import FreeCAD
import sys



sys.path.append("C:\Program Files\FreeCAD 0.21\lib")    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
