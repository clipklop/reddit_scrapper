# Reddit Scrapper

### Обучающий проект по парсингу Реддита [Reddit](https://www.reddit.com/).

В этот раз мы будем работать с Reddit. Это такая соцсеть для общения обо всём. Если вы не имели с ней дело, то устроена она так: там есть сабреддиты (тематические группы), в сабреддите пользователи постят посты, в постах есть комментарии.

Цель:
- Ваша задача – написать скрипт, который спрашивает сабреддит, парсит с него все посты за последние 3 дня и выводит топ пользователей, которые написали больше всего комментариев и топ пользователей, которые написали больше всего постов. Топ - это когда сверху тот, кто больше всех написал комментариев/постов, на втором месте следущий за ним и так далее.

- Для референса [Reddit API](https://www.reddit.com/dev/api/)

### Install
    pip install -r requirements

### Run
- Enter your Reddit API's credentianls into **praw.ini**
- To run **API Scrapper** module, use this command in the project root directory:
        
        python -m api_scrapper
- To run **Author Counter** module, use this command in the project root directory:
        
        python -m author_counter
