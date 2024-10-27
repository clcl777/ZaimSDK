from zaim_sdk import ZaimSDK, get_access_token

if __name__ == "__main__":
    CONSUMER_ID = "xxxxxxxxxx"
    CONSUMER_SECRET = "xxxxxxxxxx"
    # get_access_token(consumer_id, consumer_secret)
    ACCESS_TOKEN = "xxxxxxxxxx"
    ACCESS_TOKEN_SECRET = "xxxxxxxxxx"
    zaim = ZaimSDK(CONSUMER_ID, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
