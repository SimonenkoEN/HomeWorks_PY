import print_to_console
import add_new_line
import search
import edit_line
import delite

# проверка сушествования файла
file = open("base.csv","a")
file.close()

while True:
    print("БАЗА ДАННЫХ СПОРТИВНОЙ ШКОЛЫ")
    print("Варианты работы с БД.")
    print("1. ВЫВОД ВСЕХ ДАННЫХ НА ЭКРАН")
    print("2. ДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ")
    print("3. ПОИСК ДАННЫХ")
    print("4. РЕДАКТИРОВАНИЕ ДАННЫХ")
    print("5. УДАЛЕНИЕ ДАННЫХ")
    print("any key - ВЫХОД ")
    mode=input("Выберите необходимый пункт меню: ")
    if mode in ["1","2","3","4","5"]:
        match mode:
            case "1":
                print_to_console.print_to_console()
            case "2":
                add_new_line.add_new_line()
            case "3":
                search.search_data()
            case "4":
                edit_line.edit_line()
            case "5":
                delite.delite_line()
    else: 
        break
