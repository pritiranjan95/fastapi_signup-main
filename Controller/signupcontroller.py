from fastapi import APIRouter, Request
from Service.signupservice import SignUp
from Model.usersignup import UserdataModel,UserToSee

signup=SignUp()

router=APIRouter()

@router.post("/create", tags=["Sign_Up"])
def createuser(usermodel:UserdataModel, request:Request):
    created_data=signup.create(model=usermodel)
    print(f"Created data is{created_data}")
    return created_data

@router.get("/get_all_signup_data", tags=["Sign_Up"], response_model=list[UserToSee])
def getalldata(request:Request):
    all_datas=signup.get_all_details()
    return all_datas

@router.get("/get_with_id",tags=["Sign_Up"], response_model=UserToSee)
def get_data_by_id(id:str, request:Request):
    data_with_id=signup.get_by_id(id=id)
    return data_with_id

@router.put("/update_data/", tags=["Sign_Up"], response_model=UserToSee)
def update_data(id:str,usermodel:UserdataModel, request:Request):
    updated_data= signup.update(id=id, model=usermodel)
    return updated_data

@router.delete("/remove_data/",tags=["Sign_Up"])
def delete_data(id:str, request:Request):
    removed_data=signup.delete(id=id)
    print (f"Removed data={removed_data}")
    
    if removed_data.deleted_count==1:
        return "The data has been deleted succesfully"
    else:
        return f"The data with {id} not found"