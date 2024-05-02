#sys模組
import sys as s
print(s.platform)
print(s.path) #取得模組的搜尋路徑(所有模組必須放在這些路徑中才能應用該模組)
#s.path.append('#資料夾名稱') #新增模組的搜尋路徑
# __init__.py #兩條底線+init+兩條底線+.py，須在分類資料夾底下建立此檔名檔案，才能呼叫該資料夾程式
#呼叫封包(分類資料夾)方式:import 資料夾名稱.檔案名稱.程式名