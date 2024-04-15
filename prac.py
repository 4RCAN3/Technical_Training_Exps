Xknight, Yknight = list(map(int, input('Moves of knight: ').split(',')))
Xking, Yking = list(map(int, input('Position of king: ').split(',')))
Xqueen, Yqueen =  list(map(int, input('Position of queen: ').split(',')))

reverse_set = [(Xknight, Yknight), (Yknight, Xknight)]

queen_poss = set()
king_pos = set()

for i in reverse_set:
    queen_poss.add((Xqueen - Xknight, Yqueen - Yknight))
    queen_poss.add((Xqueen - Yknight, Yqueen - Xknight))
    queen_poss.add((Xqueen + Xknight, Yqueen + Yknight))
    queen_poss.add((Xqueen + Yknight, Yqueen + Xknight))

    queen_poss.add((Xqueen + Xknight, Yqueen - Yknight))
    queen_poss.add((Xqueen + Yknight, Yqueen - Xknight))
    queen_poss.add((Xqueen - Xknight, Yqueen + Yknight))
    queen_poss.add((Xqueen - Yknight, Yqueen + Xknight))

    king_pos.add((Xking - Xknight, Yking - Yknight))
    king_pos.add((Xking - Yknight, Yking - Xknight))
    king_pos.add((Xking + Xknight, Yking + Yknight))
    king_pos.add((Xking + Yknight, Yking + Xknight))

    king_pos.add((Xking + Xknight, Yking - Yknight))
    king_pos.add((Xking + Yknight, Yking - Xknight))
    king_pos.add((Xking - Xknight, Yking + Yknight))
    king_pos.add((Xking - Yknight, Yking + Xknight))

common = queen_poss.intersection(king_pos)
print(common)
print(len(common))
