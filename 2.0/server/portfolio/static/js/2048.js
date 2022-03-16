const table = document.getElementById("table");
const rows = 4;
const cells = 4;

function create_table() {
	table.innerHTML = "";
	board = [];

	for(i = 0; i < rows; i++) {
		var row = table.insertRow(i);
		board.push([]);

		for(j = 0; j < rows; j++) {
			board[i].push(0);
			var cell = row.insertCell(j);
			cell.id = i + "-" + j;
		}
	}
}

function check_loss() {
	var total = rows * cells;
	var count = 0;

	for (i = 0; i < rows; i++) {
		for (j = 0; j < cells; j++) {
			if (board[i][j] != 0) {
				count++;
			}
		}
	}
	loss = count == total;
	if (count == total) {
		loss_func()
	}
}

function update_board() {
	for (i = 0; i < rows; i++) {
		for (j = 0; j < cells; j++) {
			var location = i + "-" + j;
			var cell = board[i][j];

			var element = document.getElementById(location);
			element.removeAttribute("class");

			if (cell == 0) {
				element.innerHTML = "";
			} else {
				element.innerHTML = cell;
				element.classList.add("a" + cell);
			}
		}
	}
}

function random_int() {
	var empty_cells = [];

	for (i = 0; i < rows; i++) {
		for (j = 0; j < cells; j++) {
			var location = [i, j];
			var cell = board[i][j];

			if (cell == "") {
				empty_cells.push(location);
			}
		}
	}

	var random_int = Math.floor(Math.random() * Math.floor(empty_cells.length));
	var random_cell = empty_cells[random_int];

	var choice = [2, 4];
	var random_int = Math.floor(Math.random() * Math.floor(choice.length));
	var choice = choice[random_int];

	board[random_cell[0]][random_cell[1]] = choice;
	update_board();
}


function move(array) {
	var mergedDict = [];
	for (k = 0; k < rows; k++) {
		for (i = 0; i < rows; i++) {
			for (j = 0; j < cells; j++) {
				var location = [i, j];
				var cell = board[i][j];

				try {
					var cell_above = board[i + array[0]][j + array[1]];
					console.log(cell)

					if (cell_above == cell) {
						if (!mergedDict.includes(location)) {
							var new_int = cell + cell_above;
							board[i + array[0]][j + array[1]] = new_int;
							board[i][j] = 0;

							mergedDict.push([i + array[0], j + array[1]]);
						}
					} else if (cell_above == 0) {
						board[i + array[0]][j + array[1]] = cell;
						board[i][j] = 0
					}
				}
				catch(err) {
					continue
				}
			}
		}
	}
	update_board()
	random_int()
}

function loss_func() {
	const you_lost = document.getElementById("you_lost");
	you_lost.innerHTML = "You Lost."
	you_lost.classList.add("animated");
	setTimeout(function(){ you_lost.classList.remove("animated"); you_lost.innerHTML = "" }, 3000);
}

document.onkeydown = function(e) {
	if (loss == false) {
	    switch (e.keyCode) {
	        case 37:
	            move([0, -1]);
	            break;
	        case 38:
	            move([-1, 0]);
	            break;
	        case 39:
	            move([0, 1]);
	            break;
	        case 40:
	            move([1, 0]);
	            break;
	    }
	}
};


function reset_game() {
	loss = false;
	create_table();
	//random_int();
	//random_int();
	board[0][0] = 2
	board[0][1] = 2
	board[0][2] = 4
	update_board()
}
array = [[1, 2], [3, 3], [4, 4]];
console.log(array.includes([1, 2]))
reset_game()