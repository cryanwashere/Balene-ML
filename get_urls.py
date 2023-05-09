import requests

urls = []

def get_wikipedia_urls(search_term, num_urls):
    # Set up the API endpoint
    api_url = 'https://en.wikipedia.org/w/api.php'

    # Set the parameters for the API request
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': search_term,
        'srprop': '',
        'sroffset': 0,
        'srlimit': num_urls
    }

    # Send the API request
    response = requests.get(api_url, params=params)
    data = response.json()

    #print(data)

    
    if 'query' in data and 'search' in data['query']:
        for result in data['query']['search']:
            if 'title' in result:
                title = result['title']
                url = 'https://en.wikipedia.org/wiki/' + title.replace(' ', '_')
                urls.append(url)





get_wikipedia_urls("sharks", 10)
get_wikipedia_urls("machine learning", 10)


with open("urls.txt","w") as f:
    f.write("\n".join(urls))
