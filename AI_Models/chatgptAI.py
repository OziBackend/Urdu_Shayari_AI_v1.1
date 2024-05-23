from openai import OpenAI
from flask import jsonify, Flask
from Keys.authKeys import keys
import os
import re
import json

# laoding prompts file
from Data_Values.prompts import prompts
# from Data_Values.roles import roles
from Data_Values.roles import get_role


os.environ["OPENAI_API_KEY"] = keys["openAI"]  # Replace with your actual key

client = OpenAI()


####################################################################################
# =================================Functions=======================================#
####################################################################################

def genAIfunction(system_role, prompt, app, logger):
    with app.app_context():
        try:
            completion = client.chat.completions.create(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {
                                "role": "system",
                                "content": system_role,
                            },
                            {
                                "role": "user",
                                "content": prompt,
                            },
                        ],
                    )
            completed_data = completion.choices[0].message.content
            return {"flag": True, "completion_data": completed_data}

        except BaseException as e:
            logger.error('1... Exception thrown in GenAIfunction = %s', str(e))
            print(f"1... In GenAIfunction exception is = {e}")
            return {"flag": False, "completion_data": ""}

####################################################################################
# =========================Poetry by Poet and Poem Name============================#
####################################################################################


def poetry_by_name_and_poetname(app, data, logger):

    with app.app_context():

        prompt = prompts["1"].format(poet_name=data["poet_name"], poem_name=data["poem_name"])
        system_role = get_role(app, "1", "")

        print('Your Prompy is : ', prompt)

        try:
            AI_data = genAIfunction(system_role, prompt, app, logger)
            if AI_data['flag']:
                completed_data = AI_data['completion_data']
                print("Data Completion============>", completed_data)
                return {"flag": True, "completion_data": completed_data}
            else:
                logger.error('2... No data returned from GenAI function')
                return {"flag": False, "completion_data": ""}


        except BaseException as e:
            # Exception is thrown while calling ChatGPT Api
            logger.error('2... Exception thrown in poetry_by_poet_and_poem_name function = %s', str(e))
            print(f"2... In poetry_by_poet_and_poem_name exception is = {e}")
            return {"flag": False, "completion_data": ""}


def get_poetry_by_poet_and_poem_name(app, data, return_data, event, logger):
    with app.app_context():
        acquired_data = poetry_by_name_and_poetname(app, data, logger)
        # print("Completion Data: ", acquired_data['completion_data'])
        if acquired_data["flag"]:
            # data is found and processed before sending to client
            data = acquired_data["completion_data"]
            data_cleaned = re.sub(r'[{}\*)(]', "", data_cleaned)
            data_cleaned = re.sub(r',]&', "]", data_cleaned)
            data = data.split(",")
            return_data["response"] = data
        else:
            # data not found, exception was thrown, blank array is returned to client
            logger.error('3... No data returned to Main Route from get_poetry_by_poet_and_poem_name')
            return_data["response"] = []


####################################################################################
# ================================Poetry by Topic===================================#
####################################################################################


def poetry_by_topic(app, data, logger):
    with app.app_context():

        prompt = prompts["2"].format(poetry_topic=data["poetry_topic"])
        system_role = get_role(app, "1", "")

        try:
            AI_data = genAIfunction(system_role, prompt, app, logger)
            if AI_data['flag']:
                completed_data = AI_data['completion_data']
                print("Data Completion============>", completed_data)
                return {"flag": True, "completion_data": completed_data}
            else:
                logger.error('4... No data returned from GenAI function')
                return {"flag": False, "completion_data": ""}
            
        except BaseException as e:
            logger.error('4... Exception thrown in poetry_by_topic function = %s', str(e))
            print(f"4... In poetry_by_topic exception is = {e}")
            return {"flag": False, "completion_data": ""}

