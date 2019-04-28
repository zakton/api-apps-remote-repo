from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from ..models import User
from . import main
from .forms import LoginForm, WeatherForm, AirportForm
from .weather import get_temperature
from .airport import get_airports

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/weather_app', methods=['GET', 'POST'])
def weather_app():
    city = None
    temperature = 0.0   # Min. temperature ... not possible
    temp_OK = False

    form = WeatherForm()
    if form.validate_on_submit():
        temperature, temp_OK = get_temperature(form.city.data)
        if temp_OK:
            return render_template('weather_app.html', form=form, city=form.city.data, temperature=temperature)
        else:
            return render_template('weather_app.html', form=form, city=None)

    return render_template('weather_app.html', form=form)

@main.route('/travel_menu')
def travel_menu():
    return render_template('travel_menu.html')

@main.route('/airport_app', methods=['GET', 'POST'])
def airport_app():
    data_OK = False
    data = None

    form = AirportForm()
    if form.validate_on_submit():
        data, data_OK = get_airports(form.city.data)
        if data_OK:
            return render_template('airport_app.html', form=form, data=data)
        else:
            return render_template('airport_app.html', form=form, data=None)

    return render_template('airport_app.html', form=form)

### Archive

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            return redirect(url_for('main.login', **request.args))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
