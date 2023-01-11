from bitcoinia import app
from bitcoinia import db
# from utils.db import db


# TO JEST POTRZEBNE JESLI LINI KOMEND WOLA O KONTEXT
db.init_app(app)
with app.app_context(): 
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)