from website.printify_product import *

def main():
    delete_all_products()
    # client = requests.Session()
    # printify_client = PrintifyClient(client, os.getenv("PRINTIFY_ACCESS_TOKEN"))
    # shop_id = os.getenv("PRINTIFY_SHOP_ID")  # AI clothing store
    # product_id = "63b4dd24bb1cdce32201de42"  # random dude socks
    # kid_t_shirt_id = 3
    # kid_t_shirt_print_id = 74
    # request_base = os.getenv("PRINTIFY_REQUEST_BASE")
    #
    # # get blueprint data
    # variant_uri = f"https://api.printify.com/v1/catalog/blueprints/{kid_t_shirt_id}/print_providers/{kid_t_shirt_print_id}/variants.json"
    # # blueprint_response = printify_client.request('GET', variant_uri)
    # # print(blueprint_response)
    # # blueprint_uri = f'https://api.printify.com/v1/catalog/blueprints/{kid_t_shirt_id}/print_providers.json'
    # # response = printify_client.request('GET', blueprint_uri)
    # # print(response)
    # response = printify_client.request('GET', variant_uri)
    # print(response)
    #
    # # upload photo
    # photo_id = upload_image("test.png", "https://i.imgur.com/mUR5YLC.png")
    # print(photo_id)
    #
    # # payload = {
    # #     "title": "Test Product",
    # #     "description": "Test Description",
    # #     "blueprint_id": kid_t_shirt_id,
    # #     "print_provider_id": kid_t_shirt_print_id,
    # #     "variants": [{
    # #         "id": "17192",
    # #         "price": 2000
    # #     }],
    # #     "print_areas": [{
    # #         "variant_ids": [17192],
    # #         "placeholders": [{
    # #             "position": "front",
    # #             "images": [
    # #                 {
    # #                     "id": photo_id,
    # #                     "x": 0,
    # #                     "y": 0,
    # #                     "scale": 1,
    # #                     "angle": 0
    # #                 }
    # #             ]
    # #         }]
    # #     }]
    # # }
    # payload = {
    # "title": "Test Product",
    # "description": "Test Description",
    # "blueprint_id": kid_t_shirt_id,
    # "print_provider_id": kid_t_shirt_print_id,
    # "variants": [{
    #     "id": 17192,
    # "price": 100
    #     }],
    #     "print_areas": [{
    #         "variant_ids": [17192],
    #         "placeholders": [{
    #             "position": "front",
    #             "images": [
    #                 {
    #                     "id": photo_id,
    #                     "x": 0,
    #                     "y": 0,
    #                     "scale": 1,
    #                     "angle": 0
    #                 }
    #             ]
    #         }]
    #     }]
    # }
    #
    # # update_product_uri = f'{request_base}shops/{shop_id}/products/{product_id}.json'
    # # update_response = printify_client.request('PUT', update_product_uri, data=payload)
    # # print(update_response)
    #
    # product_create_uri = f'https://api.printify.com/v1/shops/{shop_id}/products.json'
    # response = printify_client.request('POST', product_create_uri, data=payload)
    # print(response)


if __name__ == "__main__":
    main()
