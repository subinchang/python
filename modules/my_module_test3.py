# File name: my_module_test3.py
def func(a):
    print('입력 값:', a)
    
if __name__ == '__main__':
    print('my_module_test3 모듈이 메인 모듈입니다.')
    func(5)
    func(3)
else:
    print('my_module_test3 모듈은 import 되는 모듈입니다.')
