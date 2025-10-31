document.getElementById("askBtn").addEventListener("click", async () => {
    const videoUrl = document.getElementById("url").value;
    const question = document.getElementById("question").value;
    const answerElement = document.getElementById("answer");
    
    if (!videoUrl || !question) {
      answerElement.innerText = "Please enter both URL and question";
      return;
    }
    
    answerElement.innerText = "Loading...";
    
    try {
      const response = await fetch("https://yt-scan.onrender.com/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
          video_url: videoUrl, 
          question: question 
        })
      });
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: response.statusText }));
        throw new Error(`HTTP ${response.status}: ${errorData.detail || 'Request failed'}`);
      }
      
      const data = await response.json();
      answerElement.innerText = data.answer || "No answer received";
      
    } catch (error) {
      answerElement.innerText = `Error: ${error.message}`;
      console.error("Request failed:", error);
    }
  });
  