# coding: utf8
# 1 - Search through all files inside a directory master page
# 2 - Store all questions inside an array
# 3 - Shuffle and print inside a .txt file
import os
from os import walk
import re
from bs4 import BeautifulSoup
import random
import csv

# Contains file names
page_list = []

# Contains parent directories corresponding to page list - same index
dir_list = []

# Contains all questions
questions = []

# Contains all HTML answers
answers = []

dict_list = []

# Extracts all HTML files within the directory main.py is located
def extract_pages():
    re_pattern = r".html$"
    for x in os.walk(os.getcwd()):
        try:
            for y in x[2]:
                if re.search(re_pattern, y):
                    page_list.append(y)
                    dir_list.append(x[0])
        except:
            continue

# Extracts questions from an individual file
def extract_questions_and_answers(indexx):

    with open(dir_list[indexx] + "/" + page_list[indexx], "rb") as file:
        soup = BeautifulSoup(file ,"lxml")

        re_pattern = "\?$"
        all_uls = soup.find_all("ul")
        for current in all_uls:
            if current["class"][0] == "toggle":
                if re.search(re_pattern, current.li.summary.text):
                    try:
                        questions.append(current.li.summary.text.strip('"'))
                        full_tag = current.li.details.children
                        i = 0
                        answer = ""
                        for child in full_tag:
                            if i > 1:
                                answer += str(child)
                            i += 1
                        answers.append(answer.strip('"'))
                    except:
                        continue

def todictionary(questions, answers):
    dict_list = []
    for i in range(len(questions)):
        current_dict = dict()
        current_dict["QUESTION"] = questions[i]
        current_dict["ANSWER"] = answers[i]
        dict_list.append(current_dict)
    return dict_list
    
def tolist(questions, answers):
    new_list = []
    for i in range(len(questions)):
        current_string = str(questions[i]) + '|' + str(answers[i])
        new_list.append(current_string)
    return new_list

def create_csv(somelist):
    with open("import_to_anki.csv", "w") as file:
        for item in somelist:
            file.write("%s\n" % item)
        file.close()




extract_pages()

for i, a in enumerate(page_list):
    extract_questions_and_answers(i)

new_list = tolist(questions,answers)
print(new_list[1])

create_csv(tolist(questions,answers))
