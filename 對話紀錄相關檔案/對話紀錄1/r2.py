def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:  # 記得encoding 的部分，-sig 是為了讀取記事本最開始的編碼
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    new = []
    person = None #預設值設成None 避免程式出錯
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #前面設成none 因此如果有值 -> if true
            new.append(person + ':' + line)
    return new

def write_file(filename, lines, ):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output', lines)

main()


