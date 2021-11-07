lib = {"GENDER": "M",
       "AGE": "19",
       "SMOKING": "FALSE",
       "YELLOW_FINGERS": "FALSE",
       "ANXIETY": "FALSE",
       "PEER_PRESSURE": "FALSE",
       "CHRONIC_DISEASE": "FALSE",
       "FATIGUE": "FALSE",
       "ALLERGY": "FALSE",
       "WHEEZING": "FALSE",
       "ALCOHOL_CONSUMING": "TRUE",
       "COUGHING": "FALSE",
       "SHORTNESS_OF_BREATH": "FALSE",
       "SWALLOWING_DIFFICULTY": "FALSE",
       "CHEST_PAIN": "FALSE"}
api_str = ''
for key in lib:
    api_str += key + "=" + lib[key] + "&"

print("?"+api_str[:-1])
