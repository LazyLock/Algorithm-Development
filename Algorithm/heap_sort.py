n = int(input('정렬할 리스트 원소의 수를 입력하시오: '))
seq = []

for _ in range(n):
    a = int(input('리스트의 원소를 입력하시오: '))
    if a == - 1:
        break
    seq.append(a)


def heap_sort(seq):
    for i in range(n // 2 - 1, -1, -1):  # 리프 노드가 아닌 노드들의 인덱스부터 보면 효율성 증가.
        heapify(seq, i, n)
    for j in range(n - 1, 0, -1):  # 제일 마지막 인덱스부터 루트 노드 직전 인덱스까지.
        seq[0], seq[j] = seq[j], seq[0]  # heapify로 인해서 루트노드는 최대값이며, 제일 끝값과 바꾸어주고 0 ~ j까지 heapify로 정렬.
        heapify(seq, 0, j)
    return seq


def heapify(seq, i, size):  # heapify는 정형화된 함수로서, 인수 i로부터 자식노드들을 재귀 순회하며 느슨한 정렬을 유지하게 함.
    left = i * 2
    right = i * 2 + 1
    biggest = i

    if left < size and seq[left] > seq[biggest]:
        biggest = left
    if right < size and seq[right] > seq[biggest]:
        biggest = right
    if biggest != i:
        seq[biggest], seq[i] = seq[i], seq[biggest]
        heapify(seq, biggest, size)


print(heap_sort(seq))