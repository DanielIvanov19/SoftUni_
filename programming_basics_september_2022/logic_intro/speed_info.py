speed = int(input())

if speed <= 10:
    print("slow")
elif speed > 10 and speed <= 50:
    print("average")
elif speed > 50 and speed <=1000:
    print("fast")
elif speed > 150 and speed <=1000:
    print("ultra fast")
else:
    print("extremely fast")