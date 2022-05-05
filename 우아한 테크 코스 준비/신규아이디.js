let new_id = "bbbb";
let new_id2 = "aa...a.a...a...a.......";

while (true) {
  if (new_id.includes("b")) {
    new_id = new_id.replace("b", "a");
  } else {
    break;
  }
}

while (true) {
  if (new_id2.includes("..")) {
    new_id2 = new_id2.replace("..", ".");
  } else {
    break;
  }
}

console.log(new_id);
console.log(new_id2);
