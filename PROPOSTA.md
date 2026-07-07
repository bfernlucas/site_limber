# Proposta — Site Institucional Limber Consultoria (versão enxuta)

> Proposta de estrutura, layout e stack para um site institucional enxuto, baseada em pesquisa de benchmarking de sites de consultoria no Brasil e no exterior (julho/2026).
>
> Acompanha um **mockup navegável** em [`mockup/index.html`](mockup/index.html) — abra no navegador para ver o layout proposto. Os textos do mockup são ilustrativos e serão ajustados ao seu posicionamento.

---

## 1. Objetivo e premissas

**Objetivo do site:** presença institucional profissional que gere confiança e converta visitantes em conversas comerciais (WhatsApp/agenda), com o menor custo de construção e manutenção possível.

**Premissas da versão enxuta:**

- Poucas páginas, foco em uma única ação principal (iniciar conversa).
- Publicável em dias, não meses; conteúdo fácil de atualizar.
- Custo de hospedagem ~zero e carregamento rápido em celular (maioria do tráfego no Brasil é mobile).
- Estrutura preparada para crescer depois (blog, cases, páginas por serviço) sem retrabalho.

---

## 2. Benchmarking

> **Complemento setorial:** ver [BENCHMARKING-MEL.md](BENCHMARKING-MEL.md) — pesquisa de consultorias de monitoramento, avaliação e aprendizagem (MEL/MEAL) no Brasil e no mundo, com padrões de posicionamento do campo e implicações diretas para o herói, os serviços e a prova social deste site.

### 2.1 O que os melhores sites de consultoria têm em comum

Analisando guias e curadorias recentes de sites de consultores e consultorias (Consulting Success, Sitebuilder Report, Freelancecake, Framer, Colorlib, Wix, e curadorias brasileiras como Task, Aurago e Vale da Web), os padrões que se repetem nos sites que geram clientes são:

1. **O herói responde 3 perguntas em segundos:** o que você faz, para quem, e como começar. Sites que enrolam no topo perdem o visitante antes do scroll.
2. **Clareza antes de criatividade.** Os melhores exemplos são intencionalmente minimalistas: poucas escolhas, navegação reduzida, atenção concentrada em uma ação primária. A sequência lógica é sempre **clareza → confiança → ação**.
3. **Copy vale mais que design.** As curadorias são unânimes: o que convence o cliente ideal é a mensagem (promessa, prova, processo), não efeitos visuais. O design serve para dar credibilidade e não atrapalhar.
4. **Prova social visível cedo:** logos de clientes, números (projetos, anos, resultados) e depoimentos curtos aparecem logo após o herói, não escondidos no rodapé.
5. **Um único CTA repetido.** Em vez de vários botões diferentes, o mesmo convite ("Agendar conversa" / "Falar no WhatsApp") se repete ao longo da página e fica fixo no mobile (sticky), o que aumenta conversão em toque.
6. **Seção de método/processo.** Consultorias que mostram "como funciona" em 3–4 passos reduzem a incerteza de contratar um serviço intangível — padrão presente em quase todos os bons exemplos.
7. **Rosto e história.** Para consultorias de porte pequeno/médio, foto real e bio curta convertem mais que fotos de banco de imagem; a pessoa é a marca.

### 2.2 One-page vs. multipágina

| Critério | One-page (âncoras) | Multipágina (4–6 páginas) |
|---|---|---|
| Conversão | Maior — narrativa única guia o visitante até o CTA, sem dispersão | Menor no curto prazo; visitante se perde entre páginas |
| Custo/prazo | Mínimo | 2–3× mais conteúdo para produzir |
| Manutenção | Um arquivo, uma história para manter coerente | Várias páginas para manter atualizadas |
| SEO | Suficiente para busca por marca + serviço principal local | Melhor para ranquear vários serviços/termos |
| Quando faz sentido | Validar oferta, captar leads, presença institucional inicial | Quando há muitos serviços distintos e produção de conteúdo ativa |

Estudos citados nas curadorias indicam que one-pages costumam alcançar **conversão maior que sites multipágina** graças à estrutura focada e navegação mínima (menor rejeição, maior engajamento). Para o mercado brasileiro, guias locais recomendam sites enxutos de **1 a 5 páginas** para validar oferta e captar leads.

