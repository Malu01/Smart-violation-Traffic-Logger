import os
import qrcode
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Violation, User

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_123'  # Flash messages-kaga

# Initialize Database
db.init_app(app)

# Create database tables within the app context
with app.app_context():
    db.create_all()
    # Create an admin user if it doesn't exist
    if not User.query.filter_by(username='police_admin').first():
        admin = User(username='police_admin', password='password123')
        db.session.add(admin)
        db.session.commit()

# --- ROUTES ---

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirect here if not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- NEW LOGIN ROUTES ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        # Simple check (In real apps, use password hashing!)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def index():
    # Ellaa violations-ayum search panni display pannuvom
    violations = Violation.query.order_by(Violation.date.desc()).all()
    return render_template('history.html', violations=violations)

@app.route('/add', methods=['GET', 'POST'])
@login_required # Only logged-in users can access this
def add_violation():
    if request.method == 'POST':
        # Form-la irundhu data eduppom
        v_number = request.form.get('vehicle_number').upper()
        v_type = request.form.get('violation_type')
        location = request.form.get('location')
        amount = request.form.get('fine_amount')

        # Database-la save pannuvom
        new_violation = Violation(
            vehicle_number=v_number,
            violation_type=v_type,
            location=location,
            fine_amount=amount
        )
        db.session.add(new_violation)
        db.session.commit()

        # QR Code Generate pannuvom
        # Inga unga system IP or localhost use pannalam
        qr_data = f"http://10.247.149.196:5000/status/{new_violation.id}"
        qr_img = qrcode.make(qr_data)
        qr_filename = f"qr_{new_violation.id}.png"
        qr_path = os.path.join('static/qrcodes', qr_filename)
        qr_img.save(qr_path)

        flash(f"Violation logged for {v_number}!", "success")
        return redirect(url_for('index'))

    return render_template('add_violation.html')

@app.route('/status/<int:violation_id>')
def status(violation_id):
    # QR scan panna intha page varum
    violation = Violation.query.get_or_404(violation_id)
    return render_template('status.html', violation=violation)

@app.route('/update_status/<int:violation_id>')
@login_required # Only logged-in users can change status
def update_status(violation_id):
    violation = Violation.query.get_or_404(violation_id)
    violation.status = 'Paid'
    db.session.commit()
    flash("Status updated to Paid!", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    