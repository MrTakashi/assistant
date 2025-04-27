
document.querySelectorAll('.topic').forEach(topic => {
    topic.addEventListener('click', function() {
        const exampleText = this.getAttribute('data-example');
        document.getElementById('userInput').value = exampleText;
        document.getElementById('userInput').focus();
    });
});

document.querySelector('.account-logo').addEventListener('click', function() {
    document.getElementById('accountPanel').classList.toggle('show');
});
