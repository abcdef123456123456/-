import os
print('hello.winos')
print('请输入help查看所有命令')
a = os.getcwd()
while True:
    a = os.getcwd()
    b = input(a)
    if b == 'cd':
        c = input('路径：')
        a = os.chdir(c)
    if b == 'md':
        c = input('路径（记得加\）：')
        d = input('文件或文件夹名：')
        e = input('方法（1.填文件，2.填文件夹）：')
        if e == '1':
            f = open(c + d, 'w+')
            f.close()
        if e == '2':            
            os.makedirs(c + d)
    if b == 'dir':
        c = input('路径：')
        d = os.listdir(c)
        print(d)
        c = input('路径：')
        d = input('文件或文件夹名')
        e = input('方法（1.删文件夹，2.删文件）')
        if e == '1':
            os.remove(d)
        if e == '2':
            os.rmdir(d)
    if b == 'help':
        print('cd:跳转到一个目录,md:新建文件或文件夹,dir:查看此目录的文件,del:删除文件或文件夹')
    


        


