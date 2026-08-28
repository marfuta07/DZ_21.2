// Общий JavaScript для всех страниц
$(document).ready(function() {
    // Обработка кнопок "Купить"
    $('.buy-btn').on('click', function(e) {
        e.preventDefault();
        var productName = $(this).closest('.card-body').find('.card-title').text();
        alert('Товар "' + productName + '" добавлен в корзину!');
    });
});