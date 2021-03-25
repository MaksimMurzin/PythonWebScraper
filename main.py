#importin Indeed Python API module
from indeed import IndeedClient

client = IndeedClient(publisher=12254335 )  # we'll do this later

parameters = {
              'q' : "python developer",
              'l' : "London, GB",
              'sort' : "date",
              'fromage' : "5",
              'limit' : "25",
              'filter' : "1",
              'userip' : "192.186.176.550:60409",
              'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
             }

# our main search function

def get_offers(params):
    # perform search
    search_results = client.search(**params) # we want this to be a dictionary

# loop through each offer element
    for elm in search_results['results']:
        offer = (elm['jobtitle'],
                 elm['formattedLocation'],
                 elm['snippet'],
                 elm['url'],
                 elm['indeedApply'],
                 elm['jobkey'],
                 elm['date'])

