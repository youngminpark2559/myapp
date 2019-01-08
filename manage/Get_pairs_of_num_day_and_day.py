import calendar

# --------------------------------------------------
# Test for March, 2019
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
year="2019"
month="03"
# c start_day: start day of March of 2019 is Friday
start_day="Fri"

# --------------------------------------------------
index_of_start_day=days.index(start_day)
len_days=len(days)

if index_of_start_day!='0':
    # c it_f_f_w: you get iteration for first week
    it_f_f_w=len_days-index_of_start_day

    # c days_of_f_w: you create days of first week
    days_of_f_w=[days[i] for i in range(index_of_start_day,len_days)]

# --------------------------------------------------
# Generate days of all other weeks
# c days_of_a_o_w: you create days of all other weeks
days_of_a_o_w=[]
for i in range(len_days):
    days_of_a_o_w.append(days[i])

days_of_a_o_w=days_of_a_o_w*5
days_of_a_o_w=days_of_a_o_w[:31]
# c days_of_m: days of month
days_of_m=days_of_f_w+days_of_a_o_w
len_days_of_m=len(days_of_m)

# --------------------------------------------------
# Generate number of day
num_d=[]
for i in range(1,10):
    num_d.append("19"+month+"0"+str(i))
for i in range(10,35):
    num_d.append("19"+month+str(i))

len_num_d=len(num_d)

# --------------------------------------------------
# Generate pairs
# c lst_d_m: last day of month
lst_d_m=calendar.monthrange(year=int(year),month=int(month.replace("0","")))[1]
pair=list(zip(num_d,days_of_m))[:lst_d_m]
for one_p in pair:
    num_d=one_p[0]
    day=one_p[1]
    print(num_d+' '+day)

# 190301 Fri
# 190302 Sat
# 190303 Sun
# 190304 Mon
# 190305 Tue
# 190306 Wed
# 190307 Thu
# 190308 Fri
# 190309 Sat
# 190310 Sun
# 190311 Mon
# 190312 Tue
# 190313 Wed
# 190314 Thu
# 190315 Fri
# 190316 Sat
# 190317 Sun
# 190318 Mon
# 190319 Tue
# 190320 Wed
# 190321 Thu
# 190322 Fri
# 190323 Sat
# 190324 Sun
# 190325 Mon
# 190326 Tue
# 190327 Wed
# 190328 Thu
# 190329 Fri
# 190330 Sat
# 190331 Sun
