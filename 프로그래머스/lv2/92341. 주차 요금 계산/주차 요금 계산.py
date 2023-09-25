import math

def getfee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    parking = dict()
    cars = dict()
    answer = []
    for record in records:
        time, num, cmd = record.split()
        hour, minute = time.split(":")
        tmp = int(hour)*60 + int(minute)
        if cmd == "IN":
            parking[num] = tmp
        else:
            if num in cars.keys():
                cars[num] += tmp - parking[num]
            else:
                cars[num] = tmp - parking[num]
            del parking[num]
    end = 23*60+59
    for num, minutes in parking.items():
        if num in cars.keys():
            cars[num] += end - minutes
        else:
            cars[num] = end - minutes
    
    car_list = sorted(list(cars.items()))
    for num,minutes in car_list:
        answer.append(getfee(minutes, fees))
    
    return answer