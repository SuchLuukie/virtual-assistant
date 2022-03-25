const rows = 10;
const cells = 15;
const table = document.getElementById("table");
const bombs = 30;
const open_to_win = rows * cells - bombs

function board_creator() {
	table.innerHTML = ""

	for (i = 0; i < rows; i++) {
		var row = table.insertRow(i);
		for (j = 0; j < cells; j++) {
			var cell = row.insertCell(j);
			cell.classList.add("normal");
			cell.id = i + "-" + j;
			cell.onclick = function() {cell_click(this)}
		}
	}
}

function bomb_creator() {
	var bomb_board = [];

	for (i = 0; i < rows; i++) {
		bomb_board.push([]);
		for (j = 0; j < cells; j++) {
			bomb_board[i].push(false);
		}
	}
	
	for (i = 0; i < bombs; i++) {
		var row_number = Math.floor(Math.random() * Math.floor(rows));
		var cell_numer = Math.floor(Math.random() * Math.floor(cells));

		if (bomb_board[row_number][cell_numer] != true) {
			bomb_board[row_number][cell_numer] = true;
		} else {
			i--;
		}
	}
	return bomb_board;
}

function flag_creator() {
	var flag_board = [];

	for (i = 0; i < rows; i++) {
		flag_board.push([]);
		for (j = 0; j < cells; j++) {
			flag_board[i].push(false);
		}
	}
	return flag_board;
}

function reset_game() {
	board_creator();
	bomb_board = bomb_creator();
	flag_board = flag_creator();
	loss = false;
	opened_cells = 0;
	flags = 0
	tracking_open_cells = [];
}

function flag_listener() {
	table.addEventListener('contextmenu', cell => {
		cell.preventDefault();
		if (loss == true) {
			return;
		}

		if (cell.target.className == "normal") {
			cell.target.classList.remove(cell.target.className);
			cell.target.classList.add("flag");
			flag_flipper(cell.target.id.split("-"));
			flags++;

		} else if (cell.target.className == "flag") {
			cell.target.classList.remove(cell.target.className);
			cell.target.classList.add("normal");
			flag_flipper(cell.target.id.split("-"));
			flags--;

		} else {
			return;
		}
		check_win()
	});
}

function flag_flipper(id) {
	flag_board[id[0]][id[1]] = !flag_board[id[0]][id[1]]
}

function check_win() {
	if (opened_cells == open_to_win && flags == bombs) {
		const you_lost = document.getElementById("you_lost");
		you_lost.innerHTML = "You Won!"
		you_lost.classList.add("animated");
		setTimeout(function(){ you_lost.classList.remove("animated"); you_lost.innerHTML = "" }, 3000);
	}
}

function loss_func() {
	const you_lost = document.getElementById("you_lost");
	you_lost.innerHTML = "You Lost."
	you_lost.classList.add("animated");
	setTimeout(function(){ you_lost.classList.remove("animated"); you_lost.innerHTML = "" }, 3000);
}

function cell_click(cell) {
	var id = cell.id.split("-");
	id = [parseInt(id[0]), parseInt(id[1])];

	if (loss == true || check_if_flag(id) == true) {
		return;
	}
	
	if (check_if_bomb(id) == true) {
		uncover_bombs();
		loss = true;
		loss_func();

	} else if (cell.className == "normal") {
		open_cell(id);
	} else {
		open_cell_flags(id);
	}
}

function open_cell_flags(id) {
	if (flags_around_cell(id) == bombs_around_cell(id)) {
		var non_flags = non_flags_around_cell(id);
		for (i = 0; i < non_flags.length; i++) {
			if (check_if_bomb(non_flags[i]) == true) {
				loss = true
				uncover_bombs()
				loss_func()
				return
			}
		}
		non_flags.forEach(open_cell)
	}
}

function check_if_bomb(cell_id) {
	if (bomb_board[cell_id[0]][cell_id[1]] == true) {
		return true;
	}
	return false;
}

function uncover_bombs() {
	for (i = 0; i < rows; i++) {
		for (j = 0; j < cells; j++) {
			if (bomb_board[i][j] == true) {
				var cell = document.getElementById(i + "-" + j)
				cell.classList.remove(cell.className)
				cell.classList.add("bomb")
			}
		}
	}
}

function check_if_flag(cell_id) {
	if (flag_board[cell_id[0]][cell_id[1]] == true) {
		return true;
	}
	return false;
}

function open_cell(id) {
	if (Math.min.apply(Math, id) > -1) {
		if (id[0] < rows && id[1] < cells) {
			if (tracking_open_cells.includes(id.join()) == false) {
				tracking_open_cells.push(id.join());

				var bombs_around = bombs_around_cell(id);
				var cell = document.getElementById(id[0] + "-" + id[1]);
				cell.classList.remove(cell.className);
				cell.classList.add("a" + bombs_around);
				opened_cells++;

				check_win()

				if (bombs_around == 0) {
					open_surrounding_cells(id)
				}
			}
		}
	}
}

function bombs_around_cell(id) {
	const surrounding = [[id[0]-1, id[1]-1], [id[0]-1, id[1]], [id[0]-1, id[1]+1], [id[0], id[1]-1], [id[0], id[1]+1], [id[0]+1, id[1]-1], [id[0]+1, id[1]], [id[0]+1, id[1]+1]];
	var count = 0;

	for (i = 0; i < surrounding.length; i++) {
		try {
			var bomb = bomb_board[surrounding[i][0]][surrounding[i][1]];
		}
		catch(err) {
			var bomb = false;
		}
		if (bomb == true) {
			count++;
		}
	}
	return count;
}

function flags_around_cell(id) {
	const surrounding = [[id[0]-1, id[1]-1], [id[0]-1, id[1]], [id[0]-1, id[1]+1], [id[0], id[1]-1], [id[0], id[1]+1], [id[0]+1, id[1]-1], [id[0]+1, id[1]], [id[0]+1, id[1]+1]];
	var count = 0;

	for (i = 0; i < surrounding.length; i++) {
		try {
			var flag = flag_board[surrounding[i][0]][surrounding[i][1]];
		}
		catch(err) {
			var flag = false;
		}
		if (flag == true) {
			count++;
		}
	}
	return count;
}

function non_flags_around_cell(id) {
	const surrounding = [[id[0]-1, id[1]-1], [id[0]-1, id[1]], [id[0]-1, id[1]+1], [id[0], id[1]-1], [id[0], id[1]+1], [id[0]+1, id[1]-1], [id[0]+1, id[1]], [id[0]+1, id[1]+1]];
	var non_flags = [];

	for (i = 0; i < surrounding.length; i++) {
		try {
			var cell = flag_board[surrounding[i][0]][surrounding[i][1]];
			if (cell == false) {
				non_flags.push(surrounding[i])
			}
		}
		catch(err) {
			continue
		}
	}
	return non_flags
}


function open_surrounding_cells(id) {
	const surrounding = [[id[0]-1, id[1]-1], [id[0]-1, id[1]], [id[0]-1, id[1]+1], [id[0], id[1]-1], [id[0], id[1]+1], [id[0]+1, id[1]-1], [id[0]+1, id[1]], [id[0]+1, id[1]+1]];
	surrounding.forEach(open_cell)
}

flag_listener()
reset_game()