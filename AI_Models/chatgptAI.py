from openai import OpenAI
from flask import jsonify, Flask
from Keys.authKeys import keys
import os
import re
import json

# laoding prompts file
from Data_Values.prompts import prompts
from Data_Values.roles import roles


os.environ["OPENAI_API_KEY"] = keys["openAI"]  # Replace with your actual key

client = OpenAI()

####################################################################################
# =========================Poetry by Poet and Poem Name=============================#
####################################################################################


def poetry_by_name_and_poetname(app, data):

    with app.app_context():
        print("Data recieved in thread worker", data)
        prompt_1 = prompts["1"]
        system_role = roles["1"]
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
                        "content": prompt_1.format(
                            poet_name=data["poet_name"], poem_name=data["poem_name"]
                        ),
                    },
                ],
            )
            completed_data = completion.choices[0].message.content
            print("Type of Completion============>", type(completed_data))
            print("Data Completion============>", completed_data)
            return {"flag": True, "completion_data": completed_data}

        except BaseException as e:
            # Exception is thrown while calling ChatGPT Api
            print(f"1... In poetry_by_poet_and_poem_name exception is = {e}")
            return jsonify({"flag": False, "completion_data": ""})


def get_poetry_by_poet_and_poem_name(app, data, return_data, event):
    with app.app_context():
        acquired_data = poetry_by_name_and_poetname(app, data)
        # print("Completion Data: ", acquired_data['completion_data'])
        print("Thread Wait Started")
        event.wait(5)
        print("Thread Wait Finished")
        if acquired_data["flag"]:
            # data is found and processed before sending to client
            data = acquired_data["completion_data"]
            data = re.sub(r"[\'\`()\[\]\"\n]", "", data)
            data = data.split(",")
            return_data["response"] = data
        else:
            # data not found, exception was thrown, blank array is returned to client
            return_data["response"] = []


####################################################################################
# ================================Poetry by Topic===================================#
####################################################################################


def poetry_by_topic(app, data):
    print("Data recieved in thread worker", data)
    with app.app_context():
        prompt_2 = prompts["2"]
        system_role = roles["1"]
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
                        "content": prompt_2.format(poetry_topic=data["poetry_topic"]),
                    },
                ],
            )
            completed_data = completion.choices[0].message.content
            print("Type of Completion============>", type(completed_data))
            print("Data Completion============>", completed_data)
            return {"flag": True, "completion_data": completed_data}

        except BaseException as e:
            # Exception is thrown while calling ChatGPT Api
            print(f"1... In poetry_by_topic exception is = {e}")
            return jsonify({"flag": False, "completion_data": ""})


def get_poetry_by_topic(app, data, returned_data):

    # returned_data["response"] = []
    acquired_data = poetry_by_topic(app, data)
    print("Completion Data: ", acquired_data["completion_data"])

    if acquired_data["flag"]:
        # data is found and processed before sending to client
        data = acquired_data["completion_data"]

        # data is converted to pure JSON format
        data_cleaned = data.replace("'", '"')
        print("Formatted Data", data_cleaned)

        # data is turned to JSON dict object
        data_dict = json.loads(data_cleaned)
        print("Type of Dict Data============>", type(data_dict))

        returned_data["response"] = data_dict
    else:
        # data not found, exception was thrown, blank array is returned to client
        returned_data["response"] = []


####################################################################################
# ==============================Poetry by Category==================================#
####################################################################################


def poetry_by_category(app, data):
    print("Data recieved in thread worker", data)
    with app.app_context():
        prompt_3 = prompts["3"]
        system_role = roles["1"]
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
                        "content": prompt_3.format(
                            poetry_category=data["poetry_category"]
                        ),
                    },
                ],
            )
            completed_data = completion.choices[0].message.content
            print("Type of Completion============>", type(completed_data))
            print("Data Completion============>", completed_data)
            return {"flag": True, "completion_data": completed_data}

        except BaseException as e:
            # Exception is thrown while calling ChatGPT Api
            print(f"1... In poetry_by_category exception is = {e}")
            return jsonify({"flag": False, "completion_data": ""})


def get_poetry_by_category(app, data, returned_data):

    # returned_data["response"] = []
    acquired_data = poetry_by_category(app, data)
    print("Completion Data: ", acquired_data["completion_data"])

    if acquired_data["flag"]:
        # data is found and processed before sending to client
        data = acquired_data["completion_data"]

        # data is converted to pure JSON format
        data_cleaned = data.replace("'", '"')
        print("Formatted Data", data_cleaned)

        # data is turned to JSON dict object
        data_dict = json.loads(data_cleaned)
        print("Type of Dict Data============>", type(data_dict))

        returned_data["response"] = data_dict
    else:
        # data not found, exception was thrown, blank array is returned to client
        returned_data["response"] = []


####################################################################################
# ==========================AI Conversations with Poets=============================#
####################################################################################


def ai_conversation(app, data):
    print("Data recieved in thread worker", data)
    with app.app_context():
        prompt = data["prompt"]
        system_role = roles["2"]
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {
                        "role": "system",
                        "content": system_role.format(poet_name=data["poet_name"]),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )
            completed_data = completion.choices[0].message.content
            print("Type of Completion============>", type(completed_data))
            print("Data Completion============>", completed_data)
            return {"flag": True, "completion_data": completed_data}

        except BaseException as e:
            # Exception is thrown while calling ChatGPT Api
            print(f"1... In ai_conversation exception is = {e}")
            return jsonify({"flag": False, "completion_data": ""})


def ai_conversation_with_poets(app, data, returned_data):

    # returned_data["response"] = []
    acquired_data = ai_conversation(app, data)
    print("Completion Data: ", acquired_data["completion_data"])

    if acquired_data["flag"]:
        # data is found and processed before sending to client
        data = acquired_data["completion_data"]
        # data = re.sub(r"\n\n", "\n", data)
        # data = re.sub(r"[\'\`()\[\]\"]", "", data)
        # print('formated by regex===============', data)
        # data = data.split("\n")
        # print('split by comma==================', data)
        returned_data["response"] = data
    else:
        # data not found, exception was thrown, blank array is returned to client
        returned_data["response"] = []
