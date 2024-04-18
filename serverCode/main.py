# all the imports needed
from fastapi import FastAPI
from fastapi import Header
from fastapi.middleware.cors import CORSMiddleware
from chatbot import *

# initialize an instance for the fast api server
app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)



# greeting api
@app.get("/")
async def root():
    return {"message": "This is car diagnosis API"}


# get chat answer
@app.get("/getChatbot")
async def chat_answer1(question: str = Header(None)):
    answer = getChat(question)
    return {'response': answer}


# get custom chat answer
@app.get("/customChat")
async def custom_chat(question: str = Header(None), carIssue: str = Header(None), carDetails: str = Header(None), carDiagnosis: str = Header(None)):
    answer = askQuestion(carIssue, carDetails, carDiagnosis, question)
    return {'response': answer}


# get diagnosis of car
@app.get("/getDiagnosis")
async def get_diagnosis(carIssue: str = Header(None), carDetails: str = Header(None)):
    answer = getDiagnosis(carDetails, carIssue)
    return {'response': answer}


# get parts for car
@app.get("/getParts")
async def custom_chat(carIssue: str = Header(None), carDetails: str = Header(None), carDiagnosis: str = Header(None)):
    pList = getParts(carIssue, carDetails, carDiagnosis)
    answer = partsList(pList)
    return {'response': answer}


# gets mechanic shops in area
@app.get("/getMech")
async def custom_chat(longitude: int = Header(None), latitude: int = Header(None)):
    answer = getMechanics()
    return {'response': answer}
    