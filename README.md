# ImplicitTreap
Неявное декартово дерево

![:)](https://raw.githubusercontent.com/ElijahOvcharenko/ImplicitTreap/master/screens/screen_1.png?token=AVGJq_o_iW6NhWyHz6lPNGvuSFr3svAVks5aTWZWwA%3D%3D)

Слайды на тему декартова дерева по неявному ключу лежат в папке **/presentation**.
В папке **/compare** - результаты сравнения данной структуры со списком в python по скорости добавления эелемента в начало.
В папке **/problem** - задача на тему неявного декартова дерева и ее решение.
В папке **/source** - сама программа.  В файле implicit_treap.py лежит класс с реализацей неявного декатова дерева который можно использовать отдельно.

Проект сосотоит из графического интерфейса для визуализации дерамиды и консольного приложения.
Для работы необходимо наличие интерпретатора python 3.X и библиотек psutil, graphviz, tkinter (АХТУНГ! полследние две нужны только для визуализации и для работы в консоли не требуются).

## Визуализация 
Для запуска графического интерфейса необходимо перейти в папку source в проекте и выполнить скрипт main.py с аргументом gui.
```bash
python3 main.py gui
```
все, наслаждемся чудесной визуалицией, тыкаем на кнопочки и радуемся :)

## Консольное приложение 
Для запуска приложения в консольном режиме необходимо выпоснить вот такую команду (просто запустить скрипт main.py):

``` bash
python3 main.py 
Interactive mode
For exit type 'exit'
If you need some help type 'help'
You have already treap with index 1 and values [1, 2, 3, 4, 5]
```

Консольная версия позволяет создавать новые дерамиды, которые хранятся в массиве (нумерация с единицы) и доступны по индексам. С ними можно выполнять разнообразные операции, которые доступны для декартова дерева по неявному ключу (split, merge, reverse, сумма на отрезке и тд). Для того что бы получить полную информацию про досткпные функции, их аргументы и вообще что они делаю существует команда help.

``` bash
Enter command: help
```

По умолчанию создается дерамида с элемнтами [1, 2, 3, 4, 5] по индексу 1.
Пример выполнения операции с дерамидой (split и print):

``` bash
Enter command: print 1

[1, 2, 3, 4, 5]

Enter command: split 1 2
First part index is 2, second part index is 3
Enter command: print 2

[1, 2]

```


## Тесты
Тесты - это набор команд которые есть в консольной версии которые описаны в одном текстовом файле.
Все тесты находятся в папке /source/tests. Текстовое описание теста находится в начале каждого файла. Для запуска теста необходимо выполнить команду read_file <путь_к_тесту> в консольном режиме. Если тест загружен из графического режма (там есть кнопка "Add from file") отображается только дерамида с индексом 1.

```
Enter command: read_file tests/13.txt

тест на добавление 100 элементов в дерамиду с индексом 2

New treap index is 2

Wait...

Execution time is 0.01228022575378418
Memory usage is around 12288 bytes
```

В конце каждого теста выводится информация о времени выполнения теста (в мс) и примерной затраченной памяти (в байтах; считается как разица между памятью, котороя была выделена на текущий процесс перед выполнение теста и сразу же после него).











