function solution(n, computers) {
  let answer = 0;
  const visit = Array.from({ length: n }, () => false);

  function dfs(tree, node, visit) {
    visit[node] = true;
    tree[node].forEach((value, index) => {
      if (index !== node) {
        if (!visit[index] && tree[node][index] == 1) dfs(tree, index, visit);
      }
    });
    return;
  }
  visit.forEach((val, idx) => {
    if (!val) {
      answer++;
      dfs(computers, idx, visit);
    }
  });

  return answer;
}
