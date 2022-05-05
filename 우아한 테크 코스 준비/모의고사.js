function sos(answers) {
  const answer1 = { list: [1, 2, 3, 4, 5], length: 5 };
  const answer2 = { list: [2, 1, 2, 3, 2, 4, 2, 5], length: 8 };
  const answer3 = { list: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], length: 10 };
  const answers_arr = [answer1, answer2, answer3];
  const answer_len = answers.length;

  const result = answers_arr.map((obj) => {
    let n = parseInt(answer_len / obj.length) + 1; // 자바스크립트에서 몫구하기 에러
    let new_list = [];
    for (let i = 0; i < n; i++) {
      new_list = new_list.concat(obj.list); // concat 에러
    }
    let sum = 0;
    for (let i = 0; i < answer_len; i++) {
      if (answers[i] == new_list[i]) sum++;
    }
    return sum;
  });

  for (let i = 1; i < 4; i++) {
    result[i - 1] = [i, result[i - 1]];
  }
  result.sort((a, b) => {
    return b[1] - a[1];
  });
  if (result[0][1] == result[1][1]) {
    if (result[1][1] == result[2][1]) {
      return result.map((arr) => arr[0]);
    } else {
      return [result[0][0], result[1][0]];
    }
  } else {
    return [result[0][0]];
  }
}

console.log(sos([1, 2, 3, 4, 5]));
