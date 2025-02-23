document.addEventListener("DOMContentLoaded", function () {
    const motorInput = document.getElementById("motor");

    // Função para formatar números com separadores de milhar
    function formatNumber(value) {
        return parseInt(value).toLocaleString("pt-BR");
    }

    // Formata o campo Valor com R$ no início

    // Formata o campo Motor com "cv" no final
    motorInput.addEventListener("input", function (e) {
        let value = e.target.value.replace(/[^\d]/g, ""); // Remove caracteres não numéricos
        e.target.dataset.rawValue = value; // Armazena o valor sem formatação
        e.target.value = value ? `${value} cv` : "";
    });

    // Permite edição contínua (sem reintroduzir sufixos ao apagar)
    [motorInput].forEach(input => {
        input.addEventListener("keydown", function (e) {
            if (e.key === "Backspace" || e.key === "Delete") {
                let rawValue = input.dataset.rawValue || ""; // Recupera o valor bruto sem formatação
                if (rawValue.length > 0) {
                    rawValue = rawValue.slice(0, -1); // Remove o último caractere
                    input.dataset.rawValue = rawValue; // Atualiza o valor bruto
                    input.value = rawValue; // Mostra o valor bruto temporariamente
                } else {
                    input.dataset.rawValue = ""; // Limpa o valor bruto
                    input.value = ""; // Limpa o campo
                }
                e.preventDefault();
            }
        });

        // Reaplica o formato ao sair do campo
        input.addEventListener("blur", function () {
            let rawValue = input.dataset.rawValue || ""; // Recupera o valor bruto
            if (input === motorInput) {
                input.value = rawValue ? `${rawValue} cv` : "";
            }
        });
    });
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
