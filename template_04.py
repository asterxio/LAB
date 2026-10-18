"""
RECORD CHECK  -  my version
===========================

Name  : sheza parkar
Lane  :  AI
Date  :9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

#A]
def load_records(path):
    """Loads dataset records from a file."""
    records = []
    with open(path) as file:
        for line in file:
         label,value,limit=line.strip().split(",")
        records.append({"label":label,"value":float(value),"limit":float(limit)})
    return records

def check_record(value,limit):
    """Calculates the difference and percentage then returns it"""
    difference=value-limit
    percent=value/limit*100
    return difference,percent

#B]
def status_of(percent):
    """Returns status of dataset"""
    if percent>=100:
        return "OVERLIMIT"
    elif percent>=90:
        return"WARNING"
    else:
        return"OK"

#C]
def print_report(label, value, limit, difference, percent, status):
    """Prints the record report."""
    print()
    print('=' * 34)
    print(f"  RECORD_CHECK - {label}")
    print('=' * 34)
    print(f"  {'loaded':<10} : {value:>10.2f}")
    print(f"  {'expected':<10} : {limit:>10.2f}")
    print(f"  {'difference':<10} : {difference:>10.2f}")
    print(f"  {'percent':<10} : {percent:>10.2f}%")
    print(f"  {'status':<10} : {status:>10}")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
def load_records(path):
    """Loads dataset records from a file."""
    records = []
    with open(path) as file:
        for line in file:
         label,value,limit=line.strip().split(",")
        records.append({"label":label,"value":float(value),"limit":float(limit)})
    return records
try:
 records=load_records("datasets.txt")
except FileNotFoundError:
    records=[]

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.
over_count = 0

with open("results.txt","w") as file:
    for record in records:
        label=record["label"]
        value=record["value"]
        limit=record["limit"]

        if limit == 0:
            print("rows cannot be zero:",label)
            continue
        difference,percent=check_record(value,limit)
        status=status_of(percent)
        if status == "OVERLIMIT":
            over_count=over_count+1

        print_report(label,value,limit,difference,percent,status)
        print(label+","+status,file=file)


print()
print("Datasets marked OVERLIMIT:",over_count)
print("Results saved in results.txt")

# ==========================================================================