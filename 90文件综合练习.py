fr = open("C:/Users/MsiLeFee/Desktop/LawFee/Bill.txt", 'r', encoding = 'UTF-8')
fw = open("C:/Users/MsiLeFee/Desktop/LawFee/Bill.txt.back", 'w', encoding = 'UTF-8')

for line in fr:
    line = line.strip()

    # words = line.split(',')

    # print(words)

    if line.split(',')[-1] == '测试':
        continue

    fw.write(line)
    fw.write('\n')

fr.close()
fw.close() # 自动flush