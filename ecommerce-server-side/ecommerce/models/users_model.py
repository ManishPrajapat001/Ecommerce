from datetime import datetime
from ecommerce.db_config import db
class UserDetailsModel(db.Model):
    __tablename__ = "user_detail"
    __table_args__= {"schema":"ecommerce_schema"}
    
    
    user_id = db.Column("user_id",db.Integer, primary_key =True)
    user_name = db.Column("user_name",db.String(40),nullable =False)
    first_name = db.Column("first_name",db.String(40),nullable =False)
    middle_name = db.Column("middle_name",db.String(40),nullable =True)
    last_name = db.Column("last_name",db.String(40),nullable =False)
    email_id = db.Column("email_id",db.String(40),nullable =False)
    mobile_number = db.Column("mobile_number",db.String(10))
    password_hash = db.Column(db.String(255), nullable=False)  # Store hashed password
    is_active = db.Column(db.Boolean, default=True)  # Account activation status
    # profile creation date
    created_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    
    
    # pass
    # user_id,USERNAME,password,first name ,middle name,last name,location,email,