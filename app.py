from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def main_page():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("main.html", image_names=image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)




if __name__ == '__main__':
    app.run(debug=True)