function solution(brown, yellow) {
  const len_carpet = brown + yellow;
  const carpet_arr = [];
  for (let i = 3; i <= Math.sqrt(len_carpet); i++) {
    if (len_carpet % i == 0) carpet_arr.push([parseInt(len_carpet / i), i]);
  }
  function calcu(w, l) {
    if ((l - 2) * (w - 2) == yellow) return true;
    return false;
  }
  return carpet_arr.filter((arr) => calcu(arr[0], arr[1]))[0];
}
