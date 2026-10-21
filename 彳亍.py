# 1 .title(所有首字母大写), .upper, .lower, .capitalize(首字母大写)
#   .strip(默认参数为空格,只看最两边,不看中间), .lstrip(删开头空格), .rstrip(删结尾空格)
#   "\t(Tap)", "\n(Enter)", "\b(退格)", "\0(空格)","\\(\)" r可以取消\的特殊性
#   占位符:%d(十进制整数), %s(字符串), %f(浮点数), %.2f(保留两位小数)
#   Ctrl + / = 快速注释, Ctrl + z = 撤回, Ctrl + Shift + z = 重做, Ctrl + a = 全选
#   Ctrl + F = 查找内容
#   Alt + Shift + Enter = 删除形参
#   类中方法相差一行，不同用法差两行，结尾空一行
#   多选后Tap 一键缩进 多选后Shift+Tap 一键取消缩进
from random import *


name = "enter your name,thanks: "
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print("Hello %s,would you like to learn some Python today?" % name)
print("世界第一吃货殿下说:'小笼包最好吃!',I believe her.But\n\tI love her better.")
name_2 = "\tpycharm\ty\\y\\ds\t!!?\b"
print(name_2)
print(name_2.rstrip())
print(name_2.lstrip())
print(name_2.strip())
print("++d d me+ ++".strip("+"))
print(str(3 + 5) + "\n" + str(2 * 4) + "\n" + str(int(8 / 1)) + "\n" + str(2 ** 3))
try:
    digit_I_love_most = int(input("number:\n"))
    print("The digit I like most is %d" % digit_I_love_most)
except ValueError:
    print("I'm sad for you.Please give me an wet digit.Thanks")

# 2 list中可插入list
#   .pop(index 为空默认最后item), del item[index], .remove(item 只删除第一个指定的值,冇则报错), .clear()清空列表
#   .insert(index,item), .append(item)结尾添加
#   .print(end默认\n,即换行)
#   .split(sep=" ") 默认参数空格，将item沿所选参数分割为列表
#   .join(item) item每个后跟str
#   .index(str, num_始, num_终) 在范围中检索str出现位置,从0开始数,与num_始无关,冇则报错
#   .find(同index) 同index，冇则返回-1
#   .copy() 返回一个新list
Guests_list = ["洛天依", "gumi", "初音未来", "IA", ["镜音铃", "镜音连"]]
print(Guests_list[4])
print(Guests_list[4][0])
print("接下来", end="")
print("有些信要", end="发给MyFriends")
print(":")
famous_name = "世界第一吃货殿下"
message = "说:'小笼包最好吃!',I believe her.But\n\tI love her better."
print(famous_name + message)
print(message.split())
print(len(message))
print(len(message.split()))
try:
    print(message.index(".", 2, 7))
except ValueError:
    print("I'm happy to tell you that she isn't here,dull body.")
print(message.index("."))
print(message.find(".", 2, 7))
message = "There=are=four=messages= =""。"
print(message.split("="))
print("__".join(message))  # message中每一个元素(除最后一个)后跟"__"
for i in Guests_list:
    a = type(i)
    if a == list:
        for s in i:
            print("Dear " + str(s) + ".I'd like to invite you to my home to join in\
our soiree.Would you come?")
    else:
        print("Dear " + str(i) + ".I'd like to invite you to my home to join in\
our soiree.Would you come?")
Guests_list_pope = Guests_list.pop(-3)
del Guests_list[-1]
try:
    Guests_list.remove('初音未来')
except ValueError:
    print("ValueError: list.remove(x): x not in list")
print("I'm so sorry to hear that " + Guests_list_pope + " can't come\
 hear for the reason that she is ill.")
print("I'm so sorry to said that l is a worry,and l have to kill it!")
miku = "初音未来"
print("It's seems that " + miku + " has no free time to take part in the soiree...")
for i in Guests_list:
    print("We only remain " + i + "!", end="\n\n")
print("But we find a bigger table,so,hey,we invited more!")
Guests_list.append("镜音铃")
Guests_list.insert(-1, "言和")
for i in Guests_list[1:]:
    print("Dear " + str(i) + ".I'd like to invite you to my home to join in\
 our soiree.Would you come?")
    print("最终" + str(i) + "出现了,")
