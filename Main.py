import random

class Deck:
    CARD_NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    CARD_SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    def __init__(self):
        self.deck_of_cards = [f'{num}{suit}' for num in self.CARD_NUMBERS for suit in self.CARD_SUITS]
        # for num in self.card_numbers:
        #     for suit in self.card_suits:
        #         card = f'{num}{suit}'
        #         self.deck_of_cards.append(card)

    def __str__(self):
        return str(self.deck_of_cards)

    def shuffle_the_cards(self) -> list:
        random.shuffle(self.deck_of_cards)

class Player:
    def __init__(self, deck: list, player_name = "USER"):
        self._player_name = player_name
        self._player_cards = self.player_cards(deck)

    def __str__(self):
        return str(self._player_cards)
    
    @property
    def player_cards(self):
        return self._player_name

    def player_cards(self, deck) -> list:
        half = len(deck) // 2
        if self._player_name == "BOT":
            return deck[:half]
        else:
            return deck[half:]
        

# Shuffle the cards
# Distribute the cards
class Gameplay:
    def __init___(self, player_bot: Player, player_user: Player):
        self._bot_cards = player_bot.player_cards
        self._user_cards = player_user.player_cards

    def __srt__(self):
        ...


    @property
    def bot_cards(self):
        return self._bot_cards

    @bot_cards.setter
    def bot_cards(self, new_bot_cards):
        self._bot_cards = new_bot_cards

    @property
    def user_cards(self):
        return self._user_cards

    @user_cards.setter
    def user_cards(self, new_user_cards):
        self._user_cards = new_user_cards


    def reveal_top_card(self):
        """
        The function does not require any arguments. It returns the card that bot revealed, the card that user revealed and the list of revealed cards
        """
        bot_card, user_card = self._bot_cards.pop(0), self._user_cards.pop(0)
        return bot_card, user_card

    
    def check_for_battle_winner(self, bot_card, user_card) -> list:
        card_values = {
            "2": 2,
            "3": 3, 
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

        bot_num = bot_card[0]
        user_num = user_card[0]
        bot_suit = bot_card[1:]
        user_suit = user_card[1:]
        # cards = [bot_card, user_card]

        if card_values[bot_num] > card_values[user_num]:
            print(f"Bot won the battle with {bot_num} of {bot_suit} over {user_num} of {user_suit}")
            winner = "BOT"
            # return {"cards": cards, "winner": winner}
            return winner
        elif card_values[bot_num] < card_values[user_num]:
            print(f"You won the battle with {user_num} of {user_suit} over {bot_num} of {bot_suit}")
            winner = "USER"
            # return {"cards": cards, "winner": winner}
            return winner
        
        return None
        

    def add_cards(self, bot_cards: list, user_cards: list, winner: str, cards: list):
        if winner == "BOT":
            return bot_cards.extend(cards)
        elif winner == "USER":
            return user_cards.extend(cards)


    def check_for_winner_of_the_game(self, user_cards: list, bot_cards: list) -> bool:
        if len(self.user_cards) == 0:
            print("Bot has won the game")
            return True
        elif len(self.bot_cards) == 0:
            print("You have won the game")
            return True
        return False
    

    def play_round(self, bot_cards: list, user_cards: str):
        bot_card, user_card = self.reveal_top_card()
        cards = [bot_card, user_card]
        while True:
            winner = self.check_for_battle_winner(bot_card = bot_card, user_card = user_card)
            if winner == None:
                bot_facedown_card, user_facedown_card = self.reveal_top_card()
                bot_card, user_card = self.reveal_top_card()
                battle = self.check_for_battle_winner(bot_card = bot_card, user_card = user_card)
            else:
                self.add_cards(winner=battle["winner"], cards=cards, user_cards=, bot_cards=)
                break

         


# Each reveals the top card
# While true
    # If there is a winner of the battle:
        # Winner takes cards +++
    # Else:
        # War
        # Winner takes cards +++
    # Check if both players still have at least 1 card
    # If not:
        # Announce the winner of the game
    # Break
def main():
    deck = Deck()
    deck.shuffle_the_cards()
    cards = deck.deck_of_cards
    player_bot = Player(cards, "BOT")
    player_me = Player(cards, "VAKARIS")
    gameplay = Gameplay()
    while True:
        gameplay.reveal_top_card
        if gameplay.check_for_tie:
            # WAR
        # gameplay.check_for_battle_winner:
            # gameplay.announce_battle_winner
            # gameplay.take_cards
            ...
            skipped_cards = gameplay.skip_cards
            gameplay.reveal_top_card
            gameplay.check_for_war_winner
            gameplay.take_cards     
        else:
            gameplay.check_for_battle_winner
            gameplay.announce_battle_winner
        
        if gameplay.check_for_game_winner:
            gameplay.announce_the_winner
            break


if __name__ == "__main__":
    main()