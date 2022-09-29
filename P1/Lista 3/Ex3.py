popA = 80000
popB = 200000
anos = 0

while popA < popB:
    popA = popA + (popA * 3/100)
    popB = popB + (popB * 1.5/100)
    anos = anos + 1

print(f"São necessário {anos} anos para que a população de A ultrapasse a de B.")