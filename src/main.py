from utils.helper_functions import getAccessToken

access_token = getAccessToken()
if __name__ == '__main__':
    try:
        access_token = getAccessToken()
        print("Succesfully logged in.")
    except Exception as e:
        print(f"Error while logging in: {e}")