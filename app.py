import textwrap
import re
import os
import json
import streamlit as st

st.set_page_config(page_title="Sistema Darcy Ribeiro", layout="centered")

st.markdown("# Seja bem-vindo ao Sistema Integrado Darcy Ribeiro!")
st.markdown("### 🔬 Conheça Departamentos, Institutos e Faculdades da Universidade de Brasília.")

# --- MENU LATERAL ---
menu = st.sidebar.radio("Menu", ["🔍 Buscar por Instituto", "🔐 Fazer Login", "👨‍🎓 Ver Perfis"])

def exibir_historia_if():
    texto = textwrap.dedent("""
    <p>O Instituto de Física (IF) foi um dos primeiros institutos da Universidade de Brasília. Seu desenvolvimento contou com a participação de físicos como José Leite Lopes, Roberto Salmeron e Jayme Tiomno, além do apoio do Centro Brasileiros de Pesquisas Físicas (CBPF), que em diversas reuniões com Darcy Ribeiro e Anísio Teixeira, fundadores da UnB, definiram as diretrizes do curso.</p>

    <p>Após o golpe militar de 1964, que causou a demissão em massa de praticamente todo o corpo docente da UnB, coube a José Acioli, Luiz Carlos Gomes e José Carlos Azevedo a difícil missão de reerguer o IF.</p>

    <p>Em um estudo recente realizado pela Universidade de Stanford, foi feito um levantamento de pesquisadores de todas as áreas e a UnB teve 25 professores, sendo 2 do Instituto de Física, entre os melhores do mundo.</p>
    """)
    st.markdown(f"<div style='text-align: justify'>{texto}</div>", unsafe_allow_html=True)
	
def exibir_biografias():
    biografias = textwrap.dedent("""
    <p>Darcy Ribeiro - Além de ter sido um dos principais fundadores da Universidade de Brasília, Darcy Ribeiro liderou o projeto da construção de quase 500 colégios públicos de ensino integral em todo o estado do Rio de Janeiro, os chamados CIEPs, entre 1983 e 1987, período no qual foi vice-governador. Nesta mesma época, criou o Sambódromo, que não só servia como espaço para o desfile das escolas de samba durante o Carnaval, mas também onde funcionavam mais de 200 salas de aula construídas embaixo das arquibancadas. Logo após a conclusão do curso de Antropologia, passou 10 anos convivendo com povos indígenas, estudando especialmente os povos Kadiwéu, Urubu Ka’apor, Ofayé, Bororo e Guarani. Criou também o Parque Indígena do Xingu, o Museu do Índio e o Memorial da América Latina. Foi preso e exilado durante a ditadura militar, tendo vivido por 12 anos entre o Uruguai, Venezuela, Chile, Peru e México. Nascido em 26 de Outubro de 1922 em Montes Claros, Minas Gerais, Darcy foi antropólogo, educador, escritor e político.</p>

    <p>Anísio Teixeira - Considerado o fundador da primeira escola pública de ensino integral do Brasil, a Escola Parque inaugurada na Bahia em 1950, Anísio Teixeira foi um dos idealizadores da Escola Nova, movimento educacional de grande projeção no século XX, que propunha que a ''educação deve ser essencialmente pública, obrigatória, gratuita, leiga e sem qualquer segregação de cor, sexo ou tipo de estudo, e desenvolver-se em estreita vinculação com as comunidades.'' Ao lado de Darcy Ribeiro, contribuiu não só no projeto da Universidade de Brasília, mas também na elaboração da Lei de Diretrizes e Bases da Educação. Anísio Teixeira nasceu em Caetité, na Bahia, em 12 de Julho de 1900.</p>

    <p>José Leite Lopes - Foi o primeiro físico a predizer a existência do bóson Z, partícula mediadora de uma das quatro forças fundamentais da natureza, a força fraca. Ao lado de César Lattes, ajudou a construir o CBPF, um dos principais centros de pesquisa em física do país e que abrigou físicos como Jayme Tiomno, Mário Schenberg, Richard Feynman e David Bohm. Nasceu em Recife, Pernambuco, em 28 de Outubro de 1918.</p>

    <p>Roberto Salmeron - Em colaboração com o CERN, esteve na primeira detecção dos neutrinos do elétron e do múon, partículas fundamentais do Modelo Padrão. Teve uma importante participação nos anos iniciais da UnB como diretor do Instituto Central de Ciências (ICC), do qual faziam parte os institutos de Física, Química e Biologia e o departamento de Matemática. Salmeron nasceu em 16 de Julho de 1922, em São Paulo.</p>
    """)
    st.markdown(f"<div style='text-align: justify'>{biografias}</div>", unsafe_allow_html=True)

