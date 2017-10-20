from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.conf.urls import url
from accounts import models
import re

# Create your views here.

searchTerm = ''

def searchResults(request):

    # Perhaps it would be better to check the search against a dictionary here before passing it to render. That way,
    # can determine what to render and have another page for a fail or something.
    searchTerm = request.session['searchTerm']

    possibleSearches = ['colleges', 'college', 'libraries', 'library', 'industries', 'industry', 'hotels', 'hotel', 'parks', 'park', 'zoos', 'zoo',
                        'museums', 'museum', 'restaurants', 'restaurant', 'malls', 'mall']


    for word in possibleSearches:
        if word in str.lower(searchTerm):

            context = {
                "searchTerm": word,
            }

            return render(request, 'searchResults.html', context)
    return HttpResponse("<html><body>No results</body></html>")

def index(request):
    curCity = models.City.objects.get(pk=2)

    #This section of code checks for a post method and then saves the search term to be used in the serach results page
    if request.POST:
        if 'item_id' in request.POST:
            for city in models.City.objects.all().values_list('cityName', flat=True):
                if request.POST['item_id'] == city:
                    curCity = models.City.objects.get(cityName=city)
            print(request.POST['item_id'])
        if 'search' in request.POST:

            #Session is a way of storing values to pass from one function to another. This avoids the problem of the script continually executing
            #and overriding values that we wish to store

            request.session['searchTerm'] = request.POST['search']
            return redirect('/results')


    if request.user.is_superuser:
        return redirect('/admin')
    elif request.user.is_authenticated():
        curUserPK = request.user.pk
        curUser = models.UserInfo.objects.get(user_id=curUserPK)
        curUserType = curUser.userTypeID.typeName
        firstName = request.user.first_name
        dropdownItems = models.City.objects.all().values_list('cityName', flat=True)
        links = {
            "restaurants": curCity.restaurantsLink,
            "colleges": curCity.collegesLink,
            "libraries": curCity.librariesLink,
            "industries": curCity.industriesLink,
            "hotels": curCity.hotelsLink,
            "parks": curCity.parksLink,
            "zoos": curCity.zoosLink,
            "museums": curCity.museumsLink,
            "malls": curCity.mallsLink
        }

        # Based on the user type, this dictates what is displayed and what is not in this order:
        # 0. restaurants, 1. colleges, 2. libraries, 3. industries, 4. hotels, 5. parks, 6. zoos, 7. museums, 8. malls
        if curUserType == 'Student':
            toDisplay = [0, 1, 1, 0, 0, 0, 0, 0, 0]
        elif curUserType == 'Businessman':
            toDisplay = [0, 0, 0, 1, 1, 0, 0, 0, 0]
        elif curUserType == 'Tourist':
            toDisplay = [0, 0, 0, 0, 1, 0, 0, 0, 0]



        context = {
            "toDiscplay": toDisplay,
            "links": links,
            "toDisplay": toDisplay,
            "firstName": firstName,
            "dropdownItems": dropdownItems
        }

        return render(request, 'main.html', context)
    return render(request, 'index.html', {})