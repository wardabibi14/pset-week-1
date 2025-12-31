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
