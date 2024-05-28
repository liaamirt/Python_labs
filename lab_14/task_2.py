import os
import csv
import matplotlib.pyplot as plt

def read_data_from_csv(file_name):
    years = []
    ukraine_data = []
    canada_data = []

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['Country Name'] != '':
                years = [int(year.split()[0]) for year in row.keys() if year != 'Country Name' and year != 'Country Code' and year != 'Series Name' and year != 'Series Code']
                
                if row['Country Name'] == 'Ukraine':
                    ukraine_data = [int(row[year]) for year in row.keys() if year != 'Country Name' and year != 'Country Code' and year != 'Series Name' and year != 'Series Code']
                elif row['Country Name'] == 'Canada':
                    canada_data = [int(row[year]) for year in row.keys() if year != 'Country Name' and year != 'Country Code' and year != 'Series Name' and year != 'Series Code']
    
    return years, ukraine_data, canada_data

def plot_population_dynamics(years, data1, data2, country1, country2):
    plt.plot(years, data1, label=country1, color='purple')
    plt.plot(years, data2, label=country2, color='yellow')
    plt.title('Population ages 0-14, male')
    plt.xlabel('Year', color = 'b')
    plt.ylabel('Population', color = 'b')
    plt.legend()
    plt.grid(True)
    plt.ticklabel_format(style='plain', axis='y')  
    plt.show()

def plot_country_data(years, data, country):
    plt.bar(years, data, color='darkgreen')
    plt.title(f'Population ages 0-14, male in {country}')
    plt.xlabel('Year', color = 'b')
    plt.ylabel('Population', color = 'b')
    plt.ticklabel_format(style='plain', axis='y') 
    plt.show()

def main_menu():
    os.system('cls')
    print("1. Побудувати графік динаміки популяції для України та Канади")
    print("2. Побудувати графік динаміки популяції для окремої країни")
    print("q. Вийти")

def country_submenu():
    os.system('cls')
    print("1. Україна")
    print("2. Канада")
    print("3. Повернутись назад")

def main():
    file_name = 'DataBase.csv'
    while True:
        main_menu()
        choice = input("Оберіть опцію: ")
        
        if choice == '1':
            os.system('cls')
            years, ukraine_data, canada_data = read_data_from_csv(file_name)
            plot_population_dynamics(years, ukraine_data, canada_data, 'Ukraine', 'Canada')
        elif choice == '2':
            while True:
                country_submenu()
                country_choice = input("Оберіть країну: ")
                
                if country_choice == '1':
                    os.system('cls')
                    years, ukraine_data, _ = read_data_from_csv(file_name)
                    plot_country_data(years, ukraine_data, 'Ukraine')
                elif country_choice == '2':
                    os.system('cls')
                    years, _, canada_data = read_data_from_csv(file_name)
                    plot_country_data(years, canada_data, 'Canada')
                elif country_choice == '3':
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")
        elif choice.lower() == 'q':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

