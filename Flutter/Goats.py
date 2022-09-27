
from flask import Flask, request

app = Flask(__name___)
    
@app.route('/api')
def hello():
        
        return 'Hello'
        
if __name__== '__name__':
    app.run()

    