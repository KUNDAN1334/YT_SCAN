document.getElementById("askBtn").addEventListener("click", async () => {
  const video_url = document.getElementById("url").value;
  const question = document.getElementById("question").value;
  
  try {
      const response = await fetch("https://yt-scan.onrender.com", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ video_url, question })
      });
      
      const data = await response.json();
      
      // Check if response contains error
      if (data.error) {
          document.getElementById("answer").innerText = `Error: ${data.error}`;
          console.error("Backend error:", data.error);
      } else if (data.answer) {
          document.getElementById("answer").innerText = data.answer;
      } else {
          document.getElementById("answer").innerText = "Received undefined response";
          console.log("Full response:", data);
      }
  } catch (error) {
      document.getElementById("answer").innerText = `Request failed: ${error.message}`;
      console.error("Fetch error:", error);
  }
});