**Recomendação para a Limber:** one-page como página principal + 1 página de apoio (política de privacidade/LGPD). Blog e páginas por serviço ficam para uma fase 2, se a estratégia pedir.

### 2.3 Referências de layout destacadas no benchmarking

- **Oakline Studio** — home "design-first" mínima: logo forte, tagline curta, pouquíssimos CTAs. Mostra que menos elementos = mais autoridade.
- **Denym** — preto e branco, direto, "sai da frente" do conteúdo. Prova que paleta reduzida funciona para serviços profissionais.
- **Josh Kremer Consulting** — muito espaço em branco, leitura fácil, header que some ao rolar e volta quando o usuário sobe (padrão que adotaremos: header fixo discreto).
- **Devon (consultor solo)** — o topo diz em uma frase exatamente o que ele faz e para quem; sem slogans vagos.
- **Padrão BR (Task, Vale da Web, Webby):** o "kit essencial" dos institucionais brasileiros que convertem é botão de WhatsApp flutuante, formulário simples, Google Analytics + Search Console, e canais de contato explícitos (WhatsApp, e-mail, Instagram) — quanto mais fácil o contato, mais rápido o visitante age.

### 2.4 Síntese: o layout enxuto que o benchmarking aponta

Estrutura de uma página, nesta ordem (cada seção tem um trabalho único):

```
Header fixo enxuto (logo + 4 âncoras + botão CTA)
1. Herói           → promessa clara + subtítulo + CTA WhatsApp (+ CTA secundário "ver método")
2. Prova social    → faixa com números e/ou logos de clientes
3. Serviços        → 3 cards (máximo 4), uma frase de resultado por card
4. Método          → "como funciona" em 4 passos numerados
5. Sobre           → foto real + bio curta orientada ao cliente
6. Depoimentos     → 2–3 citações curtas com nome/empresa
7. FAQ             → 4–5 perguntas (accordion), quebra objeções
8. CTA final       → faixa de destaque repetindo o convite
Rodapé             → contatos, redes, CNPJ, link LGPD
+ Botão WhatsApp flutuante (sticky no mobile)
```

---

## 3. Wireframe comentado (seção a seção)

O mockup em `mockup/index.html` implementa exatamente esta estrutura. Racional de cada seção:

| Seção | Objetivo | Conteúdo (a definir com você) |
|---|---|---|
| **Herói** | Passar no "teste dos 5 segundos" | H1 = transformação que você entrega + para quem; subtítulo = como; CTA primário WhatsApp |
| **Prova social** | Credibilidade imediata | 3–4 números (anos, projetos, clientes, resultado médio) ou logos |
| **Serviços** | Mostrar o cardápio sem virar catálogo | 3 ofertas, cada uma com título + resultado em 1 frase + "para quem é" |
| **Método** | Reduzir risco percebido | 4 passos: diagnóstico → plano → execução/acompanhamento → resultado |
| **Sobre** | Pessoa é a marca | Foto real, bio de 4–6 linhas escrita para o cliente (não currículo) |
| **Depoimentos** | Prova por terceiros | 2–3 citações curtas, com nome e empresa (pedir autorização) |
| **FAQ** | Quebrar objeções | Preço/formato, prazo, atendimento remoto/presencial, para quem NÃO é |
| **CTA final** | Última chance de conversão | Convite direto + botão WhatsApp com mensagem pré-preenchida |

---

## 4. Diretrizes de copy

- **Fórmula do H1:** `[Resultado desejado] para [público] sem [dor/obstáculo]` ou `Ajudo [público] a [resultado] com [método]`. Nada de "Soluções inovadoras e personalizadas".
- Tom: direto, primeira pessoa (consultoria com rosto), frases curtas.
- Cada seção termina apontando para a próxima (narrativa contínua, como uma boa conversa de vendas).
- CTA sempre com o mesmo verbo/promessa (ex.: "Agendar diagnóstico gratuito" ou "Falar no WhatsApp") — link do WhatsApp com mensagem pré-preenchida e UTM para medir origem.

## 5. Diretrizes visuais

