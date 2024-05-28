import pandas as pd
import matplotlib.pyplot as plt
import calendar

plt.style.use("ggplot") 

cycle_track_df = pd.read_csv("comptagevelo2017.csv", sep=',', parse_dates=['Date'], dayfirst=True,  index_col='Date')

cycle_track_df = cycle_track_df.apply(pd.to_numeric, errors='coerce')

cycle_track_df.drop(columns=['Unnamed: 1'], inplace=True)

monthly_sum = cycle_track_df.resample('ME').sum()

max_monthly_usage = monthly_sum.max().max()

max_month_index = monthly_sum.idxmax().iloc[0].month
max_month_name = calendar.month_name[max_month_index]

print("Максимальна кількість використань трас за місяць = ", max_monthly_usage)
print("Найбільш популярний у велосипедистів місяць: ", max_month_name)
print("Використання по доріжках в ", max_month_name, "\n", monthly_sum.max())

cycle_track_df.plot(figsize=(15, 10), title="Використання велодоріжок за рік")
plt.ylabel("Кількість використань", color="black")
plt.show()