def exibir_nucleos():
    nucleos = {
        "nucleo_1": "1. Física Atômica e Molecular",
        "nucleo_2": "2. Relatividade Geral, Gravitação e Cosmologia",
        "nucleo_3": "3. Matéria Condensada Experimental",
        "nucleo_4": "4. Matéria Condensada Teórica",
        "nucleo_5": "5. Física Matemática e Computacional",
        "nucleo_6": "6. Teoria Quântica de Campos",
        "nucleo_7": "7. Óptica Quântica",
        "nucleo_8": "8. Física de Plasma",
        "nucleo_9": "9. Física Estatística e Computacional",
        "nucleo_10": "10. Física Geral e Fundamentos da Física",
        "nucleo_11": "11. Ensino de Física"
    }

    opcoes = list(nucleos.values())
    escolha = st.selectbox("Escolha um núcleo:", opcoes, key="selectbox_nucleos")

    for chave, valor in nucleos.items():
        if valor == escolha:
            return chave

def exibir_professores_otica():
	profs = ["1. Alexandre Dodonov", "2. Caio Ribeiro"]
	escolha = st.selectbox("Escolha um professor:", profs)
	return escolha.lower()
	
def info_caio_ribeiro():
    st.markdown("### 📚 Informações sobre Caio Ribeiro")
    st.markdown("- **Contato:** caio.ribeiro@unb.br")
    st.markdown("- **Lattes:** http://lattes.cnpq.br/6459107436866263")
    st.markdown("- **Google Scholar:** https://scholar.google.com/citations?user=mR3sBh0AAAAJ&hl=pt-BR&oi=ao")

    st.markdown("#### Artigos Recentes")
    st.markdown("- *Electric current quantum superpositions in superconducting circuits* (Physics Letters A, 2025) (https://www.sciencedirect.com/science/article/abs/pii/S0375960125003792)")
    st.markdown("- *Probing cosmic expansion through small anisotropies in a Bose-Einstein condensate analogue* (arXiv, 2025) (https://arxiv.org/abs/2504.21236)")
    st.markdown("- *Energy conservation and quantum backreaction in Bose-Einstein condensates* (Physical Review A, 2025) (https://journals.aps.org/pra/abstract/10.1103/PhysRevA.111.023306)")

    st.markdown("#### Linhas de Pesquisa")
    st.markdown("- **Vácuo quântico em condensados de Bose-Einstein**")
    descricao1 = textwrap.dedent("""
    Descrição: Neste projeto buscamos estudar manifestações do vácuo quântico em condensados de Bose-Einstein, sistemas que ocupam posição estratégica na ciência e no ensino de ciência por suas propriedades peculiares e seu caráter multidisciplinar.

    De forma específica, estamos interessados em estudar o backreaction quântico em sistemas análogos e nas modificações oriundas de interações de longo alcance, como, por exemplo, ocorre quando os bósons possuem momento de dipolo elétrico ou magnético.
    """)
    st.markdown(f"<div style='text-align: justify'>{descricao1}</div>", unsafe_allow_html=True)

    st.markdown("- **Flutuações do vácuo em sistemas do tipo Casimir**")  
    descricao2 = textwrap.dedent("""
    Descrição: Em distinção à concepção clássica de vácuo, a modificação do estado de vácuo de algum campo quântico produz efeitos observáveis, como por exemplo o celebrado efeito Casimir.

    Neste projeto propomos estudar o efeito Browniano quântico em sistemas do tipo Casimir, no qual partículas que interagem com o campo adquirem dispersão em suas velocidades devido a transições entre estados de vácuo.
    """)
    st.markdown(f"<div style='text-align: justify'>{descricao2}</div>", unsafe_allow_html=True)

    st.markdown("#### Grupo de Pesquisa")
    doutorado = ["Miguel Citeli", "Giulia Aleixo"]
    mestrado = ["Patrick Oliveira", "Carine Zary"]
    graduacao = [
        "Roger Rezende Pinheiro Marzagao",
        "Vitória Alves de Souza",
        "Hugo Diniz de Souza"
    ]

    # Tenta carregar os perfis
    try:
        with open("perfis_caio.json", "r") as f:
            alunos = json.load(f)
    except Exception as e:
        st.error(f"Erro ao carregar perfis: {e}")
        alunos = []

    def exibir_por_nivel(titulo, nomes):
        st.markdown(f"##### {titulo}")
        for aluno in alunos:
            if aluno["nome"] in nomes:
                col1, col2 = st.columns([1, 5])
                with col1:
                    try:
                        st.image(aluno["foto"], width=80)
                    except:
                        st.warning("Foto não disponível.")

                with col2:
                    st.markdown(f"**{aluno['nome']}**")
                    st.markdown(f"*Tema:* {aluno['tema']}")

    exibir_por_nivel("Doutorado", doutorado)
    exibir_por_nivel("Mestrado", mestrado)
    exibir_por_nivel("Graduação", graduacao)
	
