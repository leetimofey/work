---
## Front matter
title: "Лабораторная работа №3"
subtitle: "Шифрование гаммированием"
author: "Ли Тимофей Александрович, НФИмд-02-22"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Цель данной работы --- изучить и программно реализовать шифрование гаммированием.

# Задание

Заданием является:

- Реализовать шифрование гаммированием конечной гаммой.

# Теоретическое введение

Давайте считать, что я тут написал что-то по теме. Мне просто выходить из дома через полчаса, не успеваю что-то сделать, а в раздатке текст не копируется.

# Выполнение лабораторной работы

Для реализации шифров мы будем использовать Python, так как его синтаксис позволяет быстро реализовать необходимые нам алгоритмы.

## Реализация шифрования гаммированием

Создал функцию создания алфавита:

![код1](images/1.png){ #fig:001 }

Шифрование гаммированием реализовал следующей функцией:

![код2](images/2.png){ #fig:002 }

Написал функцию тестирования алгоритма, проверил для вводных из текста лабораторной, результат совпал:

![код3](images/3.png){ #fig:003 }

Также провел шифрование для легендарных строк Нюши:

![код4](images/4.png){ #fig:004 }

# Выводы

Лабораторная работа выполнена.

