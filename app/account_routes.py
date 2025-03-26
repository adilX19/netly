from flask import (
    request, 
    render_template, 
    make_response, 
    jsonify, 
    abort, 
    session,
    redirect, 
    url_for, 
    flash
)
from flask import current_app as app
from .models import db, User
from sqlalchemy import desc
from werkzeug.utils import secure_filename
import os
import traceback
import datetime

# helper function for file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        print(session['username'])
        return render_template('feed.html')
    return redirect((url_for('login')))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()  
        if not user:
            flash('User account not found')
            return redirect((url_for('login')))
        
        if not user.check_password(password):
            flash('Password incorrect')
            return redirect((url_for('login')))
        
        session['username'] = username
        return redirect((url_for('home')))

    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect((url_for('login')))

@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        file = request.files.get('profile_picture')

        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Username already exists. Please choose a different username.')
            return redirect((url_for('home')))
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            profile_picture_path = os.path.join('profile_pics', filename)
        else:
            profile_picture_path = None

        # Create a new user
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.profile_picture = profile_picture_path
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!')

        return redirect(url_for('login'))
    
    return render_template('register.html')
    


# db.engine.execute("SET TIME ZONE 'Asia/Bangkok'")