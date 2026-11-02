const messageInput = document.getElementById("message");
const keyInput = document.getElementById("key");
const resultDisplay = document.getElementById("result");

// Sends the form values to the selected route and displays its response.
async function sendMessage(operation) {
    resultDisplay.textContent = "";
    resultDisplay.classList.remove("error");

    const message = messageInput.value;
    const key = Number(keyInput.value);

    try {
        const response = await fetch("/" + operation, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message, key: key })
        });

        const data = await response.json();
        if (!response.ok) {
            resultDisplay.textContent = data.error;
            resultDisplay.classList.add("error");
            return;
        }

        resultDisplay.textContent = data.result;
    } catch (error) {
        resultDisplay.textContent = "Could not connect to the server.";
        resultDisplay.classList.add("error");
    }
}

document.getElementById("encrypt-button").addEventListener("click", function () {
    sendMessage("encrypt");
});

document.getElementById("decrypt-button").addEventListener("click", function () {
    sendMessage("decrypt");
});
