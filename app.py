import textwrap
import re
import os
import json
import streamlit as st

st.set_page_config(page_title="Sistema Darcy Ribeiro", layout="centered")

st.markdown("# Seja bem-vindo ao Sistema Integrado Darcy Ribeiro!")
st.markdown("### 🔬 Explore os institutos, crie perfis e conheça as linhas de pesquisa.")

# --- MENU LATERAL ---
menu = st.sidebar.radio("Menu", ["🔍 Buscar por Instituto", "🔐 Fazer Login", "👨‍🎓 Ver Perfis"])

def exibir_historia_if():
    texto = """
    <div style='text-align: justify'>
    O Instituto de Física (IF) foi um dos primeiros institutos da Universidade de Brasília. Seu desenvolvimento contou com a participação de físicos como José Leite Lopes, Roberto Salmeron e Jayme Tiomno, além do apoio do Centro Brasileiros de Pesquisas Físicas (CBPF), que em diversas reuniões com Darcy Ribeiro e Anísio Teixeira, fundadores da UnB, definiram as diretrizes do curso.

    Após o golpe militar de 1964, que causou a demissão em massa de praticamente todo o corpo docente da UnB, coube a José Acioli, Luiz Carlos Gomes e José Carlos Azevedo a difícil missão de reerguer o IF.

    Em um estudo recente realizado pela Universidade de Stanford, foi feito um levantamento de pesquisadores de todas as áreas e a UnB teve 25 professores, sendo 2 do Instituto de Física, entre os melhores do mundo.
    </div>
    """
    st.markdown(texto, unsafe_allow_html=True)

	
def exibir_biografias():
    biografias = [
            "Darcy Ribeiro - Além de ter sido um dos principais fundadores da Universidade de Brasília, Darcy Ribeiro"
            "\nliderou o projeto da construção de quase 500 colégios públicos de ensino integral em todo o estado do Rio de"
            "\nJaneiro, os chamados CIEPs, entre 1983 e 1987, período no qual foi vice-governador. Nesta mesma época,"
            "\ncriou o Sambódromo, que não só servia como espaço para o desfile das escolas de samba durante o Carnaval, mas "
            "\ntambém onde funcionavam mais de 200 salas de aula construídas embaixo das arquibancadas. Logo após a conclusão"
            "\ndo curso de Antropologia, passou 10 anos convivendo com povos indígenas, estudando especialmente os povos Kadiwéu,"
            "\nUrubu Ka’apor, Ofayé, Bororo e Guarani. Criou também o Parque Indígena do Xingu, o Museu do Índio e o Memorial da"
            "\nAmérica Latina. Foi preso e exilado durante a ditadura militar, tendo vivido por 12 anos entre o Uruguai, Venezuela,"
            "\nChile, Peru e México. Nascido em 26 de Outubro de 1922 em Montes Claros, Minas Gerais, Darcy foi antropólogo, educador,"
            "\nescritor e político.",
            "\nAnísio Teixeira - Considerado o fundador da primeira escola pública de ensino integral do Brasil, a Escola Parque inaugurada "
          "\nna Bahia em 1950, Anísio Teixeira foi um dos idealizadores da Escola Nova, movimento educacional de grande projeção no século XX, "
          "\nque propunha que a ``educação deve ser essencialmente pública, obrigatória, gratuita, leiga e sem qualquer segregação de cor, sexo "
          "\nou tipo de estudo, e desenvolver-se em estreita vinculação com as comunidades.'' Ao lado de Darcy Ribeiro, contribuiu não só no projeto "
          "\nda Universidade de Brasília, mas também na elaboração da Lei de Diretrizes e Bases da Educação. Anísio Teixeira nasceu em Caetité, na Bahia, "
          "\nem 12 de Julho de 1900. ",
            "\nJosé Leite Lopes - Foi o primeiro físico a predizer a existência do bóson $Z$, partícula mediadora de uma das quatro forças fundamentais da "
            "\nnatureza, a força fraca. Ao lado de César Lattes, ajudou a construir o CBPF, um dos principais centros de pesquisa em física do país "
            "\ne que abrigou físicos como Jayme Tiomno, Mário Schenberg, Richard Feynman e David Bohm. Nasceu em Recife, Pernambuco, em 28 de Outubro de 1918. ",
            "\nRoberto Salmeron - Em colaboração com o CERN, esteve na primeira detecção dos neutrinos do elétron e do múon, partículas fundamentais do Modelo "
            "\nPadrão. Teve uma importante participação nos anos iniciais da UnB como diretor do Instituto Central de Ciências (ICC), do qual faziam parte os institutos "
            "\nde Física, Química e Biologia e o departamento de Matemática. Salmeron nasceu em 16 de Julho de 1922, em São Paulo. "
        ]
		    
    return st.markdown(biografias)
	
