## 1.Что это такое ?

Этот код позволяет сформировать и отобразить список из 20 самых популярных github репозиториев, созданных за полседние 7 дней

## 2.Системные требования
Для работы с программой понадобится Python3.5 (который скорее всего у вас уже установлен, если Вы используете Linux)  
Также может понадобиться установить модуль `requests`, сделать это можно выполнив `pip3 install -r requirements.txt`
```
# pip3 install -r requirements.txt
```

## 3.Где можно скачать  
Можно форкнуть здесь - [20 свежих и  популярных репозиториев](https://github.com/aligang/9_github_trending)  
и затем скачать 
```
git clone https://github.com/<юзернейм-аккаунта-на-гите>/9_github_trending
```

## 4.Как этим пользоваться...  
*a.Данный код может быть исползован как самостоятельная программа,*  

```bash
$   python3 github_trending.py 

Список 20  самых популярных репозиториев открытыза последние 7 дней

--------------------------------------------------------------

Репозиторий: paragonie/past,
расположен https://api.github.com/repos/paragonie/past

открытые issues:
issue: setClaims overwrites what was defined with setExpiration in the php example
описан https://api.github.com/repos/paragonie/past/issues/26

--------------------------------------------------------------

Репозиторий: burningcl/wechat_jump_hack,
расположен https://api.github.com/repos/burningcl/wechat_jump_hack

открытые issues:
issue: 运行不成功
описан https://api.github.com/repos/burningcl/wechat_jump_hack/issues/61
issue: 分最高的是用的那款手机啊？
описан https://api.github.com/repos/burningcl/wechat_jump_hack/issues/60
issue: 为什么我的手机向左跳的时候可以 但是向右跳的时候不行 biu的一下就飞了
описан https://api.github.com/repos/burningcl/wechat_jump_hack/issues/59
issue: 系统找不到指定的文件
описан https://api.github.com/repos/burningcl/wechat_jump_hack/issues/58

--------------------------------------------------------------

Репозиторий: turbo/KPTI-PoC-Collection,
расположен https://api.github.com/repos/turbo/KPTI-PoC-Collection

--------------------------------------------------------------

```

## 5.Какие функции могут быть переиспользованы в вашем коде
Функция `calculate_reference_date(days)` выдает дату, которая соответсвует дню, который был `days` суток назад
Функция `get_trending_repositories` формирует выдаёт список самых 20 популярных репозиториев созданных за последнюю неделю
Функция `get_open_issues`  обогащает список, полученный от функции `get_trending_repositories` информацией об активных issues

Импортировать и использовать функцию коди можно  следующим образом:  
```python
from github_trending import calculate_reference_date
from github_trending import get_trending_repositories
from github_trending import get_open_issues


reference_date = calculate_reference_date(days)
trending_repos_list = get_trending_repositories(top_size, reference_date)
trending_repos_info_list = get_open_issues(trending_repos_list)
```

## 6. Цели
Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
