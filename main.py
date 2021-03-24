# 1yr = 52 wks = 12 months

yr_old = input("Enter your age\n")

yr_life_wk= 52*90
yr_life_month = 12*90

# age_as_int = 90 - int(yr_old)  remaining_yr_wk = age_as_int * 52 is better to short cut


pass_yr_wk = int(yr_old) * 52
pass_yr_month = int(yr_old) * 12
pass_yr_day = int(yr_old) * 365


left_wk = yr_life_wk - pass_yr_wk
left_month = yr_life_month - pass_yr_month
left_day = (90 * 365) - pass_yr_day
print(f"Your life in days is {left_day}\n Your life in Weeks is {left_wk}\n Your life in Months is {left_month}\n")

quit()