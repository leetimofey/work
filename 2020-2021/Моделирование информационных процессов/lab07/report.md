
---
# Front matter
lang: "ru"
title: "Лабораторная работа №7"
subtitle: "Модель массового обслуживания"
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

Изучить модель массового обслуживания с 1 прибором и бесконечной очередью, реализовать ее с помощью xcos. 

# Выполнение лабораторной работы

В данной модели берем лямбда=0.3, мю=0.35 и z0=6.

Создал модель в xcos: (рис. -@fig:001):

![модель](images/1.png){ #fig:001 }

В модели использованы два суперблока, отвечающие за поступление и обработку заявок. Суперблок моделирования поступления заявок: (рис. -@fig:002)

![суперблок1](images/2.png){ #fig:002 }

Суперблок моделирования обработки заявок: (рис. -@fig:003)

![суперблок2](images/3.png){ #fig:003 }

Полученный график поступления и обработки заявок (черный и зеленый цвета соответственно): (рис. -@fig:004)

![график1](images/4.png){ #fig:004 }

График длины очереди: (рис. -@fig:005)

![график2](images/5.png){ #fig:005 }

# Выводы

Выполнил задание, изучил модель массового обслуживания.