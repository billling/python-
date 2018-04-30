#!/usr/bin/env python
#coding:utf-8

def find_file(*args):
    f1 = open("staff_table.txt", "r", encoding="utf-8")
    '''
    # 参考员工信息表中根据索引获取到的参数
    line = line.strip().split(',')
        staff_id = line[0]
        staff_name = line[1]
        staff_age = line[2]
        staff_phone = line[3]
        staff_dept = line[4]
        staff_enroll_date = line[5]
    '''
    opt_str = args[0][-2]  # 捕获 输入 sql 语句中的 大于、等于、like
    opt_num = args[0][-1]  # 捕获 输入 sql 语句中的 最后一位的数字或者字符
    opt_find = args[0][1]  # 捕获  输入 sql 语句中的 第二个字符
    count = 0
    line_effect = []
    if args[0][0] == 'find':
        print("这里用到是查找,此次查找匹配以下记录")
        if opt_str == ">":
            for line in f1:
                line = line.strip().split(',')
                if int(line[2]) > int(opt_num):
                    count += 1
                    line_effect.append(line)
            for l1 in line_effect:
                if opt_find == "*":
                    print(l1)
                else:
                    '''
                    opt_finds = opt_find.split(',')
                    print(opt_finds) # opt_finds 对应的是name 和 age ,对应文件中的索引分别是 l1[1] 和l1[2]
                   l1[1] = name
                   l1[2] = age
                    '''
                    opt_finds = opt_find.split(',')
                    if "name" in opt_finds and "age" in opt_finds:
                        print(l1[1],l1[2])
                    elif "age" in  opt_finds:
                        print(l1[2])
                    elif "name" in opt_finds :
                        print(l1[1])
                    else:
                        print("您输入的字段暂时无法提供查询")
                        exit()
            print("总共有%s 行数大于 %s,受影响的行数为%s"%(count,opt_num,count))
        elif opt_str == "=":
            for line2 in f1:
                line2 = line2.strip().split(',')
                if line2[4] == eval(opt_num): # 使用eval 让 opt_num 去掉双引号
                    count += 1
                    line_effect.append(line2)
            for l2 in line_effect:
                if opt_find == "*":
                    print(l2)
                else:
                    opt_finds = opt_find.split(',')
                    if "name" in opt_finds and "age" in opt_finds:
                        print(l2[1], l2[2])
                    elif "age" in opt_finds:
                        print(l2[2])
                    elif "name" in opt_finds:
                        print(l2[1])
                    else:
                        print("您输入的字段暂时无法提供查询")
                        exit()

            print("总共有%s 行数等于 %s,受影响的行数为%s"%(count, opt_num, count))
        elif opt_str == "like":
            for line3 in f1:
                line3 = line3.strip().split(',')
                if eval(opt_num) in line3[5]: #使用eval 让 opt_num 去掉双引号
                    count += 1
                    line_effect.append(line3)
            for l3 in line_effect:
                if opt_find == "*":
                    print(l3)
                else:
                    opt_finds = opt_find.split(',')
                    if "name" in opt_finds and "age" in opt_finds:
                        print(l3[1], l3[2])
                    elif "age" in opt_finds:
                        print(l3[2])
                    elif "name" in opt_finds:
                        print(l3[1])
                    else:
                        print("您输入的字段暂时无法提供查询")
                        exit()
            print("总共有%s 行数等于 %s,受影响的行数为%s" % (count, opt_num, count))
        else:
            print("您输入有误，目前只支持 大于 等于 like 的匹配")
    else:
        print(" add 、del、UPDATE 等新功能暂不支持，目前只支持 find 查找")
while True:
    sql_cmd = input(" 请输入您需要查询的sql语句:>").strip()
    if not sql_cmd: continue
    elif sql_cmd == 'q':
        break
    else:
        cmd = sql_cmd.split(' ')
        if len(cmd) < 8:  # 检测 sql 语句的 合法性
            print("您输入的sql 语句不合法,请重新输入")
            continue
        else:
            find_file(cmd)