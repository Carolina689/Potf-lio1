function adicionarTarefa() {
  const input = document.querySelector("input");
  const lista = document.getElementById("lista");

  if (input.value === "") return;

  const item = document.createElement("li");
  item.innerHTML = `
    ${input.value}
    <button onclick="this.parentElement.remove()">❌</button>
  `;

  lista.appendChild(item);
  input.value = "";
}