# 1yr = 52 wks = 12 months

yr_old = input("Enter your age\n")

yr_life_wk= 52*90
yr_life_month = 12*90

pass_yr_wk = int(yr_old) * 52
pass_yr_month = int(yr_old) * 12

left_wk = yr_life_wk - pass_yr_wk
left_month = yr_life_month - pass_yr_month
print(f"Your life in Week is {left_wk}\n Your life in Months is {left_month}")

quit()