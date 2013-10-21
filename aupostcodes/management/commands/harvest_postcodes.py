"""
Import postal area data from the Australia Post csv of same.

At time of writing, this was available at 
http://auspost.com.au/static/docs/pc-full_20110905.csv
or from http://auspost.com.au/apps/postcode.html.
"""

from django.core.management.base import AppCommand
import csv
import sys
import os
from aupostcodes.models import AUPostalArea, AUPostCode

class Command(AppCommand):
    args = '<csv_filename>'
    help = """Harvests Australian postcode data from csv file supplied by Australia Post"""


    def handle(self, *args, **options):
        for csv_filename in args:
            try:
                n = 0
                here = os.path.dirname(__file__)
                file_path = os.path.join(here, '../../data/', csv_filename)
                reader = csv.reader(open(file_path, 'U'))
                reader.next() # skip headers
            except Exception:
                raise

            for line in reader:
                postcode, locality, state = line[:3]
                au_postcode, created = AUPostCode.objects.get_or_create(postcode=postcode)
                au_postal_area = AUPostalArea(postcode=au_postcode, locality=locality, state=state)
                au_postal_area.save()
                n += 1
                if n % 100 == 0:
                    print "Processed %s postcodes." % n
