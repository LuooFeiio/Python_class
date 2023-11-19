def fun01():
    print('这是fun01的开始')
    num = 1 / 0
    print('这是fun01的结束')

def fun02():
    print('这是fun02的开始')
    fun01()
    print('这是fun02的结束')

def main():
    try:
        fun02()
    except Exception as e:
        print(e)

main()