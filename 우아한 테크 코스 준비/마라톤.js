function solution(participant, completion) {
  const obj = {}
  for (let runner1 in participant) {
      obj[runner1] = obj[runner1] ? obj[runner1] + 1 : 1;
      console
  }
  for (let runner2 in completion) {
      obj[runner2] -= 1
  }
  for (let key in obj) {
      if (obj[key] == 1) {
          return key
      }
  }
}