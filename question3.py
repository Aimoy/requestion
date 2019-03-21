import time
import datetime
class Aplusb(object):
    @classmethod
    def _a(cls, a, b, c=datetime.datetime.now(), **kwargs):
        # 问题1:需要加上cls参数
        # 问题2:关键字参数需要放在**kwargs之前
        return a + b, c, kwargs
sum_, time_, _ = Aplusb._a(1, 2)
# 问题3: sum是内置函数不应当作为变量名
# 问题4: time作为变量,下面的time模块无法使用
# 问题5: * 不能作为变量,一般用_表示不重要可不使用的变量
print(sum_, time_)
time.sleep(2)
sum_, time_, _ = Aplusb._a(3, 4)
print(sum_, time_)
