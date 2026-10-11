"""
RECORD CHECK  -  my version
===========================

Name  : Sheza Parkar
Lane  :  AI
Date  :9/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
def status_of(percent):
    """gives overlimit,warning,ok from percent"""
    if percent>=100:
        return'overlimit'
    elif percent>=90:
        return'warning'
    else:
        return'ok'
def check(value,limit):
    """calculates and returns difference and percentage"""
    difference=limit-value
    percent=value/limit*100
    return difference,percent
def print_report(label, value, limit, difference, percent, status):
    """Prints report"""
    print()
    print("=" * 34)
    print(f" record check - {label}")
    print("=" * 34)
    print(f" {'loaded':<10} : {value:>10.2f}")
    print(f" {'expected':<10} : {limit:>10.2f}")
    print(f" {'missing':<10} : {difference:>10.2f}")
    print(f" {'percent':<10} : {percent:>10.2f} %")
    print(f" {'status':<10} : {status:>10}")
    print("=" * 34)

# ==================================================================== INPUT
# 2. Ask for your three values.
while True:
    label = input("dataset name (type quit to stop): ")
    if label == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))


# ================================================================== PROCESS
difference,percent = check(value, limit)
status = status_of(percent)

if status == "over limit":
 over_count=over_count+1



# =================================================================== OUTPUT
print_report(label,value,limit,difference,percent,status)
print()
print('records came over limit:',over_count)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
