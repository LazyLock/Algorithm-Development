

function permu1(arr, num) {
  const result = [];
  if (num == 1) {
    return arr.map((v) => [v]);
  }
  arr.forEach((value, idx, arr) => {
    let select = value;
    let rest_arr = arr.filter((_, index) => {
      return index !== idx;
    });
    const permu1_arr = permu1(rest_arr, num - 1);
    const combine = permu1_arr.map((v) => [select, ...v]);
    result.push(...combine);
  });
  return result;
}
