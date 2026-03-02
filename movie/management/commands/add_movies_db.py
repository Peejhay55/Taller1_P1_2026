from django.core.management.base import BaseCommand
from movie.models import Movie
import csv

class Command(BaseCommand):
    help = 'Load movies from movies_initial.csv into the Movie model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the CSV file
        #Recuerde que la consola está ubicada en la carpeta DjangoProjectBase.
        #El path del archivo movie_descriptions con respecto a DjangoProjectBase sería la carpeta anterior
        csv_file_path = 'movies_initial.csv'

        # Load data from the CSV file
        movies_to_create = []

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader: # Iterates correctly over rows
                if count >= 100:
                    break

                # Parse data
                title = row['title']

                # Check duplicates not necessary if DB is cleared, but good practice
                # existing_titles logic removed for simplicity since we want exactly 100 and clean slate?
                # But user said "borrar todas las peliculas" THEN add 100. So we assume clean slate.
                # However, if CSV has duplicates in first 100, we should handle them?
                # Unlikely in top 100 movies list usually.

                # Handle year
                try:
                    year_val = int(row['year'])
                except ValueError:
                    year_val = None # Logic to extract year could be added if needed

                movies_to_create.append(
                    Movie(
                        title=title,
                        image='movie/images/default.jpg',
                        genre=row['genre'],
                        year=year_val,
                        description=row['plot']
                    )
                )
                count += 1

        Movie.objects.bulk_create(movies_to_create)

        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(movies_to_create)} movies to the database'))
