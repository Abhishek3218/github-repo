from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    bugs = db.relationship('Bug', backref='author', lazy=True)

class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='open')
    assignee = db.Column(db.String(80))
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    bugs = Bug.query.all()
    stats = {
        'total': Bug.query.count(),
        'open': Bug.query.filter_by(status='open').count(),
        'in_progress': Bug.query.filter_by(status='in-progress').count(),
        'closed': Bug.query.filter_by(status='closed').count()
    }
    return render_template('index.html', bugs=bugs, stats=stats)

@app.route('/bug/new', methods=['POST'])
@login_required
def new_bug():
    if request.method == 'POST':
        bug = Bug(
            title=request.form['title'],
            description=request.form['description'],
            priority=request.form['priority'],
            assignee=request.form['assignee'],
            due_date=datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form['due_date'] else None,
            user_id=current_user.id
        )
        db.session.add(bug)
        db.session.commit()
        flash('Bug successfully added!', 'success')
        return redirect(url_for('index'))

@app.route('/bug/<int:id>/update', methods=['POST'])
@login_required
def update_bug(id):
    bug = Bug.query.get_or_404(id)
    status_flow = ['open', 'in-progress', 'closed']
    current_index = status_flow.index(bug.status)
    bug.status = status_flow[(current_index + 1) % len(status_flow)]
    bug.updated_at = datetime.utcnow()
    db.session.commit()
    flash('Bug status updated!', 'success')
    return redirect(url_for('index'))

@app.route('/bug/<int:id>/delete', methods=['POST'])
@login_required
def delete_bug(id):
    bug = Bug.query.get_or_404(id)
    db.session.delete(bug)
    db.session.commit()
    flash('Bug deleted!', 'success')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:  # In production, use proper password hashing
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 