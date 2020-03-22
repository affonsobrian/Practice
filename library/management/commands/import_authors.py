from django.core.management.base import BaseCommand

from library.models import Author


class Command(BaseCommand):
    help = 'This command imports authors from csv to database'

    def clear_string(self, value):
        return value.replace('\n', '').strip(' ')

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'r') as f:
            for i, name in enumerate(f.readlines()):
                if i == 0:
                    continue
                author = Author(name=self.clear_string(name))
                author.save()



