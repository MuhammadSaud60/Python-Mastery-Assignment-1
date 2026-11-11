import csv


with open('results.csv', 'r', newline='', encoding='utf-8') as results_file:
    results = list(csv.DictReader(results_file))

if not results:
    raise ValueError('results.csv does not contain any student results.')

topper = max(results, key=lambda result: float(result['average']))
print(f"Topper: {topper['name']} with an average of {float(topper['average']):.2f}")
