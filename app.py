from flask import Flask, render_template
import os


cwd = os.getcwd()
print(cwd)

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('%s.html' % 'main')

if __name__ == '__main__':
    app.run(debug=True)