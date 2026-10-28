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