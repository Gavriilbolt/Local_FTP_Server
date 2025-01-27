<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Простое приложение на Python с графическим интерфейсом для настройки и запуска FTP-сервера в локальной сети.">
    <title>FTP Server GUI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #444;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-left: 3px solid #333;
            overflow-x: auto;
        }
        .lang-toggle {
            text-align: right;
            margin-bottom: 20px;
        }
        .lang-toggle button {
            padding: 10px;
            background: #0078D4;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
    </style>
    <script>
        function toggleLang(lang) {
            document.getElementById('ru').style.display = lang === 'ru' ? 'block' : 'none';
            document.getElementById('en').style.display = lang === 'en' ? 'block' : 'none';
        }
    </script>
</head>
<body>

<div class="lang-toggle">
    <button onclick="toggleLang('ru')">Русский</button>
    <button onclick="toggleLang('en')">English</button>
</div>

<div id="ru">
    <h1>FTP Server GUI</h1>
    <p>Простое приложение на Python с графическим интерфейсом для настройки и запуска FTP-сервера в локальной сети.</p>

    <h2>Возможности:</h2>
    <ul>
        <li>Выбор директории для расшаривания.</li>
        <li>Поддержка анонимного доступа или авторизации по логину и паролю.</li>
        <li>Автоматическое определение локального IP-адреса.</li>
        <li>Настройка брандмауэра для открытия порта 21.</li>
        <li>Запуск и остановка сервера одной кнопкой.</li>
        <li>Отображение текущего статуса сервера (IP-адрес и режим работы).</li>
    </ul>

    <h2>Используемые технологии:</h2>
    <ul>
        <li>Python</li>
        <li>Tkinter (для графического интерфейса)</li>
        <li>pyftpdlib (для работы с FTP-сервером)</li>
    </ul>

    <h2>Установка и запуск:</h2>
    <pre>
pip install pyftpdlib
python main.py
    </pre>
</div>

<div id="en" style="display: none;">
    <h1>FTP Server GUI</h1>
    <p>A simple Python application with a graphical interface for configuring and launching an FTP server in a local network.</p>

    <h2>Features:</h2>
    <ul>
        <li>Selecting a directory to share.</li>
        <li>Support for anonymous access or authentication via login and password.</li>
        <li>Automatic detection of local IP address.</li>
        <li>Firewall configuration to open port 21.</li>
        <li>One-click server start/stop.</li>
        <li>Displaying current server status (IP address and operating mode).</li>
    </ul>

    <h2>Technologies used:</h2>
    <ul>
        <li>Python</li>
        <li>Tkinter (for GUI)</li>
        <li>pyftpdlib (for FTP server functionality)</li>
    </ul>

    <h2>Installation and launch:</h2>
    <pre>
pip install pyftpdlib
python main.py
    </pre>
</div>

</body>
</html>
