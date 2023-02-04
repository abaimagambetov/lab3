movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

# 1
# def above(s):
#     index = 0
#
#     for i in range(len(movies)):
#         if s == movies[i]['name']:
#             index = i
#             break
#
#     if movies[i]['imdb'] > 5.5:
#         return True
#     else:
#         return False
#
#
# s = input("Enter the name of the movie: ")
# print(above(s))


# 2
# def allabove():
#     for i in range(len(movies)):
#         if movies[i]['imdb'] > 5.5:
#             print(movies[i]['name'])
#
#
# allabove()


# 3
# def category(cat):
#     for i in range(len(movies)):
#         if cat == movies[i]['category']:
#             print(movies[i]['name'])
#
#
# s = input()
# category(s)


# 4
# def averageimdbscore():
#     i = 0
#     cnt = 0
#
#     while i != len(movies):
#         cnt += movies[i]['imdb']
#         i += 1
#
#     print(cnt / i)
#
#
# averageimdbscore()



# 5
# def averagebycategory(cat):
#     j = 0
#     cnt = 0
#
#     for i in range(len(movies)):
#         if cat == movies[i]['category']:
#             cnt += movies[i]['imdb']
#             j += 1
#
#     print(cnt / j)
#
#
# s = input()
# averagebycategory(s)

