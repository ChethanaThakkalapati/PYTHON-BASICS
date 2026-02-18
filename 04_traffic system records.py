'''A traffic system records the average speed of vehicles every hour for 12 hours.
Write a program that: Reads 12 speed values (floats). Calculates the average speed. Displays whether traffic flow was “Slow” (avg < 40), “Normal” (40–80), or “Fast” (avg > 80).
Concepts: list input, loop, conditional check, average calculation.'''

# Program to record and analyze speeds over 12 hours

speeds = [12]   

print("Enter the speed of vehicles for each of the 12 hours:")

for i in range(12):
    speed = int(input(f"Hour {i+1} speed: "))
    speeds.append(speed)


average_speed = int(sum(speeds) / 12)


if average_speed < 40:
    flow = "Slow"
elif 40 <= average_speed <= 80:
    flow = "Normal"
else:
    flow = "Fast"


print("Traffic Report ")
print("Average Speed:", average_speed)
print("Traffic Flow:", flow)

