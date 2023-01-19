from python.main.printify_photo import *

client = requests.Session()
printify_client = PrintifyClient(client, os.getenv("PRINTIFY_ACCESS_TOKEN"))
shop_id = os.getenv("PRINTIFY_SHOP_ID")  # AI clothing store
request_base = os.getenv("PRINTIFY_REQUEST_BASE")

def create_product(blueprint_id=int, print_provider_id=int, image_id=str):
    payload = {
        "title": "Test Product",
        "description": "Test Description",
        "blueprint_id": blueprint_id,
        "print_provider_id": print_provider_id,
        "variants": [{
            "id": 17192,
            "price": 1599
        }],
        "print_areas": [{
            "variant_ids": [17192],
            "placeholders": [{
                "position": "front",
                "images": [
                    {
                        "id": image_id,
                        "x": 0.5,
                        "y": 0.5,
                        "scale": 1,
                        "angle": 0
                    }
                ]
            }]
        }]
    }
    product_create_uri = f'https://api.printify.com/v1/shops/{shop_id}/products.json'
    response = printify_client.request('POST', product_create_uri, data=payload)
    publish_product(response['id'])
    return response


def publish_product(product_id=str):
    product_publish_uri = f'https://api.printify.com/v1/shops/{shop_id}/products/{product_id}/publish.json'
    payload = {
    "title": True,
    "description": True,
    "images": True,
    "variants": True,
    "tags": True,
    "keyFeatures": True,
    "shipping_template": True
    }
    response = printify_client.request('POST', product_publish_uri, data=payload)
    confirm_publish(product_id)
    return response


def confirm_publish(product_id=str):
    confirm_uri = f'https://api.printify.com/v1/shops/{shop_id}/products/{product_id}/publishing_succeeded.json'
    payload = {
        "external": {
            "id": "5941187eb8e7e37b3f0e62e5",
            "handle": "https://example.com/path/to/product"
        }
    }
    try:
        response = printify_client.request('POST', confirm_uri, data=payload)
        return response
    except Exception as e:
        print(e)


def delete_all_products():
    product_get_uri = f'https://api.printify.com/v1/shops/{shop_id}/products.json'
    products = printify_client.request_product_list('GET', product_get_uri)
    for product in products:
        product_delete_uri = f'https://api.printify.com/v1/shops/{shop_id}/products/{product}.json'
        printify_client.request('DELETE', product_delete_uri)


def stop_publishing():
    product_get_uri = f'https://api.printify.com/v1/shops/{shop_id}/products.json'
    products = printify_client.request_product_list('GET', product_get_uri)
    print(products)
    for product in products:
        product_unpublish_uri = f'https://api.printify.com/v1/shops/{shop_id}/products/{product}/publishing_failed.json'
        print(printify_client.request('POST', product_unpublish_uri))