const menu = document.getElementById('sidebar-expansive');
const element_icon = document.getElementsByClassName('element-icon');
const sidebar_exp = document.getElementById('sidebar-expansive');
const img_expand = document.getElementById('img_sidebar-expansive');
const expand_button = document.getElementById('div-img_sidebar-expansive');
const icon_expand = document.getElementsByClassName('icon');
const sidebar = document.getElementById('sidebar');
const user_icon = document.getElementById('user_icon');//icone do menu de usuário0
const user_menu = document.getElementById('user_menu');
const gestor_name = document.getElementById('gestor_name');
const texto1 = document.getElementById('text-init');
const texto2 = document.getElementById('text-veicles');
const texto3 = document.getElementById('text-users');
const texto4 = document.getElementById('text-reservations');
const texto5 = document.getElementById('text-routes');
const texto6 = document.getElementById('text-maintenance');
const texto7 = document.getElementById('text-supply');
const menu_perfil = document.getElementById('sidebar-menu');
const teste = document.getElementById('content');

const page_title = document.getElementById('page_title');
const submenu_veiculos = document.getElementById('submenu-veiculos')
const submenu_usuarios = document.getElementById('submenu-usuarios')
const submenu_reservas = document.getElementById('submenu-reservas')
const submenu_rotas = document.getElementById('submenu-rotas')
const submenu_manutencao = document.getElementById('submenu-manutencao')
const submenu_abastecimento = document.getElementById('submenu-abastecimento')

const agendar_manutencao = document.getElementById('submenu-agendar-manutencao');
const editar_manutencao = document.getElementById('submenu-editar-manutencao');
const cadastrar_veiculo = document.getElementById('submenu-cadastro-veiculos');
const lista_veiculos = document.getElementById('submenu-lista-veiculos');
const cadastro_usuarios = document.getElementById('submenu-cadastro-usuarios');
const lista_usuarios = document.getElementById('submenu-lista-usuarios');
const criacao_reservas = document.getElementById('submenu-criacao-reservas');
const lista_reservas = document.getElementById('submenu-lista-reservas');
const criar_rotas = document.getElementById('submenu-criar-rotas');
const gerenciar_rotas = document.getElementById('submenu-gerenciar-rotas');
const lista_abastecimento = document.getElementById('submenu-lista-abastecimento');
const registro_abastecimento = document.getElementById('submenu-registro-abastecimento');


const container_veiculos = document.getElementById('id-veiculos');
const container_usuarios = document.getElementById('id-usuarios');
const container_reservas = document.getElementById('id-reservas');
const container_rotas = document.getElementById('id-rotas');
const container_manutencao = document.getElementById('id-manutencao');
const container_abastecimento = document.getElementById('id-abastecimento');

const icon_veiculos = document.getElementById('icon_veiculos');
const icon_usuarios = document.getElementById('icon_usuarios');
const icon_reservas = document.getElementById('icon_reservas');
const icon_rotas = document.getElementById('icon_rotas');
const icon_manutencao = document.getElementById('icon_manutencao');
const icon_abastecimento = document.getElementById('icon_abastecimento');


user_menu.addEventListener('click', () => {
    //console.log(user_menu_is_open())
    //console.log('123',sidebar_is_open())
    if (!user_menu_is_open() && sidebar_is_open()) {
        user_icon.style.transform = 'rotate(180deg)';
        menu_perfil.style.display = 'flex';
        menu_perfil.style.top = '60px';
        menu_perfil.style.left = '55px';
    } else if (!user_menu_is_open() && !sidebar_is_open()) {
        user_icon.style.transform = 'rotate(180deg)';
        menu_perfil.style.display = 'flex';
        menu_perfil.style.top = '10px';
        menu_perfil.style.left = '45px';
    } else if (user_menu_is_open()){
        close_user_menu();
    }
});

expand_button.addEventListener('click', () =>{//lógica para a barra lateral
    if (sidebar_is_open()){
        alter_element_icon()
        alter_text_sidebar()
        menu_perfil.style.display = 'none';
        menu.style.width = '44px';
        sidebar.style.width = '44px';
        user_menu.style.width = '30px';
        user_menu.style.height = '30px';
        user_menu.style.justifyContent = 'center';
        img_expand.style.rotate = '180deg';
        user_icon.style.display = 'none';
        teste.style.gridTemplateColumns = '44px 1fr';
    }
    
    else if (!sidebar_is_open()){
        alter_element_icon()
        alter_text_sidebar()
        menu_perfil.style.display = 'none';
        menu.style.transition = '800ms';
        sidebar.style.transition = '800ms';
        img_expand.style.rotate = '0deg';
        menu.style.width = '260px';
        sidebar.style.width = '260px';
        user_menu.style.width = '120px';
        user_menu.style.height = '40px';
        user_icon.style.display = 'block';
        user_menu.style.justifyContent = 'space-evenly';
        teste.style.gridTemplateColumns = '260px 1fr';
    }
})

