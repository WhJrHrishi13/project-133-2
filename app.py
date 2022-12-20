# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = "Hrishi Goyal" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def father():
    name = "Dinesh Goyal" # write your name
    age = "50" # write your age

    return render_template('father.html' , name = name , age = age)

@app.route("/")
def mother():
    name = "Kumkum Goyal" # write your name
    age = "46" # write your age

    return render_template('mother.html' , name = name , age = age)

@app.route("/")
def friend():
    name = "Harshit Nigam" # write your name
    age = "14" # write your age

    return render_template('friend.html' , name = name , age = age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
