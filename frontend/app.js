document.getElementById('summarize-button').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent form submission

    const text = document.getElementById('input-text').value;

    fetch('/summarize', {  // Use relative URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.summary) {
            document.getElementById('summary-output').innerText = data.summary;
        } else {
            document.getElementById('summary-output').innerText = 'No summary generated.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('summary-output').innerText = 'Error generating summary. Please try again.';
    });
});
