# from flask import Flask

# app = Flask(__name__)

# @app.route("/members")
# def members():
#     return {"members": ['Member1', 'Member2', 'Member3']}


# if __name__ == '__main__':
#     app.run(debug=True)

import json
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity,\
                               unset_jwt_cookies, jwt_required, JWTManager

api = Flask(__name__)

api.config["JWT_SECRET_KEY"] = "SAJTOS1234567"
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(api)

@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "sajtos@sajt.hu" or password != "testpw":
        return {"msg": "Wrong email or password!"}, 401
    
    access_token = create_access_token(identity=email)
    response = {"access_token": access_token}
    return response

@api.route("/profile")
@jwt_required()
def my_profile():
    response_body = {
        "name": "Kukac",
        "about": "Sajtból van a hold!"
    }

    return response_body

@api.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response

@api.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response
