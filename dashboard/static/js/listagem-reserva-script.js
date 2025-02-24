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

            fetch(`/dashboard/confirmar-entrega/${reservaId}/`, {  // ← Adicione "dashboard/"
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
    document.querySelectorAll(".conteudo-esquerdo").forEach(reserva => {
        const statusElement = reserva.querySelector("#status-reserva");
        const botao = reserva.querySelector(".botao-visualizar-2");

        if (statusElement && botao) {
            const status = statusElement.innerText.trim().toLowerCase(); // Normaliza o texto
            
            console.log("Status encontrado:", status); // Debug para verificar no console

            if (status !== "pendente") {
                botao.style.display = "none"; // Esconde o botão se o status NÃO for "Pendente"
            } else {
                botao.style.display = "block"; // Garante que fique visível se for "Pendente"
            }
        }
    });
});


