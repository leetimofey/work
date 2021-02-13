---
# Front matter
lang: ru-RU
title: "Лабораторная работа №1"
subtitle: "Git и markdown"
author: "Ли Тимофей Александрович, НФИбд-01-18"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
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

Освоить работу с Git, научиться пользоваться облегченным языком разметки Markdown.

# Задание

- Создать репозиторий
- Создать и загрузить файлы на github
- Сделать коммит и пуш на github
- Подключить SSH ключ к репозиторию
- Сделать релиз
- Оформить отчет и презентацию в форматах pdf, markdown


# Выполнение лабораторной работы

Создал репозиторий на github (рис. 1)

![Название рисунка](image/screen1.png){рис. 1}


Создал локальный репозиторий, добавил в него все файлы. (рис. 2)

![Название рисунка](image/screen2.png){рис. 2}


Загрузил все файлы на github (рис. 3)

![Название рисунка](image/screen3.png){рис. 3}


Подключил SSH ключ к аккаунту. (рис. 4-5)

![Название рисунка](image/screen4.png){рис. 4}
![Название рисунка](image/screen5.png){рис. 5}

Сделал релиз (рис. 6)

![Название рисунка](image/screen6.png){рис. 6}

# Выводы

Освоил работу с Git, научился пользоваться облегченным языком разметки Markdown.
