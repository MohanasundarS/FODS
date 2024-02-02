items=[6,5,10,2]
q=[3,2,4,1]
discount=10
tax=8
total=0
for i in range(0,4):
    total=total+(items[i]*q[i])
print(total)
dis=(discount/100)*total
after_dis=total-dis
tax_amt=(tax/100)*after_dis
total_after_tax=after_dis+tax_amt
print(total_after_tax)
print(after_dis)
