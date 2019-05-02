import unittest


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


class BubbleTest(unittest.TestCase):

    def test(self):
        self.assertEqual([1, 2, 4, 6, 7, 8, 9], bubble_sort([6, 8, 9, 1, 4, 7, 2]))


if __name__ == '__main__':
    a = [6, 8, 9, 1, 4, 7, 2]
    print(bubble_sort(a))
