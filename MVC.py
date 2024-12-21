# Model
class Game:
    def __init__(self, name, genre, description):
        self.name = name
        self.genre = genre
        self.description = description
        self.teams = []  # List to hold associated teams

    def __str__(self):
        return f"Game: {self.name} ({self.genre})\nDescription: {self.description}\nTeams: {', '.join([team.name for team in self.teams]) if self.teams else 'No teams added.'}"

class Team:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def __str__(self):
        return f"Team: {self.name}, Game: {self.game}"

# View: Handles user interaction
class View:
    @staticmethod
    def display_games(games):
        if not games:
            print("No games available.")
        else:
            for game in games:
                print(game)

    @staticmethod
    def display_teams(teams):
        if not teams:
            print("No teams available.")
        else:
            for team in teams:
                print(team)

    @staticmethod
    def get_game_details():
        name = input("Enter game name: ")
        genre = input("Enter game genre: ")
        description = input("Enter game description: ")
        return Game(name, genre, description)

    @staticmethod
    def get_team_details(games):
        name = input("Enter team name: ")
        print("Available games:")
        for i, game in enumerate(games):
            print(f"{i + 1}. {game.name}")
        game_choice = int(input("Select a game by number: ")) - 1
        return Team(name, games[game_choice])

    @staticmethod
    def prompt_user():
        print("\nOptions:")
        print("1. Add Game")
        print("2. View Games")
        print("3. Add Team")
        print("4. View Teams")
        print("5. Exit")
        return input("Choose an option: ")

# Controller
class Controller:
    def __init__(self, view):
        self.view = view
        self.games = []

    def add_game(self):
        game = self.view.get_game_details()
        self.games.append(game)
        print(f"Added game: {game.name}")

    def view_games(self):
        self.view.display_games(self.games)

    def add_team(self):
        if not self.games:
            print("No games available. Add a game first.")
            return
        team = self.view.get_team_details(self.games)
        team.game.teams.append(team)
        print(f"Added team: {team.name} to game: {team.game.name}")

    def view_teams(self):
        teams = [team for game in self.games for team in game.teams]
        self.view.display_teams(teams)

    def run(self):
        while True:
            option = self.view.prompt_user()
            if option == '1':
                self.add_game()
            elif option == '2':
                self.view_games()
            elif option == '3':
                self.add_team()
            elif option == '4':
                self.view_teams()
            elif option == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    view = View()
    controller = Controller(view)
    controller.run()
