from flask import jsonify

from ecommerce.db_config import db
from ecommerce.models.users_model import UserDetailsModel


class UserAuthenticationService():
    
    def user_login(user_name,email_id,password):
        if UserDetailsModel.query.filter(UserDetailsModel.email_id==email_id).first() is None and UserDetailsModel.query.filter(UserDetailsModel.user_name==user_name).first() is None :
            return {"error":"Email/username doesn't exist"},400
        
        
        # if(len(user_name)>0):
        #     user
        
        pass
        
    
    def register_user(user_name,first_name,middle_name,last_name,password,email_id,mobile_number):
        # check for necessary info
        if len(user_name) == 0 or len(first_name) == 0 or len(last_name) == 0 or len(password) == 0 or len(email_id) == 0:
            return {"error": "Provide necessary info!"}, 400
        # check if username available and email
        
        if UserDetailsModel.query.filter(UserDetailsModel.email_id==email_id).first() is not None:
            return jsonify({"message": "Customer exists with this email.Kindly login"}), 400
            
        
        if UserDetailsModel.query.filter(UserDetailsModel.user_name==user_name).first() is not None:
            return jsonify({"message": "Username already exists"}), 201
            
        # currently storing passwords,will update password to hash password
        new_user= UserDetailsModel(
            user_name=user_name,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email_id=email_id,
            mobile_number=mobile_number,
            password_hash=password
        )
        # saving a new_user to db
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201

    
    def user_logout():
        pass