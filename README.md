# site_limber

Site institucional da Limber Social (versão de teste).

- `index.html`, `assets/` — o site: página única, estática, sem dependências externas. Fontes Sora e DM Sans hospedadas no próprio repositório; cores e logotipos do brandbook.
- `BENCHMARKING.md` — comparação dos sites de consultorias de avaliação de impacto (novembro de 2026) e as decisões que saíram dela.
- `arquivo/` — estudo de julho de 2026 (proposta, benchmarking do campo e mockups), mantido para consulta.

## Antes do lançamento

1. Revisar o conteúdo (lista de trabalhos, publicações, minibio).
2. Remover de `index.html` a linha `<meta name="robots" content="noindex, nofollow">` e a faixa "Versão de teste".
3. Configurar o domínio próprio em Settings → Pages e criar o arquivo `CNAME`.

## Como editar

Abra `index.html` em qualquer editor. Cada trabalho é uma linha `<tr data-frente="...">` da tabela; o filtro usa esse atributo (`pesquisa`, `monitoramento`, `avaliacao`, `aprendizagem`).
