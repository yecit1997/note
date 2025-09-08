document.addEventListener('DOMContentLoaded', function() {
    const favoritoBtns = document.querySelectorAll('.favorito-btn');
    
    favoritoBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const notaId = this.dataset.noteId;
            const url = `/nota/toggle-favorito/${notaId}/`;

            fetch(url, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.favorito) {
                    this.classList.remove('bi-star');
                    this.classList.add('bi-star-fill');
                } else {
                    this.classList.remove('bi-star-fill');
                    this.classList.add('bi-star');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});