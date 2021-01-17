import hashlib
import os

doc_list = os.listdir('input/')
print('doc_list')
print(doc_list)
print()

if len(doc_list)==1:
    doc_list = doc_list[0]
    doc_list = 'input/' + doc_list

    with open(doc_list, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash_value = md5obj.hexdigest()
        print('md5:', hash_value)
        
    with open(doc_list, 'rb') as f:
        sha256obj = hashlib.sha256()
        sha256obj.update(f.read())
        hash_value = sha256obj.hexdigest()
        print('sha256:', hash_value)

    with open(doc_list, 'rb') as f:
        sha512obj = hashlib.sha512()
        sha512obj.update(f.read())
        hash_value = sha512obj.hexdigest()
        print('sha512:', hash_value)

else:
    print('只能输入一个文件')

print()
os.system('pause')
