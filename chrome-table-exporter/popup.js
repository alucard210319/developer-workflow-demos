const button = document.querySelector("#export");
const statusEl = document.querySelector("#status");

button.addEventListener("click", async () => {
  button.disabled = true;
  statusEl.textContent = "Exporting...";

  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ["content.js"],
    });
    statusEl.textContent = "Done. Check your downloads.";
  } catch (error) {
    statusEl.textContent = error.message || "Export failed.";
  } finally {
    button.disabled = false;
  }
});

