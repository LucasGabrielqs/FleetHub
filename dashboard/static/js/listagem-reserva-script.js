document.addEventListener('DOMContentLoaded', function() {
    const botoesVisualizar = document.querySelectorAll('.botao-visualizar-2'); // Seleciona todos os botões com essa classe
    
    botoesVisualizar.forEach(function(botaoVisualizar) {
        botaoVisualizar.addEventListener('click', function(event) {
            event.preventDefault();
            const reservaId = this.getAttribute('data-reserva-id');
            console.log("ID da Reserva:", reservaId);

            if (!reservaId) {
                console.error("ID da reserva não encontrado");
                return;
            }

            fetch(`/confirmar-entrega/${reservaId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
                    "X-Requested-With": "XMLHttpRequest"
                },
                body: JSON.stringify({
                    'acao': 'confirmar_entrega',
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("Entrega confirmada com sucesso!");
                    location.reload();
                } else {
                    console.log("Erro ao confirmar entrega: " + data.error);
                }
            })
            .catch(error => {
                console.error("Erro no AJAX:", error);
            });
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("#conteudo-esquerdo").forEach(reserva => {
        const statusElement = reserva.querySelector("#status-reserva");
        const botao = reserva.querySelector(".botao-visualizar-2"); // Usamos a classe, pois IDs devem ser únicos

        if (statusElement && botao && statusElement.innerText.trim() === "Em Andamento") {
            botao.style.display = "none";
        }
    });
});
