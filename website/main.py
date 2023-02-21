from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
    # app.run(debug=True, host="0.0.0.0", port=80,
    #         ssl_context=('C:/Certbot/live/creaite.ca/fullchain.pem', 'C:/Certbot/live/creaite.ca/privkey.pem'))
