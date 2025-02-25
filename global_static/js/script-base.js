const menu = document.getElementById('sidebar-expansive');
const element_icon = document.getElementsByClassName('element-icon');
const sidebar_exp = document.getElementById('sidebar-expansive');
const img_expand = document.getElementById('img_sidebar-expansive');
const expand_button = document.getElementById('div-img_sidebar-expansive');
const icon_expand = document.getElementsByClassName('icon');
const sidebar = document.getElementById('sidebar');
const user_icon = document.getElementById('user_icon');//icone do menu de usuário
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
const lista_manutencao = document.getElementById('submenu-lista-manutencao');
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
const container_base = document.getElementById('container-base');

//const alturaTela = window.innerHeight; // Caso precise da altura em algum lugar



//Lógica para manter aberto ou fechar o submenu
const pageName = document.body.getAttribute("data-page");
let page_name_list = ["cadastrar_veiculo", "Listagem_Veiculos", "informacoes_veiculo", 
    "cadastrar_usuario", "Listagem_Usuários", "informacoes_usuario",
    "criar_reserva", "listagem_reservas", "editar_reserva",
    "criacao_rota", "Listagem_Rotas", "visualizacao_rota",
    "agendar_manutencao", "Listagem_Manutencao", "editar_manutencao",
    "registro_abastecimento", "Listagem_Abastecimentos", "informacoes_abastecimento"
   ]
document.addEventListener("DOMContentLoaded", function () {//Lógica de Identificação de Página e ações do submenu
    for (let i = 0; i < page_name_list.length; i++){
        if (pageName == page_name_list[0] || pageName == page_name_list[1] || pageName == page_name_list[2]){
            //submenu_veiculos.style.display = 'block';


            if (container_veiculos){
                container_veiculos.style.backgroundColor = "rgba(255,255,255,0.3)";
                if (pageName == page_name_list[0]){cadastrar_veiculo.style.color = 'rgba(21, 52, 72, 0.4)';}
                else if (pageName == page_name_list[1]){lista_veiculos.style.color = 'rgba(21, 52, 72, 0.4)';}
            }

        }

        if (pageName == page_name_list[3] || pageName == page_name_list[4] || pageName == page_name_list[5]){
            //submenu_usuarios.style.display = 'block';
            container_usuarios.style.backgroundColor = "rgba(255,255,255,0.3)";
            if (pageName == page_name_list[3]){cadastro_usuarios.style.color = 'rgba(21, 52, 72, 0.4)';}
            else if (pageName == page_name_list[4]){lista_usuarios.style.color = 'rgba(21, 52, 72, 0.4)';}
        }

        if (pageName == page_name_list[6] || pageName == page_name_list[7] || pageName == page_name_list[8]){
            //submenu_reservas.style.display = 'block';
            container_reservas.style.backgroundColor = "rgba(255,255,255,0.3)";
            if (pageName == page_name_list[6]){criacao_reservas.style.color = 'rgba(21, 52, 72, 0.4)';}
            else if (pageName == page_name_list[7]){lista_reservas.style.color = 'rgba(21, 52, 72, 0.4)';}
        }

        if (pageName == page_name_list[9] || pageName == page_name_list[10] || pageName == page_name_list[11]){
            //submenu_rotas.style.display = 'block';
            container_rotas.style.backgroundColor = "rgba(255,255,255,0.3)";
            if (pageName == page_name_list[9]){criar_rotas.style.color = 'rgba(21, 52, 72, 0.4)';}
            else if (pageName == page_name_list[10]){gerenciar_rotas.style.color = 'rgba(21, 52, 72, 0.4)';}
        }

        if (pageName == page_name_list[12] || pageName == page_name_list[13] || pageName == page_name_list[14]){
            //submenu_manutencao.style.display = 'block';
            container_manutencao.style.backgroundColor = "rgba(255,255,255,0.3)";
            if (pageName == page_name_list[12]){agendar_manutencao.style.color = 'rgba(21, 52, 72, 0.4)';}
            else if (pageName == page_name_list[13]){lista_manutencao.style.color = 'rgba(21, 52, 72, 0.4)';}
        }
        if (pageName == page_name_list[15] || pageName == page_name_list[16] || pageName == page_name_list[17]){
            //submenu_abastecimento.style.display = 'block';
            container_abastecimento.style.backgroundColor = "rgba(255,255,255,0.3)";
            if (pageName == page_name_list[15]){registro_abastecimento.style.color = 'rgba(21, 52, 72, 0.4)';}
            else if (pageName == page_name_list[16]){lista_abastecimento.style.color = 'rgba(21, 52, 72, 0.4)';}
        }
        }
});


