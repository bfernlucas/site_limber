// Limber Social — interações da página

(function () {
  // menu em telas pequenas
  var abrir = document.querySelector(".menu-abrir");
  var menu = document.getElementById("menu");
  if (abrir && menu) {
    abrir.addEventListener("click", function () {
      var aberto = menu.classList.toggle("aberto");
      abrir.setAttribute("aria-expanded", String(aberto));
      abrir.textContent = aberto ? "Fechar" : "Menu";
    });
    menu.addEventListener("click", function (evento) {
      if (evento.target.closest("a")) {
        menu.classList.remove("aberto");
        abrir.setAttribute("aria-expanded", "false");
        abrir.textContent = "Menu";
      }
    });
  }

  // filtro da tabela de trabalhos
  var filtros = document.querySelectorAll(".filtro");
  var linhas = document.querySelectorAll(".trabalhos tbody tr");
  var contagem = document.getElementById("contagem");
  var total = linhas.length;

  function filtrar(frente) {
    var visiveis = 0;
    linhas.forEach(function (linha) {
      var mostra = frente === "todos" || linha.dataset.frente === frente;
      linha.hidden = !mostra;
      if (mostra) visiveis += 1;
    });
    if (contagem) {
      contagem.textContent =
        frente === "todos"
          ? total + " trabalhos"
          : "Mostrando " + visiveis + " de " + total + " trabalhos";
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
})();