- **Tipografia-primeiro:** título serifado/display + texto sem serifa; hierarquia forte substitui ilustração.
- **Paleta reduzida:** fundo claro quase-branco, texto grafite, **1 cor de acento** (no mockup usei verde-escuro institucional — trocamos pela sua identidade).
- Muito espaço em branco; nada de carrossel, pop-up ou animação pesada.
- Mobile-first: seções empilham, CTA vira botão fixo, alvos de toque generosos.

## 6. Stack técnica e hospedagem (custo ~zero)

| Item | Recomendação | Custo |
|---|---|---|
| Construção | HTML/CSS estático (como o mockup) ou Astro se quisermos componentes | R$ 0 |
| Hospedagem | GitHub Pages, Vercel ou Netlify (SSL incluso) | R$ 0 |
| Domínio | `limber.com.br` ou similar via Registro.br | ~R$ 40/ano |
| Formulário | Link direto WhatsApp (principal) + Formspree/Tally se quiser formulário | R$ 0 |
| Medição | GA4 + Google Search Console | R$ 0 |

Justificativa: site estático carrega quase instantaneamente (Core Web Vitals verdes ajudam SEO), não tem manutenção de segurança/plugins como WordPress, e o conteúdo fica versionado neste repositório.

## 7. SEO e mensuração (mínimo viável)

- Title/description otimizados para `consultoria + [especialidade] + [cidade/Brasil]`.
- Google Business Profile vinculado ao site (busca local).
- Open Graph configurado (link bonito no WhatsApp/Instagram — importante porque o tráfego virá muito de bio e conversas).
- Eventos GA4 nos cliques de WhatsApp para saber qual seção converte.

## 8. Roadmap em fases

| Fase | Escopo | Prazo estimado |
|---|---|---|
| **1 — Enxuta (esta proposta)** | One-page + LGPD + domínio + medição | 1–2 semanas após conteúdo definido |
| 2 — Autoridade | Página por serviço, cases detalhados, blog | quando houver demanda/conteúdo |
| 3 — Captação | Landing pages de campanha, lead magnet, e-mail | junto com investimento em mídia |

## 9. O que preciso confirmar com você

1. **Posicionamento:** especialidade exata da consultoria e público-alvo (ajusta H1, serviços e SEO — os textos do mockup são ilustrativos).
2. Identidade visual existente (logo, cores) ou criamos uma base simples?
3. Números/clientes que podemos usar como prova social e 2–3 depoimentos autorizados.
4. Número de WhatsApp comercial e domínio preferido.

---

## 10. Fontes do benchmarking

- [Consulting Success — The 10 Steps to Building a Client-Generating Consulting Website](https://www.consultingsuccess.com/consulting-website)
- [Sitebuilder Report — Consultant Websites: 20+ Inspiring Examples](https://www.sitebuilderreport.com/inspiration/consulting-websites)
- [Freelancecake — 29 Best Consultant Website Examples](https://www.freelancecake.com/blog/consultant-website-examples)
- [Framer — 13 Best Consulting Website Design Examples](https://www.framer.com/blog/13-best-consulting-website-design-examples/)
- [Melisa Liberman — Consulting Website Examples for Solo Consultants](https://www.melisaliberman.com/blog/consulting-website-examples)
- [Move Digital — Building a Website that Converts for Professional Services](https://movedigitalgroup.com/blog/uncategorized/website-that-converts-professional-service/)
- [Gola — One Page Template Picks (dados de conversão one-page)](https://www.gola.supply/blog/one-page-template)
- [Task — Site institucional: o que é e 7 exemplos](https://www.task.com.br/blog/site-institucional-exemplos/)
- [Aurago — Estrutura de um site institucional](https://aurago.com.br/conteudos/estrutura-de-um-site-institucional/)
- [Vale da Web — Estrutura de um site institucional](https://www.valedaweb.com.br/conheca-a-estrutura-de-um-site-institucional/)
- [Webby Propaganda — Integrações essenciais para institucionais (WhatsApp, GA, Search Console)](https://webbypropaganda.com.br/integracoes-para-sites-institucionais/)
- [LD Marketing — Sites institucionais minimalistas](https://www.ldmarketing.com.br/sites-institucionais-minimalistas/)
- [Gabriel do Site — Top 10 sites institucionais minimalistas](https://gabrieldosite.com.br/top-10-exemplos-de-sites-institucionais-minimalistas/)
