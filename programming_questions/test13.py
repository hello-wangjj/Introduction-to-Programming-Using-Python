import sys

__author__ = 'wangj'
__date__ = '2017/09/26 09:28'


def main():
    m_n = (sys.stdin.readline().strip()).split(' ')
    m = int(m_n[0])
    n = int(m_n[1])
    count = 0
    last_used_dict = {}
    last_used_ls = []
    while True:
        command_all = (sys.stdin.readline().strip()).split(' ')
        command = command_all[0]
        command_key = command_all[1]
        if command == 'put':
            command_value = command_all[2]
            if len(last_used_ls) < m:
                last_used_ls.append(command_key)
                last_used_dict[command_key] = command_value
            else:
                if command_key in last_used_dict.keys():
                    last_used_ls.remove(command_key)
                    last_used_ls.append(command_key)
                    del last_used_dict[command_key]
                    last_used_dict[command_key] = command_value
                else:
                    temp = last_used_ls.pop(0)
                    last_used_ls.append(command_key)
                    del last_used_dict[temp]
                    last_used_dict[command_key] = command_value
        elif command == 'get':
            if command_key in last_used_dict.keys():
                print(last_used_dict[command_key])
                temp = last_used_ls.pop()
                last_used_ls.append(temp)
            else:
                print('null')

        count += 1
        if n == count:
            break


if __name__ == '__main__':
    main()
