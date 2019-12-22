from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

da_bros = [
     { "name": "Kevin", "image": "kevin.jpeg", "bio": "The model paragraph uses illustration (giving examples) to prove its point. Decide on a controlling idea and create a topic sentence. Explain the controlling idea. Give an example (or multiple examples) Explain the example(s) Complete the paragraph's idea or transition into the next paragraph." },
     { "name": "Kyle", "image": "kyle.jpg", "bio": "The model paragraph uses illustration (giving examples) to prove its point. Decide on a controlling idea and create a topic sentence. Explain the controlling idea. Give an example (or multiple examples) Explain the example(s) Complete the paragraph's idea or transition into the next paragraph." },
     { "name": "Rob", "image": "rob.jpeg", "bio": "The model paragraph uses illustration (giving examples) to prove its point. Decide on a controlling idea and create a topic sentence. Explain the controlling idea. Give an example (or multiple examples) Explain the example(s) Complete the paragraph's idea or transition into the next paragraph." }
    ]

@app.route('/')
def main_page():
    image_names = os.listdir('./images/Da-Bros')
    print(image_names)
    return render_template("main.html", da_bros=da_bros)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images/Da-Bros", filename)

if __name__ == '__main__':
    app.run(debug=True)