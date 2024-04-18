# imports needed
from openai import OpenAI
import asyncio
import os
from dotenv import load_dotenv
import requests
import json
import ast

# load in and store open ai api key
load_dotenv()
openai_key = os.getenv('OPENAI_KEY')
google_key = os.getenv('GOOGLE_KEY')


### Chatbot Functions

# returns answer to a question
def getChat(question):
    client = OpenAI(
        api_key=openai_key,
    )
    

    input_text = f"""
    You are a car mechanic expert. Answer the following question sufficently: {question}
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="gpt-4-turbo",
    )

    # Extract the translated text from the model's response
    answer = response.choices[0].message.content.strip("'")
    return answer



# returns the diagnosis of the car based on car and its symptoms
def getDiagnosis(carDetails, carIssue):
    client = OpenAI(
        api_key=openai_key,
    )
    

    input_text = f"""
    Details of the car: '{carDetails}'

    Current Symptoms Car is Experiencing: '{carIssue}'

    Prompt: 'Look at the symptoms described to determine what is
    wrong with the car. Determine what is the most probable issue the
    car is facing based on the symptoms. Relatively short responce please, be percise.'
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="gpt-4-turbo",
    )

    # Extract the translated text from the model's response
    diagnosis = response.choices[0].message.content.strip("'")
    return diagnosis



# gets user question and returns with responce from chatBot
def askQuestion(carIssue, carDetails, carDiagnosis, userQuestion):
    client = OpenAI(
        api_key=openai_key,
    )
    

    input_text = f"""
    Details of the car: '{carDetails}'

    Current Symptoms Car is Experiencing: '{carIssue}'

    Diagnosis of Car: '{carDiagnosis}'

    User's Question: '{userQuestion}'

    Prompt: 'Act as a car expert mechanic and use the information of the symptoms of the car, 
    the details of the car, and the diagnosis of the car's issue to answer the user's question. Be detailed 
    and simple easy explinations. Give them a good sufficient answer.'
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="gpt-4-turbo",
    )

    # Extract the translated text from the model's response
    answer = response.choices[0].message.content.strip("'")
    return answer



# returns list of parts needed to fix issue
def getParts(carIssue, carDetails, carDiagnosis):
    client = OpenAI(
        api_key=openai_key,
    )
    

    input_text = f"""
    Details of the car: '{carDetails}'

    Current Symptoms Car is Experiencing: '{carIssue}'

    Diagnosis of Car: '{carDiagnosis}'

    Prompt: 'Strictly return a list of parts needed to fix this issue based
    on the diagnosis of the viehcle. Be specific based on the exact vehichle.
    Return it in a python list format. with each element being another list three elements of
    part needed (string data type) and how many are needed (int data type) and est price per part (double).
    Example responce would be '[...]' without prefacing ```python '
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="gpt-4-turbo",
    )

    # Extract the translated text from the model's response
    answer = response.choices[0].message.content.strip("'")
    return answer


# convert parts string to list in python
def partsList(partsString):
    parts_list = ast.literal_eval(partsString)
    return parts_list


### Other API Functions

def getMechanics(longitude, latitude):
    url = "https://places.googleapis.com/v1/places:searchNearby"
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': google_key,
        'X-Goog-FieldMask': 'places.displayName,places.rating,places.formattedAddress'
    }
    body = {
        "includedTypes": ["car_repair"],
        "maxResultCount": 10,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "radius": 10000
            }
        }
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(body))
        response.raise_for_status()  # Raise HTTPError for bad responses
        results = response.json()

        if 'places' in results:
            places = sorted(
                [place for place in results['places'] if 'rating' in place],
                key=lambda x: x['rating'],
                reverse=True
            )
            return places
        else:
            print("No car repair shops were found within the specified area.")  # Print the whole response for better debugging
            return ["No car repair shops were found within the specified area."]

    except requests.RequestException as e:
        print("Request error:", e)
        return []  # Return an empty list in case of request error


# returns answer to openai request
def getResp(question):
    client = OpenAI(
        api_key=openai_key,
    )
    

    input_text = f"""
    Convert this to a clean neat and tidy list of this information seperated by double new line (only return the list, no extra dialougue): {question}
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="gpt-4-turbo",
    )

    # Extract the translated text from the model's response
    answer = response.choices[0].message.content.strip("'")
    return answer