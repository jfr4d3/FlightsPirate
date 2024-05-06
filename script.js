document.addEventListener("DOMContentLoaded", function() {
    const submitBtn = document.getElementById("submitBtn");
  
    submitBtn.addEventListener("click", function() {
      const ciudad = document.getElementById("ciudad").value;
      const email = document.getElementById("email").value;
  
      // Aquí puedes agregar la lógica para enviar los datos a la base de datos
      // Por ahora, simplemente mostraremos un mensaje en la página
      const message = document.getElementById("message");
      message.textContent = `Gracias por suscribirte. Ciudad: ${ciudad}, Correo electrónico: ${email}`;
    });
  });
  