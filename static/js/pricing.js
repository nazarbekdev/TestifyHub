function openSubscribeForm(planName) {
    document.getElementById('plan-name').textContent = planName;
    document.querySelector('input[name="plan"]').value = planName;
    document.getElementById('subscribe-form').style.display = 'block';
}


function closeSubscribeForm() {
    document.getElementById('subscribe-form').style.display = 'none'; // Formani yashirish
}
