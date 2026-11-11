#!/usr/bin/env python3
"""Gera en/index.html a partir de index.html.

Uso: python3 ferramentas/gerar_en.py

O script troca cada texto em português pela tradução do dicionário abaixo.
Se um texto novo aparecer no site sem tradução, o script para e mostra qual é.
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# Textos que ficam iguais nos dois idiomas (nomes próprios, datas, licenças).
MANTER = {
    "limber", "social", ".", ",", "Menu", "UNICEF", "Consórcio Nordeste", "The Nature Conservancy",
    "Instituto Climate Ventures", "Petrobras Socioambiental", "PROSAMIN+, Manaus", "PAGES, Maranhão",
    "Bahia Produtiva", "Oportunidades para o Nordeste", "Redes Ceará", "Lagos do São Francisco",
    "A União Faz a Vida", "Sicredi", "Coletivo Online", "Instituto Coca-Cola Brasil", "COOPAQ",
    "No Clima da Caatinga", "Trias", "Revista Nacional de Administración, 2022", "Lucas Fernandes",
    "LinkedIn", "limbersocial@gmail.com", "Limber Pesquisas Socioeconômicas LTDA", "Wikimedia Commons",
    "CC BY-SA 2.0", "CC BY-SA 3.0", "CC BY-SA 4.0", "CC0", "Limber Social",
}

TRADUCAO = {
    # cabeçalho e capa
    "Limber Social — pesquisa, monitoramento e avaliação de programas": "Limber Social — research, monitoring and evaluation of programs",
    "A Limber Social faz pesquisa, monitoramento e avaliação de programas sociais, rurais e ambientais, com trabalho de campo no Norte e no Nordeste do Brasil.": "Limber Social does research, monitoring and evaluation of social, rural and environmental programs, with fieldwork in the North and Northeast of Brazil.",
    "Limber Social — medimos o que de fato mudou": "Limber Social — we measure what actually changed",
    "Pesquisa, monitoramento e avaliação de programas sociais, rurais e ambientais.": "Research, monitoring and evaluation of social, rural and environmental programs.",
    "Ir para o conteúdo": "Skip to content",
    "Versão de teste. O conteúdo desta página ainda está em revisão.": "Test version. The content of this page is still under review.",
    "Limber Social, início": "Limber Social, home",
    "Fechar": "Close",
    "Seções": "Sections",
    "O que fazemos": "What we do",
    "Trabalhos": "Work",
    "Método": "Method",
    "Publicações": "Publications",
    "Equipe": "Team",
    "English": "Português",
    "Falar com a Limber": "Contact Limber",
    "Medimos o que de fato mudou": "We measure what actually changed",
    "Pesquisa, monitoramento e avaliação de programas sociais, rurais e ambientais, com trabalho de campo no Norte e no Nordeste do Brasil.": "Research, monitoring and evaluation of social, rural and environmental programs, with fieldwork in the North and Northeast of Brazil.",
    "Ver os trabalhos da equipe": "See the team's work",
    "Plantação de palma forrageira no Semiárido, com cisterna e casa ao fundo": "Forage cactus plantation in the Semi-arid, with a cistern and a house in the background",
    "Cultivo de palma em Serra Preta, Bahia. Foto: Sergio Amaral, Ministério do Desenvolvimento Social": "Forage cactus plantation in Serra Preta, Bahia. Photo: Sergio Amaral, Ministério do Desenvolvimento Social",
    # financiadores
    "Financiadores": "Funders",
    "Financiadores de programas em que a equipe atuou, em contratos próprios ou em parceria com outras consultorias": "Funders of programs the team has worked on, under its own contracts or in partnership with other consultancies",
    "Banco Mundial": "World Bank",
    "Banco Interamericano de Desenvolvimento": "Inter-American Development Bank",
    "Fundo Internacional de Desenvolvimento Agrícola": "International Fund for Agricultural Development",
    # frentes
    "Quatro frentes, um mesmo rigor": "Four lines of work, one standard of rigor",
    "Cada trabalho combina o que o problema pede. Uma avaliação de impacto começa com boa pesquisa de campo e só vale a pena se o resultado chegar a quem decide.": "Each assignment combines what the problem calls for. An impact evaluation starts with good field research and is only worth doing if the results reach the people who decide.",
    "Pesquisa": "Research",
    "Desenho amostral, instrumentos e linha de base.": "Sampling design, instruments and baseline.",
    "Planejamos a amostra, escrevemos questionários e roteiros, treinamos a equipe e acompanhamos a coleta. A linha de base é o retrato da situação antes de o programa começar.": "We design the sample, write questionnaires and interview guides, train the team and supervise data collection. The baseline is the picture of the situation before the program starts.",
    "Questionários domiciliares": "Household surveys",
    "Amostragem estratificada": "Stratified sampling",
    "Entrevistas e rodas de conversa": "Interviews and group discussions",
    "Análise de dados oficiais": "Analysis of official data",
    "Monitoramento": "Monitoring",
    "Indicadores e painéis para ajustar a rota cedo.": "Indicators and dashboards to adjust course early.",
    "Partimos da teoria da mudança para definir poucos indicadores que importam, montar a rotina de coleta e entregar painéis que a equipe usa.": "We start from the theory of change to define a few indicators that matter, set up the data collection routine and deliver dashboards the team uses.",
    "Teoria da mudança": "Theory of change",
    "o caminho esperado entre as ações do programa e os resultados": "the expected path from the program's actions to its results",
    "Matriz de indicadores": "Indicator matrix",
    "Painéis interativos": "Interactive dashboards",
    "Mapas e análise de redes": "Maps and network analysis",
    "Avaliação": "Evaluation",
    "Inferência causal para medir o que de fato mudou.": "Causal inference to measure what actually changed.",
    "Escolhemos o desenho que os dados e o calendário do programa permitem e dizemos com clareza o que ele consegue afirmar.": "We choose the design that the data and the program's timeline allow, and we state clearly what it can claim.",
    "Diferença em diferenças": "Difference-in-differences",
    "compara a evolução de quem participou com a de um grupo parecido": "compares how participants changed with how a similar group changed",
    "Pareamento": "Matching",
    "compara participantes e não participantes de perfil semelhante": "compares participants and non-participants with similar profiles",
    "Regressão descontínua": "Regression discontinuity",
    "compara quem ficou logo acima e logo abaixo do critério de entrada": "compares those just above and just below the eligibility cutoff",
    "Retorno social do investimento": "Social return on investment",
    "estima o valor social gerado por real investido": "estimates the social value generated for each real invested",
    "Aprendizagem": "Learning",
    "Evidência que vira decisão com as equipes.": "Evidence that becomes decisions, together with the teams.",
    "Devolvemos os achados em oficinas, sumários executivos e notas de política, e formamos as equipes para ler e produzir os próprios números.": "We share findings in workshops, executive summaries and policy briefs, and we train teams to read and produce their own numbers.",
    "Oficinas de devolutiva": "Feedback workshops",
    "apresentação e discussão dos resultados com a equipe": "presentation and discussion of results with the team",
    "Sumários executivos": "Executive summaries",
    "Notas de política": "Policy briefs",
    "Formação em análise de dados": "Training in data analysis",
    # trabalhos em destaque
    "Trabalhos da equipe": "The team's work",
    "Avaliações, diagnósticos e sistemas de monitoramento em que a equipe da Limber atuou, a maior parte no Norte e no Nordeste do Brasil.": "Evaluations, diagnostic studies and monitoring systems the Limber team has worked on, mostly in the North and Northeast of Brazil.",
    "Imagem ilustrativa:": "Illustrative image:",
    "Igarapé canalizado entre duas vias, com casas à direita e prédios ao fundo": "Channelized urban stream between two roads, with houses on the right and buildings in the distance",
    "Igarapé do Mestre Chico, Manaus": "Mestre Chico stream, Manaus",
    "Avaliação de impacto e estudo longitudinal dos reassentamentos do programa de saneamento dos igarapés.": "Impact evaluation and longitudinal study of the resettlements under the urban streams sanitation program.",
    "Banco Interamericano de Desenvolvimento e Governo do Amazonas": "Inter-American Development Bank and Government of Amazonas",
    "Palmeiras de babaçu adultas e jovens em área rural": "Adult and young babassu palms in a rural area",
    "Babaçual no Maranhão": "Babassu palm grove in Maranhão",
    "Estratégia de identificação causal por pareamento e plano amostral da linha de base com comunidades rurais.": "Causal identification strategy based on matching, and baseline sampling plan with rural communities.",
    "Colinas verdes da Caatinga na estação chuvosa, ao entardecer": "Green Caatinga hills in the rainy season, at dusk",
    "Caatinga na estação chuvosa, Bahia": "Caatinga in the rainy season, Bahia",
    "Avaliação de resultados do programa de desenvolvimento rural do estado.": "Outcome evaluation of the state's rural development program.",
    "Banco Mundial e Governo da Bahia": "World Bank and Government of Bahia",
    "Vista aérea de aerogeradores sobre a vegetação do litoral do Rio Grande do Norte": "Aerial view of wind turbines over coastal vegetation in Rio Grande do Norte",
    "Parque eólico Cutia, Rio Grande do Norte": "Cutia wind farm, Rio Grande do Norte",
    "35 entrevistas sobre a transição energética, matriz de sistematização, painéis de visualização e análise de redes.": "35 interviews on the energy transition, a systematization matrix, visualization dashboards and network analysis.",
    "Instituto Climate Ventures e Instituto Clima e Sociedade": "Instituto Climate Ventures and Instituto Clima e Sociedade",
    # tabela
    "Todos os trabalhos": "All work",
    "Filtrar trabalhos por frente": "Filter projects by line of work",
    "Todos": "All",
    "19 trabalhos": "19 projects",
    "{n} trabalhos": "{n} projects",
    "Mostrando {v} de {n} trabalhos": "Showing {v} of {n} projects",
    "Período": "Period",
    "Trabalho": "Project",
    "Financiador": "Funder",
    "Frente": "Line of work",
    "Plano Brasil Nordeste de Transformação Ecológica": "Brazil Northeast Ecological Transformation Plan",
    "Incursões de campo nos estados, avaliação da carteira de iniciativas e estimativas de captação por eixo.": "Field visits to the states, assessment of the portfolio of initiatives and fundraising estimates by thematic axis.",
    "Ler o plano publicado": "Read the published plan (in Portuguese)",
    "Consórcio Nordeste e Organização dos Estados Ibero-americanos": "Consórcio Nordeste and Organization of Ibero-American States",
    "Restauração de paisagens e uso sustentável da terra, Pará": "Landscape restoration and sustainable land use, Pará",
    "Sistemática de monitoramento e avaliação, formulários de coleta em campo e painéis de acompanhamento.": "Monitoring and evaluation framework, field data collection forms and tracking dashboards.",
    "The Nature Conservancy Brasil": "The Nature Conservancy Brazil",
    "Conhecer o programa": "About the program (in Portuguese)",
    "Diagnóstico socioterritorial sobre insegurança alimentar e inclusão produtiva no estado.": "Territorial diagnostic study on food insecurity and productive inclusion in the state.",
    "Trilha em Análise de Dados": "Data Analysis Track",
    "Curso de estatística aplicada para a equipe técnica, com o Laboratório de Métodos Quantitativos da Universidade Federal do Rio Grande do Norte.": "Applied statistics course for the technical team, with the Quantitative Methods Laboratory of the Federal University of Rio Grande do Norte.",
    "Instituto para o Desenvolvimento do Investimento Social": "Institute for the Development of Social Investment",
    "Newton Fund Brasil": "Newton Fund Brazil",
    "Estudo de caso nacional sobre os efeitos do fundo em pesquisa, inovação e cooperação internacional.": "National case study on the fund's effects on research, innovation and international cooperation.",
    "Governo do Reino Unido": "UK Government",
    "Avaliação de retorno social do investimento, com coleta de dados primários.": "Social return on investment evaluation, with primary data collection.",
    "Embrapa e Companhia Hidro Elétrica do São Francisco": "Embrapa and Companhia Hidro Elétrica do São Francisco",
    "Avaliação quase-experimental do programa de educação, com microdados do Sistema de Avaliação da Educação Básica.": "Quasi-experimental evaluation of the education program, using microdata from the national basic education assessment system.",
    "Avaliação de impacto do projeto sobre a empregabilidade de jovens.": "Impact evaluation of the project on youth employability.",
    "Um Milhão de Oportunidades": "One Million Opportunities",
    "Estudo sobre habilidades e empregos verdes para a juventude.": "Study on green skills and jobs for young people.",
    "UNICEF Brasil": "UNICEF Brazil",
    "Sistema de monitoramento e avaliação da cooperativa, construído a partir da teoria da mudança.": "Monitoring and evaluation system for the cooperative, built from its theory of change.",
    "Programa SER": "SER Program",
    "Gestão, monitoramento e avaliação de iniciativas de desenvolvimento rural.": "Management, monitoring and evaluation of rural development initiatives.",
    "Neoenergia e Banco Nacional de Desenvolvimento Econômico e Social": "Neoenergia and the Brazilian Development Bank",
    "Avaliação de resultados do programa de desenvolvimento rural.": "Outcome evaluation of the rural development program.",
    "Acesso Mais Seguro": "Safer Access",
    "Análise quantitativa dos resultados do programa.": "Quantitative analysis of the program's results.",
    "Comitê Internacional da Cruz Vermelha": "International Committee of the Red Cross",
    "Avaliação de práticas sustentáveis de conservação e restauração no bioma.": "Evaluation of sustainable conservation and restoration practices in the biome.",
    "Organizações de Produtores para a América Latina": "Farmers' Organizations for Latin America",
    "Gestão e monitoramento do fortalecimento de organizações da agricultura familiar.": "Management and monitoring of the strengthening of family farming organizations.",
    "Fundo Internacional de Desenvolvimento Agrícola e União Europeia": "International Fund for Agricultural Development and European Union",
    "Índice de Desenvolvimento Inclusivo para Cooperativas Solidárias": "Inclusive Development Index for Solidarity Cooperatives",
    "Coordenação do índice que mede a inclusão de mulheres e jovens, publicado como Texto para Discussão do Ipea.": "Coordination of the index measuring the inclusion of women and young people, published as an Ipea discussion paper.",
    "Mostrar todos os 19 trabalhos": "Show all 19 projects",
    "A lista reúne trabalhos conduzidos por integrantes da equipe. Parte deles foi executada em parceria com outras consultorias e organizações.": "The list brings together work carried out by team members. Part of it was delivered in partnership with other consultancies and organizations.",
    # método
    "Como se mede o efeito de um programa": "How a program's effect is measured",
    "Esquema com duas linhas ao longo do tempo. Antes do programa, participantes e grupo de comparação evoluem em paralelo. Depois do início, a linha de quem participou sobe mais rápido. Uma linha pontilhada mostra o caminho que os participantes teriam seguido sem o programa. A distância entre a linha real e a pontilhada é o efeito.": "Diagram with two lines over time. Before the program, participants and the comparison group move in parallel. After the start, the participants' line rises faster. A dotted line shows the path participants would have followed without the program. The distance between the actual line and the dotted line is the effect.",
    "início do programa": "program start",
    "antes": "before",
    "depois": "after",
    "grupo de comparação": "comparison group",
    "sem o programa": "without the program",
    "quem participou": "participants",
    "efeito": "effect",
    "Como se mede o efeito de um programa.": "How a program's effect is measured.",
    "O efeito é a distância entre o que aconteceu com quem participou e o que teria acontecido sem o programa. Esquema ilustrativo de diferença em diferenças.": "The effect is the distance between what happened to participants and what would have happened without the program. Illustrative difference-in-differences diagram.",
    "Do alinhamento à devolutiva": "From kickoff to feedback",
    "Uma avaliação passa por cinco etapas. O plano de trabalho detalha os prazos de cada uma com quem contrata.": "An evaluation goes through five stages. The work plan sets the timing of each one with the client.",
    "Alinhamento": "Kickoff",
    "Reunião de partida, leitura dos documentos do programa e perguntas de avaliação fechadas.": "Kickoff meeting, review of program documents and agreed evaluation questions.",
    "Desenho": "Design",
    "Estratégia para isolar o efeito do programa, amostragem e instrumentos, validados antes de ir a campo.": "Strategy to isolate the program's effect, sampling and instruments, validated before going to the field.",
    "Campo": "Fieldwork",
    "Coleta com equipe treinada, supervisão diária e controle de qualidade dos dados.": "Data collection with a trained team, daily supervision and data quality control.",
    "Análise": "Analysis",
    "Estimação dos efeitos, testes de robustez e registro das limitações do estudo.": "Effect estimation, robustness checks and a record of the study's limitations.",
    "Devolutiva": "Feedback",
    "Apresentação e discussão dos resultados em oficina com a equipe do programa, relatório final e sumário executivo com recomendações.": "Presentation and discussion of results in a workshop with the program team, final report and executive summary with recommendations.",
    # território
    "Vale verde do Semiárido visto do alto de um lajedo, sob céu nublado": "Green Semi-arid valley seen from a rock outcrop, under a cloudy sky",
    "Do Semiárido à Amazônia": "From the Semi-arid to the Amazon",
    "A equipe trabalha onde os programas acontecem: comunidades rurais do Semiárido, cooperativas da agricultura familiar no Maranhão e no Pará, bairros de Manaus às margens dos igarapés. Conhecer o território muda a pergunta de pesquisa, o questionário e a leitura dos resultados.": "The team works where programs happen: rural communities in the Semi-arid, family farming cooperatives in Maranhão and Pará, neighborhoods along the streams of Manaus. Knowing the territory changes the research question, the questionnaire and the reading of the results.",
    "Zona rural de Malta, Paraíba. Foto: UsuárioPar": "Rural Malta, Paraíba. Photo: UsuárioPar",
    # publicações
    "Pesquisa que passa por revisão de pares": "Research that goes through peer review",
    "A equipe também publica. Os métodos usados nas avaliações são testados em congressos e periódicos de economia e desenvolvimento rural.": "The team also publishes. The methods used in our evaluations are tested at conferences and in journals of economics and rural development.",
    "Ver a lista completa de publicações": "See the full list of publications",
    "Seguro para plantar? Um ensaio sobre o impacto do Programa Garantia-Safra": "Insurance to Plant? An Essay on the Impact of the Garantia-Safra Program",
    "Encontro Nacional de Economia da ANPEC, 2025": "ANPEC National Economics Meeting, 2025",
    "Água e segurança alimentar durante a seca: estudo em áreas rurais de Medina, no Semiárido do Vale do Jequitinhonha": "Water and Food Security During Drought: A Study in Rural Areas of Medina, in the Semi-Arid Jequitinhonha Valley",
    "Artigo em periódico científico": "Journal article",
    "A inclusão de mulheres e jovens em cooperativas solidárias brasileiras: uma proposta de índice": "The Inclusion of Women and Young People in Brazilian Solidarity Cooperatives: A Proposal for an Index",
    "Elaboração do índice de desenvolvimento inclusivo para cooperativas solidárias": "Development of an Inclusive Development Index for Solidarity Cooperatives",
    "Texto para Discussão, Ipea, 2020": "Discussion Paper, Ipea, 2020",
    "Impactos da expansão de parques eólicos sobre a saúde das mulheres no Semiárido brasileiro": "Impacts of Wind Farm Developments on Women's Health in the Brazilian Semi-Arid Region",
    "Pesquisa em andamento": "Work in progress",
    # equipe
    "Quem conduz o trabalho": "Who leads the work",
    "Para cada trabalho, a Limber monta a equipe com pesquisadoras e pesquisadores associados em métodos quantitativos, pesquisa qualitativa e coordenação de campo.": "For each assignment, Limber assembles a team of associate researchers in quantitative methods, qualitative research and field coordination.",
    "Retrato de Lucas Fernandes": "Portrait of Lucas Fernandes",
    "Sócio-administrador e responsável técnico": "Managing partner and technical lead",
    "Economista, doutorando em Economia pela Universidade Federal do Rio Grande do Norte e mestre em Planejamento Urbano e Regional pela Universidade Federal de Minas Gerais. Pesquisador colaborador do Laboratório de Estudos Rurais e do Laboratório de Métodos Quantitativos da mesma universidade.": "Economist, PhD candidate in Economics at the Federal University of Rio Grande do Norte, with a master's degree in Urban and Regional Planning from the Federal University of Minas Gerais. Research collaborator at the Rural Studies Laboratory and the Quantitative Methods Laboratory of the same university.",
    "Trabalha há mais de dez anos com monitoramento, avaliação e pesquisa aplicada, da agricultura familiar e do cooperativismo solidário a programas de saneamento urbano e de transição energética. Pesquisa os efeitos dos parques eólicos e do Programa Garantia-Safra no Semiárido.": "He has worked for more than ten years in monitoring, evaluation and applied research, from family farming and solidarity cooperatives to urban sanitation and energy transition programs. He studies the effects of wind farms and of the Garantia-Safra crop insurance program in the Semi-arid.",
    "Página acadêmica": "Academic page",
    # contato e rodapé
    "Vamos conversar?": "Let's talk",
    "Conte o que você precisa avaliar, acompanhar ou pesquisar. Se já houver um termo de referência, pode enviar junto.": "Tell us what you need to evaluate, monitor or research. If you already have terms of reference, send them along.",
    "Escrever um e-mail": "Write an email",
    "Copiar endereço": "Copy address",
    "Endereço copiado": "Address copied",
    "Não foi possível copiar. Selecione o endereço e copie manualmente.": "Could not copy. Select the address and copy it manually.",
    "Natal, Rio Grande do Norte": "Natal, Rio Grande do Norte, Brazil",
    "CNPJ 61.019.077/0001-06": "Brazilian company registration (CNPJ) 61.019.077/0001-06",
    "Rodapé": "Footer",
    "Nesta página": "On this page",
    "Contato": "Contact",
    "Créditos das imagens": "Image credits",
    "Cultivo de palma em Serra Preta: Sergio Amaral, Ministério do Desenvolvimento Social,": "Forage cactus plantation in Serra Preta: Sergio Amaral, Ministério do Desenvolvimento Social,",
    "Igarapé do Mestre Chico: MI GENERAL ZAPATA,": "Mestre Chico stream: MI GENERAL ZAPATA,",
    "Babaçual no Maranhão: Marcelo Cavallari,": "Babassu palm grove in Maranhão: Marcelo Cavallari,",
    "Caatinga na estação chuvosa: A. Duarte,": "Caatinga in the rainy season: A. Duarte,",
    "Parque eólico Cutia: Copel,": "Cutia wind farm: Copel,",
    "Zona rural de Malta: UsuárioPar,": "Rural Malta: UsuárioPar,",
    "As imagens foram recortadas e tiveram a cor ajustada. As fotografias ilustram os territórios e não são registros dos trabalhos listados.": "The images were cropped and color-adjusted. The photographs illustrate the territories and are not records of the listed work.",
}

ATRIBUTOS = "alt|aria-label|content|data-todos|data-parcial|data-sucesso|data-falha|data-abrir|data-fechar"
SO_NUMEROS = re.compile(r"^[\d\s–\-./]+$")


def main():
    html = (RAIZ / "index.html").read_text(encoding="utf-8")
    faltando = []

    def traduzir(texto):
        chave = re.sub(r"\s+", " ", texto).strip()
        if not chave or chave in MANTER or SO_NUMEROS.match(chave):
            return None
        if chave in TRADUCAO:
            return TRADUCAO[chave]
        faltando.append(chave)
        return None

    def no_de_texto(m):
        bruto = m.group(1)
        novo = traduzir(bruto)
        if novo is None:
            return m.group(0)
        inicio = bruto[: len(bruto) - len(bruto.lstrip())]
        fim = bruto[len(bruto.rstrip()):]
        return ">" + inicio + novo + fim + "<"

    def atributo(m):
        valor = m.group(2)
        if not re.search(r"[A-Za-zÀ-ú]{3}", valor) or re.match(r"(https?:|width=|noindex|website|#|pt_BR|assets/)", valor):
            return m.group(0)
        novo = traduzir(valor)
        return m.group(0) if novo is None else f'{m.group(1)}="{novo}"'

    html = re.sub(r">([^<>]+)<", no_de_texto, html)
    html = re.sub(rf'\b({ATRIBUTOS})="([^"]+)"', atributo, html)

    if faltando:
        print("Textos sem tradução. Inclua no dicionário TRADUCAO ou em MANTER:")
        for t in dict.fromkeys(faltando):
            print("  -", t)
        sys.exit(1)

    # ajustes de idioma, caminhos e ligações
    base = re.search(r'<link rel="alternate" hreflang="pt-BR" href="([^"]+)">', html).group(1)
    html = html.replace('<html lang="pt-BR">', '<html lang="en">')
    html = html.replace('content="pt_BR"', 'content="en_US"')
    html = html.replace(f'<meta property="og:url" content="{base}">', f'<meta property="og:url" content="{base}en/">')
    html = re.sub(r'(src|href)="assets/', r'\1="../assets/', html)
    html = re.sub(r'(srcset="|, )assets/', r"\1../assets/", html)
    html = html.replace('<a class="idioma" href="en/" lang="en" hreflang="en">', '<a class="idioma" href="../" lang="pt-BR" hreflang="pt-BR">')
    html = html.replace("/deed.pt-br", "/deed.en")
    html = html.replace("subject=Contato%20pelo%20site%20da%20Limber%20Social", "subject=Contact%20via%20the%20Limber%20Social%20website")

    destino = RAIZ / "en"
    destino.mkdir(exist_ok=True)
    (destino / "index.html").write_text(html, encoding="utf-8")
    print("en/index.html gerado.")


if __name__ == "__main__":
    main()
