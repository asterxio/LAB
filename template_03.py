"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"

#A]
def status_of(percent):
    """returns OVER LIMIT (100% or more),WARNING (90% or more),or OK"""
    if percent>=100:
        return'OVERLIMIT'
    elif percent>=90:
        return 'WARNING' 
    else:
        return 'OK'
 #B]   
def check(value,limit):
    """calculates difference and percentage then returns it"""
    difference=value-limit
    percentage=value/limit*100
    return difference,limit
#C]
def print_report(label,value,limit,difference,percent,status):
    """prints report"""
print()
print('='*34)
print(f'  RECORD_CHECK - {label}')
print('='*34)
print(f'  {'loaded':<10} : {value:>10.2f}')
print(f'  {'expected':<10} : {limit:>10.2f}')
print(f'  {'difference':<10} : {difference:>10.2f}')
print(f'  {'percent':<10} : {percent:>10.2f}%')
print(f'  {'status':<10} : {status:>10.2f}')



# ==================================================================== INPUT
# 2. Ask for your three values.

over_count=0
while True:
    label=input('dataset name(quit to stop):')
    if label=='quit':
        break
    value=float(input('rows loaded:'))
    value=float(input('rows expected:'))

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.

difference,percent=check(value,limit)
status=status_of(percent)
if status=='OVERLIMIT':
    over_count=over_count+1

# =================================================================== OUTPUT
# 4. Print the report.
print_report(label, value, limit, difference, percent, status)
print()
print('Records came back OVERLIMIT:',over_count)

# ==========================================================================
# 5. Before you finish:
