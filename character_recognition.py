from aip import AipOcr

# 以下三项是你申请百度AI应用时自动创建的
APP_ID  = '11068652'
API_KEY = 'z0iyTnnuwjK2TffcGebWK39p'
SECRET_KEY = 'H8Rb9usEG2Dp2NKsbk7W1Li9uFvfdzsu'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

# 读取要识别的文件
def get_file_content(filepath):
    with open(filepath,'rb') as fp:
        image = fp.read()
    return image

# 图片文字识别
def basic_using(filepath):
    image = get_file_content(FilePath)
    #带参数检测，参数写入字典
    option = {'language_type':"CHN_ENG",'detect_direction':"true"}
    #print(client.basicAccurate(image,option))

    #访问输出参数字典中关键字的值
    #print(client.basicAccurate(image)['words_result'])

    result = client.basicAccurate(image)
    return result['words_result'],result['words_result_num']

# 结果输出格式转换
def words_to_conten(filepath):
    str,num = basic_using(filepath)
    content = ''
    for i in range(num):
        content += str[i]['words']
    print(content)

if __name__ == "__main__":
    FilePath = 'pictures/test.png'
    basic_using(FilePath)
    words_to_conten(FilePath)
