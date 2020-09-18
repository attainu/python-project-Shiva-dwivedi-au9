import random
import time
import sys


class Saanp_Seedhi:

    def __init__(self):

        self.DELAY_IN_ACTIONS = 1
        self.DESTINATION = 100
        self.DICE_FACE = 6

        self.text = [
            "Your move.",
            "Go on.",
            "Let's GO .",
            "You can win this."
        ]

        self.bitten_by_snake = [
            "Aeeee kataaaaaaaaaaa",
            "gaya gaya gaya gaya",
            "bitten :P",
            "oh damn",
            "damn"
        ]

        self.ladder_climb = [
            "NOICEEE",
            "GREATTTT",
            "AWESOME",
            "HURRAH...",
            "WOWWWW"
        ]

        self.snakes = {}
        self.ladders = {}
        self.players = []

        self.num_of_players = int(input("Enter the num of players(2 or 4):"))

        if self.num_of_players == 2 or self.num_of_players == 4:
            for _ in range(self.num_of_players):
                self.pl_name = input("Name of player " + str(_ + 1) + " : ")
                self.players.append(self.pl_name)

            print("\nMatch will be played between: ", end=" ")
            print(",".join(self.players[:len(self.players)-1]), end=" ")
            print("and", self.players[-1])

        else:
            print("Enter either 2 or 4")
            self.num_of_players = int(input("Enter no. of players(2 or 4):"))
            for _ in range(self.num_of_players):
                self.pl_name = input("Name of player " + str(_ + 1) + " : ")
                self.players.append(self.pl_name)

    def Snakes(self):

        num_of_snakes = int(input("No. of snakes on your board :"))

        if num_of_snakes > 0:
            print("\n Enter Head and Tail separated by a space")
            i = 0
            while i < (num_of_snakes):
                head, tail = map(int, input("\n Head and Tail: ").split())

                if head <= 100 and tail > 0:

                    if tail >= head:
                        print("\n The tail of snake should be less than head")
                        i = i-1

                    elif head == 100:
                        print("\n Snake not possible at position 100.")
                        i = i-1

                    elif head in self.snakes.keys():
                        print("\n Snake already present")
                        i = i-1

                    else:
                        self.snakes[head] = tail

                    i += 1
                else:
                    print("Invalid! kindly choose b/w 0 to 100")

            print("\n Your Snakes are at : ", self.snakes, "\n")

        else:
            print("Please enter valid number of snakes")
            self.Snakes()

        return self.snakes

    def Ladders(self):

        num_of_ladders = int(input("No. of ladders on your board :"))

        if num_of_ladders > 0:

            print("\n Enter Start and End separated by a space")

            i = 0

            while i < (num_of_ladders):
                flag = 0
                start, end = map(int, input("\n Start and End: ").split())

                if start > 0 and end < 100:

                    if end <= start:
                        print("\n The end should be greater than Start")
                        flag = 1
                        i -= 1

                    elif start in self.ladders.keys():
                        print("\n Ladder already present")
                        flag = 1
                        i -= 1

                    for k, v in self.snakes.items():

                        if k == end and v == start:
                            print("\nSnake present(will create infinite loop)")
                            print("\nPlease Enter valid Ladder")
                            flag = 1
                            i -= 1

                    else:
                        if flag == 0:
                            self.ladders[start] = end

                        else:
                            pass

                    i += 1

                else:
                    print("Invalid! kindly choose b/w 0 to 100")

            print("\n Your Ladders are at: ", self.ladders, "\n")

        else:
            print("Please select valid number of ladders")
            self.Ladders()

        return self.ladders

    def get_player_names(self):
        if self.num_of_players == 2:
            pl_1 = self.players[0]
            pl_2 = self.players[1]
            return pl_1, pl_2

        elif(self.num_of_players == 4):

            pl_1 = self.players[0]
            pl_2 = self.players[1]
            pl_3 = self.players[2]
            pl_4 = self.players[3]
            return pl_1, pl_2, pl_3, pl_4

        else:
            return("Invalid choice")

    def welcome_to_the_game(self):

        message = """
        Welcome to Saanp Seedhi.

        GAME RULES
           1. When a piece comes on a number which lies on the head of a snake,
              then the piece will land below to the tail of the snake that can
              also be said as an unlucky move.
           2. If somehow the piece falls on the ladder base, it will climb to
              the top of the ladder (which is considered to be a lucky move).
           3. Whereas if a player lands on the tail of the snake or top of a
              ladder, the player will remain in the same spot (same number)
              and will not get affected by any particular rule.
              The players can never move down ladders.
           4. The pieces of different players can overlap each other without
              knocking out anyone.There is no concept of knocking out by
              opponent players in Snakes and Ladders.
           5. To win, the player needs to roll the exact number of die to land
              on the number 100. If they fails to do so, then the player needs
              to roll the die again in the next turn. For eg, if a player is
              on the number 98 and the die roll shows the number 4, then they
              cannot move its piece until they get a 2 to win or 1 to be on
              99th number.
        """
        print(message)

    def roll_the_dice(self):
        time.sleep(self.DELAY_IN_ACTIONS)
        dice_val = random.randint(1, self.DICE_FACE)
        print("Great.You got a " + str(dice_val))
        return dice_val

    def you_got_bitten(self, old_val, curr_val, pl_name):
        print("\n" + random.choice(self.bitten_by_snake).upper() + " :(:(:(:(")
        print("\n" + pl_name + " bitten. Dropped from ", end=" ")
        print(str(old_val) + " to " + str(curr_val))

    def climbing_ladder(self, old_val, curr_val, pl_name):
        print("\n" + random.choice(self.ladder_climb).upper() + " :):):):)")
        print("\n" + pl_name + " climbed from ", end=" ")
        print(str(old_val) + " to " + str(curr_val))

    def saanp_seedhi(self, pl_name, curr_val, dice_val):
        time.sleep(self.DELAY_IN_ACTIONS)
        old_val = curr_val
        curr_val = curr_val + dice_val

        if curr_val > self.DESTINATION:
            print("You now need " + str(self.DESTINATION - old_val), end=" ")
            print(" more to win this game.", end=" ")
            print("Keep trying.You'll win")
            return old_val

        print("\n" + pl_name + " moved from " + str(old_val), end=" ")
        print(" to " + str(curr_val))
        if curr_val in self.snakes:
            final_value = self.snakes.get(curr_val)
            self.you_got_bitten(curr_val, final_value, pl_name)

        elif curr_val in self.ladders:
            final_value = self.ladders.get(curr_val)
            self.climbing_ladder(curr_val, final_value, pl_name)

        else:
            final_value = curr_val

        return final_value

    def Winner(self, pl_name, position):
        time.sleep(self.DELAY_IN_ACTIONS)
        if self.DESTINATION == position:
            print("\n\n\nBRAVO!!!!!.\n\n" + pl_name + " WON THE GAME.")
            print("CONGRATULATIONS " + pl_name)
            print("\nThank you for playing the game.")
            sys.exit(1)


