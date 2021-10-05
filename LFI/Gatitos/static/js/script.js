function gatoboton() {
    var numero = Math.floor((Math.random() * 50) + 1);
    location.href = window.location.origin + window.location.pathname + "?foto=" + numero;
}