temperatures = []

for i in range(5):
    temp = float(input(f"Enter temperature #{i+1}: "))
    temperatures.append(temp)

high_temp = max(temperatures)
low_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

print(f"Highest temperature: {high_temp}")
print(f"Lowest temperature: {low_temp}")
print(f"Average temperature: {avg_temp}")