def exibir_nucleos():
    nucleos = [
        "1. Física Atômica e Molecular",
        "2. Relatividade Geral, Gravitação e Cosmologia",
        "3. Matéria Condensada Experimental",
        "4. Matéria Condensada Teórica",
        "5. Física Matemática e Computacional",
        "6. Teoria Quântica de Campos",
        "7. Óptica Quântica",
        "8. Física de Plasma",
        "9. Física Estatística e Computacional",
        "10. Física Geral e Fundamentos da Física",
        "11. Ensino de Física"
    ]
	
    escolha = st.selectbox("Escolha um núcleo (nome ou número):", nucleos)
    return escolha.split(".")[1].strip().lower()
	
def exibir_professores_otica():
    profs = ["1. Alexandre Dodonov", "2. Caio Ribeiro"]
    escolha = st.selectbox("Professores deste núcleo:", profs)
    return escolha.split(".")[1].strip().lower()
	
def info_caio_ribeiro():
    st.markdown("### 📚 Informações sobre Caio Ribeiro")
    st.markdown("- **Contato:** caio.ribeiro@unb.br")
    st.markdown("- **Lattes:** [Link](http://lattes.cnpq.br/6459107436866263)")
    st.markdown("- **Google Scholar:** [Link](https://scholar.google.com/citations?user=mR3sBh0AAAAJ&hl=pt-BR&oi=ao)")

    st.markdown("#### Artigos Recentes")
    st.markdown("- *Electric current quantum superpositions in superconducting circuits* (Physics Letters A, 2025)")
    st.markdown("- *Probing cosmic expansion through small anisotropies in a Bose-Einstein condensate analogue* (arXiv, 2025)")
    st.markdown("- *Energy conservation and quantum backreaction in Bose-Einstein condensates* (Physical Review A, 2025)")

    st.markdown("#### Linhas de Pesquisa")
    st.markdown("- **Vácuo quântico em condensados de Bose-Einstein**")
    descricao1 = """
    Neste projeto buscamos estudar manifestações do vácuo quântico em condensados de Bose-Einstein, sistemas que ocupam posição estratégica na ciência e no ensino de ciência por suas propriedades peculiares e seu caráter multidisciplinar.

    De forma específica, estamos interessados em estudar o backreaction quântico em sistemas análogos e nas modificações oriundas de interações de longo alcance, como, por exemplo, ocorre quando os bósons possuem momento de dipolo elétrico ou magnético.

    Este projeto é executado no âmbito do grupo de pesquisa Óptica Quântica Teórica.
    """
    st.markdown(descricao1)

    st.markdown("- **Flutuações do vácuo em sistemas do tipo Casimir**")  
    descricao2 = """
    Em distinção à concepção clássica de vácuo, a modificação do estado de vácuo de algum campo quântico produz efeitos observáveis, como por exemplo o celebrado efeito Casimir.

    Neste projeto propomos estudar o efeito Browniano quântico em sistemas do tipo Casimir, no qual partículas que interagem com o campo adquirem dispersão em suas velocidades devido a transições entre estados de vácuo.
    """
    st.markdown(descricao2) 
    
    carregar_perfis()
	
def tratar_nucleo(escolha):
    if escolha in ["7", "ótica quântica", "optica", "ótica"]:
        prof = exibir_professores_otica()
        if prof in ["2", "caio ribeiro"]:
            info_caio_ribeiro()
            criar_perfil()
        elif prof in ["1", "alexandre dodonov"]:
            print("Informações de Alexandre Dodonov ainda não disponíveis.")
        else:
            print("Professor não encontrado.")
    else:
        print("Núcleo não encontrado.")

