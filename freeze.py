from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from sites import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
