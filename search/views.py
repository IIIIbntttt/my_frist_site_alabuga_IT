from django.shortcuts import render
import re

s = 'Тетрадь смерти (яп. デスノート Дэсу Но:то, Death Note) — манга за авторством Цугуми Обы, проиллюстрированная Такэси Обатой, выпускавшаяся в журнале Weekly Shonen Jump с 1 декабря 2003 года. Согласно опросу, проведённому в 2007 году министерством культуры Японии, занимает 10-е место среди лучшей манги всех времён[2].Манга «Тетрадь смерти» появилась в декабре 2003 года в виде пилотного выпуска, и в феврале 2004 года начала издаваться в еженедельном журнале Weekly Shonen Jump в виде сериала. Выход манги закончился в мае 2006 года. Манга содержала 108 глав, переизданых в 12 томах танкобонах в Японии. Позднее вышел 13-й том, своеобразная энциклопедия по миру «Тетради смерти».С октября 2006 по июнь 2007 года на телеканале Nippon TV прошла трансляция 37-серийного аниме-сериала. 31 августа 2007 года на том же телеканале Nippon TV показали «Тетрадь смерти — Переписывание: Глазами бога» — специальную полнометражную версию аниме-сериала, представляющую собой компиляцию 1-25 серий, дополненную новыми сценами. А 22 августа 2008 года вышла ещё одна специальная полнометражная версия аниме-сериала «Тетрадь смерти — Переписывание: Преемники L», представляющая собой компиляцию 26-37 серий с несколькими новыми сценами.Идея манги легла в основу двух парных игровых фильмов, вышедших в кинотеатрах Японии в июне («Тетрадь смерти») и ноябре 2006 года («Тетрадь смерти: Последнее имя»). Оба художественных фильма частично используют сюжет манги, и по большей части представляют собой самостоятельные произведения. В феврале 2008 года вышел ещё один игровой фильм «L: Изменить мир», являющийся спин-оффом первых двух фильмов. В августе 2006 года по мотивам манги вышла книга авторства Нисио Исина «Death Note Другая тетрадь. Дело о серийных убийствах B. B. в Лос-Анджелесе».10 января 2007 года аниме и манга «Тетрадь смерти» были лицензированы для издания на территории США компанией VIZ Media. 12 октября 2007 года компания «Мега-Аниме» объявила о приобретении лицензии на российское издание аниме-сериала. Трансляция прошла с 20 октября по 29 декабря 2007 года на канале 2x2. В 2019 году студия СВ-Дубль приобрела права на аниме-адаптацию, и трансляция прошла на телеканале FAN.В июне 2008 года компания «Комикс-Арт» объявила о приобретении лицензии на российское издание манги Death Note. Первый том «Скука» вышел в начале 2009 года. По состоянию на сентябрь 2012 года на русском языке выпущены все 12 томов[3].'


def index(request):
    return render(request, 'search/index.html')


def search(request):
    message = request.GET.get('q', '')
    file = s
    f = file.split(".")
    r = re.compile(".*" + message)
    if bool(list(filter(r.match, f))) == False:
        newlist = 'Совпадений не найдено'
    else:
        newlist = list(filter(r.match, f))
    return render(request, 'search/result.html', {'message': newlist})