def login():
    print("\n🔐 Login necessário para criar perfil no grupo de pesquisa")
    matricula = input("Matrícula: ").strip()
    senha = input("Senha: ").strip()

    if not os.path.exists("usuarios.json"):
        print("⚠️ Nenhum usuário cadastrado ainda.")
        return None

    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)

    for usuario in usuarios:
        if usuario["matricula"] == matricula and usuario["senha"] == senha:
            print(f"\n✅ Login bem-sucedido! Bem-vindo(a), {usuario['nome']}.\n")
            return usuario["nome"]
    
    print("❌ Matrícula ou senha incorreta.")
    return None

def criar_perfil(nome_usuario):
    print("\nVamos criar seu perfil de pesquisa:")
    nivel = input("Nível (Graduação / Mestrado / Doutorado): ").strip()
    tema = input("Tema da Pesquisa: ").strip()

    adicionais = {}
    while True:
        campo = input("Deseja adicionar mais algum campo? (ex: Instituição, Ano de Ingresso) [Enter para pular]: ").strip()
        if campo == "":
            break
        valor = input(f"{campo}: ").strip()
        adicionais[campo] = valor

    perfil = {
        "nome": nome_usuario,
        "nível": nivel,
        "tema": tema,
        **adicionais
    }

    if not os.path.exists("perfis_caio.json"):
        with open("perfis_caio.json", "w") as f:
            json.dump([], f)

    with open("perfis_caio.json", "r") as f:
        perfis = json.load(f)

    perfis.append(perfil)

    with open("perfis_caio.json", "w") as f:
        json.dump(perfis, f, indent=2)

    print("✅ Perfil criado com sucesso!")

def carregar_perfis():
    if os.path.exists("perfis_caio.json"):
        with open("perfis_caio.json", "r") as f:
            perfis = json.load(f)
        for p in perfis:
            print(f"\n- Nome: {p['nome']}")
            print(f"  Nível: {p['nível']}")
            print(f"  Tema: {p['tema']}")
            for chave in p:
                if chave not in ['nome', 'nível', 'tema']:
                    print(f"  {chave}: {p[chave]}")
    else:
        print("Nenhum perfil cadastrado ainda.")

# --- OPÇÃO 1: BUSCAR POR INSTITUTO ---
if menu == "🔍 Buscar por Instituto":
    st.subheader("Busque por um instituto ou departamento da UnB")

    consulta = st.text_input("Digite algo como 'física', 'if', 'química'...").strip().lower()
    palavras_chave = ["if", "física", "fisica", "instituto de física"]

    if st.button("Buscar"):
        if any(palavra in consulta for palavra in palavras_chave):
            st.markdown("🔗 [Site Oficial do IF](https://if.unb.br/)")
            st.markdown("### História do Instituto de Física")
            exibir_historia_if()
            st.markdown("### Biografias Selecionadas")
            exibir_biografias()
            st.markdown("### Áreas de Pesquisa")
            st.text(exibir_nucleos())
        else:
            st.warning("Instituto ainda não disponível no sistema.")

# --- OPÇÃO 2: LOGIN E CRIAÇÃO DE PERFIL ---
elif menu == "🔐 Fazer Login":
    st.subheader("Login para criação de perfil no grupo de pesquisa")

    matricula = st.text_input("Matrícula")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        nome = login(matricula, senha)
        if nome:
            st.success(f"Bem-vindo(a), {nome}!")
            criar_perfil(nome)
        else:
            st.error("Matrícula ou senha incorretas.")

# --- OPÇÃO 3: VER TODOS OS PERFIS CADASTRADOS ---
elif menu == "👨‍🎓 Ver Perfis":
    st.subheader("Perfis do Grupo de Pesquisa do Prof. Caio Ribeiro")
    carregar_perfis()

def sistema_darcy_ribeiro():
    print("Bem-vindo ao Sistema Darcy Ribeiro!")
    depto = input("Por favor, diga um departamento ou instituto da UnB: ").strip().lower()
    palavras_chave = ["if", "física", "fisica", "instituto de física"]

    if any(palavra in depto for palavra in palavras_chave):
        print("\nSite Oficial: https://if.unb.br/")
        exibir_historia_if()
        exibir_biografias()
        escolha_nucleo = exibir_nucleos()
        tratar_nucleo(escolha_nucleo)
    else:
        print("Departamento ainda não disponível no sistema.")

if __name__ == "__main__":
    sistema_darcy_ribeiro()

st.set_page_config(page_title="Sistema Darcy Ribeiro", layout="centered")
