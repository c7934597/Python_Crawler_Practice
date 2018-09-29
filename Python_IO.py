#基本的File I/O使用
# coding=utf-8
# 開啟檔案
myfile = open("test.txt", "w+")
myfile.write( "測試寫入幾個文字");

# 關閉檔案
myfile.close()