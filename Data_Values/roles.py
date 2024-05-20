def get_role(app, key, poet_name):
    with app.app_context():
        roles = {
            # Role of system, here it is to work as Urdu helper assistant
            "1": "You are a helpful assistant who is able to give Urdu poetries.",
            # To get poetries about "GIVEN TOPIC"
            #"2": "You are a poet, named as {{poet_name}}. You will respond in Urdu Language against users' queries, strictly there should be no english text.", # old prompt by ANNAS (Sajid Commenting on 17th May 2024, 3:12 PM)
            "2": f"You are a poet, named as {poet_name}. You will respond in Urdu Language only against users' queries. Your response should be only in 'اردو'.",  # new system prompt by Sajid (Sajid Commenting on 17th May 2024, 3:15 PM)
        }
        print(f"sending the role = {roles[key]}")
        return roles[key]

