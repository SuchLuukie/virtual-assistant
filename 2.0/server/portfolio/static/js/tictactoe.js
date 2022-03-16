const table = document.getElementById("table")
const rows = 3
const cells = 3 

function board_creator() {
	table.innerHTML = "";
	board = [];

	for(i = 0; i < rows; i++) {
		var row = table.insertRow(i);
		board.push([]);

		for(j = 0; j < rows; j++) {
			board[i].push("");
			var cell = row.insertCell(j);
			cell.classList.add("a" + i + j);
			cell.id = i + "-" + j;
			cell.onclick = function() {cell_click(this)};
		}
	}
}

function bestMove() {
	if (end_game == false) {
		// AI to make its turn
		let bestScore = -Infinity;
		let move;
		for (let i = 0; i < 3; i++) {
			for (let j = 0; j < 3; j++) {
				// Is the spot available?
				if (board[i][j] == '') {
					board[i][j] = ai;
					let score = minimax(board, 0, false);
					board[i][j] = '';
					if (score > bestScore) {
						bestScore = score;
						move = { i, j };
					}
				}
			}
		}
		board[move.i][move.j] = ai;
		var cell = document.getElementById(move.i + "-" + move.j);
		cell.classList.add(ai);
		turn = human
		checkWin();
	}
}

function minimax(board, depth, isMaximizing) {
	let result = checkWinner();
	if (result !== null) {
		return scores[result];
	}

	if (isMaximizing) {
		let bestScore = -Infinity;
		for (let i = 0; i < 3; i++) {
			for (let j = 0; j < 3; j++) {
				// Is the spot available?
				if (board[i][j] == '') {
					board[i][j] = ai;
					let score = minimax(board, depth + 1, false);
					board[i][j] = '';
					bestScore = Math.max(score, bestScore);
				}
			}
		}
		return bestScore;
	} else {
		let bestScore = Infinity;
		for (let i = 0; i < 3; i++) {
			for (let j = 0; j < 3; j++) {
				// Is the spot available?
				if (board[i][j] == '') {
					board[i][j] = human;
					let score = minimax(board, depth + 1, true);
					board[i][j] = '';
					bestScore = Math.min(score, bestScore);
				}
			}
		}
		return bestScore;
	}
}

function equals3(a, b, c) {
	return a == b && b == c && a != '';
}

function checkWinner() {
	let winner = null;

	// horizontal
	for (let i = 0; i < 3; i++) {
		if (equals3(board[i][0], board[i][1], board[i][2])) {
			winner = board[i][0];
		}
	}

	// Vertical
	for (let i = 0; i < 3; i++) {
		if (equals3(board[0][i], board[1][i], board[2][i])) {
			winner = board[0][i];
		}
	}

	// Diagonal
	if (equals3(board[0][0], board[1][1], board[2][2])) {
		winner = board[0][0];
	}
	if (equals3(board[2][0], board[1][1], board[0][2])) {
		winner = board[2][0];
	}

	let openSpots = 0;
	for (let i = 0; i < 3; i++) {
		for (let j = 0; j < 3; j++) {
			if (board[i][j] == '') {
				openSpots++;
			}
		}
	}

	if (winner == null && openSpots == 0) {
		return 'tie';
	} else {
		return winner;
	}
}

function randomTurn() {
	var random = Math.floor(Math.random() * Math.floor(2));
	
	if(random == 0) {
		ai = "x"
		human = "o"

		scores = {
			x: 1,
			o: -1,
			tie: 0
		};
		turn = ai
		bestMove();
	} else {
		human = "x"
		ai = "o"

		scores = {
			o: 1,
			x: -1,
			tie: 0
		};
		turn = human
		return;
	}
}

function checkWin() {
	var check = checkWinner();
	if (check != null) {
		console.log("Winner is: " + check)
		end_game = true

		if (check == human) {
			const you_lost = document.getElementById("you_lost");
			you_lost.innerHTML = "You Won!"
			you_lost.classList.add("animated_text");
			setTimeout(function(){ you_lost.classList.remove("animated_text"); you_lost.innerHTML = "" }, 3000);

		} else if (check == ai) {
			const you_lost = document.getElementById("you_lost");
			you_lost.innerHTML = "Minimax Won."
			you_lost.classList.add("animated_text");
			setTimeout(function(){ you_lost.classList.remove("animated_text"); you_lost.innerHTML = "" }, 3000);

		} else {

			const you_lost = document.getElementById("you_lost");
			you_lost.innerHTML = "It's a Tie."
			you_lost.classList.add("animated_text");
			setTimeout(function(){ you_lost.classList.remove("animated_text"); you_lost.innerHTML = "" }, 3000);
		}

		return
	}
}


function cell_click(cell) {
	var id = cell.id.split("-");
	id = [parseInt(id[0]), parseInt(id[1])];

	if (turn != human) {
		return;
	}

	if (board[id[0]][id[1]] == "" && end_game == false) {
		cell.classList.add(human);
		board[id[0]][id[1]] = human;
		checkWin();
		turn = ai
		setTimeout(bestMove, 1000)
	}
}

function reset_game() {
	end_game = false
	board_creator();
	randomTurn();
}

reset_game()