const genres = ["classic", "pop", "classic", "classic", "pop"];
const plays = [500, 600, 150, 800, 2500];

function solution(genres, plays) {
  const answer = [];
  const genres_obj = genres.reduce((result, value, index) => {
    if (!result[value]) result[value] = [];
    return result;
  }, {});

  plays.forEach((value, index) => {
    let key = genres[index];
    genres_obj[key].push({ idx: index, play_time: value });
  });

  const sum_arr = [];

  for (let key in genres_obj) {
    let genres_obj_arr = genres_obj[key];
    genres_obj_arr.sort((a, b) => {
      return b.play_time - a.play_time;
    });
    let sum = 0;
    for (let obj of genres_obj_arr) {
      sum += obj.play_time;
    }
    sum_arr.push({ genres: key, sum: sum });
  }

  sum_arr.sort((a, b) => {
    return b.sum - a.sum;
  });

  for (let sum_obj of sum_arr) {
    let key = sum_obj.genres;
    let genres_obj_arr = genres_obj[key];
    answer.push(genres_obj_arr[0].idx);
    if (genres_obj_arr.length >= 2) answer.push(genres_obj_arr[1].idx);
  }

  return answer;
}

console.log(solution(genres, plays));
