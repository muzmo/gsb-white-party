import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader
import models

#('timestamp', lambda x: datetime.datetime.strptime(x, '%m/%d/%Y %H:%M:%S').date())

class ListingLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Loader',
                                   [('username', lambda x: x.decode('utf-8')),
                                    ('name', lambda x: x.decode('utf-8')),
                                    ('year', lambda x: x.decode('utf-8')),
                                    ('section', int),
                                    ('title', lambda x: x.decode('utf-8')),
                                    ('category', lambda x: x.decode('utf-8')),
                                    ('description', lambda x: x.decode('utf-8')),
                                    ('participant_count', lambda x: x.decode('utf-8')),
                                    ('donor_list', lambda x: x.decode('utf-8')),
                                    ('email', lambda x: x.decode('utf-8')),
                                    ('opening_bid', int),
                                   ])

loaders = [ListingLoader]