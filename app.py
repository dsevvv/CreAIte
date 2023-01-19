import os

import openai
import random
import string
from python.main.printify_photo import *
from python.main.printify_product import *
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.retrieve("text-davinci-003")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["animal"]
        resolution = request.form["resolution"]
        count = request.form["count"]
        dimension = resolution.split("x")[0]

        response = openai.Image.create(
            prompt=prompt,
            n=int(count),
            size=resolution
        )
        if count == "1":
            return render_template("index.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'])
        elif count == "2":
            return render_template("index.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'],
                                   image_url_1=response['data'][1]['url'])
        elif count == "3":
            return render_template("index.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'],
                                   image_url_1=response['data'][1]['url'],
                                   image_url_2=response['data'][2]['url'])
        elif count == "4":
            return render_template("index.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'],
                                   image_url_1=response['data'][1]['url'],
                                   image_url_2=response['data'][2]['url'],
                                   image_url_3=response['data'][3]['url'])

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route('/edit', methods=["POST"])
def image_edit():
    if 'file' not in request.files:
        return "No file part in the request"

    file = request.files['file']
    prompt = request.form["animal"]
    filename = secure_filename(file.filename)

    if filename == '':
        return "No selected file"

    response = openai.Image.create_edit(
        image=file,
        mask=file,
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return render_template("index.html",
                           image_url_0=response['data'][0]['url'])


@app.route('/variation', methods=["POST"])
def image_variation():
    if 'file' not in request.files:
        return "No file part in the request"

    file = request.files['file']
    filename = secure_filename(file.filename)

    if filename == '':
        return "No selected file"

    response = openai.Image.create_variation(
        image=file,
        n=1,
        size="256x256"
    )
    return render_template("index.html",
                           image_url_0=response['data'][0]['url'])


@app.route('/publish', methods=["POST"])
def image_publish():
    #upload image with random 20 str filename
    print(request.form["image_url"])
    image_id = upload_image(file_name=generate_random_string(20), url=request.form["image_url"])
    create_product(blueprint_id=3, print_provider_id=74, image_id=image_id)
    return render_template("index.html", result="Product published!")


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
