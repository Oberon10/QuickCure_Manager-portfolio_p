import functools
import re

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from manager.model.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phoneNumber']
        age = request.form['age']
        blood_group = request.form['bloodGroup']
        
        # Regular expression patterns
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        phone_pattern = r'^\d{10}$'
        password_pattern = r'^.{8,}$'

        if not re.match(email_pattern, email):
            error = "Invalid email address. Please enter a valid email."
            return render_template("signup.html", error)
        flash(error)

        # Validate phone number
        if not re.match(phone_pattern, phone_number):
            error = "Invalid phone number. Please enter a 10-digit phone number."
            return render_template("signup.html", error)
        flash(error)

        # Validate password
        if not re.match(password_pattern, password):
            error = "Invalid password. Password should be at least 8 characters long."
            return render_template("signup.html", error)
        flash(error)

        db = get_db()
        error = None

        if error is None:
            try:
                db.execute(
                    "INSERT INTO patient (first_name, last_name, email, password, phone_number, gender, age, blood_group, country, state, home_address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (first_name, last_name, email, generate_password_hash(password), phone_number, age, blood_group,),
                )
                db.commit()
            except db.IntegrityError:
                error = f"{email} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/signup.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        patient = db.execute(
            'SELECT * FROM patient WHERE email = ?', (email,)
        ).fetchone()

        if email is None:
            error = 'Incorrect E-mail.'
        elif not check_password_hash(patient['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['patient_id'] = patient['id']
            return redirect(url_for('auth.appointment'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    patient_id = session.get('patient_id')

    if patient_id is None:
        g.patient = None
    else:
        g.patient = get_db().execute(
            'SELECT * FROM patient WHERE id = ?', (patient_id,)
        ).fetchone()


@bp.route('/index')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.patient is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.route('/appointment')
def appointment():
    session.clear()
    return render_template('auth/appointment.html')