def get_poetry_by_topic(app, data, returned_data, logger):
    with app.app_context():
        
        acquired_data = poetry_by_topic(app, data, logger)

        if acquired_data["flag"]:
            # data is found and processed before sending to client
            data = acquired_data["completion_data"]
            data_cleaned = data.replace("\n", ',')
            data_cleaned = data.replace("'", '"')
            data_cleaned = re.sub(r'[{}\*)(]', "", data_cleaned)
            data_cleaned = re.sub(r',]&', "]", data_cleaned)

            try:
                # data is turned to JSON dict object
                print('DATA TO CONVERT TO JSON',data_cleaned)
                data_dict = json.loads(data_cleaned)
                
                print("JSON Formated Data============> %s", data_dict)
                returned_data["response"] = data_dict
            except BaseException as e:
                # Exception is thrown while calling ChatGPT Api
                print(f"5... In get_poetry_by_topic exception is = {e}")
                logger.error('Error in JSON = %s', str(data_cleaned))
                logger.error('5... Exception thrown in get_poetry_by_topic = %s', e)
                returned_data["response"] = []


        else:
            # data not found, exception was thrown, blank array is returned to client
            logger.error('5... Empty Response from API: []')
            returned_data["response"] = []


####################################################################################
# ==============================Poetry by Category==================================#
####################################################################################


def poetry_by_category(app, data, logger):
    with app.app_context():

        prompt = prompts["3"].format(poetry_category=data["poetry_category"])
        system_role = get_role(app, "1", "")

        try:
            AI_data = genAIfunction(system_role, prompt, app, logger)
            if AI_data['flag']:
                completed_data = AI_data['completion_data']
                print("Data Completion============>", completed_data)
                return {"flag": True, "completion_data": completed_data}
            else:
                logger.error('6.. No data returned from GenAI function')
                return {"flag": False, "completion_data": ""}

        except BaseException as e:
            logger.error('6... Exception thrown in poetry_by_category function = %s', str(e))
            print(f"6... In poetry_by_category exception is = {e}")
            return {"flag": False, "completion_data": ""}


def get_poetry_by_category(app, data, returned_data, logger):

    with app.app_context():
        
        acquired_data = poetry_by_category(app, data, logger)

        if acquired_data["flag"]:
            # data is found and processed before sending to client
            data = acquired_data["completion_data"]
            data_cleaned = data.replace("\n", ',')
            data_cleaned = data.replace("'", '"')
            data_cleaned = re.sub(r'[{}\*)(]', "", data_cleaned)
            data_cleaned = re.sub(r',]&', "]", data_cleaned)

            try:
                # data is turned to JSON dict object
                print('DATA TO CONVERT TO JSON',data_cleaned)
                data_dict = json.loads(data_cleaned)
                
                print("JSON Formated Data============> %s", data_dict)
                returned_data["response"] = data_dict
            except BaseException as e:
                # Exception is thrown while calling ChatGPT Api
                print(f"7... In def get_poetry_by_category(app, data, returned_data, logger): exception is = {e}")
                logger.error('Error in JSON = %s', str(data_cleaned))
                logger.error('7... Exception thrown in def get_poetry_by_category(app, data, returned_data, logger): = %s', e)
                returned_data["response"] = []

        else:
            # data not found, exception was thrown, blank array is returned to client
            logger.error('7... Empty Response from API: []')
            returned_data["response"] = []


####################################################################################
# ==========================AI Conversations with Poets=============================#
####################################################################################


def ai_conversation(app, data, logger):
    
    with app.app_context():

        prompt = data["prompt"]
        system_role = get_role(app, "2", data["poet_name"]) # rename 'data["poet_name"]' to 'data["poet_name"]'
        
        try:
            AI_data = genAIfunction(system_role, prompt, app, logger)
            print('getting ai data===========++++++++++',AI_data)
            if AI_data['flag']:
                completed_data = AI_data['completion_data']
                print("Data Completion============>", completed_data)
                return {"flag": True, "completion_data": completed_data}
            else:
                logger.error('8... No data returned from GenAI function')
                return {"flag": False, "completion_data": ""}

        except BaseException as e:
            logger.error('8... Exception thrown in ai_conversation function = %s', str(e))
            print(f"8... In ai_conversation exception is = {e}")
            return {"flag": False, "completion_data": ""}


def ai_conversation_with_poets(app, data, returned_data, logger):
    with app.app_context():
        
        acquired_data = ai_conversation(app, data, logger)

        if acquired_data["flag"]:
            # data is found and processed before sending to client
            data = acquired_data["completion_data"]
            returned_data["response"] = data
        else:
            # data not found, exception was thrown, blank array is returned to client
            logger.error('9... Empty Response from API: []')
            returned_data["response"] = []
