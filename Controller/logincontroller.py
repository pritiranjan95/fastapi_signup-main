from fastapi import APIRouter
from Model.login_model import Login
from Service.signupservice import SignUp
from Service.loginservice import Login

router=APIRouter()
login=Login()

@router.get("/get_login_data/{email}", tags=["Login"])
def validate_email(email:str):
    validation_status=login.validate_data_with_mail(email=email)
    if validation_status is not None:
        return "Login Successful"
    return f"Sign Up with mail {email} has not done yet"

    