print("当然还有我们的小洛.", end="\n\n")
print("Today night is full of happiness!")

names = ["洛天依", "乐正绫", "言和", "镜音铃", "miku", "gumi"]
for name_bianli in names:
    print(name_bianli)
for name_bianli in names:
    print("早上好啊," + name_bianli + ". 昨晚又熬夜了吗?小家伙.")
names[0] = "小洛"
names.append("巡音流歌")
names.insert(2, "IA")
print(names)
del names[-1]
names_pope = names.pop(2)
names.remove('gumi')
print(names)
print(names_pope)

a = ["殿下", "喜欢", "吃小笼包"]
b = a
a[1] = "不讨厌"  # 只修改a
print(a)
print(b)  # a==b
b = a.copy()
a[1] = "讨厌"
print(a)  # 只修改a
print(b)  # a!=b

# 3 .sort(字母顺序排,num小到大), .sort(reverse=True)(字母倒序排_从大到小,永久)
#   .sorted(item 临时排), sorted(item, reverse=True)
#   .reversed(返回逆序) = str[::-1]
#   len(item 长度)
#   .count("a") 数a出现了多少次,返回int,区分大小写
#   .replace("a", "b") 将a替换为b
#   .center(num, "...") 输入num及填充str,item's num不足用str填充,str默认参数为空格
#    "..{}..".format("...") str替空槽{},槽中可写数字，默认顺序012,如果有num则所有{}都要有num
#   {0：num} num为输出长度,不够空格凑(默认)
#   {0：^num} 居中对齐 <左对齐 >右对齐
#   {0：$^num} 用$进行填充
#   {0：num,} ,为千分符,仅限int可用,千分符包括在num中
#   {0: num,.3f} 保留三位小数
#   {0: num,.3} 保留三字符长度,int或str都行
#   {0: b/c/d/o/x/X} b整数二进制形式 c(chr)输出Unicode d整数十进制 o整数八进制 x整十六进制小写 X大写
#   {0: e/E/f/%} 浮点数 e指数形式e小写 E大写 f正常写 %百分比
a = ["a", "f", "v d", "bfg", "bf", "bf"]
b = "in in in "
print(a.count("bf"))
print(type(a.count("bf")))  # <class 'int'>
print(b.count(" "))
print(b.count("n"))
print(b.count(""))  # 结果为字符串个数+1,包括空格
print(b.replace("i", "o"))
print(b.center(16, "+"))  # 不对称则右边多一个
a.sort()
print(a)
a.sort(reverse=True)
print(a, end="\n\n")
print(a)
print(sorted(a))
print(sorted(a, reverse=True))
print(a)
a.reverse()
print(a)
print((len(a)))
print("{1}好，卬{0}一件事情与你商量。".format("若", "有"))
print("{0}好，卬{0}一件事情与你商量。".format("若"))  # 若无0,IndexError报错,缺少实参
print("{:5}Go".format("My"))  # 5指的是My的长度,与Go无关,不够用空格填充 输出结果:My   Go
print("{:^5}Go".format("My"))  # 输出结果: My  Go
print("{:<5}Go".format("My"))  # 输出结果:My   Go
print("{:>5}Go".format("My"))  # 输出结果:   MyGo
print("{:$^5}Go".format("My"))  # 输出结果:$My$$Go
print("{0:{1}^{2}}Go".format("My", "$", 5))  # 输出结果同上.012漏写报错,不写or全写不报
print("宇宙答案{:>19,}".format(42424242424242))  # 输出结果:宇宙答案 42,424,242,424,242  int+,+空格=19
print("宇宙答案{:>19,.4f}".format(424242.42416))  # 输出结果:宇宙答案       424,242.4242  四舍六入
print("{:.4}".format("余明天寄给你一件东西."))  # 输出结果:余明天寄
print("{0:b}, {0:c}, {0:d}, {0:o}, {0:x}, {0:X}".format(77))  # 输出结果:1001101, M, 77, 115, 4d, 4D
print("{0:e}, {0:E}, {0:f}, {0:%}".format(3.1415))  # 输出结果:3.141500e+00, 3.141500E+00, 3.141500, 314.150000%
print("宇宙答案{0:3>20,.4%}".format(52.52))  # 注意顺序: 序号012 : 填充 排列<^> 字符num 千分符, 保留位数.num 浮点数eEf%

