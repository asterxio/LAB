RECORD CHECK  -  my version
===========================

Name  :Sheza Parkar
Lane  :Ai & Data Science
Date  :2/10/2026

Run it:   python template.py

# ==================================================================== INPUT
# 1. Ask for your three values.
overlimit_count=0
checked=0

while True:
 label = input('enter dataset:')
 if label=='quit':                         
     break

value =float(input('enter rows loaded:'))
limit =float(input('enter rows expected'))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
difference=limit-value
percent=(value/limit)*100
# 3. Decide a status and store it in a variable called status.
if percent>=100:
  status='overlimit'
  if value > limit:
   overlimit_count+=1
  checked += 1
elif percent>=90:
  status='warning'
else:
  status='ok'
  checked+=1



# =================================================================== OUTPUT
# 4. Print the report.


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f'loaded    :   {value:7.2f}')
print(f'expected  :   {limit:7.2f}')
print(f'remaining :   {difference:7.2f}')
print(f'percent   :   {percent:7.2f}%')
print(f'status    :    {status:>7}')
print("=" * 34)


print()
print(f'{overlimit_count} of {checked} were over limit')




# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
