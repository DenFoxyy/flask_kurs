from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'hei 2imi'
 
@app.route('/om')
def om():
    return 'vi lærer om flask'
 
if __name__ == '__main__':
    app.run(debug=True)