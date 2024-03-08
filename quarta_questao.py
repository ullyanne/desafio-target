monthly_revenue = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

monthly_revenue_percentage = {}

total = sum(monthly_revenue.values())

for key, value in monthly_revenue.items():
    percentage = value/total * 100
    monthly_revenue_percentage[key] = percentage
    print(f'Percentual da distribuidora {key}: {percentage:.2f}%')