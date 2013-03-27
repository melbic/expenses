from django.core.management.base import BaseCommand
from projects.models import Project

__author__ = 'dreiMac'


class Command(BaseCommand):
    args = '<count>'
    help= """
            inserts as many projects as specified
          """

    def handle(self, *args, **options):

        for x in range(1, int(args[0])+1):
            project = create_project(x)
            project.save()


def create_project(nr):
    nr_str = str(nr)
    date = '201{0}-1-1'.format(nr_str)
    name = 'Test' + nr_str
    return Project(name=name, start_date=date)