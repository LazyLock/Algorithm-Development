function solution(n, computers) {
  var answer = 0;
  var isVisited = [];

  for(var i =0; i <n; i++) {
      isVisited.push(false);
  }

  var DFS = function(computers, i) {
      if(isVisited[i]) { return; }
      isVisited[i] = true;

      for(var j = 0; j < computers.length; j++) {
          if(computers[i][j] === 1) {
              DFS(computers, j);
          }
      }
  }

  for(var i = 0; i < n; i++) {
      if(!isVisited[i]) {
          answer++;
          DFS(computers, i);
      }
  }

  return answer;
}