microwave_power_kw = 1.3
hours_per_day = 2
days_per_month = 30
electricity_price_per_kwh = 0.15
monthly_cost = (microwave_power_kw * hours_per_day * days_per_month * electricity_price_per_kwh)
monthly_consumption = (microwave_power_kw * hours_per_day * days_per_month)

print("Monthly cost (EUR):", monthly_cost)
print("Monthly consumption (kWh):", monthly_consumption)

print(f"{monthly_cost:.1f} €")
print(f"{monthly_consumption:.1f} kWh")