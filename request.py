import requests
import json
import pprint
import os.path
from os import path

#courses ka API Endpoint ya URL call kar kar, data courses.json file mei store karta hai.
link = "http://saral.navgurukul.org/api/courses"

def get_api(url):
    response=requests.get(url)
    return (response.text)
course_data = get_api(link)

data = json.loads(course_data)
dic_data = data["availableCourses"]


# availableCourse find the name and id
def availbleCourse_data():
    index=0
    for i in dic_data:
        print(index,i["name"],i["id"])
        index=index+1
availbleCourse_data()
print("\n")


print("*************** well_come ***********************")
def available_course():
    courses_list=[]
    id_list=[]
    index=0
    while(index<len(dic_data)):
        course_name=dic_data[index]["name"]
        courses_list.append(course_name)
        course_id=dic_data[index]["id"]
        id_list.append(course_id)
        index=index+1
    return [courses_list,id_list]
list_of_course = available_course()

name_list = list_of_course[0]
id_list = list_of_course[1]

user_choice=int(input("enter the number"))
print("courses of name and id:",name_list[user_choice],id_list[user_choice])

print("*************** well_come ***********************")
print("\n")


url_api= "http://saral.navgurukul.org/api/courses/" +str(id_list[user_choice])+"/exercises"
url_response = get_api(url_api)
data1 = json.loads(url_response)
dic_change_data = data1["data"]

def url_courses():
    data_list=[]
    number=0
    while(number<len(dic_change_data)):
        name_list=dic_change_data[number]["name"]
        data_list.append(name_list)
        print(number+1 ,name_list)
        chaild_exercise=dic_change_data[number]["childExercises"]

        chaild_index=0
        while chaild_index<len(chaild_exercise):
            if "parent_exercise_id" in chaild_exercise[chaild_index]:
                print(5*" ",chaild_index+1, chaild_exercise[chaild_index]["name"])
            chaild_index=chaild_index+1
        number=number+1
    return data_list
list_of_parents=url_courses()


print("*************** well_come ***********************")

exercise_index=int(input("enter the number"))
def singal_id():
    slug_list=[]
    slug_index=0
    while(slug_index<len(dic_change_data)-2):
        print(slug_index,dic_change_data[exercise_index-1]["name"])
        slug_exercise=slug_index,dic_change_data[slug_index]["slug"]
        slug_list.append(slug_exercise)
        chaild_exercise=dic_change_data[exercise_index-1]["childExercises"]
        parents=dic_change_data[slug_index]["parent_exercise_id"]

        index=0
        while(index<len(chaild_exercise)):
            if "parent_exercise_id" in chaild_exercise[index]:
                print(5*" ",index+1, chaild_exercise[index]["name"])
            elif("parent_exercise_id"=="null"):
                print(5*" ",index+1, chaild_exercise[index]["name"])
            index=index+1
        break
        slug_index=slug_index+1
    
singal_id()

chaild_exercise=dic_change_data[exercise_index-1]["childExercises"]
content = int(input("select exercise"))
slug = chaild_exercise[content-1]["slug"]
print(slug,id_list[user_choice])



url_contant="http://saral.navgurukul.org/api/courses/"+str(id_list[user_choice])+"/exercise/getBySlug?slug="+str(slug)
con_response=requests.get(url_contant)
print(con_response)
contant_data =(con_response.text)
change_int=json.loads(contant_data)
print(change_int["content"])

user=input("enter the number")
if user=="next":
    function()



