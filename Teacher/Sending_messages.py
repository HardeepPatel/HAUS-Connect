def send_message(message):
    from twilio.rest import Client

    client = Client("ACe2ef31a4d09f9846afcd486586495973", "96ea22dafa27bc780f7f87fdbba8c30a")

    numbers=["+916351816925","+917202964175","+919426508970","+918690909695"]
    names=["Sarthak","Hardeep","Utsav","Ahmed"]

    for i in range(4):
        m=("Hello {} ".format(names[i]))+message
        client.messages.create(to=numbers[i], 
                            from_="+13092711496", 
                            body=(m))

                           
