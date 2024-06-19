from lodder import input_data, print_data, edit_data, delete_data

def interface():
    print( f"Вы попали в специальный справочник."
           f"\n 1 - Ввод данных ."
           f"\n 2 - Получение данных. \n"
           f" 3 - Редоктирование данных \n"
           f" 4 - Удоление данных \n"
           f" 5 - Выход из программы")
 
    comand = int(input("Введите число: "))
    
    while comand != 1 and comand != 2 and comand != 3 and comand != 4 and comand != 5 :
        print("Неправильный ввод")
        comand = int(input("Введите число: "))
    
    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand == 3: 
        edit_data()
    elif comand == 4 :
        delete_data()
    elif comand == 5:
        print("Выход из программы.")

interface()
# Вызов функции интерфейса

