function toggleText() {
    const dots = document.getElementById("dots");
    const moreText = document.getElementById("more");
    const readMoreBtn = document.getElementById("read-more");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      moreText.style.display = "none";
      readMoreBtn.innerHTML = "Read More";
    } else {
      dots.style.display = "none";
      moreText.style.display = "inline";
      readMoreBtn.innerHTML = "Read Less";
    }
  }
  

  function toggleText2() {
    const fullText = document.getElementById("fullText");
    const hiddenDots = document.getElementById("hiddenDots");
    const toggleLink = document.getElementById("toggleLink");
  
    // Check if the full text is currently displayed
    if (fullText.style.display === "none") {
      // Show the hidden text and change the link text
      fullText.style.display = "inline";
      hiddenDots.style.display = "none";
      toggleLink.textContent = "Read Less";
    } else {
      // Hide the text and change the link text back
      fullText.style.display = "none";
      hiddenDots.style.display = "inline";
      toggleLink.textContent = "Read More";
    }
  }
  