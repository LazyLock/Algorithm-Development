function solution(board, moves) {
  const board_obj = {};
  for (let i = 1; i <= board.length; i++) {
    board_obj[i] = [];
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      let board_one = board[i][j];
      if (board_one) {
        board_obj[j + 1].unshift(board_one);
      }
    }
  }

  let result = 0;
  const basket = [];
  moves.forEach((value) => {
    let board_pop = board_obj[value].pop();
    if (board_pop) {
      if (basket.legnth == 0) {
        basket.push(board_pop);
      } else {
        let last_one = basket[basket.length - 1];
        if (last_one == board_pop) {
          result += 2;
          basket.pop();
        } else {
          basket.push(board_pop);
        }
      }
    }
  });
  return;
}

const board1 = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];
const monve = [1, 5, 3, 5, 1, 2, 1, 4];

console.log(solution(board1, monve));
