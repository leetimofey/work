
---
# Front matter
lang: "ru"
title: "Лабораторная работа №9"
subtitle: "Модель Накорми студентов"
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

Изучить модель "Накорми студента", реализовать ее с помощью cpntools. 

# Выполнение лабораторной работы

## Ход работы

Построил сеть в cpntools согласно видео-примеру: (рис. -@fig:001):

![сеть](images/1.png){ #fig:001 }

Запустил симуляцию. Последний шаг: (рис. -@fig:002)

![последний шаг симуляции](images/2.png){ #fig:002 }

Посчитал пространство состояний, посчитал граф, отобразил узлы графа: (рис. -@fig:003)

![граф состояний](images/3.png){ #fig:003 }

После этого сохранил отчет о пространстве состояний: (рис. -@fig:004)

![отчет](images/4.png){ #fig:004 }

Статистика по пространству состояний -- в графе 4 узла и 3 дуги, что видно и на изображении. Узлов и переходов у строго связанных компонентов столько же, сколько и в пространстве состояний, потому что все пути между вершинами односторонние, и компонента связности одна. 
В разделе свойств ограниченности видим максимальное и минимальное значение маркировок в двух видах (численном и мультимножества). Тут видим, что число голодных студентов принимает значение 0, значит задачу накормить всех мы выполнили. Относительно мультимножества, по верхним границам видим, что пирогов на позиции с пирогами максимум 5 шт, минимум 2, студентов на каждой из позиций от 0 до 3.
В разделе домашних свойств видим, что 4 маркировка домашняя, потому что только она достижима из всех остальных маркировок. Также из нее нет переходов, поэтому она мертвая. Отсутствие мёртвых переходов говорит о том, что нет переходов, которые никогда не смогут произойти, а отсутствие живых -- о том, что можно достигнуть такого состояния, после которого не произойдёт вообще никаких переходов. 
В разделе свойств справедливости указано, что нет последовательности бесконечных переходов, что видно и на графе. Поэтому типы справедливости не определены.

# Выводы

Выполнил задание, изучил модель "Накорми студента".