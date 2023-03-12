import requests as rq

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYWZmNDdkZTI1ODZiY2UwYTJhMzQwZjlmYjVlYjgyZiIsInN1YiI6IjY0MGUyYzFjMmEwOWJjMDBjNTJkYjkzMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vgudU3gU5L68h4Dy4L6uuBQt1EQewd-NccXnglvV74o'}

response = rq.get(url='https://api.themoviedb.org/3/movie/11/lists?api_key=eaff47de2586bce0a2a340f9fb5eb82f', headers=headers)

print(response.json())