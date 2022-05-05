const clothes = [
  ["yellowhat", "headgear"],
  ["bluesunglasses", "eyewear"],
  ["green_turban", "headgear"],
];

const clothes_obj = clothes.reduce((result, value) => {
  result[value[1]] = result[value[1]] ? result[value[1]] + 1 : 2;
  return result;
}, {});

console.log(clothes_obj);
