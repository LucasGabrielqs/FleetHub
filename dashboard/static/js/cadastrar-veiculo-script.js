document.addEventListener("DOMContentLoaded", function () {
    const valorInput = document.getElementById("valcompra");
    const kmInput = document.getElementById("km");
    const motorInput = document.getElementById("motor");

    // Função para formatar números com separadores de milhar
    function formatNumber(value) {
        return parseInt(value).toLocaleString("pt-BR");
    }

    // Formata o campo Valor com R$ no início
    valorInput.addEventListener("input", function (e) {
        let value = e.target.value.replace(/[^\d]/g, ""); // Remove caracteres não numéricos
        e.target.dataset.rawValue = value; // Armazena o valor sem formatação
        e.target.value = value ? `R$ ${formatNumber(value)}` : "";
    });

    // Formata o campo KM com "km" no final
    kmInput.addEventListener("input", function (e) {
        let value = e.target.value.replace(/[^\d]/g, ""); // Remove caracteres não numéricos
        e.target.dataset.rawValue = value; // Armazena o valor sem formatação
        e.target.value = value ? `${formatNumber(value)} km` : "";
    });

    // Formata o campo Motor com "cv" no final
    motorInput.addEventListener("input", function (e) {
        let value = e.target.value.replace(/[^\d]/g, ""); // Remove caracteres não numéricos
        e.target.dataset.rawValue = value; // Armazena o valor sem formatação
        e.target.value = value ? `${value} cv` : "";
    });

    // Permite edição contínua (sem reintroduzir sufixos ao apagar)
    [valorInput, kmInput, motorInput].forEach(input => {
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
            if (input === valorInput) {
                input.value = rawValue ? `R$ ${formatNumber(rawValue)}` : "";
            } else if (input === kmInput) {
                input.value = rawValue ? `${formatNumber(rawValue)} km` : "";
            } else if (input === motorInput) {
                input.value = rawValue ? `${rawValue} cv` : "";
            }
        });
    });
});