def criar_perfil(nome_usuario):
    st.subheader("Criação de Perfil")

    nivel = st.selectbox("Nível", ["Graduação", "Mestrado", "Doutorado"])
    tema = st.text_input("Tema da Pesquisa")
    #instituicao = st.text_input("Instituição (opcional)")
    #ano = st.text_input("Ano de Ingresso (opcional)")

    if st.button("Criar Perfil", key="botao_criar"):
        perfil = {
            "nome": nome_usuario,
            "tema": tema
        }

        if not os.path.exists("perfis_caio.json"):
            with open("perfis_caio.json", "w") as f:
                json.dump([], f)

        with open("perfis_caio.json", "r") as f:
            try:
                perfis = json.load(f)
            except json.JSONDecodeError:
                perfis = []

        if any(p["nome"] == nome_usuario for p in perfis):
            st.warning("Já existe um perfil com este nome.")
        else:
            perfis.append(perfil)

            with open("perfis_caio.json", "w") as f:
                json.dump(perfis, f, indent=2, ensure_ascii=False)

            st.success("Perfil criado com sucesso!")

def login(matricula, senha):
    if not os.path.exists("usuarios.json"):
        return None

    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)

    for usuario in usuarios:
        if usuario["matricula"] == matricula and usuario["senha"] == senha:
            return usuario["nome"]
    return None

