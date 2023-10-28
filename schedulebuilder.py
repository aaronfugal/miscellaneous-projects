import random

am_shift_capacity = 5
pm_shift_capacity = 5

# Step 1: Gather employee names
num_employees = 15
employee_names = []

for i in range(num_employees):
    employee_name = input(f"Enter the name of employee {i + 1}: ")
    employee_names.append(employee_name)

# Step 2: Generate a random schedule from Sunday to Saturday
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
schedule = {day: {"AM": [], "PM": []} for day in days_of_week}

def assign_shift(employee, day, shift):
    if employee in employee_names:
        schedule[day][shift].append(employee)
        return True
    return False

for day in days_of_week:
    for _ in range(am_shift_capacity):
        random.shuffle(employee_names)
        for employee in employee_names:
            if assign_shift(employee, day, "AM"):
                break
    
    for _ in range(pm_shift_capacity):
        random.shuffle(employee_names)
        for employee in employee_names:
            if assign_shift(employee, day, "PM"):
                break

# Step 3: Display the randomly generated schedule
for day in days_of_week:
    print(day)
    print("AM Shift:", schedule[day]["AM"])
    print("PM Shift:", schedule[day]["PM"])
    print("=" * 30)
