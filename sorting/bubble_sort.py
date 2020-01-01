def bubble_sort(seq):
    size = len(seq) -1
    for num in range(size, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                temp = seq[i]
                seq[i] = seq[i+1]
                seq[i+1] = temp
    return seq
def test_bubble_sort(module_name='this module'):
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert(bubble_sort(seq) == sorted(seq))
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))
if __name__ == '__main__':
    test_bubble_sort()