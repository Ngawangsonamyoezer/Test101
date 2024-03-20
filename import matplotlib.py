import matplotlib.pyplot as plt

# Given data
total_months = 12
dispensers_per_month = 2
cost_per_dispenser = 10000
current_month = 10
dispensers_built_so_far = 20
CPI = 0.9091

# Calculate the planned total number of dispensers
planned_dispensers = total_months * dispensers_per_month

# Calculate the earned value (EV)
EV = dispensers_built_so_far * cost_per_dispenser

# Calculate the planned value (PV)
# Since PV is the cumulative planned cost up to the current month,
# we will use the current month's planned expenditure as PV
PV = current_month * dispensers_per_month * cost_per_dispenser

# Calculate the actual cost (AC)
AC = EV / CPI

# Create a line graph for Earned Value Management
metrics = ["Planned Value (PV)", "Earned Value (EV)", "Actual Cost (AC)"]
costs = [PV, EV, AC]

plt.figure(figsize=(10, 6))
plt.plot(metrics, costs, marker='o', linestyle='-', color='b')
plt.xlabel("Metrics")
plt.ylabel("Cost (Nu.)")
plt.title("Earned Value Management Chart")
plt.grid(axis="y")
plt.show()
