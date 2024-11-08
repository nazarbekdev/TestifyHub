document.addEventListener('DOMContentLoaded', function() {
    const demoBtn = document.getElementById('watch-demo');
    const demoModal = document.getElementById('demoModal');
    const trialBtn = document.getElementById('try-free');
    const trialModal = document.getElementById('trialModal');
    const closeButtons = document.querySelectorAll('.close');

    demoBtn.addEventListener('click', function() {
        demoModal.style.display = 'flex';
    });

    trialBtn.addEventListener('click', function() {
        trialModal.style.display = 'flex';
    });

    closeButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            demoModal.style.display = 'none';
            trialModal.style.display = 'none';
        });
    });

    window.addEventListener('click', function(event) {
        if (event.target === demoModal || event.target === trialModal) {
            demoModal.style.display = 'none';
            trialModal.style.display = 'none';
        }
    });
});
