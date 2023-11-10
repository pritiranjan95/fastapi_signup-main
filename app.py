from Controller.signupcontroller import router as signup_router
from Controller.logincontroller import router as login_router
from fastapi import FastAPI
import uvicorn

app=FastAPI()

app.include_router(signup_router)
app.include_router(login_router)

@app.get("/bapi")
def index():
    return "welcome to signup service"

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8099)