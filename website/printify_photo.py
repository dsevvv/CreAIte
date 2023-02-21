import requests
import os
from website.printify_client import PrintifyClient
from dotenv import load_dotenv

load_dotenv()
BASE_URI = os.getenv("PRINTIFY_BASE_URI")
CLIENT = requests.Session()
PRINTIFY_CLIENT = PrintifyClient(CLIENT, os.getenv("PRINTIFY_ACCESS_TOKEN"))


# upload image to printify, returns image id
def upload_image(file_name=str, url=str):
    image_upload_uri = f'{BASE_URI}/uploads/images.json'
    image_data = {
        "file_name": file_name,
        "url": url
    }

    try:
        upload_response = PRINTIFY_CLIENT.request('POST', image_upload_uri, data=image_data)
        image_id = upload_response['id']
        return image_id
    except Exception as e:
        print(f'Error uploading image: {e}')


# get list of uploaded images
def get_uploaded_images():
    image_list_uri = f'{BASE_URI}/uploads.json'

    try:
        image_list_response = PRINTIFY_CLIENT.request('GET', image_list_uri)
        return image_list_response
    except Exception as e:
        print(f'Error getting image list: {e}')


# get image by id
def get_image_by_id(image_id=str):
    get_image_uri = f'{BASE_URI}/uploads/{image_id}.json'

    try:
        image_response = PRINTIFY_CLIENT.request('GET', get_image_uri)
        return image_response
    except Exception as e:
        print(f'Error getting image: {e}')


# archive image
def archive_image(image_id=str):
    image_archive_uri = f'{BASE_URI}/uploads/{image_id}/archive.json'

    try:
        image_response = PRINTIFY_CLIENT.request('POST', image_archive_uri)
        return image_response
    except Exception as e:
        print(f'Error archiving image: {e}')