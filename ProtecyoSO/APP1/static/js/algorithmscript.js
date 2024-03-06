
// script.js
document.addEventListener('DOMContentLoaded', function() {
    const RRLink = document.getElementById('RR-link');
    const FCFSLink = document.getElementById('FCFs-link');
    const SJFLink = document.getElementById('SJF-link');
    const algorithmResultsDiv = document.getElementById('algorithm-results');

    function callAlgorithm(algorithm) {
        fetch(`/algorithms/${algorithm}`)
            .then(response => response.json())
            .then(data => {
                algorithmResultsDiv.innerText = data.result;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    RRLink.addEventListener('click', function(event) {
        event.preventDefault(); // Evita la recarga de la página
        callAlgorithm('RR');
        algorithmResultsDiv.innerText = 'Bienvenido a Round Robin ';
    });

    FCFSLink.addEventListener('click', function(event) {
        event.preventDefault(); // Evita la recarga de la página
        callAlgorithm('FCFS');
        algorithmResultsDiv.innerText = 'Bienvenido a First Come First Serve';
    });

    SJFLink.addEventListener('click', function(event) {
        event.preventDefault(); // Evita la recarga de la página
        callAlgorithm('SJF');
        algorithmResultsDiv.innerText = 'Bienvenido a Shortest Job First';
    });
});


