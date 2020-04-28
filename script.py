import requests
import json
import random
from collections import defaultdict
from bs4 import BeautifulSoup


def generateNumber():
    phone = "".join([str(random.randint(0, 9)) for i in range(10)])
    return phone


def generateSkills(skills, descriptions):
    skills_dict = defaultdict(list)
    num_skills = random.randint(1, 3)
    skills_sample = random.sample(skills, num_skills)

    for skill in skills_sample:
        desc = descriptions[skill]
        skill_obj = {"skill": skill, "description": desc}
        skills_dict["skills"].append(skill_obj)
    return skills_dict["skills"]


def writeToFile(girls, boys):

    emails = ["@gmail.com", "@yahoo.com",
              "@hotmail.com", "@outlook.com", "@skidmail.com"]

    departments = ["sales", "human_resources", "marketing",
                   "engineering", "finance", "quality_assurance", "operations"]

    skills_arr = ["azure", "excel", "photoshop",
                  "illustrator", "indesign", "public_speaking", "python", "c++", "frontend"]

    skills_descriptions = {"azure": "Great at working on databases with this software.",
                           "excel": "Have worked with excel for years and if anybody needs help, please contact.",
                           "photoshop": "Have worked with it for years and can manipulate every image possible. Let me know.",
                           "illustrator": "Worked on multiple company wide projects involving illustrator and am willing to share my expertise.",
                           "indesign": "Used to be a graphic designer so if anybody needs help with graphics, bang my line.",
                           "public_speaking": "Can help people prepare for any presentations, just email me!",
                           "python": "If anybody is learning Python or just needs help with a project or piece of code, slack me!",
                           "c++": "If anybody is learning a new language and its C++ for some reason, hit me up!",
                           "frontend": "If anybody is working on web devlopment and need help with the frontend, feel free to slack me."}

    with open("employees.json", "w+") as file:
        for name in girls[:50]:
            object = {}
            object["id"] = girls.index(name) + 1
            object["name"] = name.text.split()[0]
            object["email"] = object["name"] + \
                str(random.randint(0, 999)) + random.choice(emails)
            object["department"] = random.choice(departments).lower()
            object["phone"] = generateNumber()
            object["skills"] = generateSkills(skills_arr, skills_descriptions)

            file.write(str(object) + ",")

        for name in boys[:50]:
            object = {}
            object["id"] = boys.index(name) + 51
            object["name"] = name.text.split()[0]
            object["email"] = object["name"] + \
                str(random.randint(0, 999)) + random.choice(emails)
            object["department"] = random.choice(departments).lower()
            object["phone"] = generateNumber()
            object["skills"] = generateSkills(skills_arr, skills_descriptions)

            file.write(str(object) + ",")


def main():
    url_girls = 'https://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/the-latest-top-100-girls-names-chosen-in-the-uk-this-year'
    url_boys = "https://www.familyeducation.com/baby-names/popular-names/boys"
    res_girls = requests.get(url_girls)
    res_boys = requests.get(url_boys)

    soup_girls = BeautifulSoup(res_girls.text, 'html.parser')
    soup_boys = BeautifulSoup(res_boys.text, 'html.parser')
    parent1 = soup_girls.select("article ol li")
    parent2 = soup_boys.select("section div ul li a")
    writeToFile(parent1, parent2)


main()