class Start(Saanp_Seedhi):

    def start_the_game(self):
        time.sleep(self.DELAY_IN_ACTIONS)
        if self.num_of_players == 2:
            pl_1, pl_2 = self.get_player_names()

        elif self.num_of_players == 4:
            pl_1, pl_2, pl_3, pl_4 = self.get_player_names()
        time.sleep(self.DELAY_IN_ACTIONS)

        pl_1_cur_pos = 0
        pl_2_cur_pos = 0
        pl_3_cur_pos = 0
        pl_4_cur_pos = 0

        while True:
            time.sleep(self.DELAY_IN_ACTIONS)
            if self.num_of_players == 2:
                s = " Press enter to roll dice: "
                _ = input(pl_1 + ": " + random.choice(self.text) + s)
                print("\nRolling the dice...")
                dice_val = self.roll_the_dice()
                time.sleep(self.DELAY_IN_ACTIONS)
                print(pl_1 + " moving....")
                pl_1_cur_pos = self.saanp_seedhi(pl_1, pl_1_cur_pos, dice_val)

                self.Winner(pl_1, pl_1_cur_pos)

                _ = input(pl_2 + ": " + random.choice(self.text) + s)
                print("\nRolling dice...")
                dice_val = self.roll_the_dice()
                time.sleep(self.DELAY_IN_ACTIONS)
                print(pl_2 + " moving....")
                pl_2_cur_pos = self.saanp_seedhi(pl_2, pl_2_cur_pos, dice_val)

                self.Winner(pl_2, pl_2_cur_pos)

            elif(self.num_of_players == 4):
                s = " Press enter to roll dice: "
                _ = input(pl_1 + ": " + random.choice(self.text) + s)
                print("\nRolling the dice...")
                dice_val = self.roll_the_dice()
                time.sleep(self.DELAY_IN_ACTIONS)
                print(pl_1 + " moving....")
                pl_1_cur_pos = self.saanp_seedhi(pl_1, pl_1_cur_pos, dice_val)

                self.Winner(pl_1, pl_1_cur_pos)

                _ = input(pl_2 + ": " + random.choice(self.text) + s)
                print("\nRolling dice...")
                dice_val = self.roll_the_dice()
                time.sleep(self.DELAY_IN_ACTIONS)
                print(pl_2 + " moving....")
                pl_2_cur_pos = self.saanp_seedhi(pl_2, pl_2_cur_pos, dice_val)

                self.Winner(pl_2, pl_2_cur_pos)

                _ = input(pl_3 + ": " + random.choice(self.text) + s)
                print("\nRolling dice...")
                dice_val = self.roll_the_dice()
                time.sleep(self.DELAY_IN_ACTIONS)
                print(pl_3 + " moving....")
                pl_3_cur_pos = self.saanp_seedhi(pl_3, pl_3_cur_pos, dice_val)

                self.Winner(pl_3, pl_3_cur_pos)

                _ = input(pl_4 + ": " + random.choice(self.text) + s)
                print("\nRolling dice...")
                dice_val = self.roll_the_dice()
                time.sleep(self.DELAY_IN_ACTIONS)
                print(pl_4 + " moving....")
                pl_4_cur_pos = self.saanp_seedhi(pl_4, pl_4_cur_pos, dice_val)

                self.Winner(pl_4, pl_4_cur_pos)


if __name__ == "__main__":

    lets_play_the_game = Start()
    time.sleep(1)
    lets_play_the_game.welcome_to_the_game()
    lets_play_the_game.Snakes()
    lets_play_the_game.Ladders()
    lets_play_the_game.start_the_game()
