fetch('lyric-data/song_lyrics.json')
    .then(response => response.json())
    .then(data => {
        const cardContainer = document.getElementById('card-container');
        data.forEach(item => {
            const key = Object.keys(item)[0];
            const song = item[key];
            const cardElement = document.createElement('div');
            cardElement.classList.add('card');
            cardElement.innerHTML = `
                <h2>${song["Name of the Song"]}</h2>
                <p><strong>Author:</strong> ${song["Author"]}</p>
                <p><strong>Lyric:</strong> ${song["Lyric (no period)"]}</p>
            `;
            cardContainer.appendChild(cardElement);
        });
    });
