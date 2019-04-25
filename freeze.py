from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from sites import app
from sites import ids_list

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def ids():
    for item in ids_list:
        yield { 'id': item['code'] }

if __name__ == '__main__':
    freezer.freeze()
