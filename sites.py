from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from modules import convert_to_dict
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


app = Flask(__name__)

Bootstrap(app)
GoogleMaps(app)


app.config['SECRET_KEY'] = '9iUH02Y7Dq'
app.config['GOOGLEMAPS_KEY'] = "SrfGVDYqri"



application = app

destinations = convert_to_dict("destination.csv")
cultures = convert_to_dict("culturePractice.csv")
heritages = convert_to_dict("heritage5.csv")

def get_id(source, name):
    for row in source:
        if name.lower()== row["Name"].lower():
            id = row["code"]
            return id
        return "Unknown"

class NameForm(FlaskForm):
    text = StringField('What country are you traveling to?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    name_list = []
    ids_list = []
    form = NameForm()
    message = ""
    if request.method == "POST":
    # get the input from the form
        text = request.form.get("text")
        for destination in destinations:
            if text.lower() in destination['Name'].lower():
                ids_list.append(destination['code'])
                name_list.append(destination['Name'])
        pairs_list = zip(ids_list, name_list)
        message = "Sorry, no match was found."
    if len(ids_list) == 1:
        return redirect( url_for('detail', code=ids_list[0]) )
    elif len(ids_list) > 0:
        return render_template('index.html', form=form, message=message)
    else:
        return render_template('index.html', form=form, message=message)


@app.route('/country/<code>')
def detail(code):
    heritage_list = []
    culture_list = []
    for destination in destinations:
        if destination['code'] == code:
            d = destination
            break
    for heritage in heritages:
        if d['Name'].strip(' \n\r\t') in heritage['country']:
            heritage_list.append(heritage)
    for culture in cultures:
        if d['Name'].strip(' \n\r\t') in culture['country']:
            culture_list.append(culture)
    return render_template('country.html', d=destination, h=heritage_list, c=culture_list)


if __name__ == '__main__':
    app.run(debug=True)
