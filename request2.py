import os.path 
from os import path
import requests
import json

print("---------------- welcome to the saral courses ---------------")


print("\n")
# this is the url where api will hit the request
get_saral_url = "http://saral.navgurukul.org/api/courses"
# print(get_saral_url)
def courses_api(url):
	response = requests.get(url)
	return(response.text)
path.exists

if path.exists("courses.json"):
	with open("courses.json","r") as data:
		# coverting the data into string from _io.TextIoWrapper
		read_file = json.load(data)
		# data is converting from string to dictionary  
		dictionary_type = json.loads(read_file)
else:
	response_text = courses_api(get_saral_url)
	with open("courses.json","w") as file:
		json.dump(response_text,file)
		 # while dumping the data from fil…





#  if path.exists("saral.json"):
#     with open("saral.json", "r") as file:
#         data = json.load(file)
#         dic_data = json.loads(data)

# if os.path.isfile("saral.json"):
#     with open("saral.json","r") as my_file:
#         url_data=json.load(my_file)
# else:
#     res= get_api(link)
#     with open("saral.json","w") as file:
#         json.dump(res,file)
#         dic = json.dumps(res)
#         print(dic)
    
# print(dic)
# 
# print(dic_data)

# find the courses from url again
# index=0
# for i in dic_data:
#     print(index,user["name"],i["id"])
#     index=index+1

# user=input("enter the number")