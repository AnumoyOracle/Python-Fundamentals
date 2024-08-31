import requests

def get_weather_records(region, keyword):
    base_url = "https://jsonmock.hackerrank.com/api/countries/search"
    page = 1
    records = []

    while True:
        url = f"{base_url}?region={region}&name={keyword}&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_pages = data['total_pages']
            records.extend(data['data'])

            if page >= total_pages:
                break 

            page += 1
        else:
            break    

    return records    


records = get_weather_records('asia', 'ind')
for record in records:
    print(record)
    print()
