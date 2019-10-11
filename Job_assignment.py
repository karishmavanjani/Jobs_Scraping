
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
import re

    
job = []
job_title_array = []
url= "http://maddy.zone/microworker/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
page1 = soup.find('span', class_='current')
page=int(page1.text.strip())
#print(page)
main_box = soup.find('div', class_='joblistarea')
for jobname in main_box:
    main_list = main_box.find_all('div', class_='jobname')
    #     main_pay = main_box.find_all('div', class_='jobpayment')
    #     main_success= main_box.find_all('div', class_='jobsuccess')
    #     main_ttr= main_box.find_all('div', class_='jobttr')
    #     main_status=  main_box.find_all('div', class_='jobstatus')
    #     main_done=  main_box.find_all('div', class_='jobdone')
    
    for alink in main_list:
        link = alink.find('a',href=True)
        job_link = "http://maddy.zone/microworker/" + link['href']
        #print(job_link)
        response = requests.get(job_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        main_job_box= soup.find('div', class_='jobarealeft')
        title = soup.find('div', class_='jobarealeft')
        job_title = title.find('h1').text.strip()
        job_title_array.append(job_title)
        job_break= len(job_title_array)
        if int(job_break)<49:
            Id = soup.find('div', class_= 'jobdetailsnoteleft')
            job_id = Id.find('p', text = re.compile('Job ID')).text.strip()
            #print(job_id)
            E_Id = soup.find('div', class_= 'jobdetailsnoteright')
            employer_id = E_Id.find('a').text
            #print(employer_id)
            pay = soup.find('div', class_= 'jobdetailsnoteleft')
            payment = pay.find_all('p')[1].text.strip()
            #print(payment)
            description = soup.find('div', class_= 'jobdetailsbox').text.strip()
            #print(description)
            job_listing = {
                        'job_title': job_title        ,
                        'job_id': job_id           ,
                        'employer_id': employer_id      , 
                        'payment': payment          , 
                        'description':  description     ,
                            } 
            job.append(job_listing)
            job_break= len(job)
            #print(job_break)
            # count_job_title= count(job_title)
            df = pd.DataFrame(job,columns=["job_title","job_id","employer_id","payment", "description"])
            df.to_csv("twitter.csv", index= True)    
             


        elif int(job_break)>48:
            break
             



