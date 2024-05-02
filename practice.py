from bs4 import BeautifulSoup

with open('index.html','r')as first_page :
    content=first_page.read()
    soup=BeautifulSoup(content , 'lxml') # soup=BeautifulSoup(content)
    #print(soup.prettify)
'''
    to grab a certain tag 
    h2_tag = soup.find("h2")
    print(h2_tag)

    #using this u can find the first occurence only if we use soup.find_all() it will print all occurences
    #main code 
    import requests
from bs4 import BeautifulSoup

html_content = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python+&txtLocation=").text


soup= BeautifulSoup(html_content , 'lxml')
#print(soup.prettify())


skills_known = input("Enter the your Skills ")
skill= skills_known.split(',')


#strip to remove spaces between the output
'''

company_name= soup.find("h3", class_="joblist-comp-name").text.replace(" ",'').strip()
skills=soup.find('span',class_="srp-skills").text.replace(" ",'').strip().split(',')
date=soup.find('span',class_="sim-posted").text.strip()
print(company_name)
print(skills)
print(date)

print(f"Company name : {company_name} \nSkills required : {skills}\nDate : {date}")
'''

job_list=soup.find_all("li" , class_="clearfix job-bx wht-shd-bx")
for job_list in job_list:
    skills = job_list.find('span', class_="srp-skills").text.replace(" ", '').strip().split(',')
    if skills:
        company_name = job_list.find("h3", class_="joblist-comp-name").text.replace(" ", '').strip()
        date = job_list.find('span', class_="sim-posted").text
        print(f"Company name : {company_name} \nSkills required : {skills}\nDate : {date}")
        print("**************")
    else:
        print("No skills found for the job listing.")


    h2_tags=soup.find_all("h2")
    #print(h2_tags)

    for h2_tag in h2_tags: #h2 tag in h2_Tags object jo bs4 ne find kiye ussmein se loop mein print karwaye
     
     #print(h2_tag) 
     print(h2_tag.text) #only for text 
     '''
'''class_container = soup.find_all("div", class_="course")
for class_container in class_container:
    print(class_container.h2.text)
    print(class_container.p.text)''' #this is the main process
class_container = soup.find_all("div", class_="course")
for class_container in class_container:
    print(f"Course name : {class_container.h2.text} and it costs: {class_container.p.text}" )
    print("*******")