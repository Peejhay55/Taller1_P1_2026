from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Remove all movies from the database'

    def handle(self, *args, **kwargs):
        count = Movie.objects.all().count()
        Movie.objects.all().delete()
        with open('removed.log', 'w') as f:
            f.write(f'Successfully deleted {count} movies')
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} movies from the database'))


