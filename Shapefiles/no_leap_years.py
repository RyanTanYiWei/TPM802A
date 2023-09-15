idx_no_leap_years = [np.where(datelist.is_leap_year == False)][0][0]
flow_no_leap_years = [flow[date] for date in idx_no_leap_years]
dates_no_leap_years = [dates[date] for date in idx_no_leap_years]

n_years = int(len(flow_no_leap_years)/365)
n_months = 12
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthly_flow = []
year_stamp = []
for year in range(n_years):
  start = year * 365
  month = 0
  while month < n_months:
    finish = int(start + days_per_month[month])
    year_stamp.append(dates_no_leap_years[finish-1].year)
    monthly_flow.append(np.sum(flow_no_leap_years[start:finish]))
    start += days_per_month[month]
    month += 1

n_years = len(monthly_flow)//12
monthly_flows_reshaped = np.reshape(monthly_flow, (n_years, 12)).T
monthly_flows_mean=np.mean(monthly_flows_reshaped, axis=1)
monthly_flows_min=np.min(monthly_flows_reshaped, axis=1)
monthly_flows_max=np.max(monthly_flows_reshaped, axis=1)

plt.plot(monthly_flows_mean)
plt.plot(monthly_flows_max)
plt.plot(monthly_flows_min)
plt.ylabel('Streamflow (cfs)', fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(ticks=range(12), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.show()