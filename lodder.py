from data_creat import name_data, surename_data, phone_data, address_data
def input_data():
    name = name_data()
    surename = surename_data()
    phone = phone_data()
    address = address_data()
    var = int(input("В каком формате записать данные ? \n\n"
                    f"1 Вариант : \n"
                    f" {name}\n {surename} \n {phone} \n {address} \n\n"
                    f"2 Вариант : \n"
                    f"{name}; {surename} ; {phone} ; {address} \n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))    
        
    if var == 1:
        with open("data_frst_varint.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surename} \n{phone}  \n{address} \n\n")
    elif var == 2:
        with open("dataSecondVariant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name} ; {surename} ; {phone} ; {address} ;\n")

def print_data():
    userChuse = input("Какой вариант вывести ? \n"
                      f"Вариант 1\n"
                      f"Вариант 2\n")
    if userChuse == "1":
        print("\nВывожу данные из 1-ого файла \n")
        with open("data_frst_varint.csv", "r", encoding="utf-8") as f:
            data_first = f.read()
            print(data_first)
    elif userChuse == "2":       
        print("\nВывожу данные из 2-ого файла \n")
        with open("dataSecondVariant.csv", "r", encoding="utf-8") as f:
            dataSecond = f.read()
            print(dataSecond)

def edit_data():
    userChuse = input("Какой вариант редактировать ? \n"
                      "Вариант 1\n"
                      "Вариант 2\n")
    if userChuse == "1":
        file_path = "data_frst_varint.csv"
    elif userChuse == "2":
        file_path = "dataSecondVariant.csv"
    else:
        print("Некорректный выбор.")
        return

    secChuz = input("\nВведите имя для редактирования из файла\n")

    # Чтение файла
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()

    if userChuse == "1":
        # Разделение на записи
        entries = "".join(data).split('\n\n')
        updated_entries = []
        found = False

        for entry in entries:
            if entry.startswith(secChuz):
                found = True
                print(f"Найдена запись:\n{entry}")
                new_frstName = input("Введите новое имя: ")
                new_secondName = input("Введите новую фамилию: ")
                new_phoneNumber = input("Введите новый номер телефона: ")
                new_adress = input("Введите новый адрес: ")
                
                updated_entry = f"{new_frstName}\n{new_secondName}\n{new_phoneNumber}\n{new_adress}\n"
                updated_entries.append(updated_entry)
            else:
                updated_entries.append(entry)
        
        if not found:
            print("Запись не найдена.")
            return

        # Сохранение изменений
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('\n\n'.join(updated_entries))
        print("Запись обновлена.")
    elif userChuse == "2":
        # Разделение на записи
        updated_entries = []
        found = False

        for entry in data:
            entry = entry.strip()  # Удаление лишних пробелов
            if entry.startswith(secChuz):
                found = True
                print(f"Найдена запись: {entry}")
                new_frstName = input("Введите новое имя: ")
                new_secondName = input("Введите новую фамилию: ")
                new_phoneNumber = input("Введите новый номер телефона: ")
                new_adress = input("Введите новый адрес: ")

                updated_entry = f"{new_frstName} ; {new_secondName} ; {new_phoneNumber} ; {new_adress} ;\n"
                updated_entries.append(updated_entry)
            else:
                updated_entries.append(entry + '\n')
        
        if not found:
            print("Запись не найдена.")
            return

        # Сохранение изменений
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(updated_entries)
        print("Запись обновлена.")


def delete_data():
    userChuse = input("Какой вариант редактировать ? \n"
                      "Вариант 1\n"
                      "Вариант 2\n")
    if userChuse == "1":
        file_path = "data_frst_varint.csv"
    elif userChuse == "2":
        file_path = "dataSecondVariant.csv"
    else:
        print("Некорректный выбор.")
        return

    secChuz = input("\nВведите имя для удаления из файла\n")

    # Чтение файла
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()

    if userChuse == "1":
        # Разделение на записи
        entries = "".join(data).split('\n\n')
        updated_entries = []
        found = False

        for entry in entries:
            if entry.startswith(secChuz):
                found = True
                print(f"Найдена запись для удаления:\n{entry}")
            else:
                updated_entries.append(entry)
        
        if not found:
            print("Запись не найдена.")
            return

        with open(file_path, "w", encoding="utf-8") as f:
            f.write('\n\n'.join(updated_entries))
        print("Запись удалена.")
    elif userChuse == "2":

        updated_entries = []
        found = False
        skip_next_empty = False

        for entry in data:
            stripped_entry = entry.strip()  # Удаление лишних пробелов
            if stripped_entry.startswith(secChuz):
                found = True
                print(f"Найдена запись для удаления: {entry}")
                skip_next_empty = True  
            elif skip_next_empty and stripped_entry == '':
                skip_next_empty = False  
            else:
                updated_entries.append(entry)
        
        if not found:
            print("Запись не найдена.")
            return

        # Сохранение изменений
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(updated_entries)
        print("Запись удалена.")

