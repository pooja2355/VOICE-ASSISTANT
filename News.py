import requests
import ss

api_address="https://newsapi.org/v2/top-headlines?country=us&apiKey=" + ss.key
json_data = requests.get(api_address).json()

arr=[]

def news():
    for i in range(3):
       arr.append("NUMBER"+ (str(i+1)+"+" + json_data["articles"][i]["title"]+".") )

    return arr




