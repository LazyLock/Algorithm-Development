function solution(numbers) {
  let answer = 0;
  const len_numbers = numbers.length;
  const numbers_arr = [...numbers]; // ['1','1','0']
  let result_arr = [];

  for (let i = 1; i < len_numbers + 1; i++) {
    result_arr = result_arr.concat(
      permutation(numbers_arr, i).map((arr) => parseInt(arr.join("")))
    );
  }

  const result_set = new Set(result_arr);
  for (let v of result_set) {
    if (is_prime(v)) answer += 1;
  }

  function permutation(arr, num) {
    const result = [];
    if (num == 1) return arr.map((v) => [v]);
    arr.forEach((value, index, seq) => {
      let pick = value;
      let rest_arr = seq.filter((_, idx) => index != idx);
      const permutation_arr = permutation(rest_arr, num - 1);
      const combine_arr = permutation_arr.map((v) => [pick, ...v]);
      result.push(...combine_arr);
    });
    return result;
  }

  function is_prime(n) {
    if (n < 2) return false;
    if (n == 2) return true;
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) return false;
    }
    return true;
  }

  return answer;
}

console.log(solution("110"));
