// Limber Social — interações da página.
// Os textos exibidos vêm de atributos data-* do HTML, para que cada idioma traga os seus.

(function () {
  // ---------- menu em telas pequenas ----------
  var abrir = document.querySelector(".menu-abrir");
  var menu = document.getElementById("menu");

  function fecharMenu(devolverFoco) {
    if (!menu || !menu.classList.contains("aberto")) return;
    menu.classList.remove("aberto");
    abrir.setAttribute("aria-expanded", "false");
    abrir.textContent = abrir.dataset.abrir;
    if (devolverFoco) abrir.focus();
  }

  if (abrir && menu) {
    abrir.addEventListener("click", function () {
      var aberto = menu.classList.toggle("aberto");
      abrir.setAttribute("aria-expanded", String(aberto));
      abrir.textContent = aberto ? abrir.dataset.fechar : abrir.dataset.abrir;
    });
    menu.addEventListener("click", function (evento) {
      if (evento.target.closest("a")) fecharMenu(false);
    });
    document.addEventListener("keydown", function (evento) {
      if (evento.key === "Escape") fecharMenu(true);
    });
  }

  // ---------- seção atual no menu ----------
  var links = menu ? menu.querySelectorAll('a[href^="#"]:not(.botao)') : [];
  var secoes = [];
  links.forEach(function (link) {
    var secao = document.querySelector(link.getAttribute("href"));
    if (secao) secoes.push({ link: link, secao: secao });
  });

  function marcarSecao() {
    var linha = window.innerHeight * 0.35;
    var atual = null;
    secoes.forEach(function (item) {
      var caixa = item.secao.getBoundingClientRect();
      if (caixa.top <= linha && caixa.bottom > linha) atual = item;
    });
    secoes.forEach(function (item) {
      if (item === atual) item.link.setAttribute("aria-current", "true");
      else item.link.removeAttribute("aria-current");
    });
  }
  if (secoes.length) {
    var agendado = false;
    window.addEventListener(
      "scroll",
      function () {
        if (agendado) return;
        agendado = true;
        window.requestAnimationFrame(function () {
          agendado = false;
          marcarSecao();
        });
      },
      { passive: true }
    );
    marcarSecao();
  }

  // ---------- tabela de trabalhos: filtro e "mostrar todos" ----------
  var tabela = document.querySelector(".trabalhos");
  var filtros = document.querySelectorAll(".filtro");
  var linhas = document.querySelectorAll(".trabalhos tbody tr");
  var contagem = document.getElementById("contagem");
  var mostrarTodos = document.getElementById("mostrar-todos");
  var total = linhas.length;

  function expandir() {
    if (!tabela) return;
    tabela.classList.remove("recolhida");
    if (mostrarTodos) mostrarTodos.hidden = true;
  }

  if (tabela && mostrarTodos && window.matchMedia("(max-width: 880px)").matches) {
    tabela.classList.add("recolhida");
    mostrarTodos.hidden = false;
    mostrarTodos.addEventListener("click", expandir);
  }

  function filtrar(frente) {
    var visiveis = 0;
    linhas.forEach(function (linha) {
      var mostra = frente === "todos" || linha.dataset.frente === frente;
      linha.hidden = !mostra;
      if (mostra) visiveis += 1;
    });
    if (frente !== "todos") expandir();
    if (contagem) {
      var modelo = frente === "todos" ? contagem.dataset.todos : contagem.dataset.parcial;
      contagem.textContent = modelo.replace("{v}", visiveis).replace("{n}", total);
    }
  }

  filtros.forEach(function (botao) {
    botao.addEventListener("click", function () {
      filtros.forEach(function (outro) {
        outro.setAttribute("aria-pressed", String(outro === botao));
      });
      filtrar(botao.dataset.filtro);
    });
  });

  // ---------- copiar o endereço de e-mail ----------
  var copiar = document.querySelector(".copiar");
  var aviso = document.getElementById("copiar-aviso");
  if (copiar && navigator.clipboard) {
    copiar.hidden = false;
    copiar.addEventListener("click", function () {
      navigator.clipboard.writeText(copiar.dataset.copiar).then(
        function () {
          aviso.textContent = copiar.dataset.sucesso;
        },
        function () {
          aviso.textContent = copiar.dataset.falha;
        }
      );
    });
  }
})();