user_menu.addEventListener('click', () => {
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





function sidebar_is_open() {
    return sidebar.style.width == '260px' || sidebar.style.width == '';
}

function user_menu_is_open() {
    const style = window.getComputedStyle(menu_perfil);
    return style.display === 'flex';  // Verifica se o display é 'flex'
}
function close_user_menu (){
    user_icon.style.transform = 'rotate(0deg)';
    menu_perfil.style.display = 'none';
}


function submenu_is_open(){ //retorna true se algum submenu estiver aberto
    try{
        return submenu_veiculos.style.display == 'block' || submenu_usuarios.style.display == 'block' || submenu_reservas.style.display == 'block' || submenu_rotas.style.display == 'block' || submenu_manutencao.style.display == 'block' || submenu_abastecimento.style.display == 'block';
    }catch (e){
        return submenu_usuarios.style.display == 'block' || submenu_reservas.style.display == 'block' || submenu_rotas.style.display == 'block';
    }
    
}


document.addEventListener("DOMContentLoaded", function () {
    // Define os elementos corretamente antes de usá-los
    const adminMenu = [
        { container: container_veiculos, submenu: submenu_veiculos, icon: icon_veiculos },
        { container: container_usuarios, submenu: submenu_usuarios, icon: icon_usuarios },
        { container: container_reservas, submenu: submenu_reservas, icon: icon_reservas },
        { container: container_rotas, submenu: submenu_rotas, icon: icon_rotas },
        { container: container_manutencao, submenu: submenu_manutencao, icon: icon_manutencao },
        { container: container_abastecimento, submenu: submenu_abastecimento, icon: icon_abastecimento }
    ];

    const clientMenu = [
        { container: container_usuarios, submenu: submenu_usuarios, icon: icon_usuarios },
        { container: container_reservas, submenu: submenu_reservas, icon: icon_reservas },
        { container: container_rotas, submenu: submenu_rotas, icon: icon_rotas }
    ];

    // Determina qual menu usar (Admin ou Cliente)
    let menuList = container_abastecimento ? adminMenu : clientMenu;

    menuList.forEach(item => {
        if (item.container && item.submenu && item.icon) {
            item.container.addEventListener("click", () => {
                if (sidebar_is_open()) {
                    item.submenu.style.display = item.submenu.style.display === "none" ? "block" : "none";
                    verificar_estado_icone(item.icon);
                } else {
                    expandir_sidebar();
                }
            });
        } else {
            console.warn("Elemento não encontrado no DOM:", item);
        }
    });

    function verificar_estado_icone(elemento) {
        elemento.style.transform = (elemento.style.transform === "rotate(0deg)") ? "rotate(180deg)" : "rotate(0deg)";
    }

    function alter_element_icon() {
        let width = sidebar_is_open() ? "45px" : "230px";
        let marginLeft = sidebar_is_open() ? "0" : "15px";
        let iconMargin = sidebar_is_open() ? "14px" : "10px";

        for (let i = 0; i < element_icon.length; i++) {
            element_icon[i].style.width = width;
            element_icon[i].style.marginLeft = marginLeft;
            icon_expand[i].style.marginLeft = iconMargin;
        }
    }

    function alter_text_sidebar() {
        let text_list = [
            gestor_name, texto1, texto2, texto3, texto4, texto5, texto6, texto7,
            icon_veiculos, icon_usuarios, icon_reservas, icon_rotas, icon_manutencao, icon_abastecimento
        ];
    
        let text_list_submenu = [...text_list];
    
        text_list_submenu.forEach(el => {
            if (el) { // Verifica se o elemento não é null antes de acessar .style
                el.style.display = sidebar_is_open() ? "none" : "block";
            } else {
                console.warn("Elemento não encontrado no DOM:", el);
            }
        });
    }

    function encolher_sidebar(){
        adminMenu.forEach(item => {
            if (item && item.submenu) {  // Verifica se o item e o submenu são válidos
                item.submenu.style.display = 'none';  // Acessa o submenu e o oculta
            } else {
                console.warn('Submenu não encontrado:', item);  // Mensagem de aviso para depuração
            }
        });
                
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
        container_base.style.gridTemplateColumns = '44px 1fr';
        //teste.style.gridTemplateColumns = '44px 1fr';
    }
    
    function expandir_sidebar(){
        alter_element_icon()
        alter_text_sidebar()
        menu_perfil.style.display = 'none';
        menu.style.transition = '800ms';
        sidebar.style.transition = '800ms';
        img_expand.style.rotate = '0deg';
        menu.style.width = '260px';
        sidebar.style.width = '260px';
        container_base.style.gridTemplateColumns = '260px 1fr';
        user_menu.style.width = '120px';
        user_menu.style.height = '40px';
        user_icon.style.display = 'block';
        user_menu.style.justifyContent = 'space-evenly';
        //teste.style.gridTemplateColumns = '260px 1fr';
    }
    expand_button.addEventListener('click', () =>{//lógica para a barra lateral
        if (sidebar_is_open()){
            encolher_sidebar()
        }
        else if (!sidebar_is_open()){
            expandir_sidebar()
        }
    })

        // Inicialmente verificar a largura da tela ao carregar a página
        verificarTamanhoTela();
    
        // Adicionar evento de redimensionamento
        window.addEventListener('resize', verificarTamanhoTela);

    
    function verificarTamanhoTela() {
        const larguraTela = window.innerWidth;
        console.log(larguraTela)
        if (larguraTela < 1250 && sidebar_is_open() && !submenu_is_open()) {
            encolher_sidebar();
        } else if (larguraTela > 1250 && !sidebar_is_open()) {
            expandir_sidebar();
        }
    }
});
