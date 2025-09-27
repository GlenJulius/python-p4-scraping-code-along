import sys
sys.path.append('lib')

from Scraper import Scraper

# Create a scraper instance and print courses
scraper = Scraper()
scraper.print_courses()