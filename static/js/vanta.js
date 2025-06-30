// vanta.js – Fondo animado VANTA.WAVES para sección hero

document.addEventListener("DOMContentLoaded", function () {
  if (typeof VANTA !== "undefined" && VANTA.WAVES) {
    VANTA.WAVES({
      el: "#vanta-bg",
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      scale: 1.00,
      scaleMobile: 1.00,
      color: 0x0c283b,      // ✅ corregido sin #
      shininess: 128.00,
      waveHeight: 12.00,
      waveSpeed: 1.15,
      zoom: 1.57
    });
  } else {
    console.error("VANTA.WAVES no está disponible");
  }
});
