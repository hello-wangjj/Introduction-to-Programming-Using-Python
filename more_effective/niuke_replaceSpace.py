def replaceSpace(s):
    # write code here
    target = ''
    for i in s:
        if i != ' ':
            target += i
        else:
            target += '%20'
    return target
print(replaceSpace('We Are Happy.'))
