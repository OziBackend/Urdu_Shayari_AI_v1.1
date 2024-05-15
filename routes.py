from flask import jsonify, request

# from helpers import some_helper_function
from AI_Models.groqAI import groqAI
from AI_Models.chatgptAI import (
    get_poetry_by_poet_and_poem_name,
    get_poetry_by_topic,
    get_poetry_by_category,
    ai_conversation_with_poets,
)
import threading
import re
import time

semaphores = threading.Semaphore(5)


def setup_routes(app):
    @app.route("/urdu-shayari/ai")
    def index():
        return "Hello, world!"

    # Groq API Testing
    @app.route("/urdu-shayari/ai/groq")
    def groq_AI():
        return jsonify({"message": groqAI()})

    # Urdu Shayari APIs using ChatGPT
    @app.route("/urdu-shayari/ai/get_poetry_by_poet_and_poem_name", methods=["GET"])
    def poetry_by_poet_and_poem_name():
        query_params = {}
        for key, value in request.args.items():
            query_params[key] = value

        if (
            not query_params
            or not query_params["poem_name"]
            or not query_params["poet_name"]
        ):
            print("--------Parameters missing--------")
            return (
                jsonify(
                    {"message": "Bad Request, no query found or parameters missing"}
                ),
                400,
            )

        print("Query Params===>", query_params)
        print("CHat GPT AI funtion called")
        return_data = {}
        additional_data = query_params

        # Acquire Semaphore
        print("Acquiring a Semaphore")
        semaphores.acquire()
        event = threading.Event()
        t = threading.Thread(
            target=get_poetry_by_poet_and_poem_name,
            args=(app, additional_data, return_data, event),
        )
        t.start()
        t.join()

        # Processing on response
        print(return_data)

        # Release Semaphore
        print("Releasing a Semaphore")
        semaphores.release()

        if return_data is None:
            return jsonify({"response": [] }), 500

        return jsonify(return_data)

    @app.route("/urdu-shayari/ai/get_poetry_by_topic", methods=["GET"])
    def poetry_by_topic():
        print("CHat GPT AI funtion to get_poetry_by_topic called")
        query_params = {}
        for key, value in request.args.items():
            query_params[key] = value

        if not query_params or not query_params["poetry_topic"]:
            print("--------Parameters missing--------")
            return (
                jsonify(
                    {"message": "Bad Request, no query found or parameters missing"}
                ),
                400,
            )

        print("Query Params===>", query_params)
        return_data = {}
        additional_data = query_params

        # Acquire Semaphore
        print("Acquiring a Semaphore")
        semaphores.acquire()

        t = threading.Thread(
            target=get_poetry_by_topic, args=(app, additional_data, return_data)
        )
        t.start()
        t.join()

        # Processing on response
        print(return_data)

        # Release Semaphore
        print("Releasing a Semaphore")
        semaphores.release()

        if return_data is None:
            return jsonify({"response": [] }), 500

        return jsonify(return_data)

    @app.route("/urdu-shayari/ai/get_poetry_by_category", methods=["GET"])
    def poetry_by_category():
        print("CHat GPT AI funtion to get_poetry_by_category called")
        query_params = {}
        for key, value in request.args.items():
            query_params[key] = value

        if not query_params or not query_params["poetry_category"]:
            print("--------Parameters missing--------")
            return (
                jsonify(
                    {"message": "Bad Request, no query found or parameters missing"}
                ),
                400,
            )

        print("Query Params===>", query_params)
        return_data = {}
        additional_data = query_params

        # Acquire Semaphore
        print("Acquiring a Semaphore")
        semaphores.acquire()

        t = threading.Thread(
            target=get_poetry_by_category, args=(app, additional_data, return_data)
        )
        t.start()
        t.join()

        # Processing on response
        print(return_data)

        # Release Semaphore
        print("Releasing a Semaphore")
        semaphores.release()
        
        if return_data is None:
            return jsonify({"response": [] }), 500

        return jsonify(return_data)

    @app.route("/urdu-shayari/ai/ai_conversation_with_poets", methods=["POST"])
    def ai_conversation():
        print("CHat GPT AI funtion to ai_conversation_with_poets called")

        # reading body parameters
        data = request.json
        print("<----------------------------------------->", data)
        # Process the recieved data
        if data is None:
            print("-------------Prompt Missing------------")
            return (jsonify({"message": "Bad Request, no prompt found"}), 400)

        query_params = {}
        for key, value in request.args.items():
            query_params[key] = value

        if not query_params or not query_params["poet_name"]:
            print("--------Parameters missing--------")
            return (
                jsonify(
                    {"message": "Bad Request, no query found or parameters missing"}
                ),
                400,
            )

        print("Prompt by User===>", data.get("prompt"))
        print("Poet Name===>", query_params["poet_name"])
        return_data = {}
        additional_data = {
            "prompt": data.get("prompt"),
            "poet_name": query_params["poet_name"],
        }

        # Acquire Semaphore
        print("Acquiring a Semaphore")
        semaphores.acquire()

        t = threading.Thread(
            target=ai_conversation_with_poets, args=(app, additional_data, return_data)
        )
        t.start()
        t.join()

        # Processing on response
        print(return_data)

        # Release Semaphore
        print("Releasing a Semaphore")
        semaphores.release()

        if return_data is None:
            return jsonify({"response": [] }), 500

        return jsonify(return_data)
