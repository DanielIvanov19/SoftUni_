sum_steps = 0
input_line = input()

while input_line != "Going home":
    steps = int(input_line)
    sum_steps += steps
    if sum_steps >= 10000:
        break
    input_line = input()

if input_line == "Going home":
    steps_to_home = int(input())
    sum_steps += steps_to_home
diff = abs(sum_steps-10000)
if sum_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} over the goal!")
else:
    print(f"{diff} more steps to reach the goal.")