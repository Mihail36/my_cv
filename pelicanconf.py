AUTHOR = 'Михаил Петров'
SITENAME = 'Резюме'
SITEURL = 'https://mihail36.github.io/cv'

PATH = 'content'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'

THEME = 'resume'
CSS_FILE = 'main-2.css'

NAME = 'Михаил'
TAGLINE = 'Студент ПС-42'
PIC = 'profile.jpg'

EMAIL = 'mihailpetrov24@yandex.ru'
PHONE = '+7 (905) 379-05-99'
GITHUB = 'Mihail36'

CAREER_SUMMARY = 'Студент 4 курса программной инженерии, увлечён программированием.'

SKILLS = [
    {'title': 'Python', 'level': '15'},
    {'title': 'C++', 'level': '25'},
    {'title': 'HTML5 & CSS', 'level': '10'},
    {'title': 'React', 'level': '7'},
    {'title': 'SQL', 'level': '12'},
    {'title': 'Docker', 'level': '3'},
]

PROJECT_INTRO = 'Ниже приведены репозитории, разработанные и изученные в рамках 4 курсов университета, демонстрирующие практическое применение теоретических знаний и развитие навыков программирования.'
PROJECTS = [
    {
        'title': 'Алгоритмы и структуры данных',
        'tagline': 'Репозиторий с реализациями классических алгоритмов (сортировка, поиск) и структур данных (деревья, графы).'
    },

    {
        'title': 'Контроль качества',
        'tagline': 'Проекты, посвящённые тестированию и анализу качества программного обеспечения.'
    },
    
    {
        'title': 'Параллельное программирование',
        'tagline': 'Примеры использования многопоточности и параллельных алгоритмов для повышения производительности.'
    },
    
    {
        'title': 'Распределённое программирование',
        'tagline': 'Репозиторий, демонстрирующий алгоритмы и методы распределённых вычислений.'
    },
    
    {
        'title': 'Объектно-ориентированное программирование',
        'tagline': 'Репозиторий с примерами и упражнениями по ООП, демонстрирующими принципы модульности и масштабируемости.'
    }
]

LANGUAGES = [
    {'name': 'Русский', 'description': 'Родной'},
    {'name': 'Английский', 'description': 'Средний'},
]

INTERESTS = ['Программирование', 'Музыка', 'Видеоигры']

EXPERIENCES = []

EDUCATIONS = [
    {
        'degree': 'Бакалавр программной инженерии',
        'meta': 'ПГТУ',
        'time': '2021-2025'
    },
]
