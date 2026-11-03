import { EventCard } from './components/EventCard.js';

export async function fetchAndRenderTeachers() {
    const track = document.getElementById('teachersCarousel');
    if (!track) return;

    // Показываем текст загрузки
    track.innerHTML = '<p class="loading-text">Загрузка преподавателей...</p>';

    try {
        const response = await fetch('http://127.0.0.1:8000/api/teachers/');
        if (!response.ok) throw new Error('Ошибка загрузки учителей');
        
        const teachers = await response.json();
        track.innerHTML = ''; // Очищаем текст загрузки

        if (teachers.length === 0) {
            track.innerHTML = '<p>Пока нет преподавателей</p>';
            return;
        }

        teachers.forEach(teacher => {
            const card = document.createElement('div');
            card.className = 'teacher-card';
            card.innerHTML = `
                <img src="${teacher.photo || 'assets/teachers/teacher1.jpg'}" alt="${teacher.name || 'Преподаватель'}">
                <h3>${teacher.full_name || teacher.name}</h3>
                <p>${teacher.position || ''}</p>
            `;
            track.appendChild(card);
        });
    } catch (error) {
        console.error('Ошибка:', error);
        track.innerHTML = '<p>Не удалось загрузить данные</p>';
    }
}

export async function fetchAndRenderCertificates() {
    const track = document.getElementById('certCarousel');
    if (!track) return;

    track.innerHTML = '<p class="loading-text">Загрузка сертификатов...</p>';

    try {
        const response = await fetch('http://127.0.0.1:8000/api/certificates/');
        if (!response.ok) throw new Error('Ошибка загрузки сертификатов');
        
        const certificates = await response.json();
        track.innerHTML = '';

        if (certificates.length === 0) {
            track.innerHTML = '<p>Пока нет сертификатов</p>';
            return;
        }

        certificates.forEach(cert => {
            const card = document.createElement('div');
            card.className = 'cert-card';
            card.innerHTML = `<img src="${cert.image || cert.photo}" alt="Сертификат">`;
            track.appendChild(card);
        });
    } catch (error) {
        console.error('Ошибка:', error);
        track.innerHTML = '<p>Не удалось загрузить данные</p>';
    }
}

export async function fetchAndRenderEvents() {
  const rail = document.getElementById('eventsRail');
  if (!rail) return;

  try {
    const response = await fetch('http://127.0.0.1:8000/api/events/'); // Проверь правильность URL
    if (!response.ok) throw new Error('Ошибка при загрузке событий');

    const events = await response.json();

    rail.innerHTML = '';
    events.forEach(event => {
      rail.appendChild(EventCard(event));
    });
  } catch (error) {
    console.error('Ошибка загрузки событий с бэкенда:', error);
  }
}

// Функция для подгрузки картинок с бэка по ключу (slug)
export async function fetchAndRenderPhotoByKey(key, imgElementSelector) {
  const imgElement = document.querySelector(imgElementSelector);
  if (!imgElement) return;

  try {
    const response = await fetch(`http://127.0.0.1:8000/api/other-photos/${key}/`);
    if (!response.ok) throw new Error(`Не удалось загрузить фото для ключа: ${key}`);
    
    const data = await response.json();
    
    // Проверяем поле, в котором бэкенд возвращает ссылку на картинку (обычно image или url)
    if (data.image) {
      imgElement.src = data.image;
    }
  } catch (error) {
    console.error(`Ошибка при загрузке фото (${key}):`, error);
  }
}

export async function fetchAndRenderCenterCarousel() {
  // Ищем правильный контейнер по id="centerCarousel" или классу .centerCarouselTrack
  const carouselContainer = document.getElementById('centerCarousel') || document.querySelector('.centerCarouselTrack');
  if (!carouselContainer) return;

  try {
    const response = await fetch('http://127.0.0.1:8000/api/interiors/');
    if (!response.ok) throw new Error('Ошибка загрузки фото интерьера');

    const interiors = await response.json();
    
    // Сортируем по полю order
    interiors.sort((a, b) => (a.order || 0) - (b.order || 0));

    carouselContainer.innerHTML = '';

    interiors.forEach(item => {
      // Корректируем путь к картинке, если бэкенд отдает относительный путь (например, /media/...)
      const imageUrl = item.image.startsWith('http') 
        ? item.image 
        : `http://127.0.0.1:8000${item.image}`;

      // Создаем сразу тег img, как того требуют твои CSS стили для .centerCarouselTrack img
      const img = document.createElement('img');
      img.src = imageUrl;
      img.alt = item.title || 'Интерьер центра';
      img.loading = 'lazy';

      carouselContainer.appendChild(img);
    });

  } catch (error) {
    console.error('Не удалось загрузить фото интерьера:', error);
  }
}