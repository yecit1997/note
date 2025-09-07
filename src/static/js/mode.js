let body = document.getElementById('body');
let btnMode = document.getElementById('btn-mode');

// Obtiene el modo del almacenamiento local
const mode = localStorage.getItem('mode');
if (mode === 'dark-mode') {
    body.classList.add('dark-mode');
}

btnMode.addEventListener('click', function() {
    // Alterna la clase 'dark-mode'
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        localStorage.setItem('mode', 'light-mode');
    } else {
        body.classList.add('dark-mode');
        localStorage.setItem('mode', 'dark-mode');
    }
});