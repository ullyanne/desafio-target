import json
import numpy as np

def loadJson(file):
    f = open(file)
    data = json.load(f)
    return data

def revenueOverview(data):
    smallest = np.inf
    biggest = -np.inf
    total_revenue = 0
    day_count = 0

    for dic in data:
        if dic['valor'] != 0:
            day_count += 1

            if dic['valor'] < smallest:
                smallest = dic['valor']
            if dic['valor'] > biggest:
                biggest = dic['valor']
            
            total_revenue += dic['valor']

    mean = total_revenue/day_count

    days_over_revenue_mean = 0

    for dic in data:
        if dic['valor'] != 0:
            if dic['valor'] > mean:
                days_over_revenue_mean += 1

    return {"smallest": smallest, "biggest": biggest, "days_over_revenue_mean": days_over_revenue_mean}

data = loadJson('dados.json')

report = revenueOverview(data)

print(f"O menor valor de faturamento ocorrido foi: {report['smallest']}\nO maior valor de faturamento ocorrido foi: {report['biggest']}\nNúmero de dias no mês em que o valor de faturamento diário foi superior à média mensal: {report['days_over_revenue_mean']}")

