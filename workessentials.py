from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__) 

# when using forms a secret key will protect against modifying cookies and cross site forgery attacks
app.config['SECRET_KEY'] = 'e930ee077e44c99e60e391709c6690dc'

# Dummy Posts
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1', 
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2', 
        'content': 'Second post content',
        'date_posted': 'April 10, 2018'
    }
]

@app.route("/")
@app.route("/home") # You can add another route
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

    # 27:44