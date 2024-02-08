from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location', validators=[URL()])
    open_time = StringField('Open time', description="ex. 11AM/1:30PM", validators=[DataRequired()])
    closing_time = StringField('Closing time', description="ex. 11AM/1:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", choices=['☕️','☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi_rating = SelectField(label="WiFi Rating", choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪', '✘'], validators=[DataRequired()])
    outlet_rating = SelectField(label="Outlet Rating", choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌', '✘'], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = form.data
        cafe_data = [data[i] for i in data]
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            for index in range(len(cafe_data[:-2])):
                row = cafe_data[index]
                if index == 0:
                    csv_file.write(f"\n{row},")
                elif index == len(cafe_data[:-2]) - 1:
                    csv_file.write(f"{row}")
                else:
                    csv_file.write(f"{row},")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
