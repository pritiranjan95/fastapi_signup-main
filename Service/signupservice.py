from Repository.mongoconnection import db
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status

class SignUp:
    def __init__(self):
        self.collection_name="sign_up_users_detail"
        self.db=db
        self.collection=self.db[self.collection_name]

    
    def create(self, model):
        model=jsonable_encoder(model)
        data=self.collection.insert_one(model)
        created_data=self.collection.find_one({"_id":data.inserted_id})
        return created_data
    
    def get_all_details(self):
        all_data=list(self.collection.find(limit=100))
        return all_data

    def get_by_id(self,id):
        data=self.collection.find_one({"_id":id})
        if data is not None:
            return data
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The data with id {id} is not found")
    
    def update(self,id,model):
        input_data={j:k for j,k in model.dict().items() if (j!="id") and k is not None}
        updated_data=self.collection.update_one({"_id":id},{"$set":input_data}) #Input_data is already a dictionary
    
        if updated_data.modified_count==0:          #Used in mongo db update function
            return f"the data with id {id} not found"
        else:
            existing_data=self.collection.find_one({"_id":id})
            if existing_data is not None:
                return existing_data
            
        return f"the data with id {id} not found"   

        
    def delete(self,id):
        deleted_data=self.collection.delete_one({"_id":id})
        return deleted_data



        




