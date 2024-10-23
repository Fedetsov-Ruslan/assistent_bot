## Умный ассистент, на базе ИИ

## Как он работает и что он может

# Что надо сделать:
 - Установить библиотеки из requirements.txt
 - Создать файл ".env" и перенести файла ".env.example" переменные и передать в них ключи.
 - В переменную "client_query" записываем интересующий нас запрос
 - В переменную "tagret_human" записываем нашу целевую аудиторию

# Что потом делает он:
 - Сначала он перефразирует запрос клиента, чтоб в поиске выдало более валидный результат
 - Отправляется запрос на полученне ссылок по запросу в "serper"  
 - Проходимся по полученным ссылкам и собираем текст статей из них
 - Заносим этот текст в переменную "text_blog" (Можно в файл сохронить, это уже по желанию. Я использовал на этапе проверки, чтоб не проходить предыдущие пункты)
 - Отправляем текс для анализа в GPT частями, попутно проверяя размер отправленных частей, чтоб не превысит лимит.
 - Получаем ответ. Сораняем его в "blog.docx"
 - Отправляем текст для блога обратно на анлиз, чтоб получить prompt для генерации изображения
 - Получаем ответ. Сохраняем его в "prompt_image.docx"
 - Отправляем запрос на ренерацию изображения
 - Сохраняем полученное изображение

# Используемые подходы и библиотеки
 В основном использовалась библиотека openai, для нее составлялись prompt-ы.
 Для поиска в интернете использовался API serper
 Для парсинга текста использовал BeautifulSoup
 ticktoken для подсчета токенов в запросе, чтоб не превысить лимит
 ну и так по мелочи для сохранения docx и requests

## фидбэк
 
# Как я бы усовершенствовал
 - Использовать какое либо приложение или бота, для сбора информации
    напримео: запроса, целевой аудитории, для чего составляем материла(в данному случае блог), предпочитаемый размер текста и другое.
    Очень удобно будет такую информацию собирать через бота, передавать эту информацию в данного ассистента, а он уже будет реализовывать все
 - Использовать ассинхронность 
 - Использовать предварительно созданного ассистента для генерации изображений

 # Впечатления
  - Чесно говоря, большее количество времени я потратил именно на генерацию изображений.
    До этого не приходилось генерировать изображения через openai. Я генерировал через готовые ассистенты, например через него "https://chatgpt.com/g/g-pmuQfob8d-image-generator"
    Поэтому может картинки будут детскими что ли :D
  - В остальном никаких затруднений я не испытал :)