const ctxHistogram = document.getElementById('priceHistogram').getContext('2d');
const ctxLine = document.getElementById('discountVsRating').getContext('2d');

let histogramChart = new Chart(ctxHistogram, {type: 'bar', data: {labels: [], datasets: []}});
let lineChart = new Chart(ctxLine, {type: 'line', data: {labels: [], datasets: []}});

let currentProducts = [];

function startParsing() {
    const query = document.getElementById("searchQuery").value;
    const status = document.getElementById("status");
    status.textContent = "Парсинг...";

    fetch(`/api/parse?query=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
            currentProducts = data.products;
            updateTable(currentProducts);
            updateCharts(currentProducts);
            status.textContent = "Готово!";
            document.getElementById("saveButton").style.display = "inline-block";
        })
        .catch(err => {
            console.error(err);
            status.textContent = "Ошибка";
        });
}

function saveToDatabase() {
    fetch('/api/save', { method: 'POST' })
        .then(res => res.json())
        .then(() => {
            alert("Данные сохранены в базу!");
        })
        .catch(err => {
            console.error(err);
            alert("Ошибка сохранения");
        });
}

function applyFilters() {
    const minPrice = document.getElementById('minPrice').value;
    const maxPrice = document.getElementById('maxPrice').value;
    const minRating = document.getElementById('minRating').value;
    const minReviews = document.getElementById('minReviews').value;

    let filtered = currentProducts.filter(p => {
        return (
            p.price >= parseInt(minPrice) &&
            p.price <= parseInt(maxPrice) &&
            p.rating >= parseFloat(minRating) &&
            p.reviews >= parseInt(minReviews)
        );
    });

    updateTable(filtered);
    updateCharts(filtered);
}