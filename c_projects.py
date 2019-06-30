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

# diff ... Nice clean way to show additions

print(curr_f)
print("----------")
print(proj1)
print("")
print("")

print(prev_f)
print("----------")
print(proj2)
print("")
print("")

print(type(proj2))

print("Differences?")
print("------------")
difflib.SequenceMatcher(None, curr_f, prev_f) 
