function addRow() {
    const table = document.getElementById("candidates-table").getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    const cells = ['name', 'status', 'feedback', 'rating', 'action'];

    cells.forEach((cell, index) => {
        const newCell = newRow.insertCell(index);
        if (cell === 'action') {
            newCell.innerHTML = '<button onclick="deleteRow(this)">Delete</button>';
        } else {
            newCell.innerHTML = `<input type="text" name="${cell}" required>`;
        }
    });
}

function deleteRow(btn) {
    const row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
}
