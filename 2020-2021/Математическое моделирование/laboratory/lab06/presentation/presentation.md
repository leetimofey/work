---
## Front matter
lang: "ru"
title: Лабораторная работа № 6
author: Ли Тимофей Александрович, НФИбд-01-18


## Formatting
toc: false
slide_level: 2
theme: metropolis
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: Consolas
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---


# Цель работы

## Цель работы

- Изучить модель эпидемии, построить графики изменения числа особей трех групп (восприимчивые к болезни, инфицированные и обладающие иммунитетом) для случаев I(0)<=I' и I(0)>I'.

# Задачи

## Задачи

- изучить теорию о модели эпидемии
- реализовать программный код для 32 варианта

# Ход работы

## Описание решения

![Описание решения](images/1.png){ #fig:001 }

## Начальные условия и решение системы уравнений для первого случая

![код1](images/4.png){ #fig:002 }

## Решение для второго случая

![код2](images/5.png){ #fig:003 }

## График для первого случая

![график1](images/2.png){ #fig:004 }

## График для второго случая

![график2](images/3.png){ #fig:005 }

# Выводы

  - Изучил модель эпидемии
  - Реализовал программный код для поставленной задачи