# 4 for item in items:  (注意冒号,别忘,还有缩进)
#       print(item)
cats = ["皮罗", "小黑", "威尔伯"]
print("你好,我是楠宁.")
for cat in cats:
    print("Welcome," + cat)
print("Thanks.")

# 5 range(2, 8, 3)(起始2, 结束8-1, 相隔3_可无), range(num)(0到num-1)
#   list(转化为列表)
#   min(), max()  -1<0<9<A<Z<a<z<aa<ab<abc<ac
#   sum()
#   切片/复制[起始:结束:步长_可无](0:5,即01234,包括空格)(0:,即0-最后)(:7:2,即0246)(::-1,逆序排列)
#   abs(x) x的绝对值,若复数,返回摸(根号平方和)
#   divmod(a, b) 返回a,b的商和余数
#   pow(a, b) 返回a的b次方
#   round(num, x) 四舍六入五成双,保留x位小数
#   all(items) 全为真True,空为True,否则False
#   any(items) 任意真True,空为True,否则False
#   0 False,0外任一num True
#   eval(str) 去除str的双引号
#   exec(str) 去除str语句的双引号(用得少)
for i in range(1, 8):
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end="\t")
for i in range(1, 8, 3):
    print(i, end=".")
iq = list(range(1, 8))
print(iq)
print(iq[0])
print(iq[:2])
print(iq[0:])
print(iq[::-1])
print(iq[-2:])
print(iq[3:5])
iq_me = iq[:]
print(iq_me)
print(iq)
print(iq[0::3])
print(min(iq))
print(max(1, 9, 5))
print(sum(iq))
iqs = []
for i in range(1, 4):
    iqs.append(i ** 2)
print(iqs)
iqs = [i ** 2 for i in range(1, 4)]
print(iqs)
a = ["zb", "0", "A", "-1", "z", "za", "zc", "zaa", "zca"]  # -1<0<9<A<Z<a<z<aa<ab<abc<ac
print(max(a))
print(min(a), end="\n")
print(abs(-2))
print(abs(3+2j))
print(divmod(100, 3))
print(pow(3, 4))
print(round(12.5))
a = "['hello', 'world']"
print(a)
print(type(a))
a = eval(a)
print(a)
print(type(a))
exec("a = 1 + 3")
print(a)  # 4

# 6 if ...:
#       ...
#   elif(可重复) ... :
#       ...
#   elif ... :
#       ...
#   else(非必要):
#       ...
# in(位于), not in(不位于),
writes = []
if writes:
    for write in writes:
        print("还不错嘛,小洛.奖励你吃顿好的!")
else:
    print("哦,殿下,你又又又偷懒了<[.$.]>...")
print()
me = [1, 7, 9]
try:
    you = [int(input("number number!\n"))]
    for you_1 in you:
        print(you_1)
        print(you)
        if you_1 in me:
            print("居然让你猜到了,可恶!")
        else:
            print("私下多多努力哦,殿下~")
except ValueError:
    print("Please!Give me an integer!")

# 7 dictionary
# max(),min() 比较的是dict中的键 in,not in 指的也是dict中的键
# .get(key) 返回value,冇则返回None(默认参数,可自设)  dict[key] 索引,冇则报错
# .popitem() 随机取一个键值对返回(tuple)并del
biue = {"name": "洛天依", "age": 16}
print(biue)
# 添加item
biue["love"] = "writing"
biue["love_2"] = "reading"
print(biue)
# 修改value
print("一年之后...")
biue["age"] = biue["age"] + 1
biue["love"] = "reading"
print(biue)
# 删除item
print("由于小洛不喜欢别人谈论自己的年龄，卬对字典作了删减，如下:")
del biue["age"]
print(biue.pop("love_2"))  # 默认返回key对应的value
try:
    print(biue.pop("love_2"))
except KeyError:
    print("KeyError: 'love_2'")
