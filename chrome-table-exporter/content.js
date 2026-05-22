(() => {
  const table = document.querySelector("table");
  if (!table) {
    alert("No HTML table found on this page.");
    return;
  }

  const rows = Array.from(table.querySelectorAll("tr"));
  const csv = rows
    .map((row) => {
      const cells = Array.from(row.querySelectorAll("th,td"));
      return cells.map((cell) => toCsvCell(cell.innerText.trim())).join(",");
    })
    .join("\n");

  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "table-export.csv";
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);

  function toCsvCell(value) {
    const escaped = value.replaceAll('"', '""');
    return /[",\n]/.test(escaped) ? `"${escaped}"` : escaped;
  }
})();

