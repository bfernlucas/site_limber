# site_limber

Site institucional da Limber Social (versão de teste).

- `index.html`, `assets/` — o site: página única, estática, sem dependências externas. Fontes Sora e DM Sans hospedadas no próprio repositório; cores e logotipos do brandbook.
- `assets/img/` — fotografias de licença aberta obtidas no Wikimedia Commons, recortadas e com cor ajustada. Autoria e licença de cada uma estão no rodapé do site; ao trocar uma foto, atualize o crédito.
- `en/index.html` — versão em inglês, gerada a partir de `index.html` pelo script `ferramentas/gerar_en.py`. Não edite à mão: altere o português, inclua a tradução dos textos novos no dicionário do script e rode `python3 ferramentas/gerar_en.py`.
- `BENCHMARKING.md` — comparação dos sites de consultorias de avaliação de impacto (novembro de 2026) e as decisões que saíram dela.
- `arquivo/` — estudo de julho de 2026 (proposta, benchmarking do campo e mockups), mantido para consulta.

## Antes do lançamento

1. Revisar o conteúdo (lista de trabalhos, publicações, minibio) e, se possível, trocar as fotografias por registros próprios de campo.
2. Remover de `index.html` a linha `<meta name="robots" content="noindex, nofollow">` e a faixa "Versão de teste".
3. Configurar o domínio próprio em Settings → Pages e criar o arquivo `CNAME`.
4. Trocar `https://bfernlucas.github.io/site_limber/` pelo novo endereço nas linhas `og:url`, `og:image` e `hreflang` de `index.html` e gerar o inglês de novo.
5. Incluir o retrato na seção "Quem conduz o trabalho" (há um comentário no HTML indicando o lugar).

## Como editar

Abra `index.html` em qualquer editor. Cada trabalho é uma linha `<tr data-frente="...">` da tabela; o filtro usa esse atributo (`pesquisa`, `monitoramento`, `avaliacao`, `aprendizagem`).
