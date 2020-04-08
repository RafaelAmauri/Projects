#include <iostream>

#define bool short
#define true 1
# define false 0

class Board
{
	private:
		char board[3][3];
		char turn;
		bool in_game;

	public:
		
		// creates a new board
		Board()
		{
			this->clear_board();
			turn = 'X';
			in_game = true;
		}

		// returns wether a game session is on
		bool game_active()
		{
			return this->in_game;
		}

		// changes the turn to the other player
		void change_player()
		{
			if(this->turn == 'X')
				this->turn = 'O';

			else
				this->turn = 'X';
		}

		// sets all pieces to ' '
		void clear_board()
		{
			for(int i = 0; i < 3; i++)
				for(int j = 0; j < 3; j++)
					this->board[i][j] = ' ';
		}
		
		// given a position, it sets the value
		void set(char value, int x, int y)
		{
			this->board[x][y] = value;
		}
	
		
		// prints a representation of the board
		void show()
		{
			for(int i = 0; i < 3; i++)
			{
				for(int j = 0; j < 3; j++)
				{
					if(this->board[i][j] == ' ')
					{
						printf("[%d]", (i*3)+j+1); // +1 is for the very first pos to start with 1 instead of 0
						continue;
					}
					printf("[%c]", this->board[i][j]);
				}
				printf("\n");
			}
		}


		void play()
		{
			this->show();
			printf("Sua vez, jogador \'%c\'. Onde quer jogar?\n", this->turn);

			int position;
			
			do
			{
				std::cin >> position;
			} while(position < 1 && position > 9);

			position--; // The user sees the positions with +1, so we need to back it down by 1
			
			this->set(this->turn, (position/3), (position%3) );

			this->change_player();
		}
		
};


int main()
{
	Board *board = new Board();
	
	while(board->game_active())
	{
		board->play();
	//	board->check_winner();
	}

	return 0;
}