function sidebar_is_open() {
    console.log(sidebar.style.width)
    return sidebar.style.width == '260px' || sidebar.style.width == '';
}

function user_menu_is_open() {
    const style = window.getComputedStyle(menu_perfil);
    //console.log(style.display)
    return style.display === 'flex';  // Verifica se o display é 'flex'
}

function open_user_menu (){

}

function close_user_menu (){
    user_icon.style.transform = 'rotate(0deg)';
    menu_perfil.style.display = 'none';
}

function alter_element_icon(){//altera o tamanho do container, margens e largura
    if (sidebar_is_open()){

        for (let i = 0; i < element_icon.length; i++){
            let element = element_icon[i];
            let icon = icon_expand[i];
            icon.style.marginLeft = '14px'
            element.style.marginLeft = '0';
            element.style.width = '45px';//reduzir tamanho do elemento
        }
    }
    else{

        for (let i = 0; i < element_icon.length; i++){
            let element = element_icon[i];
            let icon = icon_expand[i];
            icon.style.marginLeft = '10px'
            element.style.marginLeft = '15px';
            element.style.width = '230px';//almentar tamanho do elemento
        }
    }
}

function alter_text_sidebar(){
    if (sidebar_is_open()){
        gestor_name.style.display = 'none';
        texto1.style.display = 'none';
        texto2.style.display = 'none';
        texto3.style.display = 'none';
        texto4.style.display = 'none';
        texto5.style.display = 'none';
        texto6.style.display = 'none';
        texto7.style.display = 'none';

        icon_veiculos.style.display = 'none';
        icon_usuarios.style.display = 'none';
        icon_reservas.style.display = 'none';
        icon_rotas.style.display = 'none';
        icon_manutencao.style.display = 'none';
        icon_abastecimento.style.display = 'none';

        submenu_abastecimento.style.display = 'none';
        submenu_manutencao.style.display = 'none';
        submenu_reservas.style.display = 'none';
        submenu_rotas.style.display = 'none';
        submenu_usuarios.style.display = 'none';
        submenu_veiculos.style.display = 'none';
    }else{
        gestor_name.style.display = 'block';
        texto1.style.display = 'block';
        texto2.style.display = 'block';
        texto3.style.display = 'block';
        texto4.style.display = 'block';
        texto5.style.display = 'block';
        texto6.style.display = 'block';
        texto7.style.display = 'block';

        icon_veiculos.style.display = 'block';
        icon_usuarios.style.display = 'block';
        icon_reservas.style.display = 'block';
        icon_rotas.style.display = 'block';
        icon_manutencao.style.display = 'block';
        icon_abastecimento.style.display = 'block';
    }
}


if (page_title.innerText == "Registro de Abastecimento" || page_title.innerText == "Lista de Abastecimento" || page_title.innerText == "Registro de Abastecimento"){
    submenu_abastecimento.style.display = 'block';
}
else if (page_title.innerText == "Visualização da Rota" || page_title.innerText == "Lista de Rotas" || page_title.innerText == "Criação da Rota"){
    submenu_rotas.style.display = 'block';
}



document.addEventListener("DOMContentLoaded", function () {//Lógica de Identificação de Página e ações do submenu
    const pageName = document.body.getAttribute("data-page");
    console.log(pageName)
    switch(pageName){
        case "agendar_manutencao":
            submenu_manutencao.style.display = 'block';
            agendar_manutencao.style.color = 'rgba(21, 52, 72, 0.4)';
            container_manutencao.style.backgroundColor = "rgba(255,255,255,0.3)";
            verificar_est(icon_manutencao)
            break;
        case "editar_manutencao":
            submenu_manutencao.style.display = 'block';
            editar_manutencao.style.color = 'rgba(21, 52, 72, 0.4)';
            container_manutencao.style.backgroundColor = "rgba(255,255,255,0.3)";
            verificar_est(icon_manutencao)
            break;            
        
        case "cadastrar_veiculo":
            submenu_veiculos.style.display = 'block';
            cadastrar_veiculo.style.color = 'rgba(21, 52, 72, 0.4)';
            container_veiculos.style.backgroundColor = "rgba(255,255,255,0.3)";
            verificar_est(icon_veiculos)
            break;

        case "cadastrar_usuario":
            submenu_usuarios.style.display = 'block';
            cadastro_usuarios.style.color = 'rgba(21, 52, 72, 0.4)';
            container_usuarios.style.backgroundColor = "rgba(255,255,255,0.3)";
            verificar_est(icon_usuarios)
            break;

        case "criar_reserva":
            submenu_reservas.style.display = 'block';
            criacao_reservas.style.color = 'rgba(21, 52, 72, 0.4)';
            container_reservas.style.backgroundColor = "rgba(255,255,255,0.3)";
            verificar_est(icon_reservas)
            break;
    }
});


function verificar_est (elemento){
if (elemento.style.transform == 'rotate(0deg)'){
    elemento.style.transform = 'rotate(180deg)'
}}