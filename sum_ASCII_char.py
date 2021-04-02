n = int(input("Enter the number of lines: "))
total_sum=0
for i in range(0 , n):
    letter = str(input())
    if letter == "A":
        total_sum = total_sum + 65
    elif letter == "B":
        total_sum = total_sum + 66
    elif letter == "C":
        total_sum = total_sum + 67
    elif letter == "D":
        total_sum = total_sum + 68
    elif letter == "E":
        total_sum = total_sum + 69
    elif letter == "F":
        total_sum = total_sum + 70
    elif letter == "G":
        total_sum = total_sum + 71
    elif letter == "H":
        total_sum = total_sum + 72
    elif letter == "b":
        total_sum = total_sum + 98
    elif letter =="d":
        total_sum = total_sum + 100

print(f"The sum equals: {total_sum}")