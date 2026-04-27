document.addEventListener('DOMContentLoaded', function () {
  const rows = document.querySelectorAll('tr.hover\\:bg-slate-50');

  function calcularSubtotal(row) {
    const cantidadInput = row.querySelector('.cantidad-input');
    const precioInput = row.querySelector('.precio-input');
    const subtotalInput = row.querySelector('.subtotal-input');

    const cantidad = parseFloat(cantidadInput.value) || 0;
    const precio = parseFloat(precioInput.value) || 0;
    const subtotal = cantidad * precio;

    subtotalInput.value = subtotal > 0 ? subtotal.toFixed(2) : '';
  }

  function calcularTotalGeneral() {
    let totalSubtotal = 0;
    rows.forEach(row => {
      const subtotalInput = row.querySelector('.subtotal-input');
      const subtotal = parseFloat(subtotalInput.value) || 0;
      totalSubtotal += subtotal;
    });

    const totalGeneral = totalSubtotal;
    const subtotalGeneralValue = totalGeneral / 1.18;
    const igv = totalGeneral - subtotalGeneralValue;

    document.getElementById('subtotal-general').textContent = `S/ ${subtotalGeneralValue.toFixed(2)}`;
    document.getElementById('igv-general').textContent = `S/ ${igv.toFixed(2)}`;
    document.getElementById('total-general').textContent = `S/ ${totalGeneral.toFixed(2)}`;
  }

  rows.forEach(row => {
    const cantidadInput = row.querySelector('.cantidad-input');
    const precioInput = row.querySelector('.precio-input');

    if (!cantidadInput || !precioInput) return;

    cantidadInput.addEventListener('input', () => {
      calcularSubtotal(row);
      calcularTotalGeneral();
    });
    precioInput.addEventListener('input', () => {
      calcularSubtotal(row);
      calcularTotalGeneral();
    });
  });

  // Manejar el checkbox de "Otro"
  const otroCheckbox = document.getElementById('otro-checkbox');
  const otroInput = document.querySelector('input[name="otro_pago"]');
  if (otroCheckbox && otroInput) {
    otroCheckbox.addEventListener('change', () => {
      otroInput.disabled = !otroCheckbox.checked;
    });
  }
});
