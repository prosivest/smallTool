import os
import docx


def replace_by_keywords(path, keywords, replaced_keywords):
    fileList = os.listdir(path)  # 列出文件
    for j in range(len(fileList)):
        old_filename = path + os.sep + fileList[j]  # 文件完整路径
        new_filename = old_filename.replace(keywords, replaced_keywords)
        os.rename(old_filename, new_filename)
    print("successful!")


def rename_by_orders(path, before_txt, behind_text):
    fileList = os.listdir(path)  # 列出文件
    # n = 0
    for i in range(len(fileList)):
        old_filename = path + os.sep + fileList[i]  # 文件完整路径
        file_extension = os.path.splitext(old_filename)[-1]  # 确定文件扩展名，后续需保持扩展名不变
        new_filename = path + os.sep + before_txt + str(i + 1) + behind_text + file_extension  # 确定新文件名
        os.rename(old_filename, new_filename)  # 重命名
        # n = n + 1
    print('success!')


def append_text_before(path, before_text):
    fileList = os.listdir(path)
    for k in range(len(fileList)):
        old_filename = path + os.sep + fileList[k]
        new_filename = path + os.sep + before_text + fileList[k]
        os.rename(old_filename,new_filename)
    print("successful")


def append_text_behind(path, behind_text):
    fileList = os.listdir(path)
    for k in range(len(fileList)):
        old_filename = path + os.sep + fileList[k]
        file_extension = os.path.splitext(old_filename)[-1]
        file_name = os.path.splitext(fileList[k])[0]
        new_filename = path + os.sep + file_name + behind_text + file_extension  # 确定新文件名
        os.rename(old_filename, new_filename)
    print("successful")


def replace_word(path,keywords,replaced_keywords):
    print("test")

def test_qt():
    print("test")





# filepath = r'D:\Desktop\test'
# before_text = input('请输入序号前文字：')
# behind_text = input('请输入序号后文字：')
# rename_by_orders(filepath, before_text, behind_text)

# replace_by_keywords(filepath, "测试代码", "代码")

# before_text = input('请输入加在文件名前的文字：')
# append_text_before(filepath, before_text)

# bh_text = input('请输入加在文件名后的文字：')
# append_text_behind(filepath, bh_text)
