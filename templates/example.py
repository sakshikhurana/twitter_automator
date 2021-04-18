
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("wKf9ZYQEpzF45yxO59nvqW2ha", 
    "xoaZH7ujSt0tjRUMZgAhVeysyAEauwdNLl0TjqiVtVS4iudhj8")
auth.set_access_token("1376969671681843201-vLzL66v45MaBh5aNc1kMX1cVnMrNuG", 
    "GqBL9D99Z4hWHrlyIoUb3rhXJOBpKxQEvd8H7rJ7TmpZL")

api = tweepy.API(auth)

try:
    import pdb
    pdb.set_trace()
    api.verify_credentials()
    print("Authentication OK")
    api.update_status("Test tweet from Tweepy Python")
except:
    print("Error during authentication")