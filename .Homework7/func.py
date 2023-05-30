def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka):
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("нет такого")
    data.close()

def change(file_name, stroka, stroka1):
    data = open(file_name, 'r')
    list1 = data.readlines()
    data.close()
    if stroka+'\n' in list1:
        list1[list1.index(stroka+'\n')] = list1[list1.index(stroka+'\n')].replace(stroka,stroka1) 
        data = open(file_name, 'w')
        data.writelines(list1)
        data.close()
        print("Замена успешно произведена")
    else:
        print("Искомый элемент для замены не найден, повторите попытку")

def delete(file_name, stroka):
    data = open(file_name, 'r')
    list1 = data.readlines()
    data.close()
    if stroka+'\n' in list1:
        del list1[list1.index(stroka+'\n')]
        data = open(file_name, 'w')
        data.writelines(list1)
        data.close()
        print("Строка удалена")
    else:
        print("Нет искомой строки для удаления")
