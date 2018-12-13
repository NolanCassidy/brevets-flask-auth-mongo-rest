from itsdangerous import (TimedJSONWebSignatureSerializer \
                                  as Serializer, BadSignature, \
                                  SignatureExpired)
import time

# initialization
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

def generate_auth_token(secret,user_id):
   s = Serializer(secret, expires_in=30)
   # pass index of user
   return s.dumps(user_id) # hashes with given user id

def verify_auth_token(token,secret):
    s = Serializer(secret) # WHAT IS SERIALIZER?
    try:
        data = s.loads(token) # Decodes the hash
    except SignatureExpired:
        return False    # valid token, but expired
    except BadSignature:
        return False    # invalid token
    return True

#if __name__ == "__main__":
#    t = generate_auth_token(10)
#    for i in range(1, 20):
#	print verify_auth_token(t)
#        time.sleep(1)
