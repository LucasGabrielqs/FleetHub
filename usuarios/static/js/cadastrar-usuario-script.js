document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");
    const telefoneInput = document.getElementById("telefone");
    const cepInput = document.getElementById("input-cep");
    const form = document.querySelector("form");

    // Função para formatar o CPF (000.000.000-00)
    // if (cpfInput) {
    //     cpfInput.addEventListener("input", function (e) {
    //         let value = e.target.value.replace(/\D/g, ""); // Remove caracteres não numéricos
    //         if (value.length > 11) value = value.slice(0, 11); // Limita a 11 dígitos
    //         e.target.value = value
    //             .replace(/(\d{3})(\d)/, "$1.$2") // Adiciona o primeiro ponto
    //             .replace(/(\d{3})(\d)/, "$1.$2") // Adiciona o segundo ponto
    //             .replace(/(\d{3})(\d{2})$/, "$1-$2"); // Adiciona o hífen
    //     });
    // }

    // Função para formatar o telefone (+55 (00) 00000-0000)
    if (telefoneInput) {
        telefoneInput.addEventListener("input", function (e) {
            let value = e.target.value.replace(/\D/g, ""); // Remove caracteres não numéricos
            if (value.length > 11) value = value.slice(0, 11); // Limita a 11 dígitos
            e.target.value = value
                .replace(/(\d{2})(\d)/, "($1) $2") // Adiciona os parênteses e espaço
                .replace(/(\d{5})(\d{4})$/, "$1-$2"); // Adiciona o hífen
        });
    }

    // Função para formatar o CEP (00000-000)
    if (cepInput) {
        cepInput.addEventListener("input", function (e) {
            let value = e.target.value.replace(/\D/g, ""); // Remove caracteres não numéricos
            if (value.length > 8) value = value.slice(0, 8); // Limita a 8 dígitos
            e.target.value = value.replace(/(\d{5})(\d{3})$/, "$1-$2"); // Adiciona o hífen
        });
    }

    // Validação antes de enviar o formulário
    if (form) {
        form.addEventListener("submit", function (e) {
            if (cpfInput && cpfInput.value.replace(/\D/g, "").length !== 11) {
                alert("O CPF deve conter 11 dígitos.");
                e.preventDefault();
            }
            if (telefoneInput && telefoneInput.value.replace(/\D/g, "").length !== 11) {
                alert("O telefone deve conter 11 dígitos.");
                e.preventDefault();
            }
            if (cepInput && cepInput.value.replace(/\D/g, "").length !== 8) {
                alert("O CEP deve conter 8 dígitos.");
                e.preventDefault();
            }
        });
    }

    const alertElem = document.getElementById('alert');
    if (alertElem) {
        setTimeout(function () {
            alertElem.style.display = 'none';
        }, 5000);
    }


});

document.getElementById('img').addEventListener('change', function(event) {
    const preview = document.getElementById('preview');
    const fileInput = event.target;
    const file = fileInput.files[0];

    console.log("Arquivo selecionado: ", file);  // Para verificar se o arquivo está sendo capturado corretamente

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    } else {
        preview.style.display = 'none';
    }
});

