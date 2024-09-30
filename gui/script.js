const areas = ['area1', 'area2', 'area3', 'area4'];

areas.forEach(areaId => {
    document.getElementById(areaId).addEventListener('input', function() {
        const latexCode = this.value;
        const outputElement = document.getElementById('output');
        
        outputElement.innerHTML = `
        ${generateBasement()}<br><br><br>`;

        MathJax.typesetPromise([outputElement]).catch((err) => console.log(err.message));
    });
});


document.getElementById('viewRawCode').addEventListener('click', function() {
    const htmlContent = generateHtmlContent()
    var newTab = window.open('', '_blank');
    
    newTab.document.open();
    newTab.document.write(htmlContent);
    newTab.document.close();
});

function generateHtmlContent() {
    const area1 = document.getElementById('area1').value;
    const area2 = document.getElementById('area2').value;
    const area3 = document.getElementById('area3').value;
    const area4 = document.getElementById('area4').value;

    const htmlContent = `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="content-language" content="en">
    <meta name="keywords" content="Savchenko Problems in Physics, Savchenko solutions, physics problems, physics olympiad preparation, IPhO, Jaan Kalda">
    <meta name="description" content="${removeImageSection(area2)}">
    <meta name="author" content="Aliaksandr Melnichenka">
    <meta name="date" content="2023-10" scheme="YYYY-MM">
    <meta property="og:title" content="${removeImageSection(area2)}">
    <meta property="og:image" content="img/logo.png">
    <meta property="og:description" content="${removeImageSection(area2)}">
    <meta name="yandex-verification" content="6cfda41f74038368">
    <title>${removeImageSection(area2)}</title>
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
  <body style="">
      <header style="text-align:center;">
       <a href="../../" style="text-decoration: none;">
            <div id="logo">
                <span><img src="../../img/book.png"></span><span>Savchenko Solutions</span>
            </div>
        </a>
        <p class="author">
            Solutions&amp;nbsp;of&amp;nbsp;Savchenko Problems&amp;nbsp;in&amp;nbsp;Physics <br>
            <i><b>knowledge must be free</b></i>
        </p>
  </header>

        <h3 id="back-link"><a href="../../#${getFirstTwoSegments(document.getElementById('area1').value)}">$\\leftarrow$Back</a></h3>
    ${generateBasement()}

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

</html>`;

    return ('<html><head><title>HTML Code</title>' +
        '<style>body { background-color: black; color: white; }' +
        '</style></head>' +
        '<body><pre>' + 
        htmlContent.replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/\\\)/g, "$").replace(/\\\(/g, '$').replace(/>/g, '&gt;') + 
        '</pre></body></html>');
}

function getFirstTwoSegments(input) {
  const segments = input.split('.');
  
  return segments.slice(0, 2).join('.');
}

function removeImageSection(inputString) {
  const imageSectionRegex = /<\/p>[\s\S]*?<p>/g;
  const cleanedString = inputString.replace(imageSectionRegex, '');

  return cleanedString.replace(/\n/g, '').replace(/\$/g, '');
}

function generateBasement() {
    const area1 = document.getElementById('area1').value;
    const area2 = document.getElementById('area2').value;
    const area3 = document.getElementById('area3').value;
    const area4 = document.getElementById('area4').value;

    const htmlContent = `
        <h3> Statement </h3>
        <p>
            $${area1}.$ ${area2}
        </p>

        <h3>Solution</h3>
        <p>
            ${area3}
        </p>

        <h4>Answer</h4>
        <p>
            ${area4}
        </p>
`;

    return (htmlContent);
}

function handleDrop(event) {
    event.preventDefault();

    const textarea = event.target;
    const dropPosition = textarea.selectionStart;
    const droppedData = event.dataTransfer.getData('text/plain');

    // Check if a URL is dropped
    if (droppedData.startsWith('http') && droppedData.match(/\.(jpeg|jpg|png|gif)$/i)) {
        const imageUrl = droppedData;

        textarea.value =
        `${textarea.value.substring(0, dropPosition)}
</p>
<center>
  <figure>
    <img src="${imageUrl}"
      loading="lazy"  width="230" />
    <figcaption>
      For problem $${document.getElementById('area1').value}$
    </figcaption>
  </figure>
</center>
<p>${textarea.value.substring(dropPosition)}`;
        
    } else if (event.dataTransfer.files.length > 0) {
        // Handle local files
        const file = event.dataTransfer.files[0];
        const filePath = file.path || file.name;

        textarea.value =
        `${textarea.value.substring(0, dropPosition)}
</p>
<center>
  <figure>
    <img src="${filePath}"
      loading="lazy"  width="230" />
    <figcaption>
      For problem $${document.getElementById('area1').value}$
    </figcaption>
  </figure>
</center>
<p>${textarea.value.substring(dropPosition)}`;
    }
}
function handleDragOver(event) {
    event.preventDefault(); // Prevent default behavior to allow drop
}

['area2', 'area3'].forEach(id => {
    const textarea = document.getElementById(id);
    textarea.addEventListener('dragover', handleDragOver);
    textarea.addEventListener('drop', handleDrop);
});
