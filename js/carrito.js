// Función para agregar un producto al carrito
function addToCart(productName, productPrice) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push({ name: productName, price: productPrice });
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Escuchar los clics en los botones "Agregar al Carrito"
document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productName = button.getAttribute('data-name');
            const productPrice = parseFloat(button.getAttribute('data-price'));
            addToCart(productName, productPrice);
        });
    });
});

// Función para actualizar la visualización del carrito en la página
function updateCartDisplay() {
    const cartContainer = document.getElementById('cart-items');
    cartContainer.innerHTML = '';

    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.price}</td>
            <td><button onclick="removeFromCart('${item.name}')">Eliminar</button></td>
        `;
        cartContainer.appendChild(row);
    });
}

// Función para eliminar un producto del carrito
function removeFromCart(productName) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const index = cart.findIndex(item => item.name === productName);
    if (index !== -1) {
        cart.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartDisplay();
});
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButton = document.getElementById('addToCartButton');
    addToCartButton.addEventListener('click', function(event) {
        event.preventDefault(); 
        const productName = addToCartButton.getAttribute('data-name');
        const productPrice = parseFloat(addToCartButton.getAttribute('data-price'));
        addToCart(productName, productPrice);
    });
});
