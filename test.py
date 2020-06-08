from bs4 import BeautifulSoup

question = []
answer = []

with open("export.html", "r+", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

    all_uls = soup.find_all("ul")
    for current in all_uls:
        if current["class"][0] == "toggle":
            try:
                question.append(current.li.details.summary.text)
                full_tag = current.li.details.children
                i = 0
                answer_curr = ""
                for child in full_tag:
                    if i > 1:
                        answer_curr += str(child)
                    i += 1
                answer.append(answer_curr)
            except:
                print("NOT QUITE")