print(biue.pop("love_2", "修改完毕"))
print(biue)
# 返回键,返回值,返回键值对
print(biue.keys())
print(type(biue.keys()))
print(biue.values())
print(type(biue.values()))
print(biue.items())
print(type(biue.items()))
# 遍历dictionary
print("以下是小洛愿意公开的信息(以及卬的一点学习资料/代码):")
for key, value in biue.items():
    print("\tKey: " + key.title())
    print("\tValue: " + value.title())
for key in biue.keys():
    print(key)
for key in biue:
    print(key)
for key in sorted(biue):
    print(key)
for value in biue.values():
    print(value)
for item in biue.items():
    print(item)
    print(item[0], item[1])
# dictionary默认遍历所有键,
if "someone" not in biue:
    print("无啦啦...")
if "name" in biue:
    print("还不错.")
# set(剔除重复项)
such_as = {1: 2, 2: 2, 3: 4}
for i in such_as.values():
    print(i)
for i in set(such_as.values()):
    print(i)
# 嵌套
# 字典列表
hint = []
for i in range(4):
    hint_new = {"col": "blue", "num": "7"}
    hint.append(hint_new)
print(hint)
print(len(hint))
print(hint[:-1])
for i in hint[:-1]:
    if i["col"] == "blue":
        i["col"] = "yellow"
        i["num"] = "3"
print(hint)
# 在字典中储存列表
concept_num = {"odd": ["1", "3"],
               "even": "2"}
for key, values in concept_num.items():
    if len(values) >= 2:
        print("His concept number is " + key + ",such as:")
        for value in values:
            print(value)
    else:
        print("His concept number is " + key + ",just:")
        for value in values:
            print(value)
# 在字典中储存字典
trio = {"one": {"age": "15", "name": "gumi"},
        "two": {"age": "16", "name": "miku"},
        "three": {"age": "17", "name": "IA"}}
print(trio)
for num in trio:
    name = trio[num]["name"]
    age = trio[num]["age"]
    print("The " + num + " of trio is " + name +
          ",who is " + age + " years old")

# 8 input(默认类型str), %(求模运算符,将两个数相除并返回余数), while循环, break退出任意循环,
#   continue(如果True，返回重新开始；如果False，执行剩下代码)
shu = 0
i = 0
i_1 = 0
while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    shu = shu + i
    i_1 = i_1 + 1
    if i_1 == 3:
        break
print("halohalo!\nI'm " + str(shu) + " years old!")


# 9 形参 *args and **kwargs


def tuple_name(x, y, *args):
    print(y, x, args)


tuple_name(1, 3, 7, 2, 8)
tuple_name(1, 3, "a=7", "b=2", "c=8")


def dictionary_name(x, y, **kwargs):
    print(x, y, kwargs)


dictionary_name(1, 3, a=7, b=2, c=8)


# 字典不能为空,修改dict() or 下一行加pass


def blue_music(one, two, **others):
    print(one, two, others)
    time_name = {}
    pass
    time_name['first'] = one
    time_name['second'] = two
    for key_, value_ in others.items():
        time_name[key_] = value_
    return time_name


Blue_music = blue_music('Super Star', "Graduated", three="Yesterday \
Once More", four="Be What You Wanna Be")
print(Blue_music, end="\n\n")


# 导入函数模块(name.py)
# one:
# import 模块名
# 模块名.函数名(参数, 参数, ...)
# two:
# import 模块名 as something
# something.函数名(参数, 参数, ...)
# three:
# from 模块名 import 对象,函数...(*表示引进全部)

# 10 类--首字母大写的名称 class 名():, 类中的函数叫方法:__init__(self, ...)特殊方法:,
# 创建类Love


class Love(object):
    def __init__(self, name_, birthday):
        self.name = name_
        self.birthday = birthday
        self.time_write = 0

    def base(self):
        print("Do you know '" + self.name + "'?Let me tell\
 you.She is " + str(self.birthday) + " years old!Oh--Sorry\
,it's her birthday.")

    def sing(self):
        print(self.name + "喜欢唱歌,但是讨厌为别人唱.")

    def eat(self):
        print(self.name + "虽然喜欢吃,但绝不是大胃王,只是偶尔让仛赢一局而已.")

    def time(self, time_reading):
        if int(time_reading) >= self.time_write:
            self.time_write = int(time_reading)
        else:
            print("FuckYou!别整改老子的database!!")

    def time_incarnation(self, time_had):
        if int(time_had) >= 0:
            self.time_write += time_had
        else:
            print("可以拜托你去来世取点东西吗?鬼丫头!\n(不是殿下,别误会)")

    def reading(self):
        print(self.name + "已经读了" + str(self.time_write) + "本书.")

    def restore(self):
        if self.time_write > 0:
            self.time_write = 0
            print("It had restored")
        else:
            print("It seems that there are no things need I do.Goodbye!")


