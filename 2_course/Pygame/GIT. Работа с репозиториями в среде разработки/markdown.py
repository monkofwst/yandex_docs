# ->#

def my_superfunction():
    print('What an awesome print!')


def main():
    print('My first git program')
    print('And I change it every day')
    print('Again')
    print('UFO came and added this line')
    my_superfunction()


if __name__ == '__main__':
    main()

# ->#


"""
!!!тут.
https://semver.org/lang/ru/

Релиз/Тег — тег в ветке master, совпадающий по имени с именем релизной ветки (подробнее про теги читайте в инструкции git help tag)
В качестве примера трекинг-систем можно привести следующие:

!!!JIRA
https://www.atlassian.com/ru/software/jira

!!!Redmine
https://www.redmine.org/

!!!Яндекс.Трекер
https://tracker.yandex.ru/

Общая схема работы с репозиторием в рамках GitFlow выглядит так:

"""

'''На этом возможности PyCharm по работе с Git не заканчиваются. Сами разработчики JetBrains подготовили подробную 

!!!инструкцию
 
https://www.jetbrains.com/help/pycharm/using-git-integration.html
 
 по работе 
с Git из PyCharm (на английском языке). Там вы найдёте много полезной информации и узнаете о дополнительных возможностях PyCharm, 
которые мы не успели рассмотреть за время урока.
'''

'''Кроме того, мы не затронули целый ряд полезных тем, касающихся работы с репозиториями. Поэтому предлагаем вам изучить их самостоятельно.

!!!Форки в GitHub — очень мощный инструмент для работы с публичными репозиториями, популярный в opensource community
https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/working-with-forks

!!!Rebase — еще один очень популярный способ объединения изменений, удобный при работе над достаточно большими фичами
https://habr.com/ru/articles/161009/

!!!Cherry-pick и reset — инструменты для работы с историей коммитов: извлечением какого-либо коммита, или откатом последних коммитов
http://marklodato.github.io/visual-git-guide/index-ru.html


Так же мы рекомендуем пошаговый 
!!!самоучитель
 https://githowto.com/ru
 
 по Git для закрепления пройденного материала'''