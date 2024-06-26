# Console Ficus
Кроссплатформенное программное обеспечение для информирования данными об учёбе в средне специальных и высших учебных заведениях. Изначально разработано для студентов группы 21П2-25 Кузнецкого колледжа электронных технологий, но может быть использовано другими группами, преподавателями и учебными заведениями (посредством модификации конфигурации или исходного кода программы). Является альтернативой изначальному [Ficus](https://github.com/tpmax179/tpmax179.github.io).

## Требования
Интерпретатор Python версии 3.6 и выше.

## Установка и запуск
### Linux/macOS
1. Клонировать этот репозиторий:

```bash
git clone https://github.com/qwardo/console-ficus.git
```

2. Перейти в директорию с кодом программы:

```bash
cd console-ficus/src
```

3. Запустить главный скрипт:

```bash
python3 main.py
```

### Windows
1. [Скачать архив](https://github.com/qwardo/console-ficus/archive/refs/heads/main.zip) с программой.

2. Извлечь программу из архива.

3. Перейти в директорию с кодом программы:

```cmd
cd путь-до-извлечённой-программы\src
```

4. Запустить главный скрипт:

```cmd
python main.py
```

## Использование
После запуска, программа предложит вам вывести дополнительную информацию. Чтобы это сделать, введите одну из следующих команд:

```
h
```

или

```
help
```

Программа выведет вам руководство, в котором вы можете ознакомиться со всеми командами и операторами. Например, чтобы вывести расписание пар и тип текущей недели одновременно, введите следующие команды, разделив их с помощью ";":

```
l; w
```

или

```
lessons; week
```

Вы можете модифицировать данные в файле "config.json", который находится в директории "config". Для этого вам нужно знать синтаксис JSON. В этом файле можно:

- **Указать команды для автовыполнения после запуска программы.** За это отвечает ключ "autoexec". Значением этого ключа должна быть строка команд и операторов. Например: "c; b; t" или "clear; bells; time". Ключ является необязательным и вы можете удалить его;

- **Изменить расписание пар.** За это отвечает ключ "lessons". В значении этого ключа должны быть дни недели, в которых хранятся номера пар и информация о парах. В информации может быть: название пары, преподаватель который ведёт эту пару и номер кабинета (информация составляется из ваших предпочтений и может быть любой). Символ "-" в информации о паре означает отсутствие пары, поэтому используйте именно его для корректного обозначения отсутствия пары. Вы можете удалить любой день в расписании пар, если он вам не нужен. Обрабатываются только следующие дни: "mon" - понедельник, "tue" - вторник, "wed" - среда, "thu" - четверг, "fri" - пятница, "sat" - суббота. Вы можете добавлять неограниченное количество пар в любой день недели;

- **Изменить расписание звонков.** За это отвечает ключ "bells". В значении этого ключа должны быть 2 расписания звонков: основное (ключ "main") и субботнее (ключ "sat"), в которых хранятся номера звонков и информация о звонках (временные интервалы). В основном расписании у каждого звонка есть 2 половины, а в субботнем нет, потому что пары объединены. Вы не можете просто так добавить половины в субботнее расписание, или убрать их в основном. Вы можете добавлять неограниченное количество звонков как в основном, так и в субботнем расписании. При модификации времени, придерживайтесь формата "h1:m1-h2:m2", где h1, m1 - это часы и минуты начала, а h2, m2 - часы и минуты конца соответственно.

Если вам нужны изменения в работе программы, вы можете модифицировать её исходный код, который находится в директории "src". Для этого вам нужно знать язык программирования Python.

## Обратная связь
Если у вас возникли сложности или вопросы по использованию Console Ficus, вы хотите сообщить об ошибках или предложить изменения - [создайте обсуждение](https://github.com/qwardo/console-ficus/issues/new/choose) в данном репозитории или [напишите в Telegram](https://t.me/qqwardo).
