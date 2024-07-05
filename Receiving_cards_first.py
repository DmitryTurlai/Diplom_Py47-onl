from deuces import Card

def Choose():
    board = [Card.new('2h'), Card.new('3d'), Card.new('5s'), Card.new('9c'), Card.new('Kd')]
    hand = [Card.new('Ah'), Card.new('Ad')]
    return board, hand
