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



#optimizd approach
def team_impact_optimized(contributions):
    n = len(contributions)
    impact = [1] * n
    left_product = 1
    for i in range(n):
        impact[i] = left_product
        left_product *= contributions[i]
    right_product = 1
    for i in reversed(range(n)):
        impact[i] *= right_product
        right_product *= contributions[i]
    
    return impact
contributions = list(map(int, input("contributions = ").split()))
print(TeamImpact(contributions))
