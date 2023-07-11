# UI-автотесты для сайта Клуба приключений - [vpoxod_ru](https://www.vpoxod.ru/)
Учебный проект: UI-тесты для сайта vpoxod.ru

<!-- Технологии -->
## Использованы технологии:
<p  align="left">
  <code><img width="5%" title="Python" src="media/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="media/logo/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="media/logo/pytest.png"></code>
  <code><img width="5%" title="Selenium" src="media/logo/selenium.png"></code>
  <code><img width="5%" title="Selene" src="media/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="media/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="media/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="media/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="media/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

## Автоматизировано тестирование функционала:
* Поле поиска в хедере (позитивный и негативный сценарий)
* Форма поиска на главной - быстрый подбор путешествия по параметрам
* Подбор путешествия по параметрам (по цене)
* Проверка главного меню сайта
* Проверка файла логотипа

## Запуск тестов в Jenkins
<p  align="left">
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
</p>

### [Jenkins](https://jenkins.autotests.cloud/job/005_tsgibneva_vpoxodru_ui_tests/)

#### Запуск тестов:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
  
##### При нажатии на "Собрать сейчас" тесты собираются из GitHub и начинается прохождение тестов в Selenide.
<p  align="left">
  <code><img width="45%" title="Jenkins" src="media/screenshot/Jenkins.png"></code>
</p>

## В результате генерируется allure-отчет
<p  align="left">
  <code><img width="5%" title="Jenkins" src="media/logo/allure_report.png"></code>
</p>

### [Allure-report](https://jenkins.autotests.cloud/job/005_tsgibneva_vpoxodru_ui_tests/16/allure/)

##### Сводная инфомация по прогону тестов
<p  align="left">
  <code><img width="45%" title="Сводная информация в allure-report" src="media/screenshot/Allure_report1.png"></code>
</p>

##### Инофграфика
<p  align="left">
  <code><img width="45%" title="Инфографика в allure-report" src="media/screenshot/Allure_report2.png"></code>
  <code><img width="45%" title="Инфографика в allure-report" src="media/screenshot/Allure_report3.png"></code>
</p>

##### Во вкладке Behavoirs тесты сгруппированы с точки зрения бизнес-логики, есть описание шагов, скриншот последнего шага теста, браузерные логи, видео прохождения кейса
<p  align="left">
  <code><img width="45%" title="Результаты тестов в allure-report" src="media/screenshot/Allure_report4.png"></code>
  <code><img width="45%" title="Результаты тестов в allure-report" src="media/screenshot/Allure_report5.png"></code>
</p>

## Тут надо написать про аллюр-тестопс и джиру
<p  align="left">
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="media/logo/jira.png"></code>
</p>

## По результату прогона отправляется уведомление в телеграм
<p  align="left">
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>

<p  align="left">
  <code><img width="30%" title="Telegram notification" src="media/screenshot/telegram-notification.png"></code>
</p>


## Пример прогона теста с автоматизацией отправки формы поиска на главной
<p  align="left">
  <code><img width="5%" title="Selenoid" src="media/logo/selenoid.png"></code>
</p>

<p align="center">
  <img title="Video" src="media/screenshot/search_form_test.gif"/>
</p>
