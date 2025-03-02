document.getElementById("searchButton").addEventListener("click", function () {
    let query = document.getElementById("searchQuery").value;
    if (query.trim() === "") return;

    fetch(`http://127.0.0.1:5000/search?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = ""; // Clear previous results

            data.forEach(video => {
                let videoElement = document.createElement("div");
                videoElement.innerHTML = `
                    <div class="video-card">
                        <iframe width="100%" height="150" src="https://www.youtube.com/embed/${video.url.split('v=')[1]}" frameborder="0" allowfullscreen></iframe>
                        <p>${video.title}</p>
                    </div>
                `;
                resultsDiv.appendChild(videoElement);
            });
        })
        .catch(error => console.error("Error fetching videos:", error));
});
