let claro = 'bg-light text-dark';
let oscuro = 'bg-dark text-light';

let btnMode = document.getElementById('btn-mode');
let body = document.getElementById('body');


const mode = localStorage.getItem('mode');
if (mode) {
    body.className = mode;
} else {
    body.className = oscuro;
}

btnMode.addEventListener('click', function() {
    if (body.className === oscuro) {
        body.className = claro;
        localStorage.setItem('mode', claro);
    } else {
        body.className = oscuro;
        localStorage.setItem('mode', oscuro);
    }
});
