import csv
from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    data = list()
    # чтение csv-файла и заполнение контекста
    with open("inflation_russia.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter=';'):
            data.append(row)
    for element in data[0]:
        print(element, end=" ")
    for row in data:
        for element in row.values():
            print(element, end=" ")
        print()

    return render(request, template_name,
                  context={'data': data[0],
                           "data_val": data})
