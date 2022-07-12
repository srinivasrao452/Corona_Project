
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse

def Corona_Report_View(request):
    header_object = {
            "X-RapidAPI-Key" : "9b4bedcab6msh2c1240717443f8fp11615djsn53a12af71802",
            "X-RapidAPI-Host" : "corona-virus-world-and-india-data.p.rapidapi.com"
        }
    response = requests.get(
        url="https://corona-virus-world-and-india-data.p.rapidapi.com/api",
        headers=header_object
    )
    # print(response.text)

    if response.status_code==200:
        data = json.loads(response.text)
        print(data["countries_stat"])
        context = {
            "data" : data,
            "object_list" : data["countries_stat"][:10]
        }
        return render(request, 'getCountryData.html', context)
    else:
        print("Status Code is : ", response.status_code)
        context = {
            "error" : "Requested information not available"
        }
        return render(request, 'getCountryData.html', context)

        # return HttpResponse("Requested information not available")