function redirectToRoot() {
    window.location.href = "/";
}

window.addEventListener('load', function() {
    const form = document.getElementById('emotion-form');
    const experienceInput = document.getElementById('experience');
    const validationMessage = document.getElementById('validation-message');

    form.addEventListener('submit', function(event) {
        const wordCount = experienceInput.value.trim().split(/\s+/).length;
        if (wordCount < 5) {
            event.preventDefault();
            validationMessage.innerText = 'Please enter more than 5 words.';
        } else {
            validationMessage.innerText = '';
        }
    });
});
