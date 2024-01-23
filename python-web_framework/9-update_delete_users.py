from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://irw4n:Alxsqlprojects2024.@localhost/alx_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

@app.route('/add_user', methods=['GET', 'POST'], strict_slashes=False)
def add_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
        except Exception as e:
            flash(f'Error adding user: {str(e)}', 'error')

    return render_template('add_user.html')

@app.route('/users', strict_slashes=False)
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'], strict_slashes=False)
def update_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        try:
            new_name = request.form['name']
            new_email = request.form['email']

            # Validate data
            if not new_name or not new_email:
                flash('Both name and email are required for the update.', 'error')
            else:
                user.name = new_name
                user.email = new_email
                db.session.commit()
                flash('User updated successfully!', 'success')
        except Exception as e:
            flash(f'Error updating user: {str(e)}', 'error')

    return render_template('update_user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'], strict_slashes=False)
def delete_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        try:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error deleting user: {str(e)}', 'error')

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
