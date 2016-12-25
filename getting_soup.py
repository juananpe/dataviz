from bs4 import BeautifulSoup
import requests
import re

BASE_URL = 'http://en.wikipedia.org'
# Wikipedia will reject our request unless we add
# a 'user-agent' attribute to our http header
HEADERS = {'User-Agent':'Mozilla/5.0'}

def get_Nobel_soup():
    """ Return a parsed tag tree of our Nobel prize page """
    # Mae a request to the Nobel page, setting valid headers
    response = requests.get(
            BASE_URL + '/wiki/List_of_Nobel_laureates',
            headers = HEADERS)
    # Return the content of the response parsed by BeautifulSoup
    return BeautifulSoup(response.content, "lxml")

def get_column_titles(table):
    """ Get the Nobel categories from the table header """
    cols = []
    for th in table.select_one('tr').select('th')[1:]:
       link = th.select_one('a')
    # Store the category name and any Wikipedia link it has
       if link:
           cols.append({'name':link.text, 'href':link.attrs['href']})
       else:
         cols.append({'name':th.text, 'href':None})
    return cols


soup = get_Nobel_soup()
table = soup.select_one('table.sortable.wikitable')
table.select('th')

cols = get_column_titles(table);


def get_Nobel_winners(table):
     cols = get_column_titles(table)
     winners = []
     for row in table.select('tr')[1:-1]:
         year = int(re.findall( r'[\d]+' ,row.select_one('td').text)[0]) # gets 1st <td>
         for i, td in enumerate(row.select('td')[1:]):
             for winner in td.select('a'):
                 href = winner.attrs['href']
                 if not href.startswith('#endnote'):
                     winners.append({
                        'year': year,
                        'category': cols[i]['name'],
                        'name':winner.text,
                        'link':winner.attrs['href']
                    })
     return winners

winners = get_Nobel_winners(table)
print winners
