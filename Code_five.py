def puzzle(heads, legs):

    ns='No solutions!'
    for i in range(1,heads+1):
        j=heads-i
        if (2*i)+(4*j)==legs:
            return i,j
    return ns,ns

heads=35
legs=94

result = puzzle(heads,legs)
print(result)