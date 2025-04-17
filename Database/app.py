import uuid
from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # type: ignore

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    result = '<h1>Users</h1>'
    result += '<a href="/add_user">Add New User</a><br><br>'
    
    for user in users:
        result += ( f'ID: {user.id}, Name: {user.name}<br>'\
                   f'<a href="/update_user/{user.id}">Update</a><br>'\
                    f'<a href="/delete_user/{user.id}">Delete</a><br><br>' ) 
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        user_id = str(uuid.uuid4())
        new_user = User(id=user_id, name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/update_user/<user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.name = request.form['name']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update_user.html', user=user)


@app.route('/delete_user/<user_id>', methods=['POST'])
def delete_user(user_id):
    user_to_delete = User.query.get_or_404(user_id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "There was a problem deleting that user."
    
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Database tables created")

if __name__ == '__main__':
    app.run(debug=True)