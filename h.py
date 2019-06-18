import re

#
# l=['timeeee','abc','_abs','123','f1',"$#daw","123ADF"]
#
# #合法
# for i in l:
#     re.findall('^[_a-zA-Z][_0-9a-zA-Z]*$',i)
#     print(i)
#
# print(re.findall('-*[1-9][0-9]*',"4,-5,--405,64,69,879,dwqe"))
#
# print(re.findall('1[0-9]','15456786746'))
# print(re.findall('\D+','213123:213,sawqe1,2131'))

# print(re.findall('\w+\s+',"eqweqweqwe  "))
# print(re.findall('-?\d+\.?/?\d*%?',"15.555"))  #(\.?  表示点可以有1个或者0个,没有\ .代表任意字符)
# print(re.findall(r'\$\d+',"工资$100"))
# print(re.findall(r'\[.+?]',"hello[a#@de] world[word]"))   #(['[a#@de]', '[word]'])
#
# print(re.search(r'(ab)+',"ababababab").group())
# print(re.search(r'(王|李)\w{1,3}',"王者荣耀").group())
# print(re.findall(r", address is \w{4}\.\w{4}\.\w{4}",', address is 10f3.116c.e6a7'))
# print(re.findall(r"Internet address is \d+\.\d+\.\d+\.\d+\/\d+",
#                                         'Internet address is 192.168.100.254/24'))

"""
regex1 示例
"""

import re

s = "2019年,建国70年"
pattern = r'\d+'

# # 返回迭代器
# it = re.finditer(pattern,s)
#
# # print(dir(it.__next__()))
# for i in it:
#   print(i.group()) # 获取match对象对应内容
#
# # 完全匹配
# m = re.fullmatch(r'\w+','Jame1')
# print(m)

# 匹配开始位置
# m = re.match(r"[A-Z]\w*","Hello World")
# print(m)

# # 匹配第一处
# m = re.search(r"[A-Z]\w*"," Hello World")
# print(m)

'''
通过分析文档使用正则完成接口编写.从终端输入端口	名返回address地址
'''
import re

port_name = input("输入端口号：")

fd = open("ext.txt", 'r')

#找到port所在段
while True:
    data = ""
    for line in fd:
        if line != "\n":
            data += line
        else:
            break   #本段全部读取完毕

    # 结尾退出大循环
    if not data:
        print("没有这个端口")
        break

    result=re.match(port_name,data)  #第一个满足的
    if result:
        #pattern=r'[0-9a-f]{4}\.[0-9][4-f]{4}\.[0-9][4-f]{4}'
        pattern=r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
        try:
            address=re.search(pattern,data).groups()
            print(address)
        except:
            print("Error")
        break
