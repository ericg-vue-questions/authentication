from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

origins = [ "http://localhost:8080" ]

users = {
    "usera" : {
        "password" : "password",
        "id" : "userid"
    }
}


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/login", tags=["api"], operation_id = "login" )
async def login( username: str, password: str, response: Response ):

    print( username )
    print( password )

    authenticated = False

    if username in users:
        if users[ username ][ 'password' ] == password:
            authenticated = True
            response.set_cookie( key="user", value=str( users[ username ][ 'id' ] ), max_age = 60 * 60 * 24 )

    return authenticated
