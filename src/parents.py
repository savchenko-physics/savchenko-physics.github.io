import os
import csv

current_directory = os.getcwd().replace("src", "en")
MaxColumns = 3
def column_len(problems_number):
    ans = [problems_number // MaxColumns]*MaxColumns
    for i in range(problems_number % MaxColumns):
        ans[i]+=1
    return ans

def existed_folders():
    folders = [f for f in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, f))]
    return sorted(folders, key=lambda x: list(map(int, x.split('.'))))

def split_numbers(input_string):
    numbers = input_string.split('.')
    return [int(num) for num in numbers]

def PrimeDistribution(problems_list):
    if not len(problems_list):
        return ""

    problems_html = """
            <ul class="column">"""
    for problem in problems_list:
        problems_html += f"""
                <li><a href="./{problem}">{problem}</a></li>"""
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

BaseHtml = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="content-language" content="en">
    <meta name="keywords" content="solutions, savchenko, physics problems, olympiad physics, physics book">
    <meta name="description" content="A website with solutions to physics problems from Savchenko Textbook">
    <meta property="og:title" content="Savchenko Solutions">
    <meta property="og:image" content="img/logo.png">
    <meta property="og:description" content="A website with solutions to physics problems from Savchenko Textbook">
    <meta name="yandex-verification" content="6cfda41f74038368">
    <title>Savchenko Solutions</title>
    <link rel="stylesheet" href="https://savchenko-physics.github.io/css/css-latex/style.css">
    <link rel="icon" href="https://savchenko-physics.github.io/img/logo.png" type="image/png">
    <script src="https://savchenko-physics.github.io/js/jquery-1.10.1.min.js"></script>
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
  <header style="text-align:center;">
    <h2>Solutions of Savchenko Physics Textbook</h2>
    <p class="author">
      Aliaksandr Melnichenka <br/>
      October 2023
    </p>
  </header>

    <h2 style="text-align: center;">📜<a href="https://savchenko-physics.github.io/en/savchenko_en.pdf" target="_blank">Problem statements</a></h2>
    <h3 style="text-align: center;"><a href="https://savchenko-physics.github.io/">Russian solutions</a></h3>
    <h3 style="text-align:center; margin: 0;">
        A beta version of the solutions book has become 
        <a href="https://savchenko-physics.github.io/en/solutions.pdf" class="tooltip" target="_blank">available
            <span class="tooltiptext">Stefan Nicov, Aliaksandr Melnichenka et al.</span>
        </a>
    </h3>

    <h2>Contents</h2>
    <ol>"""
chapters = []
with open("database/chapters.csv") as file:
    reader = csv.reader(file)

    for index, row in enumerate(reader):
        dsa = f"""
        <li>
            <a href="#{row[0]}">{row[1]}</a>
        </li>
        """
        BaseHtml = BaseHtml+dsa
        chapters.append(row[1])

sections = []
with open("database/sections.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        sections.append(row)

BaseHtml = BaseHtml+"""
    </ol>


  <main>
    <article>"""

for problem in existed_folders():
    chapter = int(problem.split('.')[0])
    section = int(problem.split('.')[1])

    existed_problems[chapter][section].append(problem)

for index, chapter in enumerate(existed_problems):
    if all(not sublist for sublist in chapter):
        continue

    BaseHtml = BaseHtml+f"""
        <h2 id="{index}" style="text-align: center;">Chapter {index}. {chapters[index-1]}</h2>
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

</body>

</html>
"""

with open(f"{current_directory}\\index.html", "w", encoding="UTF-8") as file:
    file.write(BaseHtml)