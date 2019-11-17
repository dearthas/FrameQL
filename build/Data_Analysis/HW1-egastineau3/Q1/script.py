import urllib, json, sys
import urllib.request
import csv
import sys
api =sys.argv[1] 
movienumber =0
page =1
data1=[]
while movienumber<300:
    url1 = "https://api.themoviedb.org/3/discover/movie?api_key="+api+"&language=en-US&sort_by=popularity.desc&page="+str(page)+"&with_genres=35&primary_release_date.gte=2000"
    with urllib.request.urlopen(url1) as url:
        data = json.loads(url.read().decode())
        data1 = data1+data["results"]
        movienumber=movienumber+len(data["results"])
        page=page+1
with open('movie_ID_name.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    for i in range(300):
        if data1[i]["original_title"]==data1[i]["title"] and data1[i]["original_language"]=="ru":
            spamwriter.writerow([data1[i]["id"],"russian name"])
        else :
            spamwriter.writerow([data1[i]["id"],data1[i]["title"]])
        

data3=[]
with open('movie_ID_sim_movie_ID.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    for j in range(300):
        url2="https://api.themoviedb.org/3/movie/"+str(data1[j]["id"])+"/similar?api_key="+api+"&language=en-US&page=1"
        with urllib.request.urlopen(url2) as url:
            data = json.loads(url.read().decode())
            data2 = data["results"]
            k=0
            while k<5 and k<len(data2) and k!=j:
                if [min(data1[k]["id"],data1[j]["id"]),max(data1[k]["id"],data1[j]["id"])] not in data3:
                    data3.append([min(data1[j]["id"],data1[k]["id"]),max(data1[j]["id"],data1[k]["id"])])
                    spamwriter.writerow([min(data1[j]["id"],data1[k]["id"]),max(data1[j]["id"],data1[k]["id"])])
                k=k+1
                
