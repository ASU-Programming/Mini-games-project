from pymongo import MongoClient

from app_config import MONGO_URI

from pydantic import BaseModel, EmailStr

import microservies.app.main


def user_in_db(username: str):
    # connecting to the database
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("players")
    for doc in coll.find():
        if doc["_id"]["username"] == username:
            return True
    return False


def get_user_from_db(username: str):
    # connecting to the database
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("players")
    for doc in coll.find():
        if doc["_id"]["username"] == username:
            return {"username": doc["_id"]["username"], "email": doc["_id"]["email"], "disabled": doc["disabled"],
                    "banned": doc["banned"], "hashed_password": doc["hashed_password"]}


def user_row(username: str):
    # connecting to the database
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("players")
    for doc in coll.find():
        if doc["_id"]["username"] == username:
            return doc


def get_hashed_password(username: str):
    # connecting to the database
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("players")
    for doc in coll.find():
        if doc["_id"]["username"] == username:
            return doc["hashed_password"]


def sign_up(signup: microservies.app.main.SignUp):
    # connecting to the database
    client = MongoClient(MONGO_URI)
    db = client.get_database("test")
    coll = db.get_collection("players")
    sign_dict = {"_id": {
        "email": signup.email,
        "username": signup.username
    },
        "hashed_password": microservies.app.main.get_password_hash(signup.password),
        "disabled": signup.disabled,
        "banned": signup.banned}
    for doc in coll.find():
        if doc["_id"]["username"] == signup.username:
            return "username taken"
        if doc["_id"]["email"] == signup.email:
            return "email was used on another account"
    sign_coll = coll.insert_one(sign_dict)
    return "welcome " + signup.username
