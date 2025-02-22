function calcularValor() {
    const veiculoSelect = document.getElementById('veiculo');
    const dataReserva = document.getElementById('data_reserva').value;
    const dataEntrega = document.getElementById('data_entrega').value;
    const idadeCondutor = document.getElementById('idade_condutor').value;
    const valorInput = document.getElementById('valor');

    if (!veiculoSelect.value || !dataReserva || !dataEntrega || !idadeCondutor) {
        valorInput.value = '';
        return;
    }

    const valorTotalVeiculo = parseFloat(veiculoSelect.options[veiculoSelect.selectedIndex].getAttribute('data-valor')) || 0;
    const reservaDate = new Date(dataReserva);
    const entregaDate = new Date(dataEntrega);

    const dias = Math.max(1, Math.ceil((entregaDate - reservaDate) / (1000 * 60 * 60 * 24))); 

   
    const porcentagemDiaria = 0.003;  
    const diaria = valorTotalVeiculo * porcentagemDiaria; 

    let valorTotal = dias * diaria; 


    if (parseInt(idadeCondutor) < 25) {
        valorTotal *= 1.1; 
    }

    valorInput.value = valorTotal.toFixed(2); 
}