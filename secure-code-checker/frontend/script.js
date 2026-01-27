let chatHistory = [];
let lastResult = "";

async function analyzeCode() {
    const code = document.getElementById("code").value;
    const resultBox = document.getElementById("result");

    if (!code.trim()) {
        resultBox.textContent = "⚠️ Please paste some code first.";
        return;
    }

    resultBox.textContent = "🔎 Analyzing...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code })
        });

        const data = await response.json();
        resultBox.textContent = data.result;
        lastResult = data.result;

        saveToHistory(code);

    } catch (err) {
        resultBox.textContent = "❌ Error connecting to backend.";
    }
}

/* DOWNLOAD RESULT AS TXT */
function downloadResult() {
    if (!lastResult) {
        alert("No result to download");
        return;
    }

    const blob = new Blob([lastResult], { type: "text/plain" });
    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);
    link.download = "secure_code_result.txt";
    link.click();
}

/* CHAT HISTORY */
function saveToHistory(code) {
    const title = "Code " + (chatHistory.length + 1);
    chatHistory.push({ title, code });

    const historyList = document.getElementById("history");
    const li = document.createElement("li");
    li.textContent = title;

    li.onclick = () => {
        document.getElementById("code").value = code;
    };

    historyList.appendChild(li);
}
