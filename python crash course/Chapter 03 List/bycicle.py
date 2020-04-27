#bycicle.py
#列表初始化和输出
bycicles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycicles)
message = "My first bycicle was a "+ bycicles[0].title()+"."
print(message)
#替换元素
bycicles[0] = 'phi'
message = "My first bycicle was a "+ bycicles[0].title()+"."
print(message)
#添加元素
bycicles.append('redline')
print(bycicles)
#删除元素
del bycicles[-1]
print(bycicles)
