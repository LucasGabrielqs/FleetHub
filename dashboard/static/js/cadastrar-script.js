document.addEventListener("DOMContentLoaded", () => {
    // Funções de formatação para campos específicos
    const mascaras = {
        cpf: (valor) =>
            valor
                .replace(/\D/g, "") // Remove caracteres não numéricos
                .replace(/(\d{3})(\d)/, "$1.$2") // Adiciona o primeiro ponto
                .replace(/(\d{3})(\d)/, "$1.$2") // Adiciona o segundo ponto
                .replace(/(\d{3})(\d{1,2})$/, "$1-$2"), // Adiciona o traço

        telefone: (valor) =>
            valor
                .replace(/\D/g, "") // Remove caracteres não numéricos
                .replace(/^(\d{2})(\d)/, "($1) $2") // Adiciona parênteses
                .replace(/(\d{4,5})(\d{4})$/, "$1-$2"), // Adiciona o traço

        cep: (valor) =>
            valor
                .replace(/\D/g, "") // Remove caracteres não numéricos
                .replace(/(\d{5})(\d{1,3})$/, "$1-$2"), // Adiciona o traço

        ddd: (valor) =>
            valor.replace(/\D/g, "").slice(0, 2), // Remove não numéricos e limita a 2 dígitos
    };

    // Aplica máscaras nos inputs
    const camposComMascara = {
        cpf: "cpf",
        telefone: "telefone",
        cep: "cep",
        ddd: "ddd",
    };

    Object.entries(camposComMascara).forEach(([campo, id]) => {
        const input = document.getElementById(id);
        input?.addEventListener("input", (e) => {
            e.target.value = mascaras[campo](e.target.value);
        });
    });

    // Limpar os campos quando o botão "Cancelar" for clicado
    const form = document.querySelector("form");
    if (form) {
        const botaoCancelar = document.querySelector(".btn-reset");
        if (botaoCancelar) {
            botaoCancelar.addEventListener("click", () => {
                form.reset(); // Limpa os valores dos inputs
                form.querySelectorAll("input").forEach((input) => {
                    input.style.borderColor = ""; // Remove bordas de erro
                    input.setCustomValidity(""); // Limpa mensagens de erro
                });
            });
        }
    }
});
