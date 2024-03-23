
# Read in the times for swimming, cycling, and running.
swimming = float(input("Enter the swimming time in minutes: "))
cycling = float(input("Enter the cycling time in minutes: "))
running = float(input("Enter the running time in minutes: "))

# Calculate and display the total time.
total_time = swimming + cycling + running
print(f"Total time taken to complete the triathlon: {total_time} minutes")

# Determine and display the award based on the total time.
if total_time <= 100:
    print("Award: Provincial colours")
elif 101 <= total_time <= 105:
    print("Award: Provincial half colours")
elif 106 <= total_time <= 110:
    print("Award: Provincial scroll")
else:
    print("Award: No award")
