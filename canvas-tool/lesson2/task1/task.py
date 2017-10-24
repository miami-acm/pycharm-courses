from canvasapi import Canvas

api_url = 'https://miamioh.instructure.com/api/v1/'
api_key = 'TODO: Your token here'

canvas = Canvas(api_url, api_key)
for course in canvas.get_courses():
    print(course)
