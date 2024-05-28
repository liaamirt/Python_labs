import csv

try:
    with open('DataBase.csv', 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')

        print("GDP per capita for Ukraine (1991-2019):")
        for row in reader:
            if row['Country Name'] == 'Ukraine':
                for year in range(1991, 2020):
                    col_name = f"{year} [YR{year}]"
                    print(f"{year}: {row[col_name]}")
                break 

    with open('DataBase.csv', 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        data = list(reader) 

    gdp_values = [float(data[0][f"{year} [YR{year}]"]) for year in range(1991, 2020)]

    min_gdp = min(gdp_values)
    max_gdp = max(gdp_values)

    print(f"\nMin GDP per capita: {min_gdp}")
    print(f"Max GDP per capita: {max_gdp}")

    with open('GDP_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Statistic", "Value"])
        writer.writerow(["Min GDP per capita", min_gdp])
        writer.writerow(["Max GDP per capita", max_gdp])

except FileNotFoundError:
    print("File 'DataBase.csv' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
