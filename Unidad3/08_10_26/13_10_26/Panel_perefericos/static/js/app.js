async function cargarConfiguracion() {
    const response = await fetch('/api/config');

    if (!response.ok) {
        throw new Error('Error al cargar la configuración');
    }

    const datos = await response.json();
    document.querySelector("#titulo")
    .textContent = datos.titulo;
}
cargarConfiguracion()