import keyboard
import os
import time

class Control:
    def __init__(self):
        self.current_index = 0 #Выбранный пункт
        self.pointer = 1 # Указатель
        self.cursor_symbols = [' '] * 255 # Символы строк

    def get_selected_index(self):
        # Метод для получения выбранного пункта
        return self.current_index

    def get_cursor_symbol(self, index):
        # Метод для получения символа по индексу курсора
        return self.cursor_symbols[index]

    def handle_movement(self, max_index):
        time.sleep(0.17) #Ожидание перед срабатывание кнопок
        symb = '>'  # Символ для отображения курсора
        btn = keyboard.read_key()

        if btn in ["enter", "space"]:
            # Установка выбранного индекса и обновление символов
            self.cursor_symbols[self.pointer - 1] = ' '
            self.current_index = self.pointer

        if btn in ["q", "й"]:
            # Выход из программы при нажатии на Q или Й
            sys.exit()

        if btn in ["up", "w", "ц"]:
            # Обработка движения вверх
            self.handle_up_movement(max_index, symb)

        elif btn in ["down", "s", "ы"]:
            # Обработка движения вниз
            self.handle_down_movement(max_index, symb)

    def handle_up_movement(self, max_index, symb="#"):
        # Обработка движения вверх
        if self.pointer == 1:
            self.cursor_symbols[0] = ' '
            self.pointer = max_index
            self.cursor_symbols[max_index - 1] = symb
        else:
            self.cursor_symbols[self.pointer - 1] = ' '
            self.cursor_symbols[self.pointer - 2] = symb
            self.pointer -= 1

    def handle_down_movement(self, max_index, symb="#"):
        # Обработка движения вниз
        if self.pointer == max_index:
            self.cursor_symbols[max_index - 1] = ' '
            self.pointer = 1
            self.cursor_symbols[0] = symb
        else:
            self.cursor_symbols[self.pointer - 1] = ' '
            self.cursor_symbols[self.pointer] = symb
            self.pointer += 1

    def reset(self):
        # Сброс всех значений в начальное состояние
        self.current_index = 0
        self.pointer = 1
        self.cursor_symbols[0] = '>'



def cls():
    os.system("cls")


control = Control()

while True:
    #Сбрасываем положение курсора
    control.reset()
    #Цикл будет работать, пока пользователь не выбрал
    while control.get_selected_index() == 0:
        cls()
        print(f"{control.get_cursor_symbol(0)}Первый пункт"
              f"\n{control.get_cursor_symbol(1)}Второй пункт") #Получаем текущие символы для первой и второй строки

        control.handle_movement(2) # Ожидаем действие для двух строк

    match control.get_selected_index(): # Когда пользователь выбрал, переходим к реакции
        case 1:
            cls()
            print("Вы выбрали первый пункт")
            time.sleep(2) #Заглушка
        case 2:
            cls()
            print("Вы выбрали второй пункт")
            time.sleep(2) #Заглушка