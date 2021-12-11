f = open('input.txt','r')

totalsum = 0
solver = {0: set([]), 1: set([]), 2: set([]), 3:set([]), 4:set([]), 5:set([]), 6:set([])}
for index, line in enumerate(f):
        digs = line.rstrip().split(' | ')[0].split(' ')
        nums = {0: set([]), 1: set([]), 2: set([]), 3:set([]), 4:set([]), 5:set([]), 6:set([]), 7:set([]), 8:set([]), 9:set([])}
        for d in digs:
            arr = [char for char in d]
            if len(d) == 2:
                for i in arr:
                    nums[1].add(i)
            elif len(d) == 4:
                for i in arr:
                    nums[4].add(i)
            elif len(d) == 3:
                for i in arr:
                    nums[7].add(i)
            elif len(d) == 7:
                for i in arr:
                    nums[8].add(i)
            elif len(d) == 6:
                for i in arr:
                    nums[0].add(d)
                    nums[6].add(d)
                    nums[9].add(d)
            elif len(d) == 5:
                for i in arr:
                    nums[5].add(d)
                    nums[2].add(d)
                    nums[3].add(d)

        #first 6
        for k in nums[6]:
            chars = set([char for char in k])
            if not nums[1].issubset(chars):
                nums[9].remove(k)
                nums[0].remove(k)
                nums[6] = set([char for char in chars])
        #9
        for k in nums[9]:
            chars = set([char for char in k])
            if nums[4].issubset(chars):
                nums[9] = set([char for char in chars])
                nums[0].remove(k)
        #0
        if len(nums[0]) != 1:
            print('somethingS wrong i can feel it')
        else:
            nums[0] = set([char for char in list(nums[0])[0]])
        
        #5
        for k in nums[5]:
            chars = set([char for char in k])
            tmp = nums[4] - nums[7]
            if tmp.issubset(chars):
                nums[5] = set([char for char in chars])
                nums[2].remove(k)
                nums[3].remove(k)
                
        #3
        for k in nums[3]:
            chars = set([char for char in k])
            tmp = nums[8] - nums[0]
            tmp = tmp | nums[7]
            if tmp.issubset(chars):
                nums[2].remove(k)
                nums[3] = set([char for char in chars])
        #5
        if len(nums[2]) != 1:
            print('somethingS wrong i can feel it')
        else:
            nums[2] = set([char for char in list(nums[2])[0]])

        res = ''
        for el in line.rstrip().split(' | ')[1].split(' '):
            arr = set([char for char in el])
            for k in nums:
                if arr == nums[k]:
                    res = res + str(k)
        totalsum += int(res)
print(totalsum)
