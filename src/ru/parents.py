import os
import csv

current_directory = os.getcwd().replace("src\\ru", "")

MaxColumns = 3
def column_len(problems_number):
    ans = [problems_number // MaxColumns]*MaxColumns
    for i in range(problems_number % MaxColumns):
        ans[i]+=1
    return ans


def existed_folders(directory):
    def safe_key(name):
        parts = name.split('.')
        try:
            return [int(part) for part in parts if part.isdigit()]
        except ValueError:
            return name

    folders = [f for f in os.listdir(directory)
               if os.path.isdir(os.path.join(directory, f))
               and os.path.exists(os.path.join(directory, f, 'index.html'))]

    return sorted(folders, key=safe_key)

def split_numbers(input_string):
    numbers = input_string.split('.')
    return [int(num) for num in numbers]

def PrimeDistribution(problems_list):
    if not len(problems_list):
        return ""

    problems_html = """<ul class="column">"""
    for problem in problems_list:
        chapter = int(problem.split('.')[0])
        section = int(problem.split('.')[1])

        if problem in english_problems[chapter][section]:
            problems_html += f"""
                <li><a style="color: hsla(240, 100%, 33%, 1);" target="_blank"href="../en/{problem}">{problem}</a></li>"""
        else:
            problems_html += f"""
                <li><a href="../{problem.split('.')[0]}/{problem}">{problem}</a></li>"""
    problems_html+="""
            </ul>
        """
    return problems_html

def ProblemsDistribution(problems_list):
    problems_html = ""
    val1 = 0
    for i in column_len(len(problems_list)):
        val2 = val1+i
        problems_html+=PrimeDistribution(problems_list[val1:val2])
        val1 = val2
    
    return problems_html

existed_problems = [[[] for _ in range(15)] for _ in range(15)]
english_problems = [[[] for _ in range(15)] for _ in range(15)]

def load_english():
    en_directory = f"{current_directory}\\en"
    # print(en_directory)
    for problem in existed_folders(en_directory):
        if problem.count('.') != 2:
            continue

        print(problem)
        chapter = int(problem.split('.')[0])
        section = int(problem.split('.')[1])

        if problem not in existed_problems[chapter][section]:
            existed_problems[chapter][section].append(problem)
            english_problems[chapter][section].append(problem)
            # existed_problems[chapter][section].sort()
            existed_problems[chapter][section] = sorted(existed_problems[chapter][section], key=lambda s: list(map(int, s.split('.'))))


BaseHtml = """<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="content-language" content="ru">
    <meta name="keywords" content="Решение Савченко по физике, Задачи Савченко по физике, задачи по физике, подготовка к олимпиадам по физике, Международная Физическая Олимпиада">
    <meta name="description" content=" Самая большая база данных решений «Савченко. Задачи по физике». Задачи Савченко по общей физике широко используются для подготовки к олимпиадам и являются полезным пособием, позволяющим освоения и оттачивания навыков и приемов решения компететных задач. Некоторые из этих задач послужили источником вдохновения для раздаточных материалов Яана Калды и для некоторых задач NBPhO. Вы можете найти задачи из старых статей IPhO из старых работ IPhO.">
    <meta name="author" content="Aliaksandr Melnichenka">
    <meta name="date" content="2023-10" scheme="YYYY-MM">
    <meta property="og:title" content="Решение Савченко О.Я.">
    <meta property="og:image" content="img/logo.png">
    <meta property="og:description" content="Решение задач по физике Савченко О.Я.">
    <meta name="yandex-verification" content="6cfda41f74038368">
    <title>Решение Савченко О.Я.</title>
    <link rel="stylesheet" href="https://savchenkosolutions.com/css/css-latex/style.css">
    <link rel="icon" href="https://savchenkosolutions.com/img/logo.png" type="image/png">
    <script src="https://savchenkosolutions.com/js/jquery-1.10.1.min.js"></script>
    <script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            extensions: ['tex2jax.js'],
            jax: ['input/TeX', 'output/HTML-CSS'],
            tex2jax: {
                inlineMath: [['$', '$'], ['$', '$']],
                processEscapes: true,
                processClass: 'tex2jax',
                ignoreClass: 'html'
            },
            showProcessingMessages: false,
            messageStyle: 'none'
        });
    </script>
</head>

<body id="top">
    <header class = "margin-main" style="text-align:center;">
        <h2>Решение задач из Савченко О.Я.</h2>
        <p class="author">
          Aliaksandr Melnichenka <br/>
          October 2023
        </p>
        <h2 style="text-align: center; margin-top: 0.9rem; "><a href="../savchenko.pdf" target="_blank">Условия задач</a></h2>
        <h3 style="text-align: center; margin-top: 0.8rem; margin-bottom: 0.2rem;"><a style="color: hsla(240, 100%, 33%, 1);" href="https://savchenkosolutions.com/">English solutions</a></h3>
        

        <p class="description">
        Сборник задач по физике под редакцией О.Я. Савченко - один из самых популярных ресурсов для подготовки к олимпиадам по физике в странах постсоветского пространства. За более чем 30 лет, прошедших с момента его первого издания, не было создано ни одного полного руководства по решению задач из него.<br>
        На этом сайте вы можете наблюдать попытку создания первого решебника этого сборника с оформлением решений <a href="https://savchenkosolutions.com/ru/about">разных авторов</a>. Всего было опубликовано более 700 решений из 2,023 задач. В 2023 году был запущен проект, который активно развивается на русском и английском языках. Если хотите поучаствовать, пишите <a href="mailto: alex@savchenkosolutions.com" target="_blank">alex@savchenkosolutions.com</a>.
        </p>
    </header>


    <div class="pinned-container" id="pinned-container">
        <ol style="list-style-type:none; padding: 0;margin: 0;">
            <li><a href="#1">Кинематика</a></li>
            <li><a href="#2">Динамика</a></li>
            <li><a href="#3">Колебания и волны</a></li>
            <li><a href="#4">Механика жидкости</a></li>
            <li><a href="#5">Молекулярная физика</a></li>
            <li><a href="#6">Электростатика</a></li>
            <li><a href="#7">Электрическое поле</a></li>
            <li><a href="#8">Электрический ток</a></li>
            <li><a href="#9">Магнетизм</a></li>
            <li><a href="#10">Сложные поля</a></li>
            <li><a href="#11">Э/м индукция</a></li>
            <li><a href="#12">Э/м волны</a></li>
            <li><a href="#13">Оптика</a></li>
            <li><a href="#14">СТО</a></li>
        </ol>
    </div>
    <style>
        .pinned-container a {
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
        }
        .pinned-container a:hover {
            text-decoration: underline;
        }
        @media (min-width: 1024px) {
            .margin-main {
                margin-left: 50px;
                width: 100%;
            }
            .pinned-container {
                width:auto;
            }
        }
    </style>
    <script type="text/javascript">
        function checkScroll() {
            var pinnedContainer = document.getElementById('pinned-container');
            
            if (window.scrollY > 300) {
                pinnedContainer.classList.add('visible');
                pinnedContainer.classList.remove('hover-disabled');
            } else {
                pinnedContainer.classList.remove('visible');
                pinnedContainer.classList.add('hover-disabled');
            }
        }

        window.addEventListener('load', checkScroll);
        window.addEventListener('scroll', checkScroll);
    </script>"""
chapters = []
with open("database/chapters.csv", encoding="UTF-8") as file:
    reader = csv.reader(file)

    for index, row in enumerate(reader):
        # dsa = f"""
        #     <li><a href="#{row[0]}">{row[1]}</a></li>"""
        # BaseHtml = BaseHtml+dsa
        chapters.append(row[1])

sections = []
with open("database/sections.csv", encoding="UTF-8") as file:
    reader = csv.reader(file)

    for row in reader:
        sections.append(row)

BaseHtml = BaseHtml+"""
        </ol>
    </div>


<main>
    <article class="margin-main">"""

for i in range(1,14):
    directory=current_directory+str(i)
    for problem in existed_folders(directory):
        chapter = int(problem.split('.')[0])
        section = int(problem.split('.')[1])

        existed_problems[chapter][section].append(problem)

load_english()

for index, chapter in enumerate(existed_problems):
    if all(not sublist for sublist in chapter):
        continue

    BaseHtml = BaseHtml+f"""
        <h2 id="{index}" style="text-align: center;">Глава {index}. {chapters[index-1]}</h2>
      """

    for index1, section in enumerate(chapter):
        if not len(section):
            continue
        FullName = f"{index}.{index1}"

        for index2, i in enumerate(sections):

            if i[0] == FullName:
                BaseHtml = BaseHtml+f"""
        <h3 id="{FullName}" style="text-align: center;">§ {i[0]}. {i[1]}</h3>
        <div class="columns">{ProblemsDistribution(section)}</div>
        """
                break
    
BaseHtml += """
          </div>
    </article>
</main>

  <script>
    MathJax = {
      tex: {
        inlineMath: [['$', '$'],],
      },
    }
    const typeFaceToggle = document.getElementById('typeface-toggle')
    const typeface = document.getElementById('typeface')
    typeFaceToggle.addEventListener('click', () => {
      document.body.classList.toggle('libertinus')
      typeface.textContent = document.body.classList.contains('libertinus') ? 'Libertinus' : 'Latin Modern'
    })

    const darkModeToggle = document.getElementById('dark-mode-toggle')
    darkModeToggle.addEventListener('click', () => {
      document.body.classList.toggle('latex-dark')
    })
  </script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-DDMB38YMLD');
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <footer class="row container">
      <br>
        <p>
            <small> © <strong>Savchenko Solutions</strong>, 2023-2024 <br></small>
        </p>
        <p>
            <small>Все права принадлежат авторам. <br> Коммерческое использование материалов — с письменного разрешения авторов. <br> alex@savchenkosolutions.com <br></small>
        </p>
    </footer>
</body>

</html>
"""

with open(f"{current_directory}\\ru\\index.html", "w", encoding="UTF-8") as file:
    file.write(BaseHtml)
