import openai
import os
import random
import string

from flask import Blueprint
from flask import render_template, request

from website.printify_photo import upload_image
from website.printify_product import create_product, get_product

views = Blueprint('views', __name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.retrieve("text-davinci-003")


@views.route("/", methods=("GET", "POST"))
def home():
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
            return render_template("home.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'])
        elif count == "2":
            return render_template("home.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'],
                                   image_url_1=response['data'][1]['url'])
        elif count == "3":
            return render_template("home.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'],
                                   image_url_1=response['data'][1]['url'],
                                   image_url_2=response['data'][2]['url'])
        elif count == "4":
            return render_template("home.html",
                                   pic_size=dimension,
                                   image_url_0=response['data'][0]['url'],
                                   image_url_1=response['data'][1]['url'],
                                   image_url_2=response['data'][2]['url'],
                                   image_url_3=response['data'][3]['url'])

    result = request.args.get("result")
    return render_template("home.html", result=result)


@views.route('/publish', methods=["POST"])
def image_publish():
    # upload image with random 20 str filename
    print(request.form["image_url"])
    image_id = upload_image(file_name=generate_random_string(20), url=request.form["image_url"])
    # create_product(blueprint_id=3, print_provider_id=74, image_id=image_id)
    product_id = create_product(blueprint_id=269, print_provider_id=1, variant_id=93905, image_id=image_id)
    product = get_product(product_id)
    return render_template("home.html", result="Product published!", product_image=product['images'][1]['src'])


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


# @app.route('/edit', methods=["POST"])
# def image_edit():
#     if 'file' not in request.files:
#         return "No file part in the request"
#
#     file = request.files['file']
#     prompt = request.form["animal"]
#     filename = secure_filename(file.filename)
#
#     if filename == '':
#         return "No selected file"
#
#     response = openai.Image.create_edit(
#         image=file,
#         mask=file,
#         prompt=prompt,
#         n=1,
#         size="256x256"
#     )
#     return render_template("index.html",
#                            image_url_0=response['data'][0]['url'])
#
#
# @app.route('/variation', methods=["POST"])
# def image_variation():
#     if 'file' not in request.files:
#         return "No file part in the request"
#
#     file = request.files['file']
#     filename = secure_filename(file.filename)
#
#     if filename == '':
#         return "No selected file"
#
#     response = openai.Image.create_variation(
#         image=file,
#         n=1,
#         size="256x256"
#     )
#     return render_template("index.html",
#                            image_url_0=response['data'][0]['url'])