def carregar_perfis(arquivo="perfis_caio.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            try:
                perfis = json.load(f)
            except json.JSONDecodeError:
                st.warning("Erro ao carregar os perfis.")
                return

        if perfis:
            for p in perfis:
                st.markdown("---")
                st.markdown(f"**👤 Nome:** {p.get('nome', 'N/A')}")
                st.markdown(f"- **Tema da Pesquisa:** {p.get('tema', 'N/A')}")
                for chave, valor in p.items():
                    if chave not in ["nome", "tema"]:
                        st.markdown(f"- **{chave}:** {valor}")
        else:
            st.info("Nenhum perfil cadastrado ainda.")
    else:
        st.info("Nenhum perfil cadastrado ainda.")

# --- OPÇÃO 1: BUSCAR POR INSTITUTO ---
if menu == "🔍 Buscar por Instituto":
    if "busca_realizada" not in st.session_state:
        st.session_state.busca_realizada = False
    
    consulta = st.text_input("Digite algo como 'física', 'if', 'química'...").strip().lower()
    palavras_chave = ["if", "física", "fisica", "instituto de física"]
    
    if st.button("Buscar"):
        st.session_state.busca_realizada = any(p in consulta for p in palavras_chave)
    
    if st.session_state.busca_realizada:
        st.markdown("### Site Oficial do IF")
        st.markdown("https://if.unb.br/")
        st.markdown("### História do Instituto de Física")
        exibir_historia_if()
        st.markdown("### Biografias Selecionadas")
        exibir_biografias()
        st.markdown("### Áreas de Pesquisa")

        if "nucleo_escolhido" not in st.session_state:
            st.session_state.nucleo_escolhido = ""

        st.session_state.nucleo_escolhido = exibir_nucleos()

        if st.session_state.nucleo_escolhido and st.session_state.nucleo_escolhido != "nucleo_7":
            st.info("Ainda não existem professores cadastrados para este núcleo.")

        if st.session_state.nucleo_escolhido == "nucleo_7":
            st.markdown("### Professores do núcleo de Óptica Quântica")

            if "professor_escolhido" not in st.session_state:
                st.session_state.professor_escolhido = ""

            st.session_state.professor_escolhido = exibir_professores_otica()

            if "caio" in st.session_state.professor_escolhido:
                info_caio_ribeiro()

            elif "alexandre" in st.session_state.professor_escolhido:
                st.info("Informações de Alexandre Dodonov ainda não disponíveis.")

            else:
                st.warning("Professor não encontrado.")

# --- OPÇÃO 2: LOGIN E CRIAÇÃO DE PERFIL ---
elif menu == "🔐 Fazer Login":
    st.subheader("Login para criação de perfil no grupo de pesquisa")

    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if st.session_state.usuario_logado is None:

        aba = st.radio("Escolha uma opção:", ["🔐 Entrar", "📋 Fazer Cadastro"], horizontal=True)

        if aba == "🔐 Entrar":
            matricula = st.text_input("Matrícula")
            senha = st.text_input("Senha", type="password")

            if st.button("Entrar"):
                nome = login(matricula, senha)
                if nome:
                    st.session_state.usuario_logado = nome
                    st.success(f"Bem-vindo(a), {nome}!")
                    st.experimental_rerun()
                else:
                    st.error("Matrícula ou senha incorretas.")

        elif aba == "📋 Fazer Cadastro":
            nome = st.text_input("Nome Completo")
            nova_matricula = st.text_input("Matrícula")
            nova_senha = st.text_input("Senha", type="password")
            confirmar_senha = st.text_input("Confirmar Senha", type="password")

            if st.button("Cadastrar"):
                if not nome or not nova_matricula or not nova_senha or not confirmar_senha:
                    st.warning("Preencha todos os campos para cadastrar.")
                elif nova_senha != confirmar_senha:
                    st.error("As senhas não coincidem. Tente novamente.")
                else:
                    novo_usuario = {
                        "nome": nome,
                        "matricula": nova_matricula,
                        "senha": nova_senha
                    }

                    caminho_usuarios = "usuarios.json"
                    if os.path.exists(caminho_usuarios):
                        with open(caminho_usuarios, "r") as f:
                            try:
                                usuarios = json.load(f)
                            except json.JSONDecodeError:
                                usuarios = []
                    else:
                        usuarios = []

                    if any(u["matricula"] == nova_matricula for u in usuarios):
                        st.warning("Já existe um usuário com essa matrícula.")
                    else:
                        usuarios.append(novo_usuario)

                        try:
                            with open(caminho_usuarios, "w") as f:
                                json.dump(usuarios, f, indent=2, ensure_ascii=False)
                            st.success("Cadastro realizado com sucesso! Agora faça login.")
                            st.write("✅ Usuário salvo no arquivo!")
                        except Exception as e:
                            st.error(f"Erro ao salvar: {e}")

# --- OPÇÃO 3: VER TODOS OS PERFIS CADASTRADOS ---
elif menu == "👨‍🎓 Ver Perfis":
    st.subheader("Perfis do Grupo de Pesquisa do Prof. Caio Ribeiro")
    carregar_perfis()
