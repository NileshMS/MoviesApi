import json
from django.contrib.messages import error
from django.http import HttpResponse
from django.shortcuts import render
from MoviesApi.settings import MOVIES_API_FILE


def dict_data():
    dict_data = json.loads(open(MOVIES_API_FILE).read())
    titles = [x['title'][0:len(x['title']) - 1] for x in dict_data if
              x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    trailer_links = [x['trailer']['link'] for x in dict_data if
                     x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                         'plot'] != '']
    ratings = [x['rating'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    plots = [x['plot'] for x in dict_data if
             x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                 'plot'] != '']

    # print(titles)
    # print(len(ratings))
    # print(len(posters))

    context = [{'title': title, 'poster': poster, 'rating': rating, 'plot': plot, 'trailer': trailer} for
               title, poster, rating, plot, trailer in zip(titles, posters, ratings, plots, trailer_links)]
    return context


# Create your views here.
def index(request):
    context = dict_data()
    return render(request, 'index.html', {'data': context})


def searchMovie(request):
    name = request.GET.get('movieName')
    context = dict_data()
    # print(name)
    # print(context)

    for x in context:
        if x['title'] == name:
            print(x)
            return render(request, 'searched_movie.html', {'searched_movie':x})
    else:
        error(request, 'enter another movie name')
        return HttpResponse('Please Enter Correct Movie Name Or Movie is Not present')
