from flask import Flask, render_template, url_for

app = Flask(__name__) 

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

if __name__ == '__main__':
    app.run(debug=True)