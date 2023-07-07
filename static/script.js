function redirectToRoot() {
    window.location.href = "/";
}

window.addEventListener('load', function() {
    const form = document.getElementById('emotion-form');
    const experienceInput = document.getElementById('experience');
    const validationMessage = document.getElementById('validation-message');

    form.addEventListener('submit', function(event) {
        if (experienceInput.value.length < 6) {
            event.preventDefault();
            validationMessage.innerText = 'Characters should be more than 5';
        } else {
            validationMessage.innerText = '';
        }
    });
});
