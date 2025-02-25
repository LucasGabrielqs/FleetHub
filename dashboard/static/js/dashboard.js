document.addEventListener("DOMContentLoaded", function() {
    const hoje = new Date().toISOString().split("T")[0]; // Data de hoje no formato "YYYY-MM-DD"

    const reservas = document.querySelectorAll(".carro-reservado");
    const btnHoje = document.getElementById("button-hoje");
    const btnProximosDias = document.getElementById("button-proximosdias");
    const mensagemVazia = document.getElementById("mensagem-vazia");

    function filtrarReservas(filtro) {
        let reservasVisiveis = 0; // Contador de reservas visíveis

        reservas.forEach(reserva => {
            const dataReserva = reserva.getAttribute("data-data_reserva");
            if (filtro === "hoje") {
                if (dataReserva === hoje) {
                    reserva.style.display = "block";
                    reservasVisiveis++;
                } else {
                    reserva.style.display = "none";
                }
            } else if (filtro === "proximos") {
                if (dataReserva > hoje) {
                    reserva.style.display = "block";
                    reservasVisiveis++;
                } else {
                    reserva.style.display = "none";
                }
            }
        });

        // Exibir ou ocultar a mensagem caso não haja reservas visíveis
        mensagemVazia.style.display = reservasVisiveis === 0 ? "block" : "none";
        mensagemVazia.innerText = filtro === "hoje" 
            ? "Nenhuma reserva programada para hoje" 
            : "Nenhuma reserva programada para os próximos dias";
    }

    // Eventos dos botões
    btnHoje.addEventListener("click", function() {
        filtrarReservas("hoje");
    });

    btnProximosDias.addEventListener("click", function() {
        filtrarReservas("proximos");
    });

    // Mostrar apenas reservas de hoje ao carregar a página
    filtrarReservas("hoje");
});
