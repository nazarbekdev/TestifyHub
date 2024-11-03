function openSubscribeForm(plan) {
    document.getElementById('subscribe-form').style.display = 'flex'; // Formani ko'rsatish
    document.getElementById('plan-name').textContent = plan; // Plan nomini yangilash
}

function closeSubscribeForm() {
    document.getElementById('subscribe-form').style.display = 'none'; // Formani yashirish
}
