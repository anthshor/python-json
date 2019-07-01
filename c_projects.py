import datetime
import difflib

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day

curr_f = "project_list_" + today.strftime("%Y-%m-%d")
prev_f = "project_list_" + yesterday.strftime("%Y-%m-%d")

f1 = open(curr_f,'r')
proj1 = f1.read()
f1.close()

f2 = open(prev_f,'r')
proj2 = f2.read()
f2.close()

print("Comparing")

for line in difflib.unified_diff(proj2.strip().splitlines(), proj1.strip().splitlines(), fromfile=prev_f, tofile=curr_f,lineterm='', n=0):
    print(line)