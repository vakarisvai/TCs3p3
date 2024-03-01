import random
import time

class Deck:
    CARD_NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    CARD_SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    def __init__(self):
        self._deck_of_cards = [f'{num} of {suit}' for num in self.CARD_NUMBERS for suit in self.CARD_SUITS]
        # for num in self.card_numbers:
        #     for suit in self.card_suits:
        #         card = f'{num}{suit}'
        #         self.deck_of_cards.append(card)

    def __str__(self):
        return str(self.deck_of_cards)

    def shuffle_the_cards(self) -> list:
        random.shuffle(self._deck_of_cards)

class Player:
    def __init__(self, deck: list, player_name = "USER"):
        self._player_name = player_name
        self.player_cards = deck

    def __str__(self):
        return str(self._player_cards)
    
    @property
    def player_cards(self):
        return self._player_name
    
    @property
    def player_cards(self):
        return self._player_cards 
    
    @player_cards.setter
    def player_cards(self, deck):
        half = len(deck) // 2
        if self._player_name == "BOT":
            self._player_cards = deck[:half]
        else:
            self._player_cards = deck[half:]
        

class Gameplay:
    def __init__(self, player_bot: Player, player_user: Player):
        self._bot_cards = player_bot.player_cards
        self._user_cards = player_user.player_cards

    def __srt__(self):
        return str(type(self._bot_cards))

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
        The function does not require any arguments. It returns the card that bot revealed and the card that user revealed
        """
        bot_card = self._bot_cards.pop(0)
        user_card = self._user_cards.pop(0)
        return bot_card, user_card


    def get_num(self, card):
        return card.split(" ")[0]
    

    def get_suit(self, card):
        return card.split(" ")[2]

    
    def check_for_battle_winner(self, bot_card: str, user_card: str) -> list:
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

        bot_num = self.get_num(bot_card)
        bot_suit = self.get_suit(bot_card)
        user_num = self.get_num(user_card)
        user_suit = self.get_suit(user_card)
        # cards = [bot_card, user_card]


        if card_values[bot_num] > card_values[user_num]:
            print(f"Bot won the battle with {bot_card} over {user_card}")
            winner = "BOT"
            # return {"cards": cards, "winner": winner}
            return winner
        elif card_values[bot_num] < card_values[user_num]:
            print(f"You won the battle with {user_num} of {user_suit} over {bot_num} of {bot_suit}")
            winner = "USER"
            # return {"cards": cards, "winner": winner}
            return winner
        
        return None
        

    def add_cards(self, winner: str, cards: list):
        if winner == "BOT":
            self._bot_cards.extend(cards)
        elif winner == "USER":
            self._user_cards.extend(cards)


    

    def play_round(self, bot_cards: list, user_cards: str):
        try:
            bot_card, user_card = self.reveal_top_card()
            cards = [bot_card, user_card]
            while True:
                winner = self.check_for_battle_winner(bot_card = bot_card, user_card = user_card)
                if winner == None:
                    bot_facedown_card, user_facedown_card = self.reveal_top_card()
                    cards.append(bot_facedown_card)
                    cards.append(user_facedown_card)
                    bot_card, user_card = self.reveal_top_card()
                    cards.append(bot_card)
                    cards.append(user_card)
                    # winner = self.check_for_battle_winner(bot_card = bot_card, user_card = user_card)
                else:
                    self.add_cards(winner=winner, cards=cards)
                    return None
        except IndexError:
            self.return_the_winner(bot_cards=self._bot_cards, user_cards=self._user_cards)

         
    def return_the_winner(self, user_cards: list, bot_cards: list) -> bool:
        if len(self._user_cards) == 0:
            print("Bot has won the game")
            return "BOT"
        else:
            print("You have won the game")
            return "USER"



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
    cards = deck._deck_of_cards
    player_bot = Player(cards, "BOT")
    player_user = Player(cards, "VAKARIS")
    gameplay = Gameplay(player_bot, player_user)
    # print(f"gameplay {gameplay}")
    
    while True:
        winner = gameplay.play_round(bot_cards=player_bot._player_cards, user_cards=player_user._player_cards)
        print(f"Your cards: {gameplay.user_cards}")
        print("------------------------------------------------")
        print(f"Your card TEST: {player_user.player_cards}")
        print("------------------------------------------------")
        print(f"BOT cards: {gameplay.bot_cards}")
        print("------------------------------------------------")
        print("------------------------------------------------")
        
        # print(winner)
        if winner == None:
            # print("atejo")
            pass
        else:
            # gameplay.return_the_winner()
            # print("YRA WINNERIS")
            break
        time.sleep(0.2)

    print("BE ERRORU")

if __name__ == "__main__":
    main()