import random

tickets =[{'name':"Достучаться до Небес",
        'time':"21:00",
        'user_id':1,
        'room':8,
        "place": 5,
        'row': 2},
          {'name':"Кухня в париже",
        'time':"18:00",
'user_id':1,
        'room':1,
        "place": 1,
        'row': 1},
          {'name':"Я Медведь",
        'time':"",
'user_id':1,
        'room':1,
        "place": 1,
        'row': 1},
          {'name':"",
        'time':"",
'user_id':1,
        'room':1,
        "place": 1,
        'row': 1},
          {'name':"",
'user_id':1,
        'time':"",
        'room':1,
        "place": 1,
        'row': 1}]


films = [{'id':1,
          'name':"Достучаться до Небес",
          'time_id':1},
{'id': 2,
          'name': "Кухня в париже",
          "time_id":2}]

times = [{'id':1,
          'name':"11:00",
          'room_id':1
         },
         {"id":2,
          "name":"12:30",
          "room_id":2}]
places=[{'room_id':1,
        'row':5,
        'place':list(range(1,11))
         },{'room_id':1,
        'row':4,
        'place':list(range(1,11))
         },{'room_id':1,
        'row':3,
        'place':list(range(1,11))
         },{'room_id':1,
        'row':2,
        'place':list(range(1,11))
         },{'room_id':1,
        'row':1,
        'place':list(range(1,11))
         },{'room_id':2,
        'row':5,
        'place':list(range(1,11))
         },{'room_id':2,
        'row':4,
        'place':list(range(1,11))
         },{'room_id':2,
        'row':3,
        'place':list(range(1,11))
         },{'room_id':2,
        'row':2,
        'place':list(range(1,11))
         },{'room_id':2,
        'row':1,
        'place':list(range(1,11))
         }
        ]

for film in films:
    print(f"{film['name']}")
value_film_name=input("Film is ")

film_is_input = False
for film in films:
    if value_film_name == film['name']:
        for time in times:
            if time['id']==film['time_id']:
                print(time['name'])
                film_is_input=True
if film_is_input:
    place_is_input=False
    value_time = input("Input time ")
    for time in times:
        if time['name'] == value_time:
            print("Free places ")
            for place in places:
                if place['room_id']==time['room_id']:
                    print(f"{place['place']}")
                    place_is_input=True
    if place_is_input:
        input_row = input("Row is ")
        input_place = input("Place is ")
        for row in places:
            if input_place.isdigit():
                if str(row['row']) == input_row and input_place in row['place']:
                    print(f"Your row is {input_row}\n Your place is {input_place}")
                else:
                    print(str(row['row']))
                    print(row['place'])

