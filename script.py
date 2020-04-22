import requests
import json
import random
from bs4 import BeautifulSoup


def generateNumber():
    phone = "".join([str(random.randint(0, 9)) for i in range(10)])
    return phone


def writeToFile(girls, boys):
    emails = ["@gmail.com", "@yahoo.com",
              "@hotmail.com", "@outlook.com", "@skidmail.com"]
    departments = ["Sales", "Human Resources", "Marketing",
                   "Research", "Production", "Engineering", "Finance", "Quality Assurance", "Operations"]
    skills = ['Azure', "Excel", "Photoshop",
              "Illustrator", "InDesign", "Premiere"]

    with open("test.json", "w+") as file:
        for name in girls[:50]:
            object = {}
            object["EID"] = girls.index(name) + 1
            object["name"] = name.text.split()[0]
            object["email"] = object["name"] + \
                str(random.randint(0, 999)) + random.choice(emails)
            object["department"] = random.choice(departments)
            object["phone"] = generateNumber()
            file.write(str(object) + ",")
        for name in boys[:50]:
            object = {}
            object["EID"] = boys.index(name) + 51
            object["name"] = name.text.split()[0]
            object["email"] = object["name"] + \
                str(random.randint(0, 999)) + random.choice(emails)
            object["department"] = random.choice(departments)
            object["phone"] = generateNumber()
            file.write(str(object) + ",")


def readFile():
    with open("test.json", "r") as f:
        data = json.load(f)
        print(data)


def main():
    url_girls = 'https://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/the-latest-top-100-girls-names-chosen-in-the-uk-this-year'
    url_boys = "https://www.familyeducation.com/baby-names/popular-names/boys"
    res_girls = requests.get(url_girls)
    res_boys = requests.get(url_boys)

    soup_girls = BeautifulSoup(res_girls.text, 'html.parser')
    soup_boys = BeautifulSoup(res_boys.text, 'html.parser')
    parent1 = soup_girls.select("article ol li")
    parent2 = soup_boys.select("section div ul li a")
    #writeToFile(parent1, parent2)
    readFile()


main()
