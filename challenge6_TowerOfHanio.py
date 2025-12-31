#brute-force approach 
def towerOfHanoiBrute(N, from_rod, to_rod, aux_rod):
    moves = []

    def moveDisks(n, frm, to, aux):
        if n == 0:
            return
        moveDisks(n - 1, frm, aux, to)
        moves.append(f"Disk {n} moved from {frm} to {to}")
        moveDisks(n - 1, aux, to, frm)

    moveDisks(N, from_rod, to_rod, aux_rod)
    return moves

N = int(input("Enter number of disks: "))
result = towerOfHanoiBrute(N, 'A', 'C', 'B')

for move in result:
    print(move)


#Optimized approach
def towerOfHanoiOptimized(N, from_rod, to_rod, aux_rod):
    if N == 0:
        return
    towerOfHanoiOptimized(N - 1, from_rod, aux_rod, to_rod)
    print(f"Disk {N} moved from {from_rod} to {to_rod}")
    towerOfHanoiOptimized(N - 1, aux_rod, to_rod, from_rod)


N = int(input("Enter number of disks: "))

towerOfHanoiOptimized(N, 'A', 'C', 'B')

