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





terms = [
    "sharks",
    "machine learning",
    "how to make a website",
    "how to use Google Search",
    "what is the weather like today",
    "how to lose weight",
    "how to cook a chicken",
    "how to change a tire",
    "how to fix a leaky faucet",
    "how to write a book",
    "how to start a business",
    "how to learn a new language",
    "how to get a job",
    "how to make friends",
    "how to find love",
    "how to be happy",
    "how to be healthy",
    "how to be wealthy",
    "how to travel the world",
    "how to make a difference in the world",
    "how to leave a legacy",
    'apple',
    'banana',
    'cat',
    'dog',
    'elephant',
    'flower',
    'guitar',
    'house',
    'ice cream',
    'jungle',
    'koala',
    'lion',
    'mountain',
    'nature',
    'ocean',
    'piano',
    'queen',
    'rainbow',
    'sun',
    'tree',
]
for term in terms:
    get_wikipedia_urls(term, 1)


with open("urls.txt","w") as f:
    f.write("\n".join(urls))
