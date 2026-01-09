# Plan de Pruebas - SauceDemo

## Casos de Prueba

| ID | Caso de Prueba | Precondición | Pasos | Datos | Resultado Esperado |
|----|----------------|--------------|-------|-------|---------------------|
| 1 | Login exitoso | En login | Ingresar user/pass válidos → Login | standard_user / secret_sauce | Redirección a /inventory.html |
| 2 | Usuario bloqueado | En login | Ingresar locked_out_user → Login | locked_out_user / secret_sauce | Mensaje: "locked out" |
| 3 | Contraseña vacía | En login | Ingresar user, dejar pass vacío → Login | standard_user / "" | Mensaje: "Password is required" |
| 4 | Agregar al carrito | Logueado | Clic en "Add to cart" | Sauce Labs Backpack | Ícono carrito = 1 |
| 5 | Quitar del carrito | Producto en carrito | Clic en "Remove" | Sauce Labs Backpack | Ícono carrito = 0 |
| 6 | Logout | Logueado | Menú → Logout | - | Vuelve al login |
| 7 | Ordenar A-Z | En inventario | Seleccionar "Name (A to Z)" | - | Productos ordenados alfabéticamente |
| 8 | Checkout completo | 1 producto en carrito | Login → agregar → carrito → checkout → llenar → finalizar | Nombre: Test, CP: 12345 | Mensaje: "THANK YOU FOR YOUR ORDER" |

## Estrategia
- **Automatizados**: 8 casos críticos (login, carrito, checkout, logout).
- **Manual**: Ver detalle de producto (bajo riesgo).
- **Edge case detectado**: Permite checkout con carrito vacío → mejora de UX.