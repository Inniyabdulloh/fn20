def read_file(filename:str) -> int: return len(open(filename).read().split())# vazifa 1. 1-yo'l
    # 1-yo'l
    # with open(filename, 'r') as file:
    #     return len(file.read().split())

    # 3-yo'l
    # return len(open(filename).read().split())


def read_file2(filename:str) -> str: # vazifa 2
    with open(filename) as file:
        len_word = ''
        for word in file.read().split():
            if len(word) > len(len_word):
              len_word = word
        return len_word


def numbers_list(nums:list) -> int:
    for num in nums:
        try:
            if num >= nums[nums.index(num)+1]:
                return nums[nums.index(num)+1]
        except:
            continue


def chek_gmail(list:list) -> str:
    gmails = []
    for i in list:
        if type(i) == str and i.endswith('@gmail.com'):
            gmails.append(i)
    return gmails




my_list = ['salom', 54, 'dasturchi', 15.6, 'dasturchi@gmail.com', 'ismoil@gmail.com', 'python']

# print(read_file('file.txt')) # vazifa 1
# print(read_file2('file.txt')) # vazifa 2
# print(numbers_list([9,15,20,21,38,12,568])) # vazifa 3
print(chek_gmail(my_list)) # vazifa 4