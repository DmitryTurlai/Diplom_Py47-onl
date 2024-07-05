from deuces import Card, Evaluator
from Receiving_cards_first import Choose

# Создание карт на борде и в руке
board, hand = Choose()

# Создание оценщика
evaluator = Evaluator()
rank = evaluator.evaluate(board, hand)
hand_class = evaluator.get_rank_class(rank)

# Вывод результатов оценки
print(f"Hand rank: {rank}")
print(f"Hand class: {hand_class}")
print(f"Hand class name: {evaluator.class_to_string(hand_class)}")

# Строковые представления всех карт
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['h', 'd', 'c', 's']
all_cards = [value + suit for value in values for suit in suits]
print(all_cards)

# Функция для создания карты из строкового представления
def create_card(card_str):
    return Card.new(card_str)

# Функция для оценки силы руки
def evaluate_hand(board_str, hand_str):
    board = [create_card(card) for card in board_str]
    hand = [create_card(card) for card in hand_str]

    evaluator = Evaluator()
    rank = evaluator.evaluate(board, hand)
    hand_class = evaluator.get_rank_class(rank)
    hand_class_name = evaluator.class_to_string(hand_class)

    return rank, hand_class, hand_class_name

# Пример использования
board_str = [Card.int_to_str(card) for card in board]
hand_str = [Card.int_to_str(card) for card in hand]

rank, hand_class, hand_class_name = evaluate_hand(board_str, hand_str)
print(f"Hand rank: {rank}")
print(f"Hand class: {hand_class}")
print(f"Hand class name: {hand_class_name}")
