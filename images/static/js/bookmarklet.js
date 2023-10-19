// Базовый адрес сайта
const siteUrl = '//127.0.0.1:8000';

// Базовый адрес статических файлов
const styleUrl = siteUrl + 'static/css/bookmarklet.css';

// Минимальная высота и ширина изображений
const miwWidth = 250;
const minHeight = 250;


// Этот код аналогичен записи в HTML:
// <link rel="stylesheet" type="text/css" href= "//127.0.0.1:8000/static/css/
// bookmarklet.css?r=1234567890123456">
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);

// Загружаем HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
  <div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div>
  </div>`;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {

    // Извлекается главный контейнер букмарклета 
    bookmarklet = document.getElementById('bookmarklet');

    // Элемент bookmarklet используется для извлечения дочернего элемента
    // с классом images
    var imagesFound = bookmarklet.querySelector('.images');

    // Очищаем найденные изображения
    imagesFound.innerHTML = '';

    // Показать букмарклет
    bookmarklet.style.display = 'block';

    // Событие закрытия 
    bookmarklet.querySelector('#close')
                    .addEventListener('click', function(){
                        bookmarklet.style.display = 'none'
                    });

    // Найти изображения в DOM с минимальными размерами и отфильтровать подходящие
    images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
    images.forEach(image => {
        if(image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {
            var imageFound = document.createElement('img');
            imageFound.src = image.src;
            imagesFound.append(imageFound);
        }
    })

      // select image event
  imagesFound.querySelectorAll('img').forEach(image => {
    image.addEventListener('click', function(event){
      imageSelected = event.target;
      bookmarklet.style.display = 'none';
      window.open(siteUrl + 'images/create/?url='
                  + encodeURIComponent(imageSelected.src)
                  + '&title='
                  + encodeURIComponent(document.title),
                  '_blank');
    })
  })
}

// Запускаем букмарклет
bookmarkletLaunch();