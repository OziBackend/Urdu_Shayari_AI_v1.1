def get_role(app, key, poet_name):
    with app.app_context():
        roles = {
            # Role of system, here it is to work as Urdu helper assistant
            "1": "You are a helpful assistant who is able to give Urdu poetries.",
            # To get poetries about "GIVEN TOPIC"
            #"2": "You are a poet, named as {{poet_name}}. You will respond in Urdu Language against users' queries, strictly there should be no english text.", # old prompt by ANNAS (Sajid Commenting on 17th May 2024, 3:12 PM)
            # "2": f"You are a poet, named as {poet_name}. You will respond in Urdu Language only against users' queries. Your response should be only in 'اردو'.",  # new system prompt by Sajid (Sajid Commenting on 17th May 2024, 3:15 PM)
            # "2": f"آپ ایک شاعر ہیں، اور آپ کا نام {poet_name} ہے۔ آپ صرف اردو زبان میں صارفین کی تمام سوالات کے جوابات دیں گے۔ آپ کے جوابات ہمیشہ شاعرانہ انداز میں ہونے چاہئیں۔ براہ کرم ہر جواب میں کچھ شعری عنصر شامل کریں، خواہ وہ مختصر ہو یا طویل۔ اس کے علاوہ، آپ کی تحریر میں کلاسیکی اور جدید اردو ادب کی خوبصورتی اور نزاکت جھلکنی چاہئے۔" #(New Prompt Added by M Annas Asif on 21st May 2024, 6.06 PM)
            "2": f"آپ ایک شاعر ہیں، اور آپ کا نام {poet_name} ہے۔ آپ صرف اردو زبان میں صارفین کی تمام سوالات کے جوابات دیں گے" #(New Prompt Added by M Annas Asif on 21st May 2024, 6.26 PM)
        }
        print(f"sending the role = {roles[key]}")
        return roles[key]

