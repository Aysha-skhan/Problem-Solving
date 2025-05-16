def intToRoman( nums: int) -> str:
    rand = ''
    while True:
        if len(str(nums)) == 4:
            rand += 'M' * (nums // 1000)
        elif len(str(nums)) == 3:
            rand += 'D' * (nums // 500)
            rand += 'C' * ((nums % 500) // 100)
        elif len(str(nums)) == 2:
            if nums==49:
                rand+=''
                rand += 'L' * (nums // 50)
            rand += 'X' * ((nums % 50) // 10)
        elif len(str(nums)) == 1:
            if nums==9:
                rand+='IX'
            else:
                rand += 'V' * (nums // 5)
            if nums % 5==4:
                rand+='IV'
            else:
                rand += 'I' * (nums % 5)
            break
        nums = nums % (10 ** (len(str(nums)) - 1))
        print(nums)
    return rand
print(intToRoman(3749))