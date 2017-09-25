import sys

__author__ = 'wangj'
__date__ = '2017/09/18 20:05'


def main():
    v = sys.stdin.readline().strip()
    w = sys.stdin.readline().strip()
    v_ls = v.split(' ')
    w_ls = w.split(' ')
    v_w = {}
    v_w_count = {}
    for v_l, w_l in zip(v_ls, w_ls):
        if v_l not in v_w:
            v_w[v_l] = 0
            v_w[v_l] += int(w_l)
            v_w_count[v_l] = 0
        else:
            v_w[v_l] += int(w_l)
            v_w_count[v_l] += 1
    v_w_sort = sorted(v_w.items(), key=lambda item: item[1], reverse=True)
    v_w_count_sort = sorted(v_w_count.items(), key=lambda item: item[1], reverse=True)
    max_item = v_w_sort[0][1]
    # 最大的几个人
    count = []
    for i in v_w_sort:
        if i[1] == max_item:
            count.append(i[0])
    # 最大的几个数
    v_w_count_sort_list = [x[0] for x in v_w_count_sort]

    v_w_index = []
    for i in count:
        v_w_index.append(v_w_count_sort_list.index(i))
    min_item = min(v_w_index)
    print(v_w_count_sort_list[min_item])


if __name__ == '__main__':
    main()