my_love = Love('殿下', 712)
your_love = Love('阿绫', 412)
print("I like '" + my_love.name + "' most and best!" + "\
 Tell you a secret: Her birthday is " + str(my_love.birthday) + ".")
print("You like '" + your_love.name + "' best and most!" + "\
 Tell me a secret: Her birthday is " + str(your_love.birthday) + ".")
my_love.sing()
my_love.eat()
my_love.base()
your_love.sing()
your_love.eat()
your_love.base()
print()
my_love.time_write = 5
my_love.reading()
my_love.time(4)
my_love.time(6)
my_love.reading()
my_love.time_incarnation(900)
my_love.reading()
my_love.time(9)
my_love.time_incarnation(-9)
my_love.reading()
my_love.time_incarnation(7)
my_love.reading()
my_love.restore()
my_love.reading()
my_love.restore()
print()


class Something:
    def __init__(self, year=2014):
        self.year = year

    def year_birth(self):
        print("The girl is " + str(self.year) + " birth.")
        "'1.方法'"


# 创建Love的子类Lover
class Lover(Love):
    def __init__(self, name_1, birthday):
        super().__init__(name_1, birthday)
        self.age = 15
        self.year = Something()
        "'2.建立调用渠道'"

    def age_old(self):
        print(self.name + "现在才" + str(self.age) + "岁而已.")

    def eat(self):
        print("I'm sorry to tell you that '" + self.name + "' didn't\
 want to talk about her eating habit.")


his_love = Lover("小天使", 711)
his_love.base()
his_love.sing()
his_love.eat()
his_love.age_old()
print()
his_love.year.year_birth()
"'3.调用'"

# 11.文件和异常
#    except ZeroDivisionError(被除数为0) / FileNotFoundError(文件不存在)
#    pass 让python一声不吭
#    测试代码 import unittest
try:
    print(7 / 0)
except ZeroDivisionError:
    print("\nYou can't divide by zero!")

try:
    print(7 / 0)
except ZeroDivisionError:
    pass

try:
    with open("python无.py") as a:
        b = a.read()
except FileNotFoundError:
    print("File is not founded.Sorry...")
else:
    print(b.rstrip())

