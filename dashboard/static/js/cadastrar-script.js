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

document.addEventListener("DOMContentLoaded", function () {
    const senha = document.getElementById("senha");
    const confirmarSenha = document.getElementById("confirmar_senha");
    const senhaFeedback = document.getElementById("senha-feedback");
    const confirmarSenhaFeedback = document.getElementById("confirmar-senha-feedback");
    const submitBtn = document.getElementById("submit-btn");

    const senhaRequisitos = [
        { regex: /.{8,}/, message: "A senha deve ter pelo menos 8 caracteres." },
        { regex: /[A-Z]/, message: "A senha deve conter pelo menos uma letra maiúscula." },
        { regex: /[a-z]/, message: "A senha deve conter pelo menos uma letra minúscula." },
        { regex: /\d/, message: "A senha deve conter pelo menos um número." },
        { regex: /[@$!%*?&]/, message: "A senha deve conter pelo menos um caractere especial (@, $, !, %, *, ?, &)." },
    ];

    function validarSenha() {
        const senhaValue = senha.value;
        let valid = true;
        senhaFeedback.textContent = "";

        senhaRequisitos.forEach(req => {
            if (!req.regex.test(senhaValue)) {
                valid = false;
                senhaFeedback.textContent = req.message;
            }
        });

        senhaFeedback.classList.toggle("valid", valid);
        return valid;
    }

    function verificarSenhasIguais() {
        const senhaValue = senha.value;
        const confirmarSenhaValue = confirmarSenha.value;

        if (senhaValue === confirmarSenhaValue && confirmarSenhaValue !== "") {
            confirmarSenhaFeedback.textContent = "As senhas correspondem!";
            confirmarSenhaFeedback.classList.add("valid");
            return true;
        } else {
            confirmarSenhaFeedback.textContent = "As senhas não correspondem.";
            confirmarSenhaFeedback.classList.remove("valid");
            return false;
        }
    }

    senha.addEventListener("input", () => {
        validarSenha();
        verificarSenhasIguais();
    });

    confirmarSenha.addEventListener("input", verificarSenhasIguais);

    submitBtn.addEventListener("click", function (e) {
        e.preventDefault();

        const senhaValida = validarSenha();
        const senhasIguais = verificarSenhasIguais();

        if (senhaValida && senhasIguais) {
            alert("Cadastro realizado com sucesso!");
            // Aqui você pode enviar o formulário ou executar outra ação
        } else {
            alert("Por favor, corrija os erros antes de continuar.");
        }
    });
});
