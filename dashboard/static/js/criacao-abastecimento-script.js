document.getElementById('img').addEventListener('change', function(event) {
    const preview = document.getElementById('preview');
    const file = event.target.files[0]; // Obtém o arquivo selecionado

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result; // Define a imagem no preview
            preview.style.display = 'block'; // Exibe a imagem
        };
        reader.readAsDataURL(file); // Lê o arquivo como URL base64
    } else {
        preview.style.display = 'none'; // Esconde o preview se nenhum arquivo for selecionado
    }
});
