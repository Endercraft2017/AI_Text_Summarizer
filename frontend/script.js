document.getElementById("sendBtn").addEventListener("click", async () => {
    const userInput = document.getElementById("userInput").value;
    const responseBox = document.getElementById("responseBox");
    const loading = document.getElementById("loading");

    if (!userInput.trim()) {
        responseBox.innerText = "Please enter a message.";
        return;
    }

    responseBox.innerText = ""; // Clear previous response
    loading.style.display = "block"; // Show loading

    try {
        const res = await fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userInput })
        });

        const data = await res.json();
        responseBox.innerText = data.response || "No response from API.";
    } catch (err) {
        responseBox.innerText = "Error connecting to API.";
    } finally {
        loading.style.display = "none"; // Hide loading
    }
});
