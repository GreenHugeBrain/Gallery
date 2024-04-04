from ext import app, db

if __name__ == "__main__":  
    from routes import *
    app.run(debug=True)