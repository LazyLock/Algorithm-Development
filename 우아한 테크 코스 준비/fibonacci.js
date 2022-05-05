function* fibonacci() {
  let fn1 = 0, fn2 = 1;
  while (true) {
    let fnew = fn1 + fn2;
    fn1 = fn2;
    fn2 = fnew;
    reset = yield fn1;
    if (reset) {
      fn1 = 0;
      fn2 = 1;
    }
  }
}

const iter = fibonacci();
for (let i = 0;i<10;i++) {
  console.log(iter.next().value);
}

// 예상 시나리오
// 1 1 