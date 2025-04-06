import os ,datetime , bcrypt ,jwt
from flask import jsonify
from ecommerce.db_config import db
from ecommerce.models.users_model import UserDetailsModel
from datetime import datetime ,timedelta


class UserAuthenticationService():

    @staticmethod
    def generate_jwt(user_name):
        payload = {
            'user_id': user_name,
            'exp': datetime.utcnow() + timedelta(hours=1),  # expires in 1 hour
            'iat': datetime.utcnow()  # issued at
        }
        token = jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')
        return token

    
    def user_login(user_name,email_id,password):
        
    
        if email_id is not None  :
            userDetail = UserDetailsModel.query.filter(UserDetailsModel.email_id==email_id).first()
        
        elif user_name is not None:
            userDetail = UserDetailsModel.query.filter(UserDetailsModel.user_name==user_name).first()
        else:
            return {"error":"Email/username doesn't exist"},400
        
        if userDetail is None:
            return {"message":"No Such User exists"},400
        
        password_bytes=password.encode('utf-8')
        stored_password=userDetail.password_hash.encode('utf-8')
        print("password_hash",password_bytes)
        print(type(password))        # <class 'str'>
        print(type(password_bytes))
        # print("Stored hash:", hash_password_bytes)

        if  bcrypt.checkpw(password_bytes,stored_password):
            # login success ,need to provide jwt token
            
            response = jsonify({"message": "Login successful"})
            token= UserAuthenticationService.generate_jwt(userDetail.user_name)
            
            response.set_cookie(
                "access_token", 
                token,
                httponly=True,
                secure=True,  # make sure you're using HTTPS for this in production
                samesite="Strict"
            )
            return response
        
        else :
            return {"error":"Incorrect Password"},400
        
        
        
    
    def register_user(user_name,first_name,middle_name,last_name,password,email_id,mobile_number):
        try : 
            # check for necessary info
            if len(user_name) == 0 or len(first_name) == 0 or len(last_name) == 0 or len(password) == 0 or len(email_id) == 0:
                return {"error": "Provide necessary info!"}, 400
            # check if username available and email
            
            if UserDetailsModel.query.filter(UserDetailsModel.email_id==email_id).first() is not None:
                return jsonify({"message": "Customer exists with this email.Kindly login"}), 400
                
            
            if UserDetailsModel.query.filter(UserDetailsModel.user_name==user_name).first() is not None:
                return jsonify({"message": "Username already exists"}), 201
                
            # currently storing passwords,will update password to hash password
            password_bytes= password.encode('utf-8')
            salt=bcrypt.gensalt()
            hashed_password=bcrypt.hashpw(password_bytes,salt)
            hashed_password=hashed_password.decode('utf-8')
            
            new_user= UserDetailsModel(
                user_name=user_name,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                email_id=email_id,
                mobile_number=mobile_number,
                password_hash=hashed_password
            )
            # saving a new_user to db
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "User registered successfully!"}), 201
        
        except Exception as ex:
            # return jsonify()
            return jsonify(error=str(ex)), 500

    
    def user_logout():
        response = jsonify({"message":"User Logged out successfully!"},201)
        token=""
        response.set_cookie(
                "access_token", 
                token,
                httponly=True,
                secure=True,  # make sure you're using HTTPS for this in production
                samesite="Strict"
            )
        return response