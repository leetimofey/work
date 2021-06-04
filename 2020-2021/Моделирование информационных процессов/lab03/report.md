
---
# Front matter
lang: "ru"
title: "Лабораторная работа №3"
subtitle: "Моделирование стохастических процессов"
author: "Ли Тимофей Александрович"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: Fira Code
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: xelatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Исследовать стохастические процессы с помощью средства имитационного моделирования NS-2, а также с использованием приложения для построения графиков GNUplot.

# Выполнение лабораторной работы

## Пример реализации модели на NS-2

Создал файл example.tcl и написал следующий код: (рис. -@fig:001):

![example1.tcl](images/1.png){ #fig:001 }

Далее создал файл graph_plot с помощью команды touch graph_plot. Открыл его на редактирование и добавил следующий код  (рис. -@fig:002)

![graph_plot](images/2.png){ #fig:002 }

Далее сделал graph_plot исполняемым (команда chmod), далее провел компиляцию example.tcl и выполнил graph.plot с помощью gnuplot: (рис. -@fig:003)

![операции в терминале](images/3.png){ #fig:003 }

В результате был создан файл qm.pdf, содержащий результаты моделирования в виде графика средней длины очереди: (рис. -@fig:004)

![график средней длины очереди с приближением сплайном и приближением Безье](images/4.png){ #fig:004 }

# Выводы

Исследовал стохастические процессы с помощью NS-2 и GNUplot.