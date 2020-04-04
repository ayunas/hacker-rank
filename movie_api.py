import requests


def  getMovieTitles(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/"

    try:
        res = requests.get(url,params = {'Title' : substr})
        print('success', res.status_code)
        data = res.json()
        movies = [m['Title'] for m in data['data']]
        print(movies)
        movies.sort()
        return movies
    except:
        print('could not get data', res.status_code)



getMovieTitles("spiderman")

