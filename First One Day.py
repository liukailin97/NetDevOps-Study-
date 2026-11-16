#查询ip在那个楼层，如果超出楼层数显示ip不存在
floor = input('please input your floor\n')
floor_list = floor.split('.')
floor_num = int(floor_list[2])
if floor_num > 10:
        print("这个ip不存在")
else:
        print('This address blong to ' + floor_list[2] + '楼')
#split()将字符串转换为列表
#join()将列表转换为字符串
#strip()将字符串中开头和结尾移除指定字符，默认移除空格
