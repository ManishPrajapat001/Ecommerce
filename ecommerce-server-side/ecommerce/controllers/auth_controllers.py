# from urllib import request
from venv import logger
from flask import  Blueprint, request 


from ecommerce.services.auth_service import UserAuthenticationService

blp_auth = Blueprint('blp_auth',__name__,url_prefix='/api/auth')

class UserAuthenticationController:
    # login
    @blp_auth.post("/login")
    def login():
        req=request.json
        userName=req["user_name"]
        email_id=req["email_id"]
        password=req["password"]
        return UserAuthenticationService.user_login(userName,email_id,password)

    
    @blp_auth.post("/register")
    def register_user():
        req=request.json
        print('line 21',req)
        userName=req["user_name"]
        first_name=req["first_name"]
        middle_name=req["middle_name"]
        last_name=req["last_name"]
        email_id=req["email"]
        mobile_number=req["mobile_num"]
        password=req["password"]
        print('Here')
        
        return UserAuthenticationService.register_user(userName,first_name,middle_name,last_name,password,email_id,mobile_number)
        
        
    @blp_auth.get("/logout")
    def user_logout():
        return UserAuthenticationService.user_logout()
    
    # @blp_auth.post("/refresh")
    # def refresh():
    #     pass
    
    
    
    
    # # POST /register → Register new admin user
# POST /login → Authenticate user
    