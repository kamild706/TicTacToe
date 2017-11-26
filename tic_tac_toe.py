from random import randint, choice
import time, sys, os

class TicTacToe:
	board = [None for i in range(9)] # list representing game's board 
	turn = 1 # counter of computer's turns 

	def print_board(self, board = None): # printing game board 
		board = self.board if board == None else board

		os.system("clear") # use "cls" for windows
		print("|---|---|---|")
		for i, cell in enumerate(board, 1):
			print("| {} ".format(" " if cell == None else cell), end = "")
			if i % 3 == 0:
				print("|")
				print("|---|---|---|")


	def get_game_winner(self, board = None):
		board = self.board if board == None else board

		for i in range(0, 9, 3):
			if board[i] == board[i + 1] == board[i + 2]:
				if board[i] != None: return board[i]

		for i in range(0, 3):
			if board[i] == board[i + 3] == board[i + 6]:
				if board[i] != None: return board[i]

		if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
			if board[4] != None: return board[4]

		return None


	def computer_turn(self):
		position = None

		def get_line(cell):
			if cell <= 3: return 1
			if cell <= 6: return 2
			return 3

		if self.turn == 1:
			self.turn = 2
			oponent_choice = self.board.index("X")
			if oponent_choice + 1 in [1, 3, 7, 9]:
				position = 5 - 1
			else:
				position = choice([1, 3, 7, 9]) - 1
		
		elif self.turn == 2:
			self.turn = 3
			for i in [1, 3, 7, 9]:
				if self.board[i - 1] == "X":
					if self.board[5 - 1] == "X":
						position = 10 - i - 1
						if self.board[position] == "O":
							position = choice([item - 1 for item in [1, 3, 7, 9] if item not in [position + 1, i]])
						break

					for j in [1, 3, 7, 9]:
						if i != j and self.board[j - 1] == "X":
							position = i + (j - i) // 2 - 1
							if self.board[position] == "O":
								position = choice([2, 4, 6, 8]) - 1
							break

					for j in [2, 4, 6, 8]:
						if self.board[j - 1] == "X":
							diff = abs(j - i)
							if get_line(i) != get_line(j) and diff == 1:
								position = 5 - 1
							else:
								position = max(i, j) + diff
								if position > 9: position = min(i, j) - diff
								if self.board[position - 1] == "O": position = 5
								position -= 1


			if position == None:
				for i in [2, 4, 6, 8]:
					if self.board[i - 1] == "X":
						if self.board[5 - 1] == "X":
							position = 10 - i - 1
						else:
							position = 5 - 1

		if self.turn > 2:
			tmp_board = self.board[:]
			candidates = [i for i in range(9) if self.board[i] == None]
			for candidate in candidates:
				tmp_board[candidate] = "O"
				if self.get_game_winner(tmp_board) == "O":
					position = candidate
					break
				tmp_board[candidate] = None

			if position == None:
				for candidate in candidates:
					tmp_board[candidate] = "X"
					if self.get_game_winner(tmp_board) == "X":
						position = candidate
						break
					tmp_board[candidate] = None

			if position == None: position = candidates[0]


		self.board[position] = "O"


	def ask_for_choice(self):
		while True:
			try:
				print("Your choice: ", end = "")
				position = int(input())
			except ValueError:
				print("That's not an integer!")
				continue

			if 1 <= position <= 9:
				return position - 1
			else:
				print("Number must be in range 1 to 9!")


	def user_turn(self):
		position = self.ask_for_choice()

		while self.board[position] != None:
			print("This position is filled")
			position = self.ask_for_choice()

		self.board[position] = "X"


	def is_game_finished(self):
		if None not in self.board:
			print("The game ended with a draw")
			sys.exit()

		winner = self.get_game_winner()
		if winner == None: return

		if winner == "X": print("You won the game!")
		else: print("Computer won the game")
		sys.exit()


	def start(self):
		self.print_board([i for i in range(1, 10)])
		print()
		print("Hello, the game just started!")
		while True:	
			self.user_turn()
			self.print_board()
			self.is_game_finished()

			time.sleep(0.5)
			self.computer_turn()
			self.print_board()
			self.is_game_finished()


game = TicTacToe()
game.start()
