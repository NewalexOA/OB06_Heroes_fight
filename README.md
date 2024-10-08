
# Учебный проект. Битва героев

## Описание проекта

"Битва героев" — это консольная текстовая игра на Python, в которой игрок и компьютер управляют героями и сражаются друг с другом в пошаговом бою. Каждый раунд игроки по очереди наносят урон друг другу, пока один из героев не потеряет все здоровье.

## Основные функции

- Игрок может выбрать имя для своего героя.
- У каждого героя есть здоровье и сила удара.
- В игре присутствует элемент случайности: сила удара варьируется в пределах ±10% от базовой силы атаки.
- Игрок и компьютер чередуют ходы, нанося друг другу урон.
- Игра завершается, когда здоровье одного из героев падает до 0 или ниже.

## Требования

Для запуска проекта требуется Python версии 3.6 или выше.

## Установка

1. Склонируйте репозиторий с GitHub:
   ```bash
   git clone https://github.com/NewalexOA/OB06_Heroes_fight.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd OB06_Heroes_fight
   ```

## Запуск игры

1. Запустите файл `main.py`:
   ```bash
   python main.py
   ```

2. Введите имя вашего героя и следите за ходом битвы в консоли.

## Структура проекта

- `main.py`: основной файл игры, в котором реализованы классы `Hero` и `Game`.
- `README.md`: документация проекта.
- `requirements.txt`: файл зависимостей (если будут добавлены зависимости, такие как сторонние библиотеки).

## Пример игрового процесса

```
Введите имя вашего героя: Ланселот
Начало игры!
Ланселот атакует Компьютер и наносит 22 урона!
У Компьютер осталось 78 здоровья.

Компьютер атакует Ланселот и наносит 18 урона!
У Ланселот осталось 82 здоровья.

...

Ланселот победил!
```

## План проекта

### Основные этапы разработки:

1. **Инициализация проекта:**
   - Создание репозитория и базовой структуры.
   
2. **Разработка классов:**
   - Реализация классов `Hero` и `Game`.

3. **Тестирование и отладка:**
   - Проверка работоспособности игры.

4. **Документация:**
   - Написание файла `README.md`.

5. **Улучшения:**
   - Добавление новых возможностей и механик в игру.

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для получения подробной информации.

