def number(bus_stops):
    sum = 0 
    no_of_people = 0
    for item in bus_stops:
        sum = item[0]-item[1]
        no_of_people += sum
    return no_of_people
