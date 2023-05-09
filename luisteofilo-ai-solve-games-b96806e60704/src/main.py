from games.connect4.players.greedy import GreedyConnect4Player
from games.connect4.players.minimax import MinimaxConnect4Player
from games.connect4.players.random import RandomConnect4Player
from games.connect4.players.random2 import RandomConnect4Player2
from games.connect4.players.human import HumanConnect4Player
from games.connect4.players.human2 import HumanConnect4Player2
from games.connect4.players.mymini import MyminiConnect4Player
from games.connect4.simulator import Connect4Simulator
from games.game_simulator import GameSimulator
from games.poker.players.always_bet import AlwaysBetKuhnPokerPlayer
from games.poker.players.always_bet_king import AlwaysBetKingKuhnPokerPlayer
from games.poker.players.always_pass import AlwaysPassKuhnPokerPlayer
from games.poker.players.cfr import CFRKuhnPokerPlayer
from games.poker.players.random import RandomKuhnPokerPlayer
from games.poker.simulator import KuhnPokerSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA TP1")

    num_iterations = 1

    c4_simulations = [
        
        #{
        #    "name": "LYNGK - Human VS FakeMiniMax",
        #    "player1": HumanConnect4Player("Human 1 "),
        #    "player2": MyminiConnect4Player("FakeMiniMax")
        #},
        #{
        #    "name": "LYNGK - Human VS Random",
        #    "player1": HumanConnect4Player("Human 1"),
        #    "player2": RandomConnect4Player("Random 1")
        #},
        #{
        #    "name": "LYNGK - Random VS FakeMiniMax",
        #    "player1": RandomConnect4Player2("Random 2"),
        #    "player2": MyminiConnect4Player("FakeMiniMax")
        #},
        #{
        #    "name": "LYNGK - Random VS Random",
        #    "player1": RandomConnect4Player2("Random 2"),
        #    "player2": RandomConnect4Player("Random 1 ")
        #},
        {
            "name": "Human VS Human",
            "player1": HumanConnect4Player("Human 1"),
            "player2": HumanConnect4Player2("Human 2 ")
        }
    ]

    #poker_simulations = [
         
    #    {
    #        "name": "Connect4 - Human VS Random",
    #        "player1": HumanConnect4Player("Human"),
    #        "player2": RandomConnect4Player("Random")
    #    },
        #{
        #    "name": "Kuhn Poker - Random VS Random",
        #    "player1": RandomKuhnPokerPlayer("Random 1"),
        #    "player2": RandomKuhnPokerPlayer("Random 2")
        #},
        #{
        #    "name": "Kuhn Poker - AlwaysBet VS Random",
        #    "player1": AlwaysBetKuhnPokerPlayer("AlwaysBet"),
        #    "player2": RandomKuhnPokerPlayer("Random")
        #},
        #{
        #    "name": "Kuhn Poker - AlwaysPass VS Random",
        #    "player1": AlwaysPassKuhnPokerPlayer("AlwaysPass"),
        #    "player2": RandomKuhnPokerPlayer("Random")
        #},
        #{
        #    "name": "Kuhn Poker - AlwaysBet VS AlwaysPass",
        #    "player1": AlwaysBetKuhnPokerPlayer("AlwaysBet"),
        #    "player2": AlwaysPassKuhnPokerPlayer("AlwaysPass")
        #},
        #{
        #    "name": "Kuhn Poker - AlwaysBet VS AlwaysBetKing",
        #    "player1": AlwaysBetKuhnPokerPlayer("AlwaysBet"),
        #    "player2": AlwaysBetKingKuhnPokerPlayer("AlwaysBetKing")
        #},
        #{
        #    "name": "Kuhn Poker - CFR VS Random",
        #    "player1": CFRKuhnPokerPlayer("CFR"),
        #    "player2": RandomKuhnPokerPlayer("Random")
        #},
        #{
        #    "name": "Kuhn Poker - CFR VS AlwaysPass",
        #    "player1": CFRKuhnPokerPlayer("CFR"),
        #    "player2": AlwaysPassKuhnPokerPlayer("AlwaysPass")
        #},
        #{
        #    "name": "Kuhn Poker - CFR VS AlwaysBet",
        #    "player1": CFRKuhnPokerPlayer("CFR"),
        #    "player2": AlwaysBetKuhnPokerPlayer("AlwaysBet")
        #},
        #{
        #    "name": "Kuhn Poker - CFR VS AlwaysBetKing",
        #    "player1": CFRKuhnPokerPlayer("CFR"),
        #    "player2": AlwaysBetKingKuhnPokerPlayer("AlwaysBetKing")
        #}
    #]

    for sim in c4_simulations:
        run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)

    #for sim in poker_simulations:
    #    run_simulation(sim["name"], KuhnPokerSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
