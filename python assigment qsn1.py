'''1.	Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. if they want to travel three hundred miles or more tell them to drive Super-Car'''


distance=int(input("enter the distance that is to be travelled: "))
if(distance<3):
    print("Use bicycle")
elif(distance>=3 and distance<300):
    print("Use motorcycle")
else:
    print("Use super car")

