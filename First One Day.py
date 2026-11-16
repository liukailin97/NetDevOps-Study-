#查询ip在那个楼层，如果超出楼层数显示ip不存在
#split()将字符串转换为列表
#join()将列表转换为字符串
#strip()将字符串中开头和结尾移除指定字符，默认移除空格
#floor = input('please input your floor\n')
#floor_list = floor.split('.')
#floor_num = int(floor_list[2])
#if floor_num > 10:
 #       print("这个ip不存在")
#else:
#        print('This address blong to ' + floor_list[2] + '楼')
#startswith()用来判断字符串是否以给定的字符串开头
#endswith()来判断字符串是否以给定的字符串结尾
#isdigit() 就 是 用 来 判 断 字 符 串 是 否 为整 数
#isalpha() 用 来 判 断 字 符 串 是 否 为 文 字
ip = input('请输入ip地址\n')
floor_num = ip.startswith('2')
if floor_num ==True:
        print('这个ip属于此范畴')
else:
        print('不属于此范畴')
print(floor_num)