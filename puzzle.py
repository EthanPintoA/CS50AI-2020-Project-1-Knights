from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

A_says = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Biconditional(AKnight, A_says),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

A_says = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Biconditional(AKnight, A_says),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

A_says = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_says = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Biconditional(AKnight, A_says),
    Biconditional(BKnight, B_says),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# You don't know exactly what A says, so you can't use the sentence

# If A is a knight, then what B says that A said should be true
# If A is a knave, then what B says that A said should be false
B_says1 = Biconditional(AKnight, AKnave)
B_says2 = CKnave
C_says = AKnight
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Biconditional(BKnight, B_says1),
    Biconditional(BKnight, B_says2),
    Biconditional(CKnight, C_says),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
