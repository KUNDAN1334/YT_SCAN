document.getElementById("askBtn").addEventListener("click", async () => {
    const video_url = document.getElementById("url").value;
    const question = document.getElementById("question").value;
  
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ video_url, question })
    });
  
    const data = await response.json();
    document.getElementById("answer").innerText = data.answer;
  });