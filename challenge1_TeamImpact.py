#Brute force approach
def TeamImpact(contributions):
    impact = []
    n = len(contributions)
    for i in range(n):
        product = 1
        for j in range(n):
            if i!=j:
                product *= contributions[j]
        impact.append(product)
    return impact 
contributions = list(map(int, input("contributions = ").split()))
print(TeamImpact(contributions))