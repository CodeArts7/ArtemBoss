def land_perimeter(arr):
    per = 0
    for i in range(len(arr)):  # Получаем строку
        for j in range(len(arr[i])):  # Получаем элемент в строке
            if arr[i][j] == 'X':  # Получаем первый элемент строки
                per += 4
                if j > 0 and arr[i][j - 1] == 'X':  # Проверяем предыдущий (левый) символ
                    per -= 1
                if j < (len(arr[i]) - 1) and arr[i][j + 1] == 'X':  # Проверяем следующий (правый) символ
                    per -= 1
                if i > 0 and arr[i - 1][j] == 'X':  # Проверяем верхний символ на той же позиции
                    per -= 1
                if i < (len(arr)- 1) and arr[i + 1][j] == 'X':  # Проверяем нижний символ на той же позиции
                    per -= 1

    print(f'Total land perimeter: {per}')


land_perimeter(['XOOXO', 'XOOXO', 'OOOXO', 'XXOXO', 'OXOOO'])



