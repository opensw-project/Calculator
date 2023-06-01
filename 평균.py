        numlist = []
        while True:
            num = float(input('숫자를 입력하세요 :'))
            except ValueError:
                break
                print("입력 완료")
            numlist.append(num)
        average = sum(numlist) / len(numlist)
        print(average)
