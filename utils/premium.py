import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(BASE_DIR, "..", "json", "premium.json")

def loadData():
    if not os.path.exists(filePath):
        return {}

    try:
        with open(filePath, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def saveData(data):
    with open(filePath, "w") as f:
        json.dump(data, f, indent=4)

def serverHasPremium(guildID):
    data = loadData()
    return str(guildID) in data

def activatePremium(guildID, userID):
    data = loadData()
    
    if userID not in data:
        data[str(guildID)] = userID
        saveData(data)