# 12.科学计数法 查看类型type()
# 二进制0bnum or 0Bnum(num=0,1)
# 八进制0onum or 0Onum(num=0~7)
# 十六进制 0xnum or 0Xnum(num=0~9,a/A~f/F_即10~15）
# chr(num) num(十进制)⇀num(二进制)⇀python底层逻辑unicode对应字母
# ord(字母) 与chr相反
# hex(num) num⇀num(十六进制)
# oct(num) num⇀num(八进制)
# 浮点数只有十进制
# 复数z=a+bj/J,j**2=-1 z.real获取实部 z.imag获取虚部
# 整数int 浮点数float 复数complex 字符串str 布尔类型bool
# 9个运算符+-*/ //整数商 %余数 **幂 +-正负
# 增强赋值运算符 = += -= *= /= //= a%=2(a=a%2) a**=1(a=a**1)
# 关系运算符 < > <= >=(是否大于等于) ==(是否等于) !=(是否不等于)
# 逻辑运算符 and or not
print(7.1e3)
print(7.1E3)
print(7e4)
print(type(7E2))
print(chr(77))
print(ord("m"))
print(ord('M'))
print(0B10)
print(0O765)
print(oct(501))
print(0X16ac)
print(hex(5804))
print(hex(0b101))
_year = 3 + 1J
print(_year)
print(_year.real)
print(_year.imag)
print(type(_year))
_year_1 = True
print(type(_year_1))
print(10 // 3)
print(10 % 3)

# 13.函数def return返回值,谁调用返给谁
#    函数中变量为局部变量，只在函数中可用，global+变量，局部变量变全局变量
ling_birth = 777


def love():
    global ling_birth
    luo_birth = 712
    ling_birth = 412
    birth = luo_birth + ling_birth
    return birth


a = love()
print(a)
print(ling_birth)   # If no global, will return 777

# 14.集合set{不输出重复,无序(每次输出)}
#   in 是否在 not in 是否不在
#   .add(item) if冇则添加.list不可用(AttributeError: 'list' object has no attribute 'add')
#   .remove(item) 输出结果中删除item,冇则报错
#   .clear() 删除set所有元素
#   创建空集合的方式(注:a={}是空字典) a = set(), a = set({})
#   创建空列表的方式 a=list() a=[] a=list([])
#   元组(不可修改,小括号非必要)
a = {"喜欢", "殿下", 712, 712, "因为", "生日", "因为"}
b = {"喜欢", "阿绫", 412, 712, "所以", "生日", "因为"}
print(a)
print(b)
print(type(a))
print(a - b)  # a中去除b出现的元素
print(a & b)  # ab共同出现的元素
print(a ^ b)  # ab共同出现元素除去后剩下的元素
print(a | b)  # ab中所有元素
print(712 in a)
print(712 not in a)
a.add(412)
print(a)
a.remove(712)
print(a)
try:
    a.remove(712)
    print(a)
except KeyError:
    print("KeyError: 712")
a.clear()
print(a)
a = set()
print(a)
print(type(a))
a = 1, 3, 4
print(a)
print(type(a))

# 15.文件读写
#   r 只读,冇则报错(默认值),默认值
#   w 覆盖写,冇则新建,有则覆盖
#   x 创建写,冇则新建,有则报错
#   a 追加写,冇则新建,有则追加
#   b 二进制文件模式
#   t 文本文件模式,默认值
"""
try:
    ab = open("C:/Users/15268/Desktop/Luo1.txt", encoding="utf-8")  # encoding设置编码格式
except FileNotFoundError:
    print("不好意思,文件已经被殿下删了")
try:
    ba = ab.read()
except NameError:
    print("NameError: name 'ab' is not defined")
try:
    ab.close()
except NameError:
    print("NameError: name 'ab' is not defined")
try:
    print(ba)
except NameError:
    print("NameError: name 'ba' is not defined")
"""
#   文件读取
#   read readline readlines seek
"""
a = "C:/Users/15268/Desktop/Luo.txt"
b = open(a, "r", encoding="utf-8")
print(b.read(5))  # 读取5字节
a = "C:\\Users\\15268\\Desktop\\Luo.txt"
b = open(a, "rb")
print(b.read(5))  # b'\xe6\xae\xbf\xe4\xb8' /x表示十六进制(反斜杠报错,只好这样)
a = "C:\\Users\\15268\\Desktop\\Luo.txt"
b = open(a, "r", encoding="utf-8")
print(b.readline(), end="")  # 读取一行__第一行
print(b.readline(2))  # 读取一行的前2个字节__\n第二行
b.seek(0)  # 0指针回到开头 1当前位置(毛用冇) 2指针跳到结尾
print(b.readline())  # 又回到了第一行
print(b.readlines())  # 默认读取所有行,每行作为一个元素组成list
print(b.readlines(3))  # 假如一行3字,二行3字,三行有字.(3)一行,(4-7)两行,(8)三行,数到\n即到下一行
"""
#   文件写入 write writelines(传list)
"""
a = "C:/Users/15268/Desktop/Luo2.txt"
b = open(a, "w")  # w是覆盖写,可以换其他的,见开头
b.write("请问,\n殿下有喜欢的人吗?\n稍微有点好奇......")
c = ["请问,\n", "你可以回答我吗?\n", "拜托!!\n"]
b.writelines(c)
b.close()
"""

#  16.turtle库绘图
#  turtle.setup(width_窗口宽, height_高, startx_窗口距屏幕左, starty_距顶)
#  forward() 前进.简写fd()  backward() 后退.简写bk()
#  right(x) 右转x角度,顺时针  left(x) 左转,逆时针
#  setheading(angle) 改变当前朝向,绝对角度,0右90上,别名seth()
#  speed(0~10) 画笔移动速度,大==快,0例外，无动画(殆？)
#  pendown() 放下画笔(画),别名pd()down()  penup() 提起画笔(不画),别名pu()up()
#  goto(x, y) 画笔移动到绝对坐标(x, y),默认(0, 0),画笔未提起会画线
#  setx(x) 修改画笔x坐标,y不变,画笔未提起会画线  sety(y)
#  home() 画笔移至原点,朝右,画笔未提起会画线
#  pensize(num) 设置画笔粗细 别名width()
#  pencolor() 设置画笔颜色(word)or((r红, g绿, b蓝))0~1
#  bgcolor() 设置画布颜色  blueviolet 紫罗兰色(殆？) violet
#  color(画笔, 填充) 设置画笔颜色or填充颜色  fillcolor()只填充  pencolor()只画笔
#  begin_fill() 开始填充  end_fill() 结束填充
#  filling() 返回填充状态TrueFalse
#  clear() 清空当前窗口,但不改变画笔位置
#  reset() 彻底清空
#  screensize() 设置画布宽高和颜色
#  hideturtle() 隐藏画笔
#  showturtle() 显示画笔
#  isvisible() 返回画笔状态TrueFalse
#  write(str, fond=None) 输出fond字体的字符串
#  circle(radius, e) 绘制一个指定半径r和角度e的圆or弧(e默认360,也就是圆)
#  circle(radius, steps=n) 绘制一个半径为r的圆的内切n边形(不显示圆)
#  dot(size, color) 绘制一个直径size,color色的圆点
#  undo() 撤销最后一步
#  shape("name") set画笔形状 arrow箭头 turtle海龟 circle圆 square方块 triangle三角 classic铅笔 blank空白
#  tracer(False)  不显示绘制过程
#  bye() 关闭窗口，退出程序
"""
保存生成的Turtle图,eps可用ps打开
from PIL import Image
getcanvas().postscript(file="效果图.eps")
img = Image.open("效果图.eps")
"""
"""
from turtle import *


setup(700, 700, 770, 70)
pu()
fd(100)
right(-45)
color("red", "pink")
begin_fill()
down()
goto(0, 0)
bk(200)
# clear()
left(90)
pensize(4)
print(filling())
pencolor((0, 0, 1))
fd(100)
end_fill()
# reset()
screensize(700, 700, "pink")
hideturtle()
print(isvisible())
showturtle()
print(isvisible())
write("kais")
done()
"""

#  17.random库
#     random() 生成0.0~1.0之间的随机小数,不包括1.0
#     seed(a = None) 初始化随机数种子,默认值当前系统时间
#     randint(a, b) 生成a~b之间的随机整数,包括b
#     uniform(a, b) 生成a~b之间的随机小数
#     getrandbits(k) 生成一个k比特长度的随机整数(二进制长度)
#     randrange(a, b, c) 在a~b,c步长(默认1)生成的数中随机抽
#     choice(seq) 从序列类型(如list)中随机返回一个元素
#     shuffle(seq) 打乱序列类型再返回
#     sample(pop, k) 从pop中随机选取k个元素,返回list
print(random())
seed(7)
print(random())  # 0.32383276483316237
print(random())  # 0.15084917392450192
seed(7)
print(random())  # 0.32383276483316237
print(random())  # 0.15084917392450192
seed()
print(randint(2, 7))
print(getrandbits(9))
print(randrange(2, 19, 3))
print(uniform(3, 7))
a = [1, 4, 0]
print(choice(a))
shuffle(a)
print(a)
print(sample(a, 2))

# 18.第三方库jieba,分词器
# lcut(s) 精确模式,返回list
# lcut_for_search(s) 搜索引擎模式
# lcut(s, cut_all=True) 全模式
# jieba.add_word(w) 向分词字典中add新词w
"""
from jieba import *
a = lcut("我永远喜欢世界第一可爱,殿下来殿下!")
print(a)
a = lcut("我永远喜欢世界第一可爱,殿下来殿下!", cut_all=True)
print(a)
a = lcut_for_search("我永远喜欢世界第一可爱,殿下来殿下!")
print(a)
"""

print("end")
