import random
logo = logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you wanna play a game of blackjack? Type 'y' for yes and 'n' for no.") == 'y':
  user_status = ''
  user_choice = True
  # Cards
  user_cards = [random.choice(cards), random.choice(cards)]
  computer_cards = [random.choice(cards), random.choice(cards)]

  # Score
  user_score = sum(user_cards)
  computer_score = sum(computer_cards)

# determining final user_score and final user_cards
  while user_choice == True and user_score < 21:

# displaying user's cards and score and 1 card of computer
    print(logo)
    print(f"You cards: {user_cards}, Your score: {user_score}.")
    print(f"Computer's first card: {computer_cards[0]}")

# itroducing blackjack
    blackjack = cards[0] + (cards[9] or cards[10] or cards[11] or cards[12])



    if user_score == computer_score == blackjack:
      user_status = "It's a Draw."
      print(f"You final cards: {user_cards}, Your final score: {user_score}.")
      print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
      print(f"Your score is equal to computer's score. {user_status}")
    elif user_score == blackjack:
      user_status = "You Win."
      print(f"You final cards: {user_cards}, Your final score: {user_score}.")
      print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
      print(f"You have a blackjack. {user_status}")
    elif computer_score == blackjack:
      user_status = "You Lose."
      print(f"You final cards: {user_cards}, Your final score: {user_score}.")
      print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
      print(f"Computer has a blackjack. {user_status}")
    else:
      if user_score > 21:
        if cards[0] in user_cards:
          for card in range(len(user_cards)):
            if user_cards[card] == cards[0]:
              user_cards[card] == 1
              user_score = sum(user_cards)
          if user_score > 21:
            user_status = "You Lose."
            print(f"You final cards: {user_cards}, Your final score: {user_score}.")
            print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
            print(f"Your score is more than 21. {user_status}")
          elif user_score == 21:
            user_status = "You Win."
            print(f"You final cards: {user_cards}, Your final score: {user_score}.")
            print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
            print(f"You have a blackjack. {user_status}")
      if user_status == "" and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        new_user_number = random.choice(cards)
        user_score += new_user_number
        user_cards.append(new_user_number)
      else:
        user_choice = False
  while computer_score < 17:
    new_computer_number = random.choice(cards)
    computer_score += new_computer_number
    computer_cards.append(new_computer_number)
  if user_score > 21:
    user_status = 'You Lose.'
    print(f"You final cards: {user_cards}, Your final score: {user_score}.")
    print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
    print(f"Your score is more than 21. {user_status}")
  elif computer_score > 21:
    user_status = 'You Win.'
    print(f"You final cards: {user_cards}, Your final score: {user_score}.")
    print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
    print(f"Computer's score is more than 21. {user_status}")
  elif computer_score == 21 == user_score:
    user_status = "It's a Draw."
    print(f"You final cards: {user_cards}, Your final score: {user_score}.")
    print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
    print(f"Both, computer and you have a blackjack. {user_status}")
  elif computer_score == 21:
    user_status = "You Lose."
    print(f"You final cards: {user_cards}, Your final score: {user_score}.")
    print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
    print(f"Computer has a blackjack. {user_status}")
  else:
    if user_score == computer_score:
      user_status = "It's a Draw."
      print(f"You final cards: {user_cards}, Your final score: {user_score}.")
      print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
      print(f"Your score is equal to computer's score. {user_status}")
    elif user_score > computer_score:
      user_status = "You Win."
      print(f"You final cards: {user_cards}, Your final score: {user_score}.")
      print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
      print(f"Your score is greter than computer's score. {user_status}")
    else:
      user_status = "You Lose."
      print(f"You final cards: {user_cards}, Your final score: {user_score}.")
      print(f"Computer's final cards: {computer_cards}, Computer's final score: {computer_score}.")
      print(f"Your score is lesser than computer's score. {user_status}")
