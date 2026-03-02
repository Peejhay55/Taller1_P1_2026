from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import matplotlib.pyplot as plt
import io
import base64, urllib
import matplotlib


def statistics_view(request):
    matplotlib.use('Agg')
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year = "None"
        count = movies_in_year.count()
        movie_counts_by_year[year] = count

    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_year))

    # Plotting
    plt.figure()
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'statistics.html', {'graphic': graphic})


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def statistics_view_genre(request):
    matplotlib.use('Agg')
    all_genres = Movie.objects.values_list('genre', flat=True).exclude(genre__isnull=True).exclude(genre='')
    movie_counts_by_genre = {}

    for genre in all_genres:
        if genre:
            first_genre = genre.split(',')[0].strip()
            if first_genre:
                movie_counts_by_genre[first_genre] = movie_counts_by_genre.get(first_genre, 0) + 1

    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_genre))
    sorted_genres = sorted(movie_counts_by_genre.keys())
    sorted_counts = [movie_counts_by_genre[genre] for genre in sorted_genres]

    # Plotting
    plt.figure()
    plt.bar(bar_positions, sorted_counts, width=bar_width, align='center')
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, sorted_genres, rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'statistics_genre.html', {'graphic': graphic})


# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie', '')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies, 'name': 'Pablo José Benítez'})


def about(request):
    return render(request, 'about.html')
