
---
# Front matter
lang: "ru"
title: "Лабораторная работа №11"
subtitle: "Модель СМО М/М/1"
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

Изучить модель СМО М/М/1, реализовать ее с помощью cpntools. 

# Выполнение лабораторной работы

## Ход работы

Построил модель в cpntools: (рис. -@fig:001):

![модель](images/1.png){ #fig:001 }

Добавил брейкпоинт Ostanovka и мониторы Queue Delay, Queue Delay Real, Long Delay Time: (рис. -@fig:002)

![брейкпоинт и мониторы](images/2.png){ #fig:002 }

Запустил симуляцию: (рис. -@fig:003)

![симуляция](images/3.png){ #fig:003 }

В результате создается директория output/logfiles с логами: (рис. -@fig:004)

![логи](images/4.png){ #fig:004 }

Затем я запустил ВМ, чтобы построить график изменения задержки очереди и график, показывающий, в какое время задержки превышали заданное значение (200). Первый график в gnuplot: (рис. -@fig:005)

![график задержки очереди](images/5.png){ #fig:005 }

 и второй: (рис. -@fig:006)

![график превышения задержки](images/6.png){ #fig:006 }

# Выводы

Выполнил задание, изучил модель СМО М/М/1.