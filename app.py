from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def my_function():
    return render_template('index.html')

@app.route('/about_us')
def my_function1():
    return render_template('about_us.html')

@app.route('/about_us')
def my_function2():
    return render_template('membership.html')

if __name__ == '__main__':
    app.run(debug=True)