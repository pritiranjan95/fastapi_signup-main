from Service.signupservice import SignUp

signup=SignUp()

class Login:

    def validate_data_with_mail(self, email):
        user_data=signup.collection.find_one({"mail_id":email})
        return user_data
    