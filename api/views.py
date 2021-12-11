from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from operator import itemgetter
from .weather_data import data_1, data_2, data_3, data_4


# Flight Data [rapidapi.com]
@api_view(['POST'])
def flight_search(request):
    context = {}
    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/cheap"
    querystring = request.data
    destination = querystring['destination']
    print(destination)

    # querystring = {"origin": "DAC", "page": "None", "currency": "USD", "depart_date": "2021-12-10",
    #                "return_date": "2021-12-16", "destination": "DXB"}

    headers = {
        'x-access-token': "2e082d5c4155b4547875293928cb300e",
        'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
        'x-rapidapi-key': "7c1e647c21msh993266fd5386d3dp14cd93jsn5bf2b2a1ef96"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
    return Response(response.json())


# WeatherAPI.com [rapidapi.com]
@api_view(['POST'])
def weather_search(request):
    url = "https://weatherapi-com.p.rapidapi.com/history.json"

    querystring = request.data
    # querystring = {"q": "Dhaka", "dt": "2021-12-04", "lang": "en"}

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "7c1e647c21msh993266fd5386d3dp14cd93jsn5bf2b2a1ef96"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return Response(response.json())


# AeroDataBox [rapidapi.com]
@api_view(['GET'])
def airport_search_by_free_text(request, city):
    # q = request.data['city']
    url = "https://aerodatabox.p.rapidapi.com/airports/search/term"

    querystring = {"q": city, "limit": "5"}

    headers = {
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
        'x-rapidapi-key': "623e200af3mshd4ec1166dcee84ap1a17a4jsn0593d116cf92"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.json())
    return Response(response.json())


@api_view(['GET'])
def airport_data(request):
    context = []
    # Opening JSON file
    f = open('api/new_data.txt', encoding="utf8")
    data = json.load(f)
    for i in data:
        if "Asia/" in i['time_zone']:
            context.append({
                "value": i['code'], 'label': i['name']
            })
    f.close()

    return Response(context)


@api_view(['GET'])
def weather_api_marge_data(request):
    marge_weather_data_list = [data_1, data_2, data_3, data_4]
    lst_two_weather_data = marge_weather_data_list[-2:]
    return Response(lst_two_weather_data)


# Flight Data [rapidapi.com]
@api_view(['POST'])
def flight_search2(request):
    context = {}
    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/cheap"

    if request.data:
        origin = request.data['origin']
        depart_date = request.data['depart_date']
        return_date = request.data['return_date']
        destination = request.data['destination']
        sort = request.data['sort']

        querystring = {"origin": origin, "page": "None", "currency": "USD", "depart_date": depart_date,
                       "return_date": return_date, "destination": destination}

        # {"origin": "DAC", "page": "None", "currency": "USD", "depart_date": "2021-12-12", "return_date": "",
        #  "destination": "DXB", "sort": ""}

        # querystring = {"origin": "DAC", "page": "None", "currency": "USD", "depart_date": "2021-12-12",
        #                "return_date": "", "destination": "DXB"}

        headers = {
            'x-access-token': "2e082d5c4155b4547875293928cb300e",
            'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
            'x-rapidapi-key': "7c1e647c21msh993266fd5386d3dp14cd93jsn5bf2b2a1ef96"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.json()['data'] != {}:
            flight_dic = response.json()['data'][destination]
            flight_list = []
            for k, v in flight_dic.items():
                flight_list.append(v)
            if sort == 'low':
                flight_list = sorted(flight_list, key=itemgetter('price'))
            elif sort == 'high':
                flight_list = sorted(flight_list, key=itemgetter('price'), reverse=True)
            context = {"success": True, "data": flight_list}
            return Response(context)
        else:
            context = {"success": True, "data": []}
            return Response(context)


    else:
        context = {"success": True, "data": []}
        return Response(context)
