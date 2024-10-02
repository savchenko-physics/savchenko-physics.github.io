import os
import csv
from src import count_solutions


def update_en(directory):
    MaxColumns = 3
    current_directory = f"{directory}\\en"
    def column_len(problems_number):
        ans = [problems_number // MaxColumns]*MaxColumns
        for i in range(problems_number % MaxColumns):
            ans[i]+=1
        return ans


    def existed_folders():
        folders = [f for f in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, f)) and "." in f]
        return sorted(folders, key=lambda x: list(map(int, x.split('.'))))

    def split_numbers(input_string):
        numbers = input_string.split('.')
        return [int(num) for num in numbers]

    def PrimeDistribution(problems_list):
        if not len(problems_list):
            return ""

        problems_html = """<ul class="column">"""
        for problem in problems_list:
            problems_html += f"""
                <li><a href="en/{problem}">{problem}</a></li>"""
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
    <meta name="keywords" content="Savchenko Problems in Physics, Savchenko solutions, physics problems, physics olympiad preparation, IPhO, Jaan Kalda">
    <meta name="description" content="The largest dataset of solutions of 'Savchenko. Problems in Physics'. Savchenko’s Problems in General Physics is widely used to prepare for olympiads and it is a useful tool to
master and sharpen your skills and techniques in comptetitive problem solving. Some of these problems were a source
of inspiration for Jaan Kalda’s handouts and to some NBPhO problems. You may find problems from old IPhO
papers.">
    <meta name="author" content="Aliaksandr Melnichenka">
    <meta name="date" content="2023-10" scheme="YYYY-MM">
    <meta property="og:title" content="Savchenko Solutions">
    <meta property="og:image" content="img/logo.png">
    <meta property="og:description" content="A website with solutions to physics problems from Savchenko Textbook">
    <meta name="yandex-verification" content="6cfda41f74038368">
    <title>Savchenko Solutions</title>
    <link rel="stylesheet" href="css/css-latex/style.css">
    <link rel="icon" href="img/logo.png" type="image/png">
    <script src="js/jquery-1.10.1.min.js"></script>
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
       <a href="" style="text-decoration: none;">
            <div id="logo">
                <span><img src="img/book.png"></span><span>Savchenko Solutions</span>
            </div>
        </a>

        <p class="author">
            Solutions&nbsp;of&nbsp;Savchenko Problems&nbsp;in&nbsp;Physics <br>
            <i><b>knowledge must be free</b></i>
        </p>
        <h2 style="text-align: center;margin:0; font-size: 2.0rem;"><a href="ru">Решения на русском</a></h2>
        <h2 style="text-align: center; margin-top: 0.9rem; "><a href="en/savchenko_en.pdf" target="_blank">Problem statements</a></h2>


        <p class="description" id="description">
        The collection of problems in physics edited by O.Y. Savchenko is one of the most popular resources for preparation for physics olympiads in post-soviet countries. Some of these problems were a source of inspiration for Jaan Kalda’s handouts and to some NBPhO problems. You may find problems from old IPhO papers. For more than 30 years since its first edition, not a single complete guide to solving problems from it has been created.<br>
        On this website, you can observe a non-profit startup creating the first wizard of this collection with the design of solutions of <a href="about#team">different authors</a>. In total,  """ + str(
        count_solutions.count(directory)) + """ solutions have been published, out of 2,023 problems. In 2023, the project was launched, which is actively developing in Russian and English. If you'd like to contribute, feel free to email <a href="mailto: alex@savchenkosolutions.com" target="_blank">alex@savchenkosolutions.com</a>.
        </p>
    </header>


    <div class="pinned-container" id="pinned-container">
        <ol style="list-style-type:none; padding: 0;margin: 0;">
            <li><a href="#1">Kinematics</a></li>
            <li><a href="#2">Dynamics</a></li>
            <li><a href="#3">Oscillations and Waves</a></li>
            <li><a href="#4">Fluid Mechanics</a></li>
            <li><a href="#5">Molecular Physics</a></li>
            <li><a href="#6">Electrostatics</a></li>
            <li><a href="#7">Particles in an electric field</a></li>
            <li><a href="#8">Electric current</a></li>
            <li><a href="#9">Constant magnetic field</a></li>
            <li><a href="#10">Particles in complex fields</a></li>
            <li><a href="#11">Electromagnetic induction</a></li>
            <li><a href="#12">Electromagnetic waves</a></li>
            <li><a href="#13">Optics. Quantum physics</a></li>
            <li><a href="#14">Special theory of relativity</a></li>
        </ol>
    </div>
    <style>
        .pinned-container a {
            text-decoration: none;
            font-weight: bolder;
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
    with open("database/chapters.csv") as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            # dsa = f"""
            #     <li><a href="#{row[0]}">{row[1]}</a></li>"""
            # BaseHtml = BaseHtml+dsa
            chapters.append(row[1])

    sections = []
    with open("database/sections.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            sections.append(row)

    BaseHtml = BaseHtml+"""
        </ol>
    </div>


<main>
    <article class="margin-main">"""

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
    <footer class="row container">
      <br>
        <p>
            <small> © <strong>Savchenko Solutions</strong>, 2023-2024 <br></small>
        </p>
        <p>
            <small>All rights belong to the authors. <br> Commercial use of materials - with the written permission of the authors. <br> alex@savchenkosolutions.com <br></small>
        </p>
    </footer>
</body>

</html>
"""

    with open(f"{current_directory.replace("\\en", "")}\\index.html", "w", encoding="UTF-8") as file:
        file.write(BaseHtml)
