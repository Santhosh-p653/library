document.addEventListener("DOMContentLoaded", () => {
    const searchBtn = document.getElementById("searchBtn");
    if (searchBtn) {
        searchBtn.addEventListener("click", searchBooks);
    }
});

async function searchBooks() {
    const query = document.getElementById("searchInput").value;

    if (query.trim() === "") {
        alert("Please enter a book name");
        return;
    }

    try {
        const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
        const books = await response.json();
        const results = document.getElementById("results");
        
        results.innerHTML = "";

        if (books.length === 0) {
            results.innerHTML = `<h2 style="text-align:center; width: 100%;">No Books Found</h2>`;
            return;
        }

        books.forEach(book => {
            const card = document.createElement("div");
            card.className = "book-card";

            card.innerHTML = `
                <img 
                    src="${book.image}"
                    alt="Book Cover"
                    onerror="this.src='https://via.placeholder.com/200x300?text=No+Cover'"
                >
                <div class="book-content">
                    <h3>${book.title}</h3>
                    <p>${book.author}</p>
                    <button class="save-btn">Save Book</button>
                </div>
            `;

            const saveBtn = card.querySelector(".save-btn");
            saveBtn.addEventListener("click", () => {
                saveBook(book.title, book.author);
            });

            results.appendChild(card);
        });

    } catch (error) {
        console.error(error);
        alert("Error fetching books");
    }
}

async function saveBook(title, author) {
    try {
        const response = await fetch("/save", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: title, author: author })
        });

        const data = await response.json();
        alert(data.message);

    } catch (error) {
        console.error(error);
        alert("Error saving book");
    }
}