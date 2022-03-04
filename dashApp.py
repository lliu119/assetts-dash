import requests as rq
import bs4
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_multiple_Olympic_gold_medalists'
page = rq.get(url)
## print out the first 200 characters just to see what it looks like
page.text[0 : 99